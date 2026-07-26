---
name: build-optical-coating-review
description: Build evidence-traceable optical-coating literature review projects. Use for Chinese or English literature search and screening, SCI Narrative Review or Systematic Review planning, full-paper reading, evidence cards, literature maps, claim-evidence matrices, synthesis, review outlines and figures, section-by-section writing, citation audits, journal selection, submission, or revision involving optical coatings, infrared chalcogenide glass, DLC, optical thin films, or related materials research.
---

# Build Optical Coating Review

Build a persistent, approval-gated literature review in which sources, claims, figures, tables, decisions, and risks remain auditable. Default to Chinese process reports while preserving original English titles, terms, formulas, and citations.

## Start Here

1. Read [references/state-machine.md](references/state-machine.md) before creating or resuming a project.
2. Read [references/schema-and-template-map.md](references/schema-and-template-map.md) before editing structured data.
3. Copy the required files from `assets/templates/` into a new project directory; never edit the installed templates as project data.
4. Complete Step 00 database and environment preflight before Task 01.
5. Execute one task at a time by default. End at `REVIEW_REQUIRED`, report results, and pause for explicit approval.

Do not treat acknowledgements such as “好的” as approval. Only an unambiguous decision such as `确认通过`, a task-specific approval, or `进入下一步` with exactly one pending gate may advance state.

## State and Recovery

Validate project state against [project-state.schema.json](references/project-state.schema.json). Use [task-result.schema.json](references/task-result.schema.json) for task results. Task 21A-21H are independent resumable records; Task 21B also records and gates each chapter.

On resume, restore in this order: project state, approved task records, latest approved outputs and hashes, risks, manual checks, current input, then the user's last formal decision. Stop on conflict. Approved outputs are immutable; create a new version and later mark the old one `SUPERSEDED`.

`stage_batch` must pause immediately for login, VPN, CAPTCHA, missing full text, metadata conflict, academic judgment, insufficient evidence, failed gates, manual checks, or conflict with approved work.

## Evidence Contract

- Assign every literature record a stable `Source_ID`.
- Assign every substantive manuscript claim a `Claim_ID` in the form `CLM-section-sequence`.
- Use V0-V5 verification levels. Core prose facts require at least V3. Mechanisms, quantitative comparisons, and figure/table data require at least V4.
- Separate observed results, author interpretation, author speculation, and Skill synthesis.
- Do not infer an academic relationship from title similarity alone.
- Do not equate Raman fitting directly with precise sp3 content.
- Record figure, figure-element, table, and key-cell provenance with [figure-table-traceability.schema.json](references/figure-table-traceability.schema.json).
- Never invent papers, DOI values, result counts, full-text access, evidence locations, or database capabilities.

## Core Contracts

Use these Schema files as normative field definitions:

- [project-state.schema.json](references/project-state.schema.json)
- [task-result.schema.json](references/task-result.schema.json)
- [source-record.schema.json](references/source-record.schema.json)
- [claim.schema.json](references/claim.schema.json)
- [evidence-card.schema.json](references/evidence-card.schema.json)
- [roadmap-item.schema.json](references/roadmap-item.schema.json)
- [literature-map.schema.json](references/literature-map.schema.json)
- [figure-table-traceability.schema.json](references/figure-table-traceability.schema.json)

Use [common.schema.json](references/common.schema.json) for shared enums and identifiers.

## Core Templates

Use the YAML/JSON/Markdown templates for state, task reporting, structured reading, evidence cards, project diagnosis, project prompts, outline review, and revision tracking. Use the XLSX workbooks for database preflight, research roadmap, literature registry, screening, sources, claims, evidence cards, figure/table traceability, and literature-map nodes and edges. Use `review_outline_template.docx` only after Task 20 approval.

Array-valued XLSX fields use semicolon-delimited text; escape a literal semicolon as `\;`. Normalize workbook rows into JSON before Schema validation.

## Workflow References

Read the reference for the current task before acting. Do not load later-task references unless needed for interface validation or recovery.

