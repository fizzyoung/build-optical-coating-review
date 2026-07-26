from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

from _common import (
    EXIT_EXTERNAL,
    ScriptError,
    normalize_doi,
    normalize_title,
    records_from_payload,
    run_cli,
    utc_now,
    validate_against_schema,
    write_json,
)

DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Validate source metadata locally and optionally cross-check DOI records with Crossref.")
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--crossref", action="store_true", help="Opt in to lawful, rate-limited Crossref DOI checks")
    result.add_argument("--cache", type=Path, default=Path(".metadata-cache"))
    result.add_argument("--rate-limit", type=float, default=1.0, help="Minimum seconds between network requests")
    result.add_argument("--timeout", type=float, default=15.0)
    result.add_argument("--mailto", help="Contact email for Crossref polite identification; never written into project output")
    result.add_argument("--max-records", type=int, help="Bound external checks")
    return result


def cache_file(directory: Path, doi: str) -> Path:
    return directory / (hashlib.sha256(doi.encode("utf-8")).hexdigest() + ".json")


def crossref_lookup(doi: str, args: argparse.Namespace) -> tuple[dict | None, str, str | None]:
    cache = cache_file(args.cache.resolve(), doi)
    if cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8")), "CACHE_HIT", None
    query = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{query}"
    agent = "build-optical-coating-review/1.0"
    if args.mailto:
        agent += f" (mailto:{args.mailto})"
    request = urllib.request.Request(url, headers={"User-Agent": agent, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, "EXTERNAL_CHECK_FAILED", str(exc)
    cache.parent.mkdir(parents=True, exist_ok=True)
    write_json(cache, payload, overwrite=False)
    return payload, "NETWORK_OK", None


def crossref_year(message: dict) -> int | None:
    for field in ["published-print", "published-online", "issued", "created"]:
        parts = message.get(field, {}).get("date-parts", [])
        if parts and parts[0]:
            return int(parts[0][0])
    return None


def main() -> int:
    args = parser().parse_args()
    if args.rate_limit < 0.5:
        raise ScriptError("--rate-limit must be at least 0.5 seconds", 2)
    records = records_from_payload(json.loads(args.input.read_text(encoding="utf-8-sig")))
    results = []
    external_failures = 0
    network_count = 0
    last_request = 0.0
    for index, record in enumerate(records):
        local_errors = validate_against_schema(record, "source-record.schema.json")
        doi = normalize_doi(record.get("doi"))
        if doi and not DOI_PATTERN.match(doi):
            local_errors.append("doi: invalid DOI syntax")
        result = {
            "source_id": record.get("source_id"),
            "doi": doi,
            "local_status": "INVALID" if local_errors else "VALID",
            "local_errors": local_errors,
            "external_status": "NOT_REQUESTED",
            "external_error": None,
            "title_similarity": None,
            "year_match": None,
            "crossref_title": None,
            "crossref_year": None,
            "checked_at": utc_now(),
        }
        if args.crossref:
            if not doi:
                result["external_status"] = "NOT_CHECKED_NO_DOI"
            elif args.max_records is not None and network_count >= args.max_records:
                result["external_status"] = "NOT_CHECKED_LIMIT_REACHED"
            else:
                cache_exists = cache_file(args.cache.resolve(), doi).is_file()
                if not cache_exists:
                    elapsed = time.monotonic() - last_request
                    if elapsed < args.rate_limit:
                        time.sleep(args.rate_limit - elapsed)
                    last_request = time.monotonic()
                    network_count += 1
                payload, status, error = crossref_lookup(doi, args)
                result["external_status"] = status
                result["external_error"] = error
                if payload is None:
                    external_failures += 1
                else:
                    message = payload.get("message", {})
                    title_values = message.get("title") or []
                    title = title_values[0] if title_values else None
                    year = crossref_year(message)
                    result["crossref_title"] = title
                    result["crossref_year"] = year
                    if title and record.get("title"):
                        result["title_similarity"] = round(
                            SequenceMatcher(None, normalize_title(record["title"]), normalize_title(title)).ratio(), 4
                        )
                    if year and record.get("year"):
                        result["year_match"] = year == record["year"]
                    if result["title_similarity"] is not None and result["title_similarity"] < 0.85 or result["year_match"] is False:
                        result["external_status"] = "METADATA_CONFLICT"
                    else:
                        result["external_status"] = "VERIFIED_MATCH"
        results.append(result)

    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "network_enabled": args.crossref,
        "legal_boundary": "Crossref public API only; no authentication, CAPTCHA, subscription, or access-control bypass.",
        "results": results,
        "counts": {
            "records": len(records),
            "local_invalid": sum(item["local_status"] == "INVALID" for item in results),
            "external_failures": external_failures,
            "metadata_conflicts": sum(item["external_status"] == "METADATA_CONFLICT" for item in results),
        },
    }
    write_json(args.output, output, overwrite=False)
    print(json.dumps({"status": "EXTERNAL_CHECK_FAILED" if external_failures else "OK", **output["counts"]}, ensure_ascii=False, indent=2))
    return EXIT_EXTERNAL if external_failures else 0


if __name__ == "__main__":
    run_cli(main)
