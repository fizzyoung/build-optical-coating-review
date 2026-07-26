from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import (
    EXIT_VALIDATION,
    ScriptError,
    assert_no_secrets,
    load_data,
    run_cli,
    sha256_file,
    validate_against_schema,
)

TASK_DIRS = {
    "STEP-00": "00_preflight",
    "TASK-01": "01_project_initialization",
    "TASK-02": "02_review_type",
    "TASK-03": "03_scope_definition",
    "TASK-04": "04_existing_reviews",
    "TASK-05": "05_topic_evaluation",
    "TASK-06": "06_terminology",
    "TASK-07": "07_concept_groups",
    "TASK-08": "08_database_plan",
    "TASK-09": "09_search_queries",
    "TASK-10": "10_search_execution",
    "TASK-11": "11_metadata_cleaning",
    "TASK-12": "12_eligibility_criteria",
    "TASK-13": "13_title_abstract_screening",
    "TASK-14": "14_full_text_screening",
    "TASK-15": "15_library_audit",
    "TASK-16": "16_full_text_reading",
    "TASK-17": "17_evidence_cards",
    "TASK-18": "18_claim_evidence_matrix",
    "TASK-19": "19_synthesis_and_gaps",
    "TASK-20": "20_outline_and_figures",
}
ACTIVE_STATES = {"IN_PROGRESS", "BLOCKED", "REVIEW_REQUIRED"}
ACCEPTED_PREREQUISITES = {"APPROVED", "SKIPPED_WITH_RISK"}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Validate project structure, state, task records, hashes, and recovery invariants.")
    result.add_argument("project_root", type=Path)
    result.add_argument("--strict", action="store_true", help="Treat warnings as validation failures")
    result.add_argument("--report", type=Path, help="Optional JSON report path")
    return result


def task_path(root: Path, task_id: str) -> Path:
    if task_id.startswith("TASK-21"):
        return root / "21_manuscript_submission_revision" / task_id.replace("TASK-", "")
    return root / TASK_DIRS[task_id]


def main() -> int:
    args = parser().parse_args()
    root = args.project_root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    state_path = root / "project_state.yaml"
    manifest_path = root / "project_manifest.json"
    if not state_path.is_file():
        raise ScriptError(f"Missing project state: {state_path}", EXIT_VALIDATION)
    if not manifest_path.is_file():
        raise ScriptError(f"Missing project manifest: {manifest_path}", EXIT_VALIDATION)

    state = load_data(state_path)
    manifest = load_data(manifest_path)
    for label, value in [("project_state", state), ("project_manifest", manifest)]:
        try:
            assert_no_secrets(value, label)
        except ScriptError as exc:
            errors.append(str(exc))
    errors.extend(f"project_state: {item}" for item in validate_against_schema(state, "project-state.schema.json"))
    if manifest.get("project_id") != state.get("project_id"):
        errors.append("project_id differs between state and manifest")
    if manifest.get("project_title") != state.get("project_title"):
        warnings.append("project_title differs between state and manifest")

    records = list(state.get("tasks", [])) + list(state.get("task_21_subtasks", []))
    by_id = {record.get("task_id"): record for record in records}
    expected = list(TASK_DIRS) + [f"TASK-21{letter}" for letter in "ABCDEFGH"]
    if list(by_id) != expected:
        errors.append("Task register is missing, duplicated, or out of canonical order")

    active = [record["task_id"] for record in records if record.get("status") in ACTIVE_STATES]
    if len(active) > 1:
        errors.append(f"More than one active task exists: {active}")
    if active and state.get("current_task") not in active:
        errors.append("current_task does not identify the sole active task")

    for task_id in expected:
        directory = task_path(root, task_id)
        if not directory.is_dir():
            errors.append(f"Missing task directory: {directory.relative_to(root)}")
            continue
        for child in ["inputs", "working", "outputs", "qa", "logs"]:
            if not (directory / child).is_dir():
                errors.append(f"Missing task child directory: {(directory / child).relative_to(root)}")
        status_path = directory / "task_status.yaml"
        if not status_path.is_file():
            errors.append(f"Missing task_status.yaml for {task_id}")
            continue
        status = load_data(status_path)
        try:
            assert_no_secrets(status, str(status_path.relative_to(root)))
        except ScriptError as exc:
            errors.append(str(exc))
        errors.extend(f"{task_id} task_status: {item}" for item in validate_against_schema(status, "task-result.schema.json"))
        if status.get("task_id") != task_id:
            errors.append(f"{task_id} directory contains task_status for {status.get('task_id')}")
        if status.get("status") != by_id.get(task_id, {}).get("status"):
            errors.append(f"{task_id} status differs between project_state and task_status")
        for output in status.get("outputs", []):
            output_path = (root / output["path"]).resolve()
            if not output_path.is_file():
                errors.append(f"{task_id} output is missing: {output['path']}")
            elif output.get("sha256") and sha256_file(output_path) != output["sha256"]:
                errors.append(f"{task_id} output hash mismatch: {output['path']}")

        task = by_id.get(task_id, {})
        if task.get("status") != "NOT_STARTED":
            for prerequisite in task.get("prerequisites", []):
                status_value = by_id.get(prerequisite, {}).get("status")
                if status_value not in ACCEPTED_PREREQUISITES:
                    errors.append(f"{task_id} advanced while prerequisite {prerequisite} is {status_value}")
        if task.get("status") == "APPROVED" and not task.get("approval"):
            errors.append(f"{task_id} is APPROVED without an approval record")
        for output in task.get("output_paths", []):
            if not (root / output).is_file():
                errors.append(f"{task_id} approved/recorded output is missing: {output}")

    if by_id.get("TASK-21B", {}).get("status") in ACTIVE_STATES and not state.get("current_chapter"):
        errors.append("TASK-21B is active but current_chapter is empty")

    for relative, expected_hash in manifest.get("file_hashes", {}).items():
        full = root / relative
        if not full.is_file():
            errors.append(f"Manifest file is missing: {relative}")
        elif sha256_file(full) != expected_hash:
            warnings.append(f"Manifest hash differs for editable project copy: {relative}")

    report = {
        "status": "FAIL" if errors or (args.strict and warnings) else "PASS",
        "project_root": str(root),
        "tasks_checked": len(expected),
        "active_tasks": active,
        "errors": errors,
        "warnings": warnings,
    }
    text = json.dumps(report, ensure_ascii=False, indent=2)
    print(text)
    if args.report:
        from _common import atomic_write_text

        atomic_write_text(args.report, text + "\n")
    return EXIT_VALIDATION if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    run_cli(main)
