from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from _common import (
    ScriptError,
    normalize_doi,
    normalize_title,
    records_from_payload,
    run_cli,
    unique_strings,
    utc_now,
    validate_against_schema,
    write_json,
)

ARRAY_FIELDS = {
    "authors", "database_sources", "materials", "substrates", "coatings", "deposition_routes",
    "interface_strategies", "optical_properties", "mechanical_properties", "environmental_properties",
    "manufacturing_properties", "characterization_methods", "themes", "intended_uses",
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Deduplicate Source Records while preserving identifiers, conflicts, and version candidates.")
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--decision-log", type=Path)
    return result


def merge_into(canonical: dict[str, Any], duplicate: dict[str, Any]) -> list[dict[str, Any]]:
    conflicts = []
    for key, value in duplicate.items():
        if key in {"source_id", "schema_version", "supersedes_source_id"}:
            continue
        if key in ARRAY_FIELDS:
            canonical[key] = unique_strings(list(canonical.get(key, [])) + list(value or []))
        elif canonical.get(key) in (None, "", "UNASSESSED", "V0", "NOT_REQUESTED", "UNSCREENED") and value not in (None, ""):
            canonical[key] = value
        elif value not in (None, "") and canonical.get(key) != value:
            conflicts.append({"field": key, "kept": canonical.get(key), "other": value})
    return conflicts


def choose_canonical(records: list[dict[str, Any]]) -> dict[str, Any]:
    return min(records, key=lambda item: (0 if normalize_doi(item.get("doi")) else 1, item["source_id"]))


def main() -> int:
    args = parser().parse_args()
    records = records_from_payload(json.loads(args.input.read_text(encoding="utf-8-sig")))
    errors = []
    ids = set()
    for index, record in enumerate(records):
        errors.extend(f"record[{index}] {item}" for item in validate_against_schema(record, "source-record.schema.json"))
        if record.get("source_id") in ids:
            errors.append(f"record[{index}] repeats Source_ID {record.get('source_id')}")
        ids.add(record.get("source_id"))
    if errors:
        raise ScriptError("Input validation failed: " + " | ".join(errors), 3)

    active = {record["source_id"]: dict(record) for record in records}
    relations: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []

    doi_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        doi = normalize_doi(record.get("doi"))
        if doi:
            doi_groups[doi].append(record)
    for doi, group in sorted(doi_groups.items()):
        if len(group) < 2:
            continue
        canonical = choose_canonical(group)
        for duplicate in sorted(group, key=lambda item: item["source_id"]):
            if duplicate["source_id"] == canonical["source_id"] or duplicate["source_id"] not in active:
                continue
            conflicts = merge_into(active[canonical["source_id"]], duplicate)
            del active[duplicate["source_id"]]
            relations.append({"from_source_id": duplicate["source_id"], "to_source_id": canonical["source_id"], "relation": "DUPLICATE_OF", "basis": f"Exact normalized DOI: {doi}"})
            decisions.append({"decision": "AUTO_MERGE", "method": "DOI_EXACT", "canonical": canonical["source_id"], "removed": duplicate["source_id"], "conflicts": conflicts})

    title_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in active.values():
        title = normalize_title(record.get("title"))
        if title:
            title_groups[title].append(record)
    for title, group in sorted(title_groups.items()):
        if len(group) < 2:
            continue
        doi_values = {normalize_doi(item.get("doi")) for item in group if normalize_doi(item.get("doi"))}
        years = {item.get("year") for item in group if item.get("year") is not None}
        if len(doi_values) > 1:
            issue = {
                "status": "MANUAL_REVIEW_REQUIRED",
                "reason": "EXACT_TITLE_DIFFERENT_DOI",
                "source_ids": sorted(item["source_id"] for item in group),
                "doi_values": sorted(doi_values),
                "normalized_title": title,
            }
            unresolved.append(issue)
            decisions.append({"decision": "KEEP_SEPARATE", **issue})
            continue
        if len(years) > 1:
            issue = {
                "status": "MANUAL_REVIEW_REQUIRED",
                "reason": "EXACT_TITLE_YEAR_CONFLICT",
                "source_ids": sorted(item["source_id"] for item in group),
                "years": sorted(years),
                "normalized_title": title,
            }
            unresolved.append(issue)
            decisions.append({"decision": "KEEP_SEPARATE", **issue})
            continue
        canonical = choose_canonical(group)
        for duplicate in sorted(group, key=lambda item: item["source_id"]):
            if duplicate["source_id"] == canonical["source_id"] or duplicate["source_id"] not in active:
                continue
            candidate = copy.deepcopy(active[canonical['source_id']])
            conflicts = merge_into(candidate, duplicate)
            if conflicts:
                unresolved.append({"status": "MANUAL_REVIEW_REQUIRED", "reason": "TITLE_MATCH_FIELD_CONFLICT", "source_ids": [canonical["source_id"], duplicate["source_id"]], "conflicts": conflicts})
                decisions.append({"decision": "KEEP_SEPARATE", "method": "TITLE_EXACT", "source_ids": [canonical["source_id"], duplicate["source_id"]], "conflicts": conflicts})
                continue
            active[canonical['source_id']] = candidate
            del active[duplicate["source_id"]]
            relations.append({"from_source_id": duplicate["source_id"], "to_source_id": canonical["source_id"], "relation": "DUPLICATE_OF", "basis": "Exact normalized title with no DOI/year conflict"})
            decisions.append({"decision": "AUTO_MERGE", "method": "TITLE_EXACT", "canonical": canonical["source_id"], "removed": duplicate["source_id"], "conflicts": []})

    for record in records:
        if record.get("supersedes_source_id"):
            relations.append({"from_source_id": record["source_id"], "to_source_id": record["supersedes_source_id"], "relation": "SUPERSEDES", "basis": "Explicit source-record version link"})

    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "records": sorted(active.values(), key=lambda item: item["source_id"]),
        "relations": relations,
        "decision_log": decisions,
        "unresolved": unresolved,
        "counts": {"input": len(records), "retained": len(active), "merged": len(records) - len(active), "manual_review": len(unresolved)},
    }
    write_json(args.output, output, overwrite=False)
    if args.decision_log:
        write_json(args.decision_log, decisions, overwrite=False)
    print(json.dumps({"status": "REVIEW_REQUIRED" if unresolved else "OK", **output["counts"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
