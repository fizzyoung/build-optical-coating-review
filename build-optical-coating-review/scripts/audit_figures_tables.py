from __future__ import annotations

import argparse
import json
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


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Audit figure, figure-element, table, and key-cell provenance and copyright gates.")
    result.add_argument("traces", type=Path)
    result.add_argument("sources", type=Path)
    result.add_argument("output", type=Path)
    return result


def main() -> int:
    args = parser().parse_args()
    traces = records_from_payload(json.loads(args.traces.read_text(encoding="utf-8-sig")), "traces")
    sources = records_from_payload(json.loads(args.sources.read_text(encoding="utf-8-sig")))
    source_by_id = {record.get("source_id"): record for record in sources}
    blockers: list[dict] = []
    warnings: list[dict] = []
    trace_ids = set()
    artifact_keys = set()

    for index, trace in enumerate(traces):
        trace_id = trace.get("trace_id") or f"index:{index}"
        if trace_id in trace_ids:
            blockers.append({"trace_id": trace_id, "check": "UNIQUE_TRACE_ID", "detail": "Duplicate trace_id"})
        trace_ids.add(trace_id)
        for error in validate_against_schema(trace, "figure-table-traceability.schema.json"):
            blockers.append({"trace_id": trace_id, "check": "SCHEMA", "detail": error})
        artifact_key = (trace.get("artifact_id"), trace.get("element_id"), trace.get("source_id"), trace.get("original_location"))
        if artifact_key in artifact_keys:
            warnings.append({"trace_id": trace_id, "check": "POSSIBLE_DUPLICATE", "detail": "The same artifact element and source location are recorded more than once"})
        artifact_keys.add(artifact_key)
        source = source_by_id.get(trace.get("source_id"))
        if source is None:
            blockers.append({"trace_id": trace_id, "check": "SOURCE_EXISTS", "detail": f"Unknown Source_ID: {trace.get('source_id')}"})
        elif not verification_at_least(source.get("verification_level", "V0"), trace.get("verification_level", "V0")):
            blockers.append({"trace_id": trace_id, "check": "LEVEL_CONFLICT", "detail": "Trace verification exceeds source-record verification"})
        if not verification_at_least(trace.get("verification_level", "V0"), "V4"):
            blockers.append({"trace_id": trace_id, "check": "EVIDENCE_LEVEL", "detail": "Figure/table provenance requires V4 or V5"})
        if trace.get("artifact_type") in {"FIGURE_ELEMENT", "TABLE_CELL"} and not str(trace.get("element_id") or "").strip():
            blockers.append({"trace_id": trace_id, "check": "ELEMENT_ID", "detail": "Element-level trace lacks element_id"})
        if trace.get("transformation") in {"DIGITIZED", "CALCULATED", "SYNTHESIZED"} and not str(trace.get("calculation") or "").strip():
            blockers.append({"trace_id": trace_id, "check": "TRANSFORMATION_METHOD", "detail": "Digitized, calculated, or synthesized content requires a reproducible method/calculation"})
        copyright_status = trace.get("copyright_status")
        if copyright_status in {"UNASSESSED", "PERMISSION_REQUIRED", "NOT_REUSABLE"}:
            blockers.append({"trace_id": trace_id, "check": "COPYRIGHT", "detail": f"copyright_status={copyright_status}"})
        if copyright_status in {"LICENSED", "PERMISSION_OBTAINED"} and not str(trace.get("permission_reference") or "").strip():
            blockers.append({"trace_id": trace_id, "check": "PERMISSION_REFERENCE", "detail": "License or permission evidence is missing"})
        if trace.get("human_status") != "ACCEPTED":
            warnings.append({"trace_id": trace_id, "check": "HUMAN_REVIEW", "detail": f"human_status={trace.get('human_status')}"})

    report = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "status": "FAIL" if blockers else "PASS",
        "traces_checked": len(traces),
        "artifacts": len({trace.get("artifact_id") for trace in traces}),
        "blockers": blockers,
        "warnings": warnings,
    }
    write_json(args.output, report, overwrite=False)
    print(json.dumps({"status": report["status"], "traces_checked": len(traces), "blockers": len(blockers), "warnings": len(warnings)}, ensure_ascii=False, indent=2))
    return EXIT_VALIDATION if blockers else 0


if __name__ == "__main__":
    run_cli(main)