- Step 00: [Database and environment preflight](references/task-00-preflight.md)
- Task 01: [Project initialization](references/task-01-project-initialization.md)
- Task 02: [Review type](references/task-02-review-type.md)
- Task 03: [Scope and questions](references/task-03-scope-and-questions.md)
- Task 04: [Existing reviews](references/task-04-existing-reviews.md)
- Task 05: [Topic evaluation](references/task-05-topic-evaluation.md)
- Task 06: [Terminology](references/task-06-terminology.md)
- Task 07: [Concept groups](references/task-07-concept-groups.md)
- Task 08: [Database plan](references/task-08-database-plan.md)
- Task 09: [Search strategies](references/task-09-search-strategies.md)
- Task 10: [Run searches](references/task-10-run-searches.md)
- Task 11: [Metadata cleaning](references/task-11-metadata-cleaning.md)
- Task 12: [Eligibility criteria](references/task-12-eligibility-criteria.md)
- Task 13: [Title and abstract screening](references/task-13-title-abstract-screening.md)
- Task 14: [Full-text screening](references/task-14-full-text-screening.md)
- Task 15: [Library audit](references/task-15-library-audit.md)
- Task 16: [Structured reading](references/task-16-structured-reading.md)
- Task 17: [Evidence cards](references/task-17-evidence-cards.md)
- Task 18: [Claim-evidence matrix](references/task-18-claim-evidence-matrix.md)
- Task 19: [Evidence synthesis](references/task-19-evidence-synthesis.md)
- Task 20: [Outline and figures](references/task-20-outline-and-figures.md)
- Task 21A-21H: [Writing, submission, and revision](references/task-21-writing-submission-revision.md)

## Method and Domain References

- Read [database access and search operations](references/database-access-and-search.md) for Step 00 and Tasks 04, 08, 09, and 10.
- Read [Systematic Review strict branch](references/systematic-review-branch.md) only after Task 02 approves `SYSTEMATIC_REVIEW`.
- Read [optical-coating integrated domain pack](references/optical-coating-integrated.md) for terminology, reading, comparison, evidence gates, and DLC-on-chalcogenide-glass decisions.
- Read [core prompt library](references/prompt-library-core.md) when Task 05 creates the editable project prompt library or a later task updates it. Never use prompts to bypass state or evidence gates.

## Deterministic Scripts

Run scripts from the Skill root through an environment that provides PyYAML, jsonschema, and openpyxl. A uniform verified invocation is:

```powershell
uv run --with PyYAML --with jsonschema --with openpyxl python scripts/<script>.py --help
```

Treat exit code 3 as validation failure, 4 as a state or overwrite conflict, and 5 as an external verification failure. Keep network verification opt-in; use the built-in cache and rate limit, and never pass credentials to a script.

- [init_project.py](scripts/init_project.py): initialize or safely resume the persistent project structure.
- [transition_state.py](scripts/transition_state.py): enforce legal task transitions, approvals, blockers, risks, and chapter state.
- [validate_project.py](scripts/validate_project.py): validate state, task records, files, hashes, prerequisites, and recovery invariants.
- [import_records.py](scripts/import_records.py): import CSV, TSV, XLSX, JSON/Zotero, RIS, BibTeX, and EndNote XML without external inference.
- [deduplicate_records.py](scripts/deduplicate_records.py): merge exact duplicates conservatively and retain conflict/version decisions.
- [validate_metadata.py](scripts/validate_metadata.py): validate locally or explicitly opt into rate-limited, cached Crossref checks.
- [build_literature_map.py](scripts/build_literature_map.py): build nodes and only explicitly supplied, evidenced relationships.
- [audit_claims.py](scripts/audit_claims.py): enforce Claim-Evidence Schema, Source_ID, original-location, and V3-V5 gates.
- [audit_figures_tables.py](scripts/audit_figures_tables.py): audit element/cell provenance, transformations, calculations, and copyright.
- [version_output.py](scripts/version_output.py): create immutable numbered copies and a hash manifest.
- [build_full_skill.py](scripts/build_full_skill.py): deterministically build the portable source document when Stage 5 is approved.
- [check_distribution_parity.py](scripts/check_distribution_parity.py): check source/content hashes and core workflow parity.

## Current Development Boundary

The state machine, core Schema, core templates, Step 00 and Task 01-21H workflow references, database/search method, strict Systematic Review branch, optical-coating domain pack, core prompt library, and 12 deterministic operational scripts are implemented and tested.

The Stage 5 portable `SKILL_FULL.md` artifact is generated outside the installable Skill and verified against modular source and content hashes. Rebuild and re-run parity after every modular source change; never edit the generated file manually.

The modular source package, DLC-on-chalcogenide-glass demonstration project, local Codex installation, and portable distribution artifact are implemented and regression-tested. GitHub publication is not yet implemented; do not claim that a remote repository or release is available until publication is completed and verified.
