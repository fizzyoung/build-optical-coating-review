from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

WORKSPACE = Path(__file__).resolve().parents[2]
SKILL = WORKSPACE / "build-optical-coating-review"
SCRIPTS = SKILL / "scripts"
SCRIPT_NAMES = [
    "init_project.py",
    "transition_state.py",
    "validate_project.py",
    "import_records.py",
    "deduplicate_records.py",
    "validate_metadata.py",
    "build_literature_map.py",
    "audit_claims.py",
    "audit_figures_tables.py",
    "version_output.py",
    "build_full_skill.py",
    "check_distribution_parity.py",
]


def run_script(name: str, *arguments: object, expected: int = 0) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONUTF8"] = "1"
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / name), *map(str, arguments)],
        text=True,
        encoding="utf-8",
        capture_output=True,
        env=environment,
        timeout=90,
        check=False,
    )
    if result.returncode != expected:
        raise AssertionError(
            f"{name} returned {result.returncode}, expected {expected}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def source(source_id: str, *, doi: str | None = None, title: str = "DLC coating", level: str = "V4") -> dict:
    return {
        "schema_version": "1.0.0",
        "source_id": source_id,
        "title": title,
        "authors": ["A. Author"],
        "year": 2024,
        "journal": "Example Journal",
        "document_type": "JOURNAL_ARTICLE",
        "doi": doi,
        "url": None,
        "language": "en",
        "database_sources": ["fixture"],
        "record_version": "1",
        "supersedes_source_id": None,
        "verification_level": level,
        "verification_date": "2026-07-26",
        "full_text_status": "AVAILABLE",
        "screening_decision": "INCLUDE",
        "screening_reason": None,
        "materials": ["DLC"],
        "substrates": ["chalcogenide glass"],
        "coatings": ["a-C:H"],
        "deposition_routes": ["PECVD"],
        "interface_strategies": [],
        "optical_properties": ["transmittance"],
        "mechanical_properties": ["adhesion"],
        "environmental_properties": [],
        "manufacturing_properties": [],
        "characterization_methods": ["FTIR"],
        "themes": ["infrared protection"],
        "research_stage": "laboratory",
        "intended_uses": ["CORE"],
        "evidence_strength": "STRONG",
        "notes": None,
    }


class ScriptTests(unittest.TestCase):
    def test_all_scripts_support_help(self):
        for name in SCRIPT_NAMES:
            with self.subTest(name=name):
                run_script(name, "--help")

    def test_project_state_transitions_validation_and_versioning(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "review"
            run_script("init_project.py", root, "--project-id", "PRJ-TEST", "--title", "Test review")
            self.assertEqual(9, len(list((root / "_project_control" / "schemas").glob("*.schema.json"))))
            run_script("validate_project.py", root)
            run_script(
                "transition_state.py", root, "STEP-00", "--to", "APPROVED",
                "--decision-text", "确认通过", expected=4,
            )
            run_script("transition_state.py", root, "STEP-00", "--to", "IN_PROGRESS")
            output = root / "00_preflight" / "outputs" / "preflight.md"
            output.write_text("verified", encoding="utf-8")
            run_script(
                "transition_state.py", root, "STEP-00", "--to", "REVIEW_REQUIRED",
                "--quality-gate", "pass", "--output", output.relative_to(root),
            )
            run_script(
                "transition_state.py", root, "STEP-00", "--to", "APPROVED",
                "--decision-text", "确认通过", "--decided-by", "test-user",
            )
            run_script("validate_project.py", root)
            output.write_text("tampered", encoding="utf-8")
            run_script("validate_project.py", root, expected=3)
            output.write_text("verified", encoding="utf-8")
            versions = root / "_archive" / "versions"
            run_script("version_output.py", output, versions)
            run_script("version_output.py", output, versions)
            self.assertTrue((versions / "preflight.v001.md").is_file())
            self.assertTrue((versions / "preflight.v002.md").is_file())
            run_script("version_output.py", output, versions, "--version", "v001", expected=4)

    def test_task_21b_requires_current_chapter(self):
        with tempfile.TemporaryDirectory() as directory:
            import yaml

            root = Path(directory) / "review"
            run_script("init_project.py", root, "--project-id", "PRJ-21B", "--title", "Chapter gate")
            state_path = root / "project_state.yaml"
            state = yaml.safe_load(state_path.read_text(encoding="utf-8"))
            for task in state["tasks"] + state["task_21_subtasks"]:
                if task["task_id"] in {"TASK-20", "TASK-21A"}:
                    task["status"] = "APPROVED"
            state_path.write_text(yaml.safe_dump(state, sort_keys=False, allow_unicode=True), encoding="utf-8")
            run_script("transition_state.py", root, "TASK-21B", "--to", "IN_PROGRESS", expected=4)

    def test_import_csv_and_deduplicate_exact_doi(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_path = root / "records.csv"
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Title", "Authors", "Year", "Journal", "DOI"])
                writer.writeheader()
                writer.writerow({"Title": "DLC on glass", "Authors": "A;B", "Year": "2024", "Journal": "J", "DOI": "https://doi.org/10.1000/test"})
                writer.writerow({"Title": "DLC on glass", "Authors": "A;B", "Year": "2024", "Journal": "J", "DOI": "10.1000/TEST"})
            imported = root / "imported.json"
            run_script("import_records.py", csv_path, imported, "--database", "fixture", "--query-id", "Q-1")
            records = json.loads(imported.read_text(encoding="utf-8"))
            self.assertEqual(2, len({item["source_id"] for item in records}))
            deduplicated = root / "deduplicated.json"
            run_script("deduplicate_records.py", imported, deduplicated)
            payload = json.loads(deduplicated.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["counts"]["retained"])
            self.assertEqual("DUPLICATE_OF", payload["relations"][0]["relation"])

    def test_import_rejects_reused_explicit_source_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw.json"
            first = source("SRC-SAME", doi="10.1000/one", title="One")
            second = source("SRC-SAME", doi="10.1000/two", title="Two")
            write_json(raw, [first, second])
            run_script("import_records.py", raw, root / "out.json", expected=3)

    def test_title_conflict_keeps_both_records_unmodified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = source("SRC-FIRST", doi="10.1000/first", title="Same title")
            second = source("SRC-SECOND", doi="10.1000/second", title="Same title")
            second["journal"] = "Other Journal"
            source_path = root / "sources.json"
            output = root / "dedup.json"
            write_json(source_path, [first, second])
            run_script("deduplicate_records.py", source_path, output)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(2, result["counts"]["retained"])
            self.assertEqual(1, result["counts"]["manual_review"])
            retained = {item["source_id"]: item for item in result["records"]}
            self.assertEqual("Example Journal", retained["SRC-FIRST"]["journal"])

    def test_import_ris_bibtex_endnote_and_xlsx(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixtures = {
                "sample.ris": "TY  - JOUR\nTI  - RIS title\nAU  - A. Author\nPY  - 2024\nDO  - 10.1000/ris\nER  -\n",
                "sample.bib": "@article{x, title={Bib title}, author={A. Author and B. Author}, year={2023}, doi={10.1000/bib}}\n",
                "sample.xml": "<xml><records><record><ref-type>Journal Article</ref-type><contributors><authors><author>A. Author</author></authors></contributors><titles><title>XML title</title></titles><dates><year>2022</year></dates><electronic-resource-num>10.1000/xml</electronic-resource-num></record></records></xml>",
            }
            for name, text in fixtures.items():
                input_path = root / name
                input_path.write_text(text, encoding="utf-8")
                run_script("import_records.py", input_path, root / f"{name}.json")
            from openpyxl import Workbook

            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Source Registry"
            sheet.append(["Title", "Authors", "Year", "DOI"])
            sheet.append(["XLSX title", "A. Author", 2021, "10.1000/xlsx"])
            xlsx = root / "sample.xlsx"
            workbook.save(xlsx)
            run_script("import_records.py", xlsx, root / "xlsx.json")

    def test_local_metadata_validation_does_not_infer_external_values(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = root / "records.json"
            output = root / "metadata.json"
            write_json(records, [source("SRC-ONE", doi="10.1000/test")])
            run_script("validate_metadata.py", records, output)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(result["network_enabled"])
            self.assertEqual("NOT_REQUESTED", result["results"][0]["external_status"])
            self.assertIsNone(result["results"][0]["crossref_title"])

    def test_external_metadata_failure_returns_explicit_status_without_network(self):
        if str(SCRIPTS) not in sys.path:
            sys.path.insert(0, str(SCRIPTS))
        import validate_metadata

        with tempfile.TemporaryDirectory() as directory:
            args = SimpleNamespace(cache=Path(directory), timeout=0.1, mailto=None)
            with mock.patch.object(validate_metadata.urllib.request, "urlopen", side_effect=urllib.error.URLError("offline")):
                payload, status, error = validate_metadata.crossref_lookup("10.1000/offline", args)
            self.assertIsNone(payload)
            self.assertEqual("EXTERNAL_CHECK_FAILED", status)
            self.assertIn("offline", error)

    def test_literature_map_uses_only_explicit_edges(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "sources.json"
            edges = root / "edges.json"
            output = root / "map.json"
            write_json(sources, [source("SRC-ONE"), source("SRC-TWO", title="Second")])
            write_json(edges, [{
                "edge_id": "EDGE-ONE", "from_source_id": "SRC-ONE", "to_source_id": "SRC-TWO",
                "relation": "SUPPORTS", "basis": "Full-text comparison", "original_locations": ["p. 4"],
                "verification_level": "V4", "human_status": "ACCEPTED",
            }])
            run_script("build_literature_map.py", sources, output, "--edges", edges, "--project-id", "PRJ-TEST")
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, len(result["edges"]))
            no_edges = root / "map-no-edges.json"
            run_script("build_literature_map.py", sources, no_edges)
            self.assertEqual([], json.loads(no_edges.read_text(encoding="utf-8"))["edges"])

    def test_claim_audit_passes_v4_and_blocks_overclaim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "sources.json"
            write_json(sources, [source("SRC-ONE")])
            valid_claim = {
                "schema_version": "1.0.0", "claim_id": "CLM-3.1-01", "claim_text_zh": "在给定条件下透过率提高。",
                "claim_text_en": None, "claim_type": "QUANTITATIVE",
                "source_links": [{"source_id": "SRC-ONE", "original_location": "p. 4, Fig. 2", "relation": "SUPPORTS", "verification_level": "V4"}],
                "evidence_type": "FIGURE", "evidence_strength": "STRONG", "consistency": "SINGLE_SOURCE",
                "applicability_conditions": ["8-12 um"], "limitations": ["single sample"], "intended_section": "3.1",
                "human_status": "ACCEPTED", "minimum_verification_level": "V4", "notes": None,
            }
            claims = root / "claims.json"
            report = root / "claim-report.json"
            write_json(claims, [valid_claim])
            run_script("audit_claims.py", claims, sources, report)
            invalid = dict(valid_claim)
            invalid["claim_id"] = "CLM-3.1-02"
            invalid["claim_text_en"] = "Raman gives exact sp3 content."
            invalid["minimum_verification_level"] = "V3"
            invalid_path = root / "invalid-claims.json"
            write_json(invalid_path, [invalid])
            run_script("audit_claims.py", invalid_path, sources, root / "invalid-report.json", expected=3)
            v5 = dict(valid_claim)
            v5["claim_id"] = "CLM-3.1-03"
            v5["minimum_verification_level"] = "V5"
            v5_path = root / "v5-claims.json"
            write_json(v5_path, [v5])
            run_script("audit_claims.py", v5_path, sources, root / "v5-report.json", expected=3)

    def test_figure_audit_checks_v4_calculation_and_copyright(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "sources.json"
            write_json(sources, [source("SRC-ONE")])
            trace = {
                "schema_version": "1.0.0", "trace_id": "TRC-ONE", "artifact_id": "FIG-1",
                "artifact_type": "FIGURE_ELEMENT", "element_id": "curve-a", "target_location": "Figure 1",
                "source_id": "SRC-ONE", "original_location": "p. 4, Fig. 2", "transformation": "DIGITIZED",
                "calculation": "Digitized with calibrated axes; raw points retained", "copyright_status": "LICENSED",
                "permission_reference": "CC BY 4.0", "verification_level": "V4", "human_status": "ACCEPTED", "notes": None,
            }
            traces = root / "traces.json"
            write_json(traces, [trace])
            run_script("audit_figures_tables.py", traces, sources, root / "trace-report.json")
            invalid = dict(trace)
            invalid.update(trace_id="TRC-TWO", calculation=None, copyright_status="UNASSESSED")
            invalid_path = root / "invalid-traces.json"
            write_json(invalid_path, [invalid])
            run_script("audit_figures_tables.py", invalid_path, sources, root / "invalid-trace-report.json", expected=3)

    def test_distribution_hash_normalizes_text_line_endings(self):
        if str(SCRIPTS) not in sys.path:
            sys.path.insert(0, str(SCRIPTS))
        import _distribution

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lf_root = root / "lf"
            crlf_root = root / "crlf"
            fixtures = {
                "SKILL.md": "---\nname: fixture\ndescription: Fixture skill.\n---\n\n# Fixture\n",
                "agents/openai.yaml": "interface:\n  display_name: Fixture\n",
                "references/example.md": "# Example\n\nCanonical text.\n",
            }
            for relative, text in fixtures.items():
                lf_path = lf_root / relative
                crlf_path = crlf_root / relative
                lf_path.parent.mkdir(parents=True, exist_ok=True)
                crlf_path.parent.mkdir(parents=True, exist_ok=True)
                lf_path.write_bytes(text.encode("utf-8"))
                crlf_path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
            self.assertEqual(_distribution.source_hash(lf_root), _distribution.source_hash(crlf_root))
            self.assertEqual(_distribution.source_manifest(lf_root), _distribution.source_manifest(crlf_root))

    def test_portable_builder_is_reproducible_and_parity_detects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "full-1.md"
            second = root / "full-2.md"
            stamp = "2026-07-26T00:00:00Z"
            run_script("build_full_skill.py", SKILL, first, "--generated-at", stamp)
            run_script("build_full_skill.py", SKILL, second, "--generated-at", stamp)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            portable_text = first.read_text(encoding="utf-8")
            self.assertNotIn("](references/", portable_text)
            self.assertIn('<a id="module-references-state-machine-md"></a>', portable_text)
            anchors = set(re.findall(r'<a id="([^"]+)"></a>', portable_text))
            fenced = False
            body_links = []
            for line in portable_text.splitlines():
                if line.startswith(chr(96) * 3):
                    fenced = not fenced
                    continue
                if not fenced:
                    body_links.extend(re.findall(r"\]\(#([^)]+)\)", line))
            self.assertEqual([], sorted(set(body_links) - anchors))
            run_script("check_distribution_parity.py", SKILL, first)
            tampered = root / "tampered.md"
            tampered.write_text(first.read_text(encoding="utf-8").replace("Source_ID", "Removed_ID", 1), encoding="utf-8")
            run_script("check_distribution_parity.py", SKILL, tampered, expected=3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
