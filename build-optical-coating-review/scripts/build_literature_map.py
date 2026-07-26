from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from _common import (
    ScriptError,
    records_from_payload,
    run_cli,
    utc_now,
    validate_against_schema,
    write_json,
)

VIEWS = [
    "TIME_EVOLUTION",
    "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE",
    "THEME_CLUSTER",
    "METHOD_CHARACTERIZATION_MATRIX",
    "CONSENSUS_CONTROVERSY",
    "EVIDENCE_LAYER",
]
NODE_FIELDS = [
    "source_id", "title", "year", "journal", "document_type", "materials", "substrates", "coatings",
    "deposition_routes", "interface_strategies", "optical_properties", "mechanical_properties",
    "environmental_properties", "manufacturing_properties", "characterization_methods", "verification_level",
    "themes", "research_stage", "intended_uses", "evidence_strength",
]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Build a literature-map JSON using only explicit Source_ID nodes and verified edge records.")
    result.add_argument("records", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--edges", type=Path, help="JSON array or object containing explicit edges; no relationships are inferred")
    result.add_argument("--project-id")
    result.add_argument("--map-id")
    return result


def main() -> int:
    args = parser().parse_args()
    records = records_from_payload(json.loads(args.records.read_text(encoding="utf-8-sig")))
    source_errors = []
    for index, record in enumerate(records):
        source_errors.extend(f"record[{index}] {item}" for item in validate_against_schema(record, "source-record.schema.json"))
    if source_errors:
        raise ScriptError("Source validation failed: " + " | ".join(source_errors), 3)

    nodes = []
    for record in sorted(records, key=lambda item: item["source_id"]):
        node = {field: record.get(field) for field in NODE_FIELDS}
        node["evidence_types"] = []
        nodes.append(node)
    ids = {node["source_id"] for node in nodes}
    edges = []
    if args.edges:
        payload = json.loads(args.edges.read_text(encoding="utf-8-sig"))
        edges = records_from_payload(payload, "edges")
        edge_ids = set()
        for index, edge in enumerate(edges):
            if edge.get("edge_id") in edge_ids:
                raise ScriptError(f"Duplicate edge_id: {edge.get('edge_id')}", 3)
            edge_ids.add(edge.get("edge_id"))
            if edge.get("from_source_id") not in ids or edge.get("to_source_id") not in ids:
                raise ScriptError(f"edge[{index}] references an unknown Source_ID", 3)
            if edge.get("from_source_id") == edge.get("to_source_id"):
                raise ScriptError(f"edge[{index}] cannot be a self-edge", 3)
            if not str(edge.get("basis") or "").strip():
                raise ScriptError(f"edge[{index}] lacks an evidence basis", 3)

    identity = "|".join(sorted(ids)).encode("utf-8")
    literature_map = {
        "schema_version": "1.0.0",
        "map_id": args.map_id or "LM-" + hashlib.sha256(identity).hexdigest()[:12].upper(),
        "project_id": args.project_id,
        "generated_at": utc_now(),
        "nodes": nodes,
        "edges": sorted(edges, key=lambda item: item["edge_id"]),
        "views": VIEWS,
    }
    errors = validate_against_schema(literature_map, "literature-map.schema.json")
    if errors:
        raise ScriptError("Literature map validation failed: " + " | ".join(errors), 3)
    write_json(args.output, literature_map, overwrite=False)
    print(json.dumps({"status": "OK", "nodes": len(nodes), "edges": len(edges), "relationships_inferred": False}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
