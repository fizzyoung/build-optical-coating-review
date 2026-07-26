from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import (
    EXIT_VALIDATION,
    records_from_payload,
    run_cli,
    utc_now,
    validate_against_schema,
    verification_at_least,
    write_json,
)

V4_TYPES = {"QUANTITATIVE", "MECHANISTIC", "CAUSAL"}
V4_EVIDENCE = {"TABLE", "FIGURE", "SUPPLEMENT", "DERIVED_CALCULATION"}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Audit Claim-Evidence records for Schema, provenance, and verification-gate failures.")
    result.add_argument("claims", type=Path)
    result.add_argument("sources", type=Path)
    result.add_argument("output", type=Path)
    return result


def main() -> int:
    args = parser().parse_args()
    claims = records_from_payload(json.loads(args.claims.read_text(encoding="utf-8-sig")), "claims")
    sources = records_from_payload(json.loads(args.sources.read_text(encoding="utf-8-sig")))
    source_by_id = {record.get("source_id"): record for record in sources}
    blockers: list[dict] = []
    warnings: list[dict] = []
    claim_ids = set()

    for index, claim in enumerate(claims):
        claim_id = claim.get("claim_id") or f"index:{index}"
        if claim_id in claim_ids:
            blockers.append({"claim_id": claim_id, "check": "UNIQUE_CLAIM_ID", "detail": "Duplicate Claim_ID"})
        claim_ids.add(claim_id)
        for error in validate_against_schema(claim, "claim.schema.json"):
            blockers.append({"claim_id": claim_id, "check": "SCHEMA", "detail": error})
        if not claim.get("claim_text_zh") and not claim.get("claim_text_en"):
            blockers.append({"claim_id": claim_id, "check": "CLAIM_TEXT", "detail": "Both Chinese and English claim text are empty"})
        links = claim.get("source_links", [])
        if not links:
            blockers.append({"claim_id": claim_id, "check": "SOURCE_LINK", "detail": "No Source_ID is linked"})

        required = "V4" if claim.get("claim_type") in V4_TYPES or claim.get("evidence_type") in V4_EVIDENCE else "V3"
        declared = claim.get("minimum_verification_level", "V0")
        if verification_at_least(declared, required):
            required = declared
        if not verification_at_least(claim.get("minimum_verification_level", "V0"), required):
            blockers.append({"claim_id": claim_id, "check": "MINIMUM_LEVEL", "detail": f"Claim requires {required} but declares {claim.get('minimum_verification_level')}"})
        substantive_links = []
        for link in links:
            source_id = link.get("source_id")
            source = source_by_id.get(source_id)
            if source is None:
                blockers.append({"claim_id": claim_id, "check": "SOURCE_EXISTS", "detail": f"Unknown Source_ID: {source_id}"})
                continue
            if not verification_at_least(source.get("verification_level", "V0"), link.get("verification_level", "V0")):
                blockers.append({"claim_id": claim_id, "check": "LEVEL_CONFLICT", "detail": f"{source_id} record is {source.get('verification_level')} but link claims {link.get('verification_level')}"})
            if link.get("relation") != "BACKGROUND_ONLY":
                substantive_links.append(link)
                if not verification_at_least(link.get("verification_level", "V0"), required):
                    blockers.append({"claim_id": claim_id, "check": "EVIDENCE_LEVEL", "detail": f"{source_id} is below required {required}"})
                if required == "V4" and not str(link.get("original_location") or "").strip():
                    blockers.append({"claim_id": claim_id, "check": "ORIGINAL_LOCATION", "detail": f"{source_id} lacks a page, section, figure, or table location"})
        if links and not substantive_links:
            blockers.append({"claim_id": claim_id, "check": "SUBSTANTIVE_SUPPORT", "detail": "All links are BACKGROUND_ONLY"})
        if claim.get("claim_type") in {"CONSENSUS", "CONTROVERSY"}:
            independent = {link.get("source_id") for link in substantive_links}
            if len(independent) < 2:
                blockers.append({"claim_id": claim_id, "check": "MULTI_SOURCE_SYNTHESIS", "detail": "Consensus or controversy requires at least two Source_ID values"})
        if claim.get("human_status") != "ACCEPTED":
            warnings.append({"claim_id": claim_id, "check": "HUMAN_REVIEW", "detail": f"human_status={claim.get('human_status')}"})
        claim_text = " ".join(filter(None, [claim.get("claim_text_zh"), claim.get("claim_text_en"), claim.get("notes")]))
        if re.search(r"raman", claim_text, re.IGNORECASE) and re.search(r"(?:精确|exact|precise).{0,20}sp\s*3|sp\s*3.{0,20}(?:精确|exact|precise)", claim_text, re.IGNORECASE):
            blockers.append({"claim_id": claim_id, "check": "RAMAN_SP3_OVERCLAIM", "detail": "Raman must not be equated directly with precise sp3 content"})

    report = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "status": "FAIL" if blockers else "PASS",
        "claims_checked": len(claims),
        "sources_available": len(sources),
        "blockers": blockers,
        "warnings": warnings,
    }
    write_json(args.output, report, overwrite=False)
    print(json.dumps({"status": report["status"], "claims_checked": len(claims), "blockers": len(blockers), "warnings": len(warnings)}, ensure_ascii=False, indent=2))
    return EXIT_VALIDATION if blockers else 0


if __name__ == "__main__":
    run_cli(main)
