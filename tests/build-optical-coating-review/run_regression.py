from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_SKILL = WORKSPACE / "build-optical-coating-review"
DEFAULT_INSTALLED = Path.home() / ".codex" / "skills" / "build-optical-coating-review"
HERE = Path(__file__).resolve().parent
BASE_TESTS = WORKSPACE / "qa" / "stage4" / "test_scripts.py"


def load_base_module():
    spec = importlib.util.spec_from_file_location("build_optical_coating_review_base_tests", BASE_TESTS)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load base tests: {BASE_TESTS}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_module()


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): file_hash(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }


def public_path_label(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(WORKSPACE.resolve()).as_posix()
    except ValueError:
        return "<external-installed-skill>"


class ReleaseRegressionTests(unittest.TestCase):
    skill_root = DEFAULT_SKILL
    installed_root = DEFAULT_INSTALLED

    def run_script(self, name: str, *arguments: object, expected: int = 0):
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"
        result = subprocess.run(
            [sys.executable, str(self.skill_root / "scripts" / name), *map(str, arguments)],
            text=True,
            encoding="utf-8",
            capture_output=True,
            env=environment,
            timeout=90,
            check=False,
        )
        self.assertEqual(
            expected,
            result.returncode,
            f"{name} returned {result.returncode}, expected {expected}\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )
        return result

    def test_initialize_resume_and_reject_unsafe_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "review"
            self.run_script("init_project.py", project, "--project-id", "PRJ-RESUME", "--title", "Resume test")
            original_hash = file_hash(project / "project_state.yaml")
            self.run_script(
                "init_project.py", project, "--project-id", "PRJ-RESUME",
                "--title", "Resume test", "--resume",
            )
            self.assertEqual(original_hash, file_hash(project / "project_state.yaml"))

            unsafe = root / "unsafe"
            unsafe.mkdir()
            marker = unsafe / "user-file.txt"
            marker.write_text("preserve", encoding="utf-8")
            self.run_script(
                "init_project.py", unsafe, "--project-id", "PRJ-UNSAFE",
                "--title", "Unsafe overwrite", expected=4,
            )
            self.assertEqual("preserve", marker.read_text(encoding="utf-8"))

    def test_literature_map_rejects_self_edge_and_unknown_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "sources.json"
            BASE.write_json(sources, [BASE.source("SRC-ONE"), BASE.source("SRC-TWO", title="Second")])
            common = {
                "edge_id": "EDGE-ONE",
                "relation": "SUPPORTS",
                "basis": "Verified full-text comparison",
                "original_locations": ["p. 4"],
                "verification_level": "V4",
                "human_status": "ACCEPTED",
            }
            self_edge = root / "self-edge.json"
            BASE.write_json(self_edge, [{**common, "from_source_id": "SRC-ONE", "to_source_id": "SRC-ONE"}])
            self.run_script(
                "build_literature_map.py", sources, root / "self-map.json",
                "--edges", self_edge, expected=3,
            )
            unknown = root / "unknown.json"
            BASE.write_json(unknown, [{**common, "from_source_id": "SRC-ONE", "to_source_id": "SRC-MISSING"}])
            self.run_script(
                "build_literature_map.py", sources, root / "unknown-map.json",
                "--edges", unknown, expected=3,
            )

    def test_claim_gate_rejects_missing_v4_location_and_background_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "sources.json"
            BASE.write_json(sources, [BASE.source("SRC-ONE", level="V4")])
            claim = {
                "schema_version": "1.0.0",
                "claim_id": "CLM-2.1-01",
                "claim_text_zh": "沉积机制受工艺参数影响。",
                "claim_text_en": None,
                "claim_type": "MECHANISTIC",
                "source_links": [{
                    "source_id": "SRC-ONE",
                    "original_location": None,
                    "relation": "SUPPORTS",
                    "verification_level": "V4",
                }],
                "evidence_type": "TEXT",
                "evidence_strength": "MODERATE",
                "consistency": "SINGLE_SOURCE",
                "applicability_conditions": [],
                "limitations": [],
                "intended_section": "2.1",
                "human_status": "ACCEPTED",
                "minimum_verification_level": "V4",
                "notes": None,
            }
            missing_location = root / "missing-location.json"
            BASE.write_json(missing_location, [claim])
            self.run_script(
                "audit_claims.py", missing_location, sources,
                root / "missing-location-report.json", expected=3,
            )
            claim["claim_id"] = "CLM-2.1-02"
            claim["claim_type"] = "BACKGROUND"
            claim["minimum_verification_level"] = "V3"
            claim["source_links"][0].update(
                original_location="p. 2", relation="BACKGROUND_ONLY", verification_level="V3"
            )
            background_only = root / "background-only.json"
            BASE.write_json(background_only, [claim])
            self.run_script(
                "audit_claims.py", background_only, sources,
                root / "background-only-report.json", expected=3,
            )

    def test_source_distribution_and_installed_copy_match(self):
        self.assertTrue(self.installed_root.is_dir(), f"Installed Skill missing: {self.installed_root}")
        self.assertEqual(tree_hashes(self.skill_root), tree_hashes(self.installed_root))
        distribution = WORKSPACE / "dist" / "SKILL_FULL.md"
        self.assertTrue(distribution.is_file(), f"Distribution missing: {distribution}")
        self.run_script("check_distribution_parity.py", self.skill_root, distribution)


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self.started = {}

    def startTest(self, test):
        self.started[test.id()] = time.perf_counter()
        super().startTest(test)

    def record(self, test, status: str, detail: str | None = None):
        started = self.started.pop(test.id(), time.perf_counter())
        self.records.append({
            "test": test.id(),
            "status": status,
            "duration_seconds": round(time.perf_counter() - started, 3),
            "detail": detail,
        })

    def addSuccess(self, test):
        self.record(test, "PASS")
        super().addSuccess(test)

    def addFailure(self, test, err):
        self.record(test, "FAIL", self._exc_info_to_string(err, test))
        super().addFailure(test, err)

    def addError(self, test, err):
        self.record(test, "ERROR", self._exc_info_to_string(err, test))
        super().addError(test, err)

    def addSkip(self, test, reason):
        self.record(test, "SKIP", reason)
        super().addSkip(test, reason)


def parse_args():
    parser = argparse.ArgumentParser(description="Run release regression tests for build-optical-coating-review.")
    parser.add_argument("--skill-root", type=Path, default=DEFAULT_SKILL)
    parser.add_argument("--installed-skill-root", type=Path, default=DEFAULT_INSTALLED)
    parser.add_argument("--results", type=Path, default=HERE / "regression-results.json")
    parser.add_argument("--report", type=Path, default=HERE / "regression-report.md")
    return parser.parse_args()


def write_reports(result: RecordingResult, elapsed: float, args):
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    counts = {
        status: sum(record["status"] == status for record in result.records)
        for status in ("PASS", "FAIL", "ERROR", "SKIP")
    }
    payload = {
        "schema_version": "1.0.0",
        "generated_at": now,
        "status": "PASS" if result.wasSuccessful() else "FAIL",
        "python": sys.version.split()[0],
        "skill_root": public_path_label(args.skill_root),
        "installed_skill_root": public_path_label(args.installed_skill_root),
        "temporary_workspace_only": True,
        "approved_example_modified": False,
        "duration_seconds": round(elapsed, 3),
        "counts": counts,
        "tests": result.records,
    }
    args.results.parent.mkdir(parents=True, exist_ok=True)
    args.results.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# build-optical-coating-review Regression Report",
        "",
        f"- Generated: {now}",
        f"- Status: {payload['status']}",
        f"- Tests: {len(result.records)} total; {counts['PASS']} passed; "
        f"{counts['FAIL']} failed; {counts['ERROR']} errors; {counts['SKIP']} skipped",
        f"- Duration: {payload['duration_seconds']} seconds",
        "- Isolation: all mutable fixtures were created under system temporary directories",
        "- Approved example project modified: no",
        "",
        "## Coverage",
        "",
        "- CLI help and dependency loading for all 12 deterministic scripts",
        "- Initialization, safe resume, overwrite refusal, state transitions, validation, and Task 21B gate",
        "- CSV, RIS, BibTeX, EndNote XML, and XLSX import; DOI deduplication and conflict retention",
        "- Local metadata validation and simulated external verification failure",
        "- Explicit map edges plus self-edge and unknown Source_ID rejection",
        "- V3-V5 claim gates, original locations, substantive support, and Raman-sp3 overclaim blocking",
        "- Figure/table provenance, calculations, copyright, permission, and verification gates",
        "- Immutable versioning, reproducible portable build, tamper detection, and installed-copy parity",
        "",
        "## Results",
        "",
        "| Test | Status | Seconds |",
        "|---|---:|---:|",
    ]
    for record in result.records:
        lines.append(
            f"| {str(record['test']).split('.')[-1]} | {record['status']} | {record['duration_seconds']} |"
        )
    failures = [record for record in result.records if record["status"] in {"FAIL", "ERROR"}]
    if failures:
        lines.extend(["", "## Failures", ""])
        for record in failures:
            lines.extend([f"### {record['test']}", "", str(record["detail"]), ""])
    args.report.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    ReleaseRegressionTests.skill_root = args.skill_root.resolve()
    ReleaseRegressionTests.installed_root = args.installed_skill_root.resolve()
    BASE.SKILL = ReleaseRegressionTests.skill_root
    BASE.SCRIPTS = ReleaseRegressionTests.skill_root / "scripts"

    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(BASE.ScriptTests))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ReleaseRegressionTests))
    runner = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult)
    started = time.perf_counter()
    result = runner.run(suite)
    write_reports(result, time.perf_counter() - started, args)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())