from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import (
    EXIT_CONFLICT,
    ScriptError,
    append_jsonl_atomic,
    load_data,
    run_cli,
    sha256_file,
    utc_now,
    validate_against_schema,
    write_data,
)

STATUSES = [
    "NOT_STARTED",
    "IN_PROGRESS",
    "BLOCKED",
    "REVIEW_REQUIRED",
    "APPROVED",
    "REJECTED",
    "SKIPPED_WITH_RISK",
    "SUPERSEDED",
    "ARCHIVED",
]
DIRECT_TRANSITIONS = {
    "NOT_STARTED": {"IN_PROGRESS", "BLOCKED"},
    "IN_PROGRESS": {"REVIEW_REQUIRED", "BLOCKED"},
    "REVIEW_REQUIRED": {"APPROVED", "REJECTED", "IN_PROGRESS", "SKIPPED_WITH_RISK", "BLOCKED"},
    "REJECTED": {"IN_PROGRESS", "BLOCKED"},
    "APPROVED": {"SUPERSEDED"},
    "SKIPPED_WITH_RISK": {"SUPERSEDED"},
    "SUPERSEDED": {"ARCHIVED"},
    "ARCHIVED": set(),
}
ACCEPTED_PREREQUISITES = {"APPROVED", "SKIPPED_WITH_RISK"}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Apply one legal, auditable project-state transition.")
    result.add_argument("project_root", type=Path)
    result.add_argument("task_id", help="STEP-00, TASK-01..TASK-20, or TASK-21A..TASK-21H")
    result.add_argument("--to", required=True, choices=STATUSES)
    result.add_argument("--quality-gate", choices=["pass", "fail"])
    result.add_argument("--decision-text")
    result.add_argument("--decided-by", default="user")
    result.add_argument("--risk-id")
    result.add_argument("--blocker-id")
    result.add_argument("--result-id")
    result.add_argument("--output", action="append", default=[])
    result.add_argument("--current-chapter")
    result.add_argument("--reason")
    return result


def all_task_records(state: dict) -> list[dict]:
    return list(state["tasks"]) + list(state["task_21_subtasks"])


def find_task(state: dict, task_id: str) -> dict:
    for task in all_task_records(state):
        if task["task_id"] == task_id:
            return task
    raise ScriptError(f"Unknown task_id: {task_id}", 2)


def explicit_decision(target: str, text: str | None) -> bool:
    value = (text or "").strip()
    if target == "APPROVED":
        return value == "进入下一步" or "确认通过" in value or value.upper() == "APPROVED" or value.startswith("批准")
    if target == "REJECTED":
        return "拒绝" in value or value.startswith("修改：") or value.upper() == "REJECTED"
    if target == "SKIPPED_WITH_RISK":
        return "跳过" in value and "风险" in value
    return True


def blocked_origin(log_path: Path, task_id: str) -> str | None:
    if not log_path.exists():
        return None
    entries = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            entries.append(json.loads(line))
    for entry in reversed(entries):
        if entry.get("task_id") == task_id and entry.get("to_status") == "BLOCKED":
            return entry.get("from_status")
    return None


def task_directory(project_root: Path, task_id: str) -> Path | None:
    if task_id == "STEP-00":
        return project_root / "00_preflight"
    if task_id.startswith("TASK-21"):
        return project_root / "21_manuscript_submission_revision" / task_id.replace("TASK-", "")
    number = int(task_id.split("-")[1])
    matches = sorted(project_root.glob(f"{number:02d}_*"))
    return matches[0] if len(matches) == 1 else None


def stage_for(task_id: str) -> str:
    if task_id == "STEP-00":
        return "STEP_00"
    if task_id.startswith("TASK-21"):
        return "STAGE_4"
    number = int(task_id.split("-")[1])
    if number <= 5:
        return "STAGE_1"
    if number <= 15:
        return "STAGE_2"
    return "STAGE_3"


def sync_task_status(project_root: Path, task_id: str, target: str, task: dict, approval: dict | None) -> None:
    directory = task_directory(project_root, task_id)
    if directory is None:
        return
    path = directory / "task_status.yaml"
    if not path.exists():
        return
    status = load_data(path)
    now = utc_now()
    status["status"] = target
    status["result_id"] = task.get("result_id")
    if target == "IN_PROGRESS" and status.get("started_at") is None:
        status["started_at"] = now
    if target == "REVIEW_REQUIRED":
        status["completed_at"] = now
    status["quality_gate"]["passed"] = task.get("quality_gate_passed")
    if task.get("quality_gate_passed") is not None:
        status["quality_gate"]["checked_at"] = now
    status["approval"] = approval
    output_records = []
    for relative in task.get("output_paths", []):
        full = (project_root / relative).resolve()
        output_records.append(
            {
                "path": relative,
                "role": "task_output",
                "sha256": sha256_file(full) if full.is_file() else None,
                "version": None,
            }
        )
    status["outputs"] = output_records
    write_data(path, status)


