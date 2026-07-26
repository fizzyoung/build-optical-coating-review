from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from _common import ScriptError, load_data, run_cli, sha256_file, utc_now, write_data

TASK_DIRECTORIES = [
    "00_preflight",
    "01_project_initialization",
    "02_review_type",
    "03_scope_definition",
    "04_existing_reviews",
    "05_topic_evaluation",
    "06_terminology",
    "07_concept_groups",
    "08_database_plan",
    "09_search_queries",
    "10_search_execution",
    "11_metadata_cleaning",
    "12_eligibility_criteria",
    "13_title_abstract_screening",
    "14_full_text_screening",
    "15_library_audit",
    "16_full_text_reading",
    "17_evidence_cards",
    "18_claim_evidence_matrix",
    "19_synthesis_and_gaps",
    "20_outline_and_figures",
]
CONTROL_DIRECTORIES = [
    "_project_control",
    "_source_registry",
    "_master_library",
    "_maps",
    "_templates",
    "_exports",
    "_archive",
]
TASK_CHILDREN = ["inputs", "working", "outputs", "qa", "logs"]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Initialize an evidence-traceable review project without overwriting project data.")
    result.add_argument("destination", type=Path, help="New or resumable project directory")
    result.add_argument("--project-id", required=True, help="Stable project identifier")
    result.add_argument("--title", required=True, help="Project title")
    result.add_argument(
        "--review-type",
        choices=["UNDECIDED", "NARRATIVE_REVIEW", "SYSTEMATIC_REVIEW"],
        default="UNDECIDED",
    )
    result.add_argument("--language", choices=["zh", "en", "bilingual"], default="zh")
    result.add_argument("--resume", action="store_true", help="Create only missing directories and files; never overwrite existing files")
    return result


def copy_missing(source: Path, target: Path) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def initialize_task(directory: Path, task_id: str, template_dir: Path, project_id: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for child in TASK_CHILDREN:
        (directory / child).mkdir(exist_ok=True)

    status_path = directory / "task_status.yaml"
    if not status_path.exists():
        status = load_data(template_dir / "task_status.yaml")
        status["project_id"] = project_id
        status["task_id"] = task_id
        write_data(status_path, status, overwrite=False)
    copy_missing(template_dir / "stage_report.md", directory / "stage_report.md")


def main() -> int:
    args = parser().parse_args()
    destination = args.destination.resolve()
    template_dir = Path(__file__).resolve().parent.parent / "assets" / "templates"
    reference_dir = Path(__file__).resolve().parent.parent / "references"
    if destination.exists() and any(destination.iterdir()) and not args.resume:
        raise ScriptError(f"Destination is not empty; use --resume to preserve existing files: {destination}", 4)
    destination.mkdir(parents=True, exist_ok=True)

    for name in CONTROL_DIRECTORIES:
        (destination / name).mkdir(exist_ok=True)
    for index, name in enumerate(TASK_DIRECTORIES):
        task_id = "STEP-00" if index == 0 else f"TASK-{index:02d}"
        initialize_task(destination / name, task_id, template_dir, args.project_id)

    task_21 = destination / "21_manuscript_submission_revision"
    task_21.mkdir(exist_ok=True)
    for letter in "ABCDEFGH":
        initialize_task(task_21 / f"21{letter}", f"TASK-21{letter}", template_dir, args.project_id)

    state_path = destination / "project_state.yaml"
    if not state_path.exists():
        state = load_data(template_dir / "project_state.yaml")
        now = utc_now()
        state.update(
            project_id=args.project_id,
            project_title=args.title,
            review_type=args.review_type,
            created_at=now,
            updated_at=now,
        )
        write_data(state_path, state, overwrite=False)

    copied_templates: list[str] = []
    for source in sorted(template_dir.iterdir(), key=lambda item: item.name.casefold()):
        if source.is_file():
            target = destination / "_templates" / source.name
            copy_missing(source, target)
            copied_templates.append(target.relative_to(destination).as_posix())

    schema_target = destination / "_project_control" / "schemas"
    schema_target.mkdir(parents=True, exist_ok=True)
    copied_schemas: list[str] = []
    for source in sorted(reference_dir.glob("*.schema.json"), key=lambda item: item.name.casefold()):
        target = schema_target / source.name
        copy_missing(source, target)
        copied_schemas.append(target.relative_to(destination).as_posix())

    manifest_path = destination / "project_manifest.json"
    if not manifest_path.exists():
        manifest = load_data(template_dir / "project_manifest.json")
        now = utc_now()
        manifest.update(
            project_id=args.project_id,
            project_title=args.title,
            review_type=args.review_type,
            language=args.language,
            created_at=now,
            updated_at=now,
            state_file="project_state.yaml",
        )
        manifest["schema_directory"] = "_project_control/schemas"
        manifest["file_hashes"] = {
            relative: sha256_file(destination / relative) for relative in copied_templates + copied_schemas
        }
        write_data(manifest_path, manifest, overwrite=False)

    report = {
        "status": "OK",
        "project_root": str(destination),
        "project_id": args.project_id,
        "task_directories": len(TASK_DIRECTORIES) + 8,
        "templates": len(copied_templates),
        "schemas": len(copied_schemas),
        "resume": args.resume,
    }
    print(__import__("json").dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
