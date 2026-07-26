from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from _common import EXIT_VALIDATION, ScriptError, run_cli
from _distribution import source_hash

REQUIRED_TOKENS = [
    "NOT_STARTED", "IN_PROGRESS", "BLOCKED", "REVIEW_REQUIRED", "APPROVED", "REJECTED",
    "SKIPPED_WITH_RISK", "SUPERSEDED", "ARCHIVED", "STEP-00",
    *[f"TASK-{number:02d}" for number in range(1, 21)],
    *[f"TASK-21{letter}" for letter in "ABCDEFGH"],
    "确认通过", "进入下一步", "重新执行当前任务", "查看研究路线图", "查看项目提示词库",
    "查看文献地图", "批量执行当前阶段", "跳过当前门禁并记录风险",
    "Source_ID", "Claim_ID", "V3", "V4", "UNVERIFIED", "Raman", "sp3",
    "project-state.schema.json", "source-record.schema.json", "claim.schema.json",
    "evidence-card.schema.json", "literature-map.schema.json", "figure-table-traceability.schema.json",
    "project_state.yaml", "task_status.yaml", "review_outline_template.docx",
]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Check source hash and core workflow parity between modular Skill and SKILL_FULL.md.")
    result.add_argument("skill_root", type=Path)
    result.add_argument("full_skill", type=Path)
    result.add_argument("--report", type=Path)
    return result


def main() -> int:
    args = parser().parse_args()
    root = args.skill_root.resolve()
    full_path = args.full_skill.resolve()
    if not full_path.is_file():
        raise ScriptError(f"Portable Skill does not exist: {full_path}", 2)
    text = full_path.read_text(encoding="utf-8-sig")
    match = re.search(r"Source SHA-256:\s*`([a-f0-9]{64})`", text)
    actual_hash = source_hash(root)
    recorded_hash = match.group(1) if match else None
    content_match = re.search(r"Portable Content SHA-256:\s*`([a-f0-9]{64})`", text)
    recorded_content_hash = content_match.group(1) if content_match else None
    unhashed_content = text.replace(recorded_content_hash, "__PORTABLE_CONTENT_SHA256__", 1) if recorded_content_hash else text
    actual_content_hash = hashlib.sha256(unhashed_content.encode("utf-8")).hexdigest()
    missing = [token for token in REQUIRED_TOKENS if token not in text]
    errors = []
    if recorded_content_hash != actual_content_hash:
        errors.append({"check": "CONTENT_HASH", "expected": actual_content_hash, "recorded": recorded_content_hash})
    if recorded_hash != actual_hash:
        errors.append({"check": "SOURCE_HASH", "expected": actual_hash, "recorded": recorded_hash})
    if missing:
        errors.append({"check": "REQUIRED_TOKENS", "missing": missing})
    if "GENERATED FILE: DO NOT EDIT" not in text:
        errors.append({"check": "GENERATED_MARKER", "detail": "Missing generated-file marker"})
    report = {
        "status": "FAIL" if errors else "PASS",
        "skill_root": str(root),
        "full_skill": str(full_path),
        "source_sha256": actual_hash,
        "required_tokens": len(REQUIRED_TOKENS),
        "errors": errors,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.report:
        from _common import atomic_write_text

        atomic_write_text(args.report, rendered + "\n")
    return EXIT_VALIDATION if errors else 0


if __name__ == "__main__":
    run_cli(main)