def main() -> int:
    args = parser().parse_args()
    project_root = args.project_root.resolve()
    state_path = project_root / "project_state.yaml"
    log_path = project_root / "_project_control" / "state_transition_log.jsonl"
    state = load_data(state_path)
    errors = validate_against_schema(state, "project-state.schema.json")
    if errors:
        raise ScriptError("Project state is invalid before transition: " + " | ".join(errors))
    task = find_task(state, args.task_id)
    source = task["status"]
    target = args.to

    legal = target in DIRECT_TRANSITIONS.get(source, set())
    if source == "BLOCKED":
        legal = target == blocked_origin(log_path, args.task_id)
    if not legal:
        raise ScriptError(f"Illegal state transition: {source} -> {target}", EXIT_CONFLICT)

    if source == "NOT_STARTED" and target == "IN_PROGRESS":
        for prerequisite in task["prerequisites"]:
            prerequisite_state = find_task(state, prerequisite)["status"]
            if prerequisite_state not in ACCEPTED_PREREQUISITES:
                raise ScriptError(
                    f"Prerequisite {prerequisite} is {prerequisite_state}, not approved or risk-waived",
                    EXIT_CONFLICT,
                )
    if args.quality_gate is not None:
        task["quality_gate_passed"] = args.quality_gate == "pass"
    if source == "IN_PROGRESS" and target == "REVIEW_REQUIRED" and task["quality_gate_passed"] is None:
        raise ScriptError("A quality gate must be recorded before REVIEW_REQUIRED", EXIT_CONFLICT)
    if target == "APPROVED" and task["quality_gate_passed"] is not True:
        raise ScriptError("APPROVED requires a passed quality gate; use SKIPPED_WITH_RISK for an explicit waiver", EXIT_CONFLICT)
    if target in {"APPROVED", "REJECTED", "SKIPPED_WITH_RISK"} and not explicit_decision(target, args.decision_text):
        raise ScriptError(f"An explicit user decision is required for {target}", EXIT_CONFLICT)
    if target == "SKIPPED_WITH_RISK" and not args.risk_id:
        raise ScriptError("SKIPPED_WITH_RISK requires --risk-id", EXIT_CONFLICT)
    if target == "BLOCKED" and not args.blocker_id:
        raise ScriptError("BLOCKED requires --blocker-id", EXIT_CONFLICT)
    if target in {"SUPERSEDED", "ARCHIVED"} and not args.reason:
        raise ScriptError(f"{target} requires --reason", EXIT_CONFLICT)
    chapter = args.current_chapter or state.get("current_chapter")
    if args.task_id == "TASK-21B" and target in {"IN_PROGRESS", "REVIEW_REQUIRED"} and not chapter:
        raise ScriptError("TASK-21B requires --current-chapter before work or review can begin", EXIT_CONFLICT)

    now = utc_now()
    outputs = list(dict.fromkeys(task.get("output_paths", []) + args.output))
    approval = None
    if target in {"APPROVED", "REJECTED", "SKIPPED_WITH_RISK"}:
        approval = {
            "decision": target,
            "decision_text": args.decision_text.strip(),
            "decided_by": args.decided_by,
            "decided_at": now,
            "output_paths": outputs,
            "risk_id": args.risk_id,
        }
        task["approval"] = approval
        state["last_user_decision"] = approval
    task.update(
        status=target,
        output_paths=outputs,
        blocker_id=args.blocker_id if target == "BLOCKED" else None,
        result_id=args.result_id or task.get("result_id"),
        updated_at=now,
    )
    if args.risk_id and args.risk_id not in state["risk_ids"]:
        state["risk_ids"].append(args.risk_id)
    if target == "APPROVED":
        state["approved_task"] = args.task_id
        state["last_approved_output"] = outputs[-1] if outputs else None
    state.update(
        project_status=target,
        current_stage=stage_for(args.task_id),
        current_task=args.task_id,
        current_subtask=args.task_id if args.task_id.startswith("TASK-21") else None,
        current_chapter=chapter if args.task_id == "TASK-21B" else state.get("current_chapter"),
        paused=target in {"BLOCKED", "REVIEW_REQUIRED"},
        pause_reason=args.reason if target == "BLOCKED" else ("Awaiting explicit user approval" if target == "REVIEW_REQUIRED" else None),
        updated_at=now,
    )
    errors = validate_against_schema(state, "project-state.schema.json")
    if errors:
        raise ScriptError("Transition would create invalid state: " + " | ".join(errors))
    write_data(state_path, state)
    sync_task_status(project_root, args.task_id, target, task, approval)
    append_jsonl_atomic(
        log_path,
        {
            "task_id": args.task_id,
            "from_status": source,
            "to_status": target,
            "changed_at": now,
            "decision_text": args.decision_text,
            "risk_id": args.risk_id,
            "blocker_id": args.blocker_id,
            "reason": args.reason,
            "outputs": outputs,
        },
    )
    print(json.dumps({"status": "OK", "task_id": args.task_id, "from": source, "to": target}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
