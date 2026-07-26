Portable Content SHA-256: `cad76bc38d40abbcdaff9d65c0f29362c562f5f270f48c76976d90195ba690e5`
<!-- GENERATED FILE: DO NOT EDIT. Rebuild with scripts/build_full_skill.py. -->
# Build Optical Coating Review - Portable Full Skill

Generated at: `2026-07-26T00:00:00Z`  
Source SHA-256: `9c61ec3d13665aa6c57d4142eb4968e98cff1e383025783223d3913ffe3a8d1a`

This portable document mirrors the modular Skill. The modular Codex Skill remains the authoritative runtime form.

## Module Index

- [`SKILL.md`](#module-skill-md)
- [`agents/openai.yaml`](#module-agents-openai-yaml)
- [`references/claim.schema.json`](#module-references-claim-schema-json)
- [`references/common.schema.json`](#module-references-common-schema-json)
- [`references/database-access-and-search.md`](#module-references-database-access-and-search-md)
- [`references/evidence-card.schema.json`](#module-references-evidence-card-schema-json)
- [`references/figure-table-traceability.schema.json`](#module-references-figure-table-traceability-schema-json)
- [`references/literature-map.schema.json`](#module-references-literature-map-schema-json)
- [`references/optical-coating-integrated.md`](#module-references-optical-coating-integrated-md)
- [`references/project-state.schema.json`](#module-references-project-state-schema-json)
- [`references/prompt-library-core.md`](#module-references-prompt-library-core-md)
- [`references/roadmap-item.schema.json`](#module-references-roadmap-item-schema-json)
- [`references/schema-and-template-map.md`](#module-references-schema-and-template-map-md)
- [`references/source-record.schema.json`](#module-references-source-record-schema-json)
- [`references/state-machine.md`](#module-references-state-machine-md)
- [`references/systematic-review-branch.md`](#module-references-systematic-review-branch-md)
- [`references/task-00-preflight.md`](#module-references-task-00-preflight-md)
- [`references/task-01-project-initialization.md`](#module-references-task-01-project-initialization-md)
- [`references/task-02-review-type.md`](#module-references-task-02-review-type-md)
- [`references/task-03-scope-and-questions.md`](#module-references-task-03-scope-and-questions-md)
- [`references/task-04-existing-reviews.md`](#module-references-task-04-existing-reviews-md)
- [`references/task-05-topic-evaluation.md`](#module-references-task-05-topic-evaluation-md)
- [`references/task-06-terminology.md`](#module-references-task-06-terminology-md)
- [`references/task-07-concept-groups.md`](#module-references-task-07-concept-groups-md)
- [`references/task-08-database-plan.md`](#module-references-task-08-database-plan-md)
- [`references/task-09-search-strategies.md`](#module-references-task-09-search-strategies-md)
- [`references/task-10-run-searches.md`](#module-references-task-10-run-searches-md)
- [`references/task-11-metadata-cleaning.md`](#module-references-task-11-metadata-cleaning-md)
- [`references/task-12-eligibility-criteria.md`](#module-references-task-12-eligibility-criteria-md)
- [`references/task-13-title-abstract-screening.md`](#module-references-task-13-title-abstract-screening-md)
- [`references/task-14-full-text-screening.md`](#module-references-task-14-full-text-screening-md)
- [`references/task-15-library-audit.md`](#module-references-task-15-library-audit-md)
- [`references/task-16-structured-reading.md`](#module-references-task-16-structured-reading-md)
- [`references/task-17-evidence-cards.md`](#module-references-task-17-evidence-cards-md)
- [`references/task-18-claim-evidence-matrix.md`](#module-references-task-18-claim-evidence-matrix-md)
- [`references/task-19-evidence-synthesis.md`](#module-references-task-19-evidence-synthesis-md)
- [`references/task-20-outline-and-figures.md`](#module-references-task-20-outline-and-figures-md)
- [`references/task-21-writing-submission-revision.md`](#module-references-task-21-writing-submission-revision-md)
- [`references/task-result.schema.json`](#module-references-task-result-schema-json)
- [`scripts/_common.py`](#module-scripts-common-py)
- [`scripts/_distribution.py`](#module-scripts-distribution-py)
- [`scripts/audit_claims.py`](#module-scripts-audit-claims-py)
- [`scripts/audit_figures_tables.py`](#module-scripts-audit-figures-tables-py)
- [`scripts/build_core_workbooks.mjs`](#module-scripts-build-core-workbooks-mjs)
- [`scripts/build_full_skill.py`](#module-scripts-build-full-skill-py)
- [`scripts/build_literature_map.py`](#module-scripts-build-literature-map-py)
- [`scripts/build_outline_template.py`](#module-scripts-build-outline-template-py)
- [`scripts/check_distribution_parity.py`](#module-scripts-check-distribution-parity-py)
- [`scripts/deduplicate_records.py`](#module-scripts-deduplicate-records-py)
- [`scripts/import_records.py`](#module-scripts-import-records-py)
- [`scripts/init_project.py`](#module-scripts-init-project-py)
- [`scripts/transition_state.py`](#module-scripts-transition-state-py)
- [`scripts/validate_metadata.py`](#module-scripts-validate-metadata-py)
- [`scripts/validate_project.py`](#module-scripts-validate-project-py)
- [`scripts/version_output.py`](#module-scripts-version-output-py)
- [`assets/templates/evidence_and_claims.xlsx`](#module-assets-templates-evidence-and-claims-xlsx)
- [`assets/templates/evidence_card.md`](#module-assets-templates-evidence-card-md)
- [`assets/templates/literature_map.xlsx`](#module-assets-templates-literature-map-xlsx)
- [`assets/templates/literature_registry.xlsx`](#module-assets-templates-literature-registry-xlsx)
- [`assets/templates/outline_review_report.md`](#module-assets-templates-outline-review-report-md)
- [`assets/templates/preflight_and_roadmap.xlsx`](#module-assets-templates-preflight-and-roadmap-xlsx)
- [`assets/templates/project_diagnosis.md`](#module-assets-templates-project-diagnosis-md)
- [`assets/templates/project_manifest.json`](#module-assets-templates-project-manifest-json)
- [`assets/templates/project_state.yaml`](#module-assets-templates-project-state-yaml)
- [`assets/templates/prompt_library.md`](#module-assets-templates-prompt-library-md)
- [`assets/templates/reading_note.md`](#module-assets-templates-reading-note-md)
- [`assets/templates/review_outline_template.docx`](#module-assets-templates-review-outline-template-docx)
- [`assets/templates/revision_recommendations.md`](#module-assets-templates-revision-recommendations-md)
- [`assets/templates/stage_report.md`](#module-assets-templates-stage-report-md)
- [`assets/templates/task_status.yaml`](#module-assets-templates-task-status-yaml)

<a id="module-skill-md"></a>
## Module: `SKILL.md`

---
name: build-optical-coating-review
description: Build evidence-traceable optical-coating literature review projects. Use for Chinese or English literature search and screening, SCI Narrative Review or Systematic Review planning, full-paper reading, evidence cards, literature maps, claim-evidence matrices, synthesis, review outlines and figures, section-by-section writing, citation audits, journal selection, submission, or revision involving optical coatings, infrared chalcogenide glass, DLC, optical thin films, or related materials research.
---

### Build Optical Coating Review

Build a persistent, approval-gated literature review in which sources, claims, figures, tables, decisions, and risks remain auditable. Default to Chinese process reports while preserving original English titles, terms, formulas, and citations.

#### Start Here

1. Read [references/state-machine.md](#module-references-state-machine-md) before creating or resuming a project.
2. Read [references/schema-and-template-map.md](#module-references-schema-and-template-map-md) before editing structured data.
3. Copy the required files from `assets/templates/` into a new project directory; never edit the installed templates as project data.
4. Complete Step 00 database and environment preflight before Task 01.
5. Execute one task at a time by default. End at `REVIEW_REQUIRED`, report results, and pause for explicit approval.

Do not treat acknowledgements such as “好的” as approval. Only an unambiguous decision such as `确认通过`, a task-specific approval, or `进入下一步` with exactly one pending gate may advance state.

#### State and Recovery

Validate project state against [project-state.schema.json](#module-references-project-state-schema-json). Use [task-result.schema.json](#module-references-task-result-schema-json) for task results. Task 21A-21H are independent resumable records; Task 21B also records and gates each chapter.

On resume, restore in this order: project state, approved task records, latest approved outputs and hashes, risks, manual checks, current input, then the user's last formal decision. Stop on conflict. Approved outputs are immutable; create a new version and later mark the old one `SUPERSEDED`.

`stage_batch` must pause immediately for login, VPN, CAPTCHA, missing full text, metadata conflict, academic judgment, insufficient evidence, failed gates, manual checks, or conflict with approved work.

#### Evidence Contract

- Assign every literature record a stable `Source_ID`.
- Assign every substantive manuscript claim a `Claim_ID` in the form `CLM-section-sequence`.
- Use V0-V5 verification levels. Core prose facts require at least V3. Mechanisms, quantitative comparisons, and figure/table data require at least V4.
- Separate observed results, author interpretation, author speculation, and Skill synthesis.
- Do not infer an academic relationship from title similarity alone.
- Do not equate Raman fitting directly with precise sp3 content.
- Record figure, figure-element, table, and key-cell provenance with [figure-table-traceability.schema.json](#module-references-figure-table-traceability-schema-json).
- Never invent papers, DOI values, result counts, full-text access, evidence locations, or database capabilities.

#### Core Contracts

Use these Schema files as normative field definitions:

- [project-state.schema.json](#module-references-project-state-schema-json)
- [task-result.schema.json](#module-references-task-result-schema-json)
- [source-record.schema.json](#module-references-source-record-schema-json)
- [claim.schema.json](#module-references-claim-schema-json)
- [evidence-card.schema.json](#module-references-evidence-card-schema-json)
- [roadmap-item.schema.json](#module-references-roadmap-item-schema-json)
- [literature-map.schema.json](#module-references-literature-map-schema-json)
- [figure-table-traceability.schema.json](#module-references-figure-table-traceability-schema-json)

Use [common.schema.json](#module-references-common-schema-json) for shared enums and identifiers.

#### Core Templates

Use the YAML/JSON/Markdown templates for state, task reporting, structured reading, evidence cards, project diagnosis, project prompts, outline review, and revision tracking. Use the XLSX workbooks for database preflight, research roadmap, literature registry, screening, sources, claims, evidence cards, figure/table traceability, and literature-map nodes and edges. Use `review_outline_template.docx` only after Task 20 approval.

Array-valued XLSX fields use semicolon-delimited text; escape a literal semicolon as `\;`. Normalize workbook rows into JSON before Schema validation.

#### Workflow References

Read the reference for the current task before acting. Do not load later-task references unless needed for interface validation or recovery.

- Step 00: [Database and environment preflight](#module-references-task-00-preflight-md)
- Task 01: [Project initialization](#module-references-task-01-project-initialization-md)
- Task 02: [Review type](#module-references-task-02-review-type-md)
- Task 03: [Scope and questions](#module-references-task-03-scope-and-questions-md)
- Task 04: [Existing reviews](#module-references-task-04-existing-reviews-md)
- Task 05: [Topic evaluation](#module-references-task-05-topic-evaluation-md)
- Task 06: [Terminology](#module-references-task-06-terminology-md)
- Task 07: [Concept groups](#module-references-task-07-concept-groups-md)
- Task 08: [Database plan](#module-references-task-08-database-plan-md)
- Task 09: [Search strategies](#module-references-task-09-search-strategies-md)
- Task 10: [Run searches](#module-references-task-10-run-searches-md)
- Task 11: [Metadata cleaning](#module-references-task-11-metadata-cleaning-md)
- Task 12: [Eligibility criteria](#module-references-task-12-eligibility-criteria-md)
- Task 13: [Title and abstract screening](#module-references-task-13-title-abstract-screening-md)
- Task 14: [Full-text screening](#module-references-task-14-full-text-screening-md)
- Task 15: [Library audit](#module-references-task-15-library-audit-md)
- Task 16: [Structured reading](#module-references-task-16-structured-reading-md)
- Task 17: [Evidence cards](#module-references-task-17-evidence-cards-md)
- Task 18: [Claim-evidence matrix](#module-references-task-18-claim-evidence-matrix-md)
- Task 19: [Evidence synthesis](#module-references-task-19-evidence-synthesis-md)
- Task 20: [Outline and figures](#module-references-task-20-outline-and-figures-md)
- Task 21A-21H: [Writing, submission, and revision](#module-references-task-21-writing-submission-revision-md)

#### Method and Domain References

- Read [database access and search operations](#module-references-database-access-and-search-md) for Step 00 and Tasks 04, 08, 09, and 10.
- Read [Systematic Review strict branch](#module-references-systematic-review-branch-md) only after Task 02 approves `SYSTEMATIC_REVIEW`.
- Read [optical-coating integrated domain pack](#module-references-optical-coating-integrated-md) for terminology, reading, comparison, evidence gates, and DLC-on-chalcogenide-glass decisions.
- Read [core prompt library](#module-references-prompt-library-core-md) when Task 05 creates the editable project prompt library or a later task updates it. Never use prompts to bypass state or evidence gates.

#### Deterministic Scripts

Run scripts from the Skill root through an environment that provides PyYAML, jsonschema, and openpyxl. A uniform verified invocation is:

```powershell
uv run --with PyYAML --with jsonschema --with openpyxl python scripts/<script>.py --help
```

Treat exit code 3 as validation failure, 4 as a state or overwrite conflict, and 5 as an external verification failure. Keep network verification opt-in; use the built-in cache and rate limit, and never pass credentials to a script.

- [init_project.py](#module-scripts-init-project-py): initialize or safely resume the persistent project structure.
- [transition_state.py](#module-scripts-transition-state-py): enforce legal task transitions, approvals, blockers, risks, and chapter state.
- [validate_project.py](#module-scripts-validate-project-py): validate state, task records, files, hashes, prerequisites, and recovery invariants.
- [import_records.py](#module-scripts-import-records-py): import CSV, TSV, XLSX, JSON/Zotero, RIS, BibTeX, and EndNote XML without external inference.
- [deduplicate_records.py](#module-scripts-deduplicate-records-py): merge exact duplicates conservatively and retain conflict/version decisions.
- [validate_metadata.py](#module-scripts-validate-metadata-py): validate locally or explicitly opt into rate-limited, cached Crossref checks.
- [build_literature_map.py](#module-scripts-build-literature-map-py): build nodes and only explicitly supplied, evidenced relationships.
- [audit_claims.py](#module-scripts-audit-claims-py): enforce Claim-Evidence Schema, Source_ID, original-location, and V3-V5 gates.
- [audit_figures_tables.py](#module-scripts-audit-figures-tables-py): audit element/cell provenance, transformations, calculations, and copyright.
- [version_output.py](#module-scripts-version-output-py): create immutable numbered copies and a hash manifest.
- [build_full_skill.py](#module-scripts-build-full-skill-py): deterministically build the portable source document when Stage 5 is approved.
- [check_distribution_parity.py](#module-scripts-check-distribution-parity-py): check source/content hashes and core workflow parity.

#### Current Development Boundary

The state machine, core Schema, core templates, Step 00 and Task 01-21H workflow references, database/search method, strict Systematic Review branch, optical-coating domain pack, core prompt library, and 12 deterministic operational scripts are implemented and tested.

The Stage 5 portable `SKILL_FULL.md` artifact is generated outside the installable Skill and verified against modular source and content hashes. Rebuild and re-run parity after every modular source change; never edit the generated file manually.

The modular source package, DLC-on-chalcogenide-glass demonstration project, local Codex installation, and portable distribution artifact are implemented and regression-tested. GitHub publication is not yet implemented; do not claim that a remote repository or release is available until publication is completed and verified.

<a id="module-agents-openai-yaml"></a>
## Module: `agents/openai.yaml`

```yaml
interface:
  display_name: "Optical Coating Review Builder"
  short_description: "Build evidence-traceable optical coating literature reviews"
  default_prompt: "Use $build-optical-coating-review to initialize an evidence-traceable optical coating literature review project and stop after the first approval gate."
```

<a id="module-references-claim-schema-json"></a>
## Module: `references/claim.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/claim.schema.json",
  "title": "Claim",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "claim_id", "claim_text_zh", "claim_text_en", "claim_type", "source_links", "evidence_type", "evidence_strength", "consistency", "applicability_conditions", "limitations", "intended_section", "human_status", "minimum_verification_level", "notes"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "claim_id": {"$ref": "common.schema.json#/$defs/claimId"},
    "claim_text_zh": {"type": ["string", "null"]},
    "claim_text_en": {"type": ["string", "null"]},
    "claim_type": {"enum": ["BACKGROUND", "DESCRIPTIVE", "COMPARATIVE", "QUANTITATIVE", "MECHANISTIC", "CAUSAL", "METHOD", "CONSENSUS", "CONTROVERSY", "RESEARCH_GAP", "APPLICATION"]},
    "source_links": {"type": "array", "items": {"$ref": "#/$defs/sourceLink"}},
    "evidence_type": {"enum": ["METADATA", "ABSTRACT", "FULL_TEXT_STATEMENT", "TABLE", "FIGURE", "SUPPLEMENT", "STANDARD", "DERIVED_CALCULATION", "SYNTHESIS"]},
    "evidence_strength": {"enum": ["UNASSESSED", "WEAK", "MODERATE", "STRONG"]},
    "consistency": {"enum": ["UNASSESSED", "CONSISTENT", "MIXED", "CONTRADICTORY", "SINGLE_SOURCE"]},
    "applicability_conditions": {"type": "array", "items": {"type": "string"}},
    "limitations": {"type": "array", "items": {"type": "string"}},
    "intended_section": {"type": ["string", "null"]},
    "human_status": {"enum": ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REVISE", "REJECTED"]},
    "minimum_verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
    "notes": {"type": ["string", "null"]}
  },
  "$defs": {
    "sourceLink": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "original_location", "relation", "verification_level"],
      "properties": {
        "source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
        "original_location": {"type": ["string", "null"]},
        "relation": {"enum": ["SUPPORTS", "CONTRADICTS", "QUALIFIES", "BACKGROUND_ONLY"]},
        "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"}
      }
    }
  }
}
```

<a id="module-references-common-schema-json"></a>
## Module: `references/common.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/common.schema.json",
  "title": "Optical Coating Review Common Definitions",
  "$defs": {
    "nonEmptyString": {"type": "string", "minLength": 1},
    "nullableString": {"type": ["string", "null"]},
    "dateTime": {"type": "string", "format": "date-time"},
    "status": {
      "type": "string",
      "enum": ["NOT_STARTED", "IN_PROGRESS", "BLOCKED", "REVIEW_REQUIRED", "APPROVED", "REJECTED", "SKIPPED_WITH_RISK", "SUPERSEDED", "ARCHIVED"]
    },
    "verificationLevel": {
      "type": "string",
      "enum": ["V0", "V1", "V2", "V3", "V4", "V5"]
    },
    "taskId": {
      "type": "string",
      "pattern": "^(STEP-00|TASK-(0[1-9]|1[0-9]|20|21[A-H]))$"
    },
    "sourceId": {"type": "string", "pattern": "^SRC-[A-Z0-9][A-Z0-9._-]*$"},
    "claimId": {"type": "string", "pattern": "^CLM-[A-Za-z0-9.]+-[0-9]{2,}$"},
    "approvalRecord": {
      "type": "object",
      "additionalProperties": false,
      "required": ["decision", "decision_text", "decided_by", "decided_at", "output_paths"],
      "properties": {
        "decision": {"enum": ["APPROVED", "REJECTED", "SKIPPED_WITH_RISK"]},
        "decision_text": {"$ref": "#/$defs/nonEmptyString"},
        "decided_by": {"$ref": "#/$defs/nonEmptyString"},
        "decided_at": {"$ref": "#/$defs/dateTime"},
        "output_paths": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
        "risk_id": {"type": ["string", "null"]}
      }
    },
    "fileRecord": {
      "type": "object",
      "additionalProperties": false,
      "required": ["path", "role", "sha256"],
      "properties": {
        "path": {"type": "string", "minLength": 1},
        "role": {"type": "string", "minLength": 1},
        "sha256": {"type": ["string", "null"], "pattern": "^[a-fA-F0-9]{64}$"},
        "version": {"type": ["string", "null"]}
      }
    }
  }
}
```

<a id="module-references-database-access-and-search-md"></a>
## Module: `references/database-access-and-search.md`

### Database Access and Search Operations

#### Purpose

Use this reference in Step 00 and Tasks 04, 08, 09, and 10. Treat access, search, metadata, export, and full text as separate capabilities. Never bypass authentication, CAPTCHA, subscriptions, robots restrictions, or platform terms.

#### Platform Roles

| Role | Platforms | Primary use | Not sufficient alone for |
|---|---|---|---|
| Comprehensive index | Web of Science Core Collection, Scopus | Core multidisciplinary retrieval, cited/citing links, exports | Guaranteed full text |
| Discipline index | PubMed, GeoRef, Engineering Village | Topic-specific terminology and engineering coverage | Complete optical-coating coverage by itself |
| Chinese database | CNKI, 万方 | Chinese journals, theses, standards and local engineering work | English SCI coverage |
| Discovery | Google Scholar, 百度学术 | Seed finding, citation discovery, hard-to-find records | Reproducible exhaustive counts or clean bulk export |
| Metadata verification | Crossref, OpenAlex | DOI, title, author, venue and relationship checks | Subscription full text or definitive indexing status |
| Publisher full text | ScienceDirect, SpringerLink | Record pages, abstracts, supplements and lawful full text | Comprehensive cross-publisher search |

#### Access Record

For every platform record `database_name`, `database_category`, `access_status`, `access_level`, `access_route`, `test_date`, login/VPN requirements, search/record/abstract/full-text/export availability, export formats, test query, real result count, automation restrictions, limitations and user confirmation.

Access states are `ACCESSIBLE`, `PARTIALLY_ACCESSIBLE`, `VPN_REQUIRED`, `LOGIN_REQUIRED`, `NO_SUBSCRIPTION`, `CAPTCHA_OR_MANUAL_OPERATION_REQUIRED`, `TEMPORARILY_UNAVAILABLE`, `REGION_RESTRICTED`, `NOT_REQUIRED_FOR_THIS_PROJECT`, `USER_WAIVED`, and `UNVERIFIED`. Capability levels are L0 closed, L1 homepage, L2 search, L3 record/abstract, L4 export, and L5 lawful required full text.

Before Task 01, no required platform may remain `UNVERIFIED`. `NOT_REQUIRED_FOR_THIS_PROJECT` and `USER_WAIVED` require explicit user approval.

#### Browser and Account Boundary

- Ask the user to complete login, institutional SSO, VPN, CAPTCHA, MFA, consent, download approval, or subscription decisions.
- Do not capture passwords, tokens, cookies, session storage, or private account data in project files or logs.
- Do not automate bulk access when platform terms or visible restrictions prohibit it.
- Use rate limits, bounded pages, and caching when automation is permitted.
- Record a failed access attempt as a status; do not fabricate results or silently substitute a different database.

#### Three-Layer Search Design

1. Broad: maximize recall with substrate/coating concepts and verified synonyms.
2. Balanced: add optical, protection, interface, or manufacturing context to reduce unrelated uses.
3. Precise: add a specific process, mechanism, performance, or application group for focused questions.

Write platform-neutral Boolean logic first. Translate only after verifying field names, phrase rules, wildcard behavior, proximity syntax, query length, language handling and date filters on the live platform. Keep exclusion clauses narrow and test them against known relevant records.

#### Query Record

Every executed query records a stable query ID, platform, database collection, query tier, exact string, fields, filters, date/time, result count, sort order, export range, export format, file path, operator, version, and error or restriction. Results counts must come from the live interface or exported file.

#### Export and Provenance

- Preserve raw exports as read-only inputs.
- Include platform, query ID, tier, version, date and batch in filenames.
- Tag each imported record with all source platforms and queries before deduplication.
- Accept CSV, XLSX, RIS, BibTeX, EndNote XML, Zotero mappings and JSON only through format-aware parsers.
- Reconcile `reported result count`, `exported rows`, `parse failures`, `duplicates`, `retained records` and `unresolved records`.

#### Citation Chasing

Record seed Source_ID, direction (`BACKWARD`, `FORWARD`, `RELATED`), platform, date and inclusion reason. Citation connection is a discovery path, not proof that two papers agree. Create literature-map relations only after reading evidence that supports the relation.

#### Metadata Verification

Normalize DOI by removing resolver prefixes and lowercasing for matching while preserving the display form. Cross-check title, author, year and venue before V2. When Crossref, OpenAlex, publisher and PDF disagree, retain all values, identify their sources, and create a manual conflict rather than selecting the most convenient field.

#### Stop Conditions

Pause on login/VPN/CAPTCHA, unexpected download prompts, export truncation, result-count drift without explanation, syntax rejection, platform outage, source conflicts, full-text mismatch or any instruction that would bypass access controls. Resume only after state and access records are updated.

<a id="module-references-evidence-card-schema-json"></a>
## Module: `references/evidence-card.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/evidence-card.schema.json",
  "title": "Evidence Card",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "evidence_card_id", "source_id", "citation", "research_question", "material_system", "substrate", "coating", "deposition_method", "interface_strategy", "process_conditions", "characterization_methods", "key_results", "author_interpretation", "skill_assessment", "supported_claim_ids", "comparison_uses", "figure_table_uses", "original_locations", "verification_level", "evidence_strength", "limitations", "citation_risks", "human_status"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "evidence_card_id": {"type": "string", "pattern": "^EC-[A-Z0-9][A-Z0-9._-]*$"},
    "source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
    "citation": {"type": ["string", "null"]},
    "research_question": {"type": ["string", "null"]},
    "material_system": {"type": ["string", "null"]},
    "substrate": {"type": ["string", "null"]},
    "coating": {"type": ["string", "null"]},
    "deposition_method": {"type": ["string", "null"]},
    "interface_strategy": {"type": ["string", "null"]},
    "process_conditions": {"type": "array", "items": {"type": "string"}},
    "characterization_methods": {"type": "array", "items": {"type": "string"}},
    "key_results": {"type": "array", "items": {"$ref": "#/$defs/result"}},
    "author_interpretation": {"type": "array", "items": {"type": "string"}},
    "skill_assessment": {"type": "array", "items": {"type": "string"}},
    "supported_claim_ids": {"type": "array", "items": {"$ref": "common.schema.json#/$defs/claimId"}, "uniqueItems": true},
    "comparison_uses": {"type": "array", "items": {"type": "string"}},
    "figure_table_uses": {"type": "array", "items": {"type": "string"}},
    "original_locations": {"type": "array", "items": {"type": "string"}},
    "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
    "evidence_strength": {"enum": ["UNASSESSED", "WEAK", "MODERATE", "STRONG"]},
    "limitations": {"type": "array", "items": {"type": "string"}},
    "citation_risks": {"type": "array", "items": {"type": "string"}},
    "human_status": {"enum": ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REVISE", "REJECTED"]}
  },
  "$defs": {
    "result": {
      "type": "object",
      "additionalProperties": false,
      "required": ["metric", "value", "unit", "conditions", "original_location"],
      "properties": {
        "metric": {"type": "string"},
        "value": {"type": ["number", "string", "null"]},
        "unit": {"type": ["string", "null"]},
        "conditions": {"type": ["string", "null"]},
        "original_location": {"type": ["string", "null"]}
      }
    }
  }
}
```

<a id="module-references-figure-table-traceability-schema-json"></a>
## Module: `references/figure-table-traceability.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/figure-table-traceability.schema.json",
  "title": "Figure and Table Traceability Record",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "trace_id", "artifact_id", "artifact_type", "element_id", "target_location", "source_id", "original_location", "transformation", "calculation", "copyright_status", "permission_reference", "verification_level", "human_status", "notes"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "trace_id": {"type": "string", "pattern": "^TRC-[A-Z0-9][A-Z0-9._-]*$"},
    "artifact_id": {"type": "string", "pattern": "^(FIG|TAB)-[A-Za-z0-9._-]+$"},
    "artifact_type": {"enum": ["FIGURE", "FIGURE_ELEMENT", "TABLE", "TABLE_CELL"]},
    "element_id": {"type": ["string", "null"]},
    "target_location": {"type": ["string", "null"]},
    "source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
    "original_location": {"type": "string", "minLength": 1},
    "transformation": {"enum": ["DIRECT_REUSE", "REDRAWN", "ADAPTED", "DIGITIZED", "CALCULATED", "SYNTHESIZED"]},
    "calculation": {"type": ["string", "null"]},
    "copyright_status": {"enum": ["UNASSESSED", "ORIGINAL", "LICENSED", "PERMISSION_REQUIRED", "PERMISSION_OBTAINED", "FAIR_USE_ASSESSED", "NOT_REUSABLE"]},
    "permission_reference": {"type": ["string", "null"]},
    "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
    "human_status": {"enum": ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REVISE", "REJECTED"]},
    "notes": {"type": ["string", "null"]}
  }
}
```

<a id="module-references-literature-map-schema-json"></a>
## Module: `references/literature-map.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/literature-map.schema.json",
  "title": "Literature Map",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "map_id", "project_id", "generated_at", "nodes", "edges", "views"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "map_id": {"type": ["string", "null"]},
    "project_id": {"type": ["string", "null"]},
    "generated_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]},
    "nodes": {"type": "array", "items": {"$ref": "#/$defs/node"}},
    "edges": {"type": "array", "items": {"$ref": "#/$defs/edge"}},
    "views": {"type": "array", "items": {"enum": ["TIME_EVOLUTION", "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE", "THEME_CLUSTER", "METHOD_CHARACTERIZATION_MATRIX", "CONSENSUS_CONTROVERSY", "EVIDENCE_LAYER"]}, "uniqueItems": true}
  },
  "$defs": {
    "node": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "title", "year", "journal", "document_type", "materials", "substrates", "coatings", "deposition_routes", "interface_strategies", "optical_properties", "mechanical_properties", "environmental_properties", "manufacturing_properties", "characterization_methods", "evidence_types", "verification_level", "themes", "research_stage", "intended_uses", "evidence_strength"],
      "properties": {
        "source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
        "title": {"type": ["string", "null"]},
        "year": {"type": ["integer", "null"], "minimum": 1600, "maximum": 2200},
        "journal": {"type": ["string", "null"]},
        "document_type": {"type": ["string", "null"]},
        "materials": {"type": "array", "items": {"type": "string"}},
        "substrates": {"type": "array", "items": {"type": "string"}},
        "coatings": {"type": "array", "items": {"type": "string"}},
        "deposition_routes": {"type": "array", "items": {"type": "string"}},
        "interface_strategies": {"type": "array", "items": {"type": "string"}},
        "optical_properties": {"type": "array", "items": {"type": "string"}},
        "mechanical_properties": {"type": "array", "items": {"type": "string"}},
        "environmental_properties": {"type": "array", "items": {"type": "string"}},
        "manufacturing_properties": {"type": "array", "items": {"type": "string"}},
        "characterization_methods": {"type": "array", "items": {"type": "string"}},
        "evidence_types": {"type": "array", "items": {"type": "string"}},
        "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
        "themes": {"type": "array", "items": {"type": "string"}},
        "research_stage": {"type": ["string", "null"]},
        "intended_uses": {"type": "array", "items": {"enum": ["CORE", "SUPPORTING", "BACKGROUND", "METHOD", "CONFLICT"]}},
        "evidence_strength": {"enum": ["UNASSESSED", "WEAK", "MODERATE", "STRONG"]}
      }
    },
    "edge": {
      "type": "object",
      "additionalProperties": false,
      "required": ["edge_id", "from_source_id", "to_source_id", "relation", "basis", "original_locations", "verification_level", "human_status"],
      "properties": {
        "edge_id": {"type": "string", "pattern": "^EDGE-[A-Z0-9][A-Z0-9._-]*$"},
        "from_source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
        "to_source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
        "relation": {"enum": ["SUPPORTS", "CONTRADICTS", "EXTENDS", "USES_METHOD_FROM", "SHARES_MATERIAL_SYSTEM", "SHARES_DEPOSITION_ROUTE", "REPORTS_COMPARABLE_METRIC", "STRUCTURAL_REFERENCE", "BACKGROUND_ONLY"]},
        "basis": {"type": "string", "minLength": 1},
        "original_locations": {"type": "array", "items": {"type": "string"}},
        "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
        "human_status": {"enum": ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REJECTED"]}
      }
    }
  }
}
```

<a id="module-references-optical-coating-integrated-md"></a>
## Module: `references/optical-coating-integrated.md`

### Optical Coating Integrated Domain Pack

本专业包默认服务红外光学镀膜，同时支持可见、紫外和激光薄膜。它规定检索概念、精读字段、跨研究可比条件和领域门禁，不替代已核验文献或标准。

#### Contents

1. 领域对象与规范化
2. 物理与薄膜光学
3. 基底与材料
4. 膜层材料科学
5. 制备技术
6. 界面工程
7. 制造与工程放大
8. 机械可靠性
9. 光学与环境可靠性
10. 表征方法
11. 应用与工程成熟度
12. 主张证据门禁
13. DLC-硫系玻璃专项框架
14. 停止与人工核查条件

#### 1. 领域对象与规范化

用“基底-前处理-界面/过渡层-功能膜层-后处理-测试环境-应用”描述样品。每篇文献至少提取：基底确切组成或牌号、表面状态、层序、各层材料与厚度、制备路线、温度历史、关键工艺条件、测试方法、样品尺寸/曲率、目标波段和用途。

分别记录论文报告值、从图表读取值、换算值和模型拟合值。单位换算保留原值、原单位、公式和有效数字。没有确切组成时写“原文未报告”，不得用材料家族默认成分填补。

#### 2. 物理与薄膜光学

##### 检索与提取

覆盖干涉、Fresnel 系数、光学导纳、特征矩阵、n/k、色散、偏振、入射角、膜厚、光谱带宽、红外多声子吸收和散射/吸收损耗。记录模型、边界条件、基底背面处理、参考样品、仪器、分辨率和拟合区间。

##### 可比条件

- 透射、反射和吸收必须对应相同波长范围、角度、偏振、基底厚度、表面状态和环境。
- 膜系与裸基底比较要说明单面/双面、背面反射、归一化和基底吸收。
- n/k 由椭偏或光谱拟合得到时记录色散模型、固定参数、厚度耦合和拟合误差。
- “高透过”必须给波段、阈值或相对基线；单点峰值不能代表全带平均性能。
- 激光损伤阈值必须记录波长、脉宽、重复频率、光斑定义、判据和测试标准。

##### 门禁

能量不守恒、参考样品不明、波段/角度缺失或模型参数不可识别时，不进行定量横向排名。模拟设计只能支持设计可行性，不能替代实测制造性能。

#### 3. 基底与材料

##### 检索与提取

覆盖硫系玻璃、氧化物玻璃、晶体、半导体和聚合物；记录组成、结构、折射率、吸收边、热膨胀系数、玻璃转变/软化温度、硬度、化学耐久性、加工方法、粗糙度、亚表面损伤和环境敏感性。

##### 可比条件

- “硫系玻璃”不是单一材料；至少区分 S/Se/Te 系和具体 Ge-As-Se、As-Se、Ge-Sb-Se 等组成或牌号。
- 热预算要与 Tg、软化、结晶、挥发和成分迁移风险比较，而非只报告设备设定温度。
- 附着和应力比较需考虑基底模量、CTE、厚度、表面粗糙度和加工损伤。
- 不把 Si、Ge、ZnS、ZnSe 等红外材料上的 DLC 结果直接外推到硫系玻璃；只能作为方法或背景证据并标明差异。

##### 门禁

基底组成未知时，材料相容性结论降级；使用通用“glass”结果支持硫系玻璃机制前必须有直接材料证据或清晰的适用性论证。

#### 4. 膜层材料科学

##### 检索与提取

覆盖非晶/纳米晶结构、sp2/sp3 键合、氢含量、密度、孔隙、缺陷、成分、化学键、相、界面、残余应力、热稳定和时效。区分 a-C、a-C:H、ta-C、ta-C:H、掺杂 DLC 和多层/纳米复合膜。

##### 证据组合

- Raman D/G 峰位置、宽度、强度比和色散反映有序度与键合环境，但不能单独给出精确 sp3 原子分数。
- 精确 sp3 主张优先要求经校准的 EELS、NEXAFS、XPS/Auger 组合或等价直接证据，并说明表面污染、深度和拟合模型。
- 密度由 XRR、RBS/ERDA 等获得时记录模型与误差；由折射率间接推断时明确模型依赖。
- 残余应力记录测量方法、基底、膜厚、弹性参数和曲率公式；不同方法结果不无条件互换。

##### 门禁

禁止把 Raman 拟合直接等同精确 sp3；禁止用单一峰位变化证明完整成键机制；禁止把成分相关性自动升级为应力、硬度或透过变化的因果解释。

#### 5. 制备技术

##### 路线覆盖

覆盖 PVD、CVD、PECVD、磁控溅射、离子束、FCVA、PLD、蒸发、ALD 和复合沉积。对每种方法记录设备构型、靶/前驱体、气体与流量、压力、功率、偏压、离子能量、基底温度、距离、时间、速率、膜厚、冷却和后处理。

##### 可比条件

- 设备功率不能跨腔体直接比较；优先比较功率密度、偏压、离子能量或可解释的过程参数。
- “低温”给出基底实测或可信上限，并与基底热预算关联。
- 沉积速率、膜厚、应力、缺陷和均匀性共同描述工艺窗口，不能只以硬度或峰值透过优化。
- FCVA/PLD 关注颗粒、过滤、面积和复杂曲面；PECVD/CVD 关注气相化学、氢、温度与等离子损伤；溅射/离子束关注离子轰击、靶中毒和成分转移；ALD 关注成核、循环、温度窗口和界面层用途。

##### 门禁

没有真实工艺参数、温度和膜厚时不能形成可复现实验建议；实验室单片结果不能直接声称量产适用。

#### 6. 界面工程

##### 检索与提取

覆盖清洗、去污染、活化、等离子处理、离子刻蚀、过渡层、梯度层、扩散层、化学键匹配、CTE/模量匹配、应力释放和附着。记录步骤顺序、时间、气氛、功率/能量、等待时间、层厚和界面表征。

##### 因果链

推荐用“处理 -> 表面化学/形貌 -> 成核与界面结构 -> 应力/附着 -> 失效模式”组织证据。每一箭头分别核验；只观察最终附着提高时，不反推全部中间机制均成立。

##### 证据要求

附着结论记录测试方法、划痕载荷程序、压头、失效判据、声发射/显微观察、样本数和统计；界面化学优先使用深度分辨 XPS、截面 TEM/EELS、ToF-SIMS 或等价直接证据，并评估制样影响。

##### 门禁

相关性、作者示意图或单一表面谱不能作为扩散或化学键合机制的确定证据。过渡层提高性能的主张必须说明厚度、材料、基底和工艺条件。

#### 7. 制造与工程放大

##### 检索与提取

覆盖超精密加工、清洗线、装夹、遮蔽、曲面、大口径、膜厚/光学均匀性、批间一致性、在线监控、工艺窗口、良率、维护、周期、成本和规模放大。

##### 可比条件

- 记录样品口径、曲率、装夹方向、测点网格、边缘排除和均匀性定义。
- 单片多测点不能代替多批次一致性；“稳定”需要时间或批次证据。
- 工程放大同时评估热负荷、等离子体/蒸汽分布、颗粒、清洗、节拍和设备维护。
- 成本结论说明材料、设备折旧、真空时间、良率、返工和检测边界。

##### 门禁

小面积平片研究不直接支持大口径曲面结论；没有批次、均匀性或良率数据时只可写“潜在可扩展”。

#### 8. 机械可靠性

##### 检索与提取

覆盖硬度、模量、残余应力、附着、磨损、摩擦、裂纹、剥落、疲劳、热循环和冲击。记录标准、仪器、压头/对偶、载荷、速度、环境、循环数、样本数、失效判据和误差。

##### 可比条件

- 纳米压痕记录最大深度/膜厚比例和基底效应；“小于膜厚 10%”仅为常用启发式，不是所有材料的充分保证。
- 划痕临界载荷依赖压头、加载速率、膜厚、基底和判据，不能脱离方法比较。
- 磨损率需统一体积、载荷、距离和单位；摩擦系数不等同耐磨寿命。
- 裂纹和剥落应区分内聚、界面和基底失效。

##### 门禁

不同测试标准、载荷或基底上的单一数值不做直接优劣排名；没有重复或误差时避免精细差异结论。

#### 9. 光学与环境可靠性

##### 检索与提取

覆盖透射、反射、吸收、散射、激光损伤、湿热、盐雾、温度、辐照、风沙、冲蚀、腐蚀和服役寿命。记录标准、条件、暴露时间、循环、样本数、前后光谱与机械变化、失效判据。

##### 可比条件

- 老化前后用相同光学配置比较，并报告基线和不确定性。
- 盐雾、湿热、热循环和冲蚀必须按具体标准或完整条件分组；“通过测试”不跨标准直接比较。
- 服役寿命外推需要加速模型、边界和现场证据；短时实验不等同多年寿命。
- 防护性能同时考虑光学损失、附着、裂纹、污染和可修复性。

##### 门禁

只展示代表性显微图而无判据/重复时不声称统计可靠；单一环境测试不支持“全环境稳定”。

#### 10. 表征方法

##### 方法矩阵

| 方法 | 主要信息 | 关键限制 |
|---|---|---|
| 光谱/FTIR | 波段透射、反射、吸收与振动信息 | 基底、背面、厚度、散射和分辨率耦合 |
| 椭偏 | n/k、厚度和色散模型 | 参数相关、粗糙/梯度/基底模型依赖 |
| Raman | 碳结构有序度、D/G 特征和应力线索 | 荧光、激光加热、拟合选择；不直接给精确 sp3 |
| XPS/AES | 表面成分和化学态 | 表面敏感、溅射损伤、峰拟合与充电 |
| XRD | 晶相与有序结构 | 非晶弱信号、基底峰和检测限 |
| SEM/TEM | 表面/截面形貌、层结构和局部缺陷 | 制样伪影、局部代表性和束流损伤 |
| AFM | 粗糙度和局部形貌 | 扫描尺度、探针卷积和代表性 |
| 压痕/划痕/磨损 | 力学、附着和摩擦磨损响应 | 基底效应、判据、设备和参数依赖 |
| 曲率/衍射 | 残余应力 | 弹性参数、膜厚、各向异性和温度历史 |

##### 互证规则

结构-性能机制优先需要至少两类互补证据和排除替代解释。例如 Raman + XPS 仍可能不足以证明界面扩散；需要深度或截面证据。局部 TEM 图像不能单独代表全片均匀性。

#### 11. 应用与工程成熟度

覆盖红外成像、探测、激光、航天窗口、传感、军民用防护、工程放大、产业化和成本。记录器件结构、波段、口径、环境、系统指标、标准、技术成熟度、批次和现场数据。

区分材料性能、元件性能和系统性能。膜层透过提高不自动等同成像质量或探测率提升；系统主张需要 MTF、杂散光、信噪比、热背景或相应系统级证据。应用可行性、原型验证、工程定型和量产是不同等级。

#### 12. 主张证据门禁

| 主张类型 | 最低证据 | 禁止越界 |
|---|---|---|
| 题录与研究范围 | V2-V3 记录页或摘要 | 用题名推断实验细节 |
| 定量光学/机械值 | V4 原文表、图或结果位置，含条件 | 脱离波段、载荷、膜厚或基底比较 |
| 材料组成/键合 | V4 直接表征及拟合方法 | Raman 单独给精确 sp3 |
| 界面/失效机制 | V4 多方法证据；关键结论建议 V5 | 相关性或作者推测写成因果事实 |
| 工程放大/寿命 | V4 工程规模、批次或标准测试；关键事实建议 V5 | 小样短试验外推量产和多年寿命 |
| 共识/争议 | 多个独立 Source_ID 与条件分层 | 用论文数量投票忽略质量和条件 |
| 研究空白 | 文献地图和 Claim-Evidence 缺口 | 仅凭“检索较少”宣称空白 |

#### 13. DLC-硫系玻璃专项框架

##### 必答问题

1. 红外元件需要 DLC 防护解决哪些磨损、环境和光学问题？
2. 硫系玻璃的热、机械、化学和加工特性为何限制沉积窗口？
3. DLC 类型、氢、缺陷、密度和应力如何影响红外损耗与可靠性？
4. 清洗、活化、过渡层和梯度层如何改变界面与失效？
5. 不同低温沉积路线的可比工艺窗口是什么？
6. 光学、机械、环境和制造指标如何进行多目标综合评价？
7. 标准、寿命、界面直接证据、批次一致性和工程放大的缺口在哪里？

##### 推荐概念组

基底组：`chalcogenide glass` 及具体组成/牌号。膜层组：`diamond-like carbon`、DLC 及经核验的碳膜类别。界面组：interlayer、buffer、graded、plasma activation、adhesion。工艺组：PECVD、sputtering、ion beam、FCVA、PLD 等。性能组：infrared transmittance、optical constants、stress、adhesion、hardness、erosion、humidity、thermal cycling。应用组：infrared window、imaging、detector、laser、aerospace。

概念组用于检索设计，不意味着词项之间材料学等价。

##### 推荐综合主线

以“基底限制 -> 低温制备与界面策略 -> DLC 结构/应力 -> 光学-机械-环境权衡 -> 元件与工程放大”组织跨文献比较。若证据不足，可将某环节标为研究空白，不用推测填补机制链。

#### 14. 停止与人工核查条件

遇到以下情况停止相应主张：基底组成不明却需材料外推；工艺参数或膜厚缺失却需复现；Raman 被用于精确 sp3；定量值缺单位/条件；图中读数无法确认坐标；全文与摘要结论不一致；单一表征支撑复杂机制；不同标准被直接排名；小样结果外推大口径或寿命；图表版权不明。将问题登记到人工核查清单，不用常识补值。

<a id="module-references-project-state-schema-json"></a>
## Module: `references/project-state.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/project-state.schema.json",
  "title": "Project State",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "project_id", "project_title", "review_type", "execution_mode", "project_status", "current_stage", "current_task", "current_subtask", "paused", "tasks", "task_21_subtasks", "risk_ids", "manual_check_ids", "current_inputs", "last_user_decision", "updated_at"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "project_id": {"type": ["string", "null"]},
    "project_title": {"type": ["string", "null"]},
    "review_type": {"enum": ["UNDECIDED", "NARRATIVE_REVIEW", "SYSTEMATIC_REVIEW"]},
    "execution_mode": {"enum": ["single_task_confirmation", "stage_batch"]},
    "project_status": {"$ref": "common.schema.json#/$defs/status"},
    "current_stage": {"enum": ["STEP_00", "STAGE_1", "STAGE_2", "STAGE_3", "STAGE_4"]},
    "current_task": {"anyOf": [{"$ref": "common.schema.json#/$defs/taskId"}, {"type": "null"}]},
    "current_subtask": {"type": ["string", "null"], "pattern": "^TASK-21[A-H]$"},
    "current_chapter": {"type": ["string", "null"]},
    "paused": {"type": "boolean"},
    "pause_reason": {"type": ["string", "null"]},
    "tasks": {"type": "array", "items": {"$ref": "#/$defs/taskState"}, "uniqueItems": true},
    "task_21_subtasks": {"type": "array", "items": {"$ref": "#/$defs/taskState"}, "uniqueItems": true},
    "approved_task": {"anyOf": [{"$ref": "common.schema.json#/$defs/taskId"}, {"type": "null"}]},
    "last_approved_output": {"type": ["string", "null"]},
    "risk_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "manual_check_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "current_inputs": {"type": "array", "items": {"$ref": "common.schema.json#/$defs/fileRecord"}},
    "last_user_decision": {"anyOf": [{"$ref": "common.schema.json#/$defs/approvalRecord"}, {"type": "null"}]},
    "created_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]},
    "updated_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]}
  },
  "$defs": {
    "taskState": {
      "type": "object",
      "additionalProperties": false,
      "required": ["task_id", "status", "prerequisites", "input_paths", "output_paths", "quality_gate_passed", "approval", "blocker_id", "result_id", "updated_at"],
      "properties": {
        "task_id": {"$ref": "common.schema.json#/$defs/taskId"},
        "status": {"$ref": "common.schema.json#/$defs/status"},
        "prerequisites": {"type": "array", "items": {"$ref": "common.schema.json#/$defs/taskId"}, "uniqueItems": true},
        "input_paths": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
        "output_paths": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
        "quality_gate_passed": {"type": ["boolean", "null"]},
        "approval": {"anyOf": [{"$ref": "common.schema.json#/$defs/approvalRecord"}, {"type": "null"}]},
        "blocker_id": {"type": ["string", "null"]},
        "result_id": {"type": ["string", "null"]},
        "updated_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]}
      }
    }
  }
}
```

<a id="module-references-prompt-library-core-md"></a>
## Module: `references/prompt-library-core.md`

### Core Prompt Library

本文件提供可编辑的项目提示词母版。Task 05 后应把适用条目复制并改写为项目级 `prompt_library.md`，填入已批准范围、真实数据库能力、Source_ID 和 Claim_ID。提示词库是可编辑工作手册，不得替代 Skill 状态机、任务门禁、Schema、原始记录或阶段 4 的确定性脚本。

#### Contents

1. 选题诊断
2. 已有综述比较
3. 术语扩展
4. 检索式设计
5. 筛选解释
6. 全文精读
7. 证据卡
8. 争议综合
9. 研究空白
10. 大纲审查
11. 段落写作
12. 引用核查
13. 期刊匹配
14. 审稿回复

#### 使用规则

- 只使用已批准任务输出和已核验来源；缺失信息明确标为待补充。
- 保留论文原始题名、术语、公式、数值、单位和正式引文。
- 输出必须能回写项目模板；不得在提示词回答中虚构 Source_ID、Claim_ID、DOI、全文位置或数据库结果。
- 遇到登录、VPN、验证码、付费墙、全文缺失、元数据冲突、范围判断或证据不足时停止并登记人工操作。
- 将每条提示词的执行记录绑定到任务、输入版本、输出版本和日期。

#### 1. 选题诊断

- `prompt_id`: `CORE-TOPIC-DIAGNOSIS-01`
- `phase`: Task 03-05，定题
- `intent`: 判断课题范围、创新空间、证据可得性和执行风险。
- `when_to_use`: 已形成初始研究方向，但尚未批准最终题目时。
- `required_inputs`: 项目简报、综述类型、范围声明、已有综述矩阵、数据库预检结果。
- `tool_or_database_prerequisites`: Step 00 已批准；至少能核验题录和摘要，动态期刊信息需联网。
- `prompt_text`: 分析给定研究方向，生成至少 3 个边界清楚的候选题。逐项比较研究对象、材料/基底、膜层、工艺、性能、应用、时间范围、与已有综述的差异、证据可得性、预计贡献和主要风险。对每项判断标明所用 Source_ID 或“待核验”，不要把检索数量少直接称为研究空白。给出推荐题目、拒绝其他题目的理由和必须由用户决定的问题。
- `expected_outputs`: 候选题评分矩阵、推荐题目、项目诊断要点、路线图初始项和待决策清单。
- `stop_conditions`: 已有综述无法核验；范围关键选择缺失；核心数据库均不可检索；证据量明显不足或过载。
- `quality_checks`: 至少 3 个候选题；差异化可追溯；题目不过大或过窄；每个核心问题连接证据任务与交付物。

#### 2. 已有综述比较

- `prompt_id`: `CORE-REVIEW-COMPARISON-01`
- `phase`: Task 04，定题
- `intent`: 建立已有综述的覆盖、结构、贡献与更新空间比较。
- `when_to_use`: 需要判断新综述是否重复以及哪些结构可借鉴时。
- `required_inputs`: 已核验综述记录、摘要或全文位置、范围声明、时间与语言边界。
- `tool_or_database_prerequisites`: 可访问题录/摘要；比较详细方法或结论时必须有合法全文。
- `prompt_text`: 对输入的综述逐篇提取检索截止时间、对象、材料、工艺、性能、应用、纳入文献类型、结构、主要贡献、明确局限和证据等级。生成交叉覆盖矩阵，区分直接重合、部分重合、结构参考和背景用途。只在有证据时提出更新空间，并把可借鉴结构绑定到 Source_ID 和原文位置。
- `expected_outputs`: 已有综述矩阵、覆盖地图、结构参考登记、可核验的更新机会。
- `stop_conditions`: 仅凭标题推断内容；综述版本或全文不匹配；结构借鉴来源无法定位。
- `quality_checks`: 时间覆盖与主题覆盖分开；贡献和局限不混写；没有把“未发现”表述为“并不存在”。

#### 3. 术语扩展

- `prompt_id`: `CORE-TERM-EXPANSION-01`
- `phase`: Task 06-07，建库
- `intent`: 建立中英文术语表和可组合概念组。
- `when_to_use`: 范围已批准、准备设计数据库检索式时。
- `required_inputs`: 批准题目、PICO/对象框架或研究问题、领域包、种子文献术语。
- `tool_or_database_prerequisites`: 可查权威词表、标准或数据库索引词；具体数据库语法尚不在此步骤假定。
- `prompt_text`: 围绕基底、膜层、界面、制备、结构、光学、机械、环境、制造和应用生成术语。每个术语记录中文、标准英文、缩写、旧称、拼写变体、上下位词、排除歧义、来源和适用数据库。对 DLC 区分 a-C、a-C:H、ta-C、ta-C:H、掺杂和复合体系；对硫系玻璃区分元素体系与具体组成。将术语组织为可独立测试的概念组，不直接拼成最终查询。
- `expected_outputs`: 术语表、概念组、歧义与排除清单、待数据库验证的语法问题。
- `stop_conditions`: 术语来源不明；材料类别被错误等同；关键对象存在未决边界。
- `quality_checks`: 中英文双向覆盖；缩写无歧义；同义词与上下位词分开；排除词经已知相关文献反测。

#### 4. 检索式设计

- `prompt_id`: `CORE-QUERY-DESIGN-01`
- `phase`: Task 08-10，建库
- `intent`: 设计可复现的宽、平衡、精确三级检索策略并适配各数据库。
- `when_to_use`: 概念组和数据库计划已批准时。
- `required_inputs`: 术语表、概念组、数据库访问矩阵、研究范围、种子文献。
- `tool_or_database_prerequisites`: 目标数据库至少 L2；已现场核验字段、短语、通配、邻近和长度规则。
- `prompt_text`: 先生成平台中立的布尔逻辑，再为每个获批数据库翻译为宽、平衡、精确三级查询。逐条说明字段、过滤器、预期用途、召回风险和精度风险。用已知相关文献做正向校验，用典型噪声做反向校验。不要编造结果数；实际执行后才登记 query_id、时间、精确字符串、结果数和导出批次。
- `expected_outputs`: 平台中立逻辑、数据库专用检索式、测试矩阵、查询版本和运行记录字段。
- `stop_conditions`: 数据库语法未核验；登录/CAPTCHA；查询被截断或拒绝；种子文献无法召回且原因未解释。
- `quality_checks`: 三级查询目的不同；过滤条件透明；每条实跑查询可复现；报告数与导出数可对账。

#### 5. 筛选解释

- `prompt_id`: `CORE-SCREENING-RATIONALE-01`
- `phase`: Task 12-14，建库
- `intent`: 对题名摘要或全文筛选给出一致、可审计的建议与理由。
- `when_to_use`: 纳排标准已批准并需要处理待筛选记录时。
- `required_inputs`: Source_ID、题名、摘要或全文、纳排标准版本、已有人工决策示例。
- `tool_or_database_prerequisites`: 题名摘要筛选至少有真实题录；全文筛选必须打开匹配的合法全文。
- `prompt_text`: 按当前纳排标准逐条评估记录，输出 INCLUDE、EXCLUDE 或 UNCERTAIN 建议、命中的标准编号、证据文本、解释和需人工核查项。信息缺失时选择 UNCERTAIN，不从标题补全材料、工艺或结果。Systematic Review 中只提供辅助建议，不冒充第二位独立人类筛选者。
- `expected_outputs`: 筛选建议、标准编号、排除原因、证据位置和冲突/人工复核队列。
- `stop_conditions`: 全文与题录不匹配；标准版本不明；关键信息仅在不可访问全文中；两个人类审稿者发生未解决冲突。
- `quality_checks`: 排除原因单一且可复核；同类记录标准一致；UNCERTAIN 不被强制归类；系统综述角色表述真实。

#### 6. 全文精读

- `prompt_id`: `CORE-FULLTEXT-READING-01`
- `phase`: Task 16，搭架
- `intent`: 从全文提取可定位、可比较的研究设计与结果。
- `when_to_use`: 文献已通过全文筛选并进入精读优先队列时。
- `required_inputs`: Source_ID、匹配全文、结构化阅读模板、领域包、研究问题。
- `tool_or_database_prerequisites`: 合法全文可读；扫描件需要可验证 OCR；图表提取需要页码和元素定位能力。
- `prompt_text`: 从头至尾阅读全文，分别记录研究目的、样品链、基底组成、膜层与层序、工艺参数、表征方法、测试条件、结果、误差、作者解释、作者推测、局限和与研究问题的关系。每个数字或机制结论给出页码、章节、图或表位置。区分正文报告值、图中读取值、换算值和模型值；无法读取处明确标记。
- `expected_outputs`: 结构化精读记录、可用证据位置、数据冲突、缺失字段和后续证据卡候选。
- `stop_conditions`: PDF 错配/残缺；OCR 破坏关键数字或公式；补充材料缺失导致核心结论不可核验。
- `quality_checks`: 关键结果达到 V4；观察、解释、推测和 Skill 综合分开；条件与单位完整；未把 Raman 拟合当作精确 sp3。

#### 7. 证据卡

- `prompt_id`: `CORE-EVIDENCE-CARD-01`
- `phase`: Task 17-18，搭架
- `intent`: 将可用证据封装为可回查的主张候选。
- `when_to_use`: 全文精读获批，需要构建 Claim-Evidence Matrix 时。
- `required_inputs`: Source_ID、全文精读记录、原文位置、研究问题、`evidence-card.schema.json`。
- `tool_or_database_prerequisites`: 原文位置可回查；元数据至少 V2，核心证据通常 V4。
- `prompt_text`: 为一项原子化证据生成证据卡，包含原文结论/数据、证据类型、样品与条件、方法、原文位置、核验等级、支持强度、适用边界、局限、替代解释、可支持与不可支持的主张。机制卡必须逐段检查因果链；定量卡必须保留单位、误差和比较基线。
- `expected_outputs`: 符合 Schema 的证据卡、候选 Claim_ID 关系和人工复核标记。
- `stop_conditions`: 找不到原文位置；数值条件不全；主张范围大于证据；元数据冲突未关闭。
- `quality_checks`: 一卡一主要证据；来源与位置可回查；支持/反驳/无关关系明确；证据强度不过度提升。

#### 8. 争议综合

- `prompt_id`: `CORE-CONTROVERSY-SYNTHESIS-01`
- `phase`: Task 19，搭架
- `intent`: 解释跨研究结论不一致及其条件边界。
- `when_to_use`: Claim-Evidence Matrix 已批准且同一主张存在冲突证据时。
- `required_inputs`: Claim_ID、支持与反驳证据卡、样品/工艺/测试条件、质量与核验等级。
- `tool_or_database_prerequisites`: 关键全文证据达到 V4；可按领域包字段比较。
- `prompt_text`: 围绕指定 Claim_ID 分组比较支持、反驳和条件性证据。优先检查基底组成、DLC 类型、界面层、膜厚、应力、工艺能量/温度、光学波段、机械载荷、环境标准、样本数和测量方法。区分真实矛盾、条件差异、测量差异、证据不足和术语混用。形成条件化结论，不按论文数量投票。
- `expected_outputs`: 争议矩阵、差异原因排序、条件化共识、残余不确定性和新增研究问题。
- `stop_conditions`: 关键条件缺失；冲突只来自摘要；比较跨越不可换算标准；证据质量无法评估。
- `quality_checks`: 每项解释有证据；替代解释被讨论；少数高质量反证未被多数低质量记录淹没；措辞与核验等级一致。

#### 9. 研究空白

- `prompt_id`: `CORE-RESEARCH-GAP-01`
- `phase`: Task 19-20，搭架
- `intent`: 从证据地图识别可证成、可行动的研究空白。
- `when_to_use`: 文献地图、证据矩阵和争议综合已形成时。
- `required_inputs`: 研究问题、文献地图、Claim-Evidence Matrix、时间/方法/材料覆盖、未关闭风险。
- `tool_or_database_prerequisites`: 核心数据库检索和引用追踪已记录；主要全文缺口已知。
- `prompt_text`: 从材料、工艺、界面、表征、性能、标准、寿命、制造放大和系统应用维度寻找证据断点。对每个候选空白说明已覆盖范围、缺失证据、检索与全文限制、为何重要、可检验问题和所需方法。区分真正证据空白、报告不足、数据库不可访问、术语遗漏和范围外问题。
- `expected_outputs`: 分级空白清单、证据依据、可信度、可行动研究问题和路线图更新项。
- `stop_conditions`: 检索覆盖不可审计；空白仅依据“命中少”；关键数据库或语种被省略且未批准风险。
- `quality_checks`: 每个空白连接地图节点/关系与 Claim；限制透明；不使用“首次”“无人研究”等绝对表述，除非有充分验证。

#### 10. 大纲审查

- `prompt_id`: `CORE-OUTLINE-REVIEW-01`
- `phase`: Task 20，搭架
- `intent`: 检查三级大纲的论证递进、证据配置和图表可追溯性。
- `when_to_use`: 已生成候选大纲但尚未请求 Task 20 批准时。
- `required_inputs`: 三级大纲、研究问题、Claim-Evidence Matrix、文献地图、图表计划、篇幅约束。
- `tool_or_database_prerequisites`: 核心 Claim 和图表来源可回查；目标期刊结构要求若使用必须联网核验。
- `prompt_text`: 逐级审查大纲。对每个三级标题说明其问题、中心命题、主要证据、比较、冲突、局限、阶段判断和图表。识别作者流水账、重复、章节失衡、无证据主张、孤立图表和范围漂移。把每条修改建议标记优先级、位置、证据和关闭条件。
- `expected_outputs`: `outline_review_report.md` 内容、修订建议、章节证据覆盖表和阻断项。
- `stop_conditions`: 核心章节无 Claim；关键争议无位置；图表版权或来源不明；大纲版本冲突。
- `quality_checks`: 每个三级标题连接至少一个合格 Claim_ID/Source_ID；关键问题关闭前不批准；未经明确批准不进入 Task 21。

#### 11. 段落写作

- `prompt_id`: `CORE-PARAGRAPH-WRITING-01`
- `phase`: Task 21B，成稿
- `intent`: 按批准大纲和证据边界写出可审计的综述段落。
- `when_to_use`: 写作语言与当前章节已批准，且该段证据子集完整时。
- `required_inputs`: 批准大纲位置、段落功能、Claim_ID、证据卡、正式引文、术语规则、语言决定。
- `tool_or_database_prerequisites`: 核心事实至少 V3；机制、定量和图表证据至少 V4。
- `prompt_text`: 仅用给定 Claim 和证据写一个综述段落，按中心观点、主要证据、跨研究比较、差异原因、适用条件、局限和阶段性判断组织。每个事实、数字和机制紧邻正式引文；对证据不一致使用条件化措辞。不要新增未登记主张，不要写作者流水账，不要把相关性升级为因果。
- `expected_outputs`: 带正式引文的段落、内部 Claim/Source 审计映射、未解决问题。
- `stop_conditions`: 段落需要的新主张没有 Claim_ID；证据低于门禁；引用与原文不符；批准大纲不支持该段。
- `quality_checks`: 一段一中心功能；每项主张可追溯；比较条件完整；措辞强度不超过证据；完成当前章节后必须暂停审批。

#### 12. 引用核查

- `prompt_id`: `CORE-CITATION-AUDIT-01`
- `phase`: Task 21D，成稿
- `intent`: 逐句检查主张、引文、数字和原文证据的一致性。
- `when_to_use`: 全文整合稿已批准进入引用审计时。
- `required_inputs`: 审计版稿件、Claim-Evidence Matrix、Source registry、全文位置、图表追踪。
- `tool_or_database_prerequisites`: 可访问被核查的真实来源；DOI/元数据可交叉验证。
- `prompt_text`: 逐句识别可核查事实、数字、比较、机制、因果、范围和引文。为每项登记 Claim_ID、Source_ID、原文位置、核验等级、支持/部分支持/不支持、问题类型和建议修正。重点查找无来源数字、二次引用、引用漂移、范围扩大、条件丢失、同引文支持多项无关主张和图表来源缺口。
- `expected_outputs`: 引用审计记录、阻断项、可执行修订和复核状态。
- `stop_conditions`: 来源无法打开或错配；主张没有证据记录；图表关键单元格无法追溯；DOI 冲突未解决。
- `quality_checks`: 核心句逐句覆盖；机制/定量达到 V4；修订后复核；所有关键问题关闭前不生成清洁投稿版。

#### 13. 期刊匹配

- `prompt_id`: `CORE-JOURNAL-MATCH-01`
- `phase`: Task 21F，成稿
- `intent`: 基于当前官方政策比较目标期刊的学术适配、成本和投稿风险。
- `when_to_use`: 清洁候选稿和用户偏好已形成时。
- `required_inputs`: 稿件题目/摘要/范围、文章类型、篇幅、图表、开放获取与预算偏好、候选期刊。
- `tool_or_database_prerequisites`: 必须联网访问期刊/出版商官方页面并记录核验日期；指标来源需标明年份和来源。
- `prompt_text`: 为候选期刊核验 scope、可投稿综述类型、是否邀约、字数、图表、参考文献、APC、开放获取、版权、数据和 AI 政策。记录官方 URL、页面名称和访问日期。比较主题适配、读者、格式改造成本、政策风险与备选顺序；无法确认的信息标为人工核查，不用记忆补齐。
- `expected_outputs`: 期刊比较矩阵、推荐顺序、格式差距、成本与风险、官方来源记录。
- `stop_conditions`: 官方页面不可访问；文章类型/邀约要求不明确；费用或政策相互冲突；用户尚未决定关键预算或投稿目标。
- `quality_checks`: 动态字段均有当前官方证据；学术适配与指标分开；不保证录用；最终选择由用户明确批准。

#### 14. 审稿回复

- `prompt_id`: `CORE-REVIEWER-RESPONSE-01`
- `phase`: Task 21H，返修
- `intent`: 形成意见、响应、证据、稿件修改和位置闭环。
- `when_to_use`: 已收到真实编辑/审稿意见和对应投稿版本时。
- `required_inputs`: 原始意见、投稿稿件版本、期刊要求、Claim-Evidence Matrix、实际完成的修改或实验。
- `tool_or_database_prerequisites`: 可读取带行号稿件和相关证据；新增期刊政策需联网核验。
- `prompt_text`: 逐条原样登记意见并分类严重度和响应类型。起草礼貌、直接的回复，说明同意、部分同意或有证据的不同意；列出实际修改文本、稿件位置、Claim_ID/Source_ID 和仍需作者完成的事项。不得编造实验、分析、页码、行号或已完成修改。跨意见冲突时先建立决策清单。
- `expected_outputs`: 审稿回复矩阵、逐条回复草稿、稿件修改建议、未关闭事项和最终 response letter 草案。
- `stop_conditions`: 意见文本不完整；稿件版本错配；要求新实验但尚未完成；作者立场或数据需确认；修改位置无法核验。
- `quality_checks`: 每条意见均闭环；回复与稿件实际修改一致；不同意有证据且语气专业；所有作者声明和新增结果经人工确认。

#### 项目化规则

Task 05 创建项目级 `prompt_library.md` 时，只保留与已批准路线图相关的条目，并将泛化输入替换为项目文件、版本和 ID。后续在 Task 10、15、20 和 21 更新执行前提与输出路径，但保留旧版本。项目提示词库可由用户修改；任何修改若改变任务顺序、审批门禁、证据阈值或确定性文件操作，必须回到相应规范或脚本，而不能只改提示词。

<a id="module-references-roadmap-item-schema-json"></a>
## Module: `references/roadmap-item.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/roadmap-item.schema.json",
  "title": "Research Roadmap Item",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "roadmap_item_id", "research_question", "stage", "task", "prerequisites", "evidence_needed", "preferred_sources", "planned_deliverable", "decision_gate", "risk", "status", "owner", "last_updated"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "roadmap_item_id": {"type": "string", "pattern": "^RM-[0-9]{3,}$"},
    "research_question": {"type": "string", "minLength": 1},
    "stage": {"enum": ["STEP_00", "STAGE_1", "STAGE_2", "STAGE_3", "STAGE_4"]},
    "task": {"$ref": "common.schema.json#/$defs/taskId"},
    "prerequisites": {"type": "array", "items": {"type": "string"}},
    "evidence_needed": {"type": "array", "items": {"type": "string"}, "minItems": 1},
    "preferred_sources": {"type": "array", "items": {"type": "string"}},
    "planned_deliverable": {"type": "string", "minLength": 1},
    "decision_gate": {"type": "string", "minLength": 1},
    "risk": {"type": ["string", "null"]},
    "status": {"$ref": "common.schema.json#/$defs/status"},
    "owner": {"type": ["string", "null"]},
    "last_updated": {"type": ["string", "null"], "format": "date"}
  }
}
```

<a id="module-references-schema-and-template-map-md"></a>
## Module: `references/schema-and-template-map.md`

### Schema and Template Map

Use Schema files as the field contract. Markdown, YAML, JSON, XLSX, and DOCX assets are editable working surfaces; scripts must normalize them into Schema-conformant records before validation.

| Contract | Primary template or workbook |
|---|---|
| `project-state.schema.json` | `assets/templates/project_state.yaml`, `assets/templates/task_status.yaml` |
| `task-result.schema.json` | `assets/templates/stage_report.md` and per-task JSON results |
| `source-record.schema.json` | `assets/templates/literature_registry.xlsx` / `Source Registry` |
| `claim.schema.json` | `assets/templates/evidence_and_claims.xlsx` / `Claims` |
| `evidence-card.schema.json` | `assets/templates/evidence_card.md`, `assets/templates/evidence_and_claims.xlsx` / `Evidence Cards` |
| `roadmap-item.schema.json` | `assets/templates/preflight_and_roadmap.xlsx` / `Research Roadmap` |
| `literature-map.schema.json` | `assets/templates/literature_map.xlsx` |
| `figure-table-traceability.schema.json` | `assets/templates/evidence_and_claims.xlsx` / `Figure-Table Trace` |

#### Flat-Table Encoding

XLSX cells cannot directly store JSON arrays. Encode arrays as semicolon-delimited values in workbooks, preserving semicolons inside a value by escaping them as `\;`. Import scripts must split and unescape these fields. Empty cells normalize to empty arrays or `null` according to the corresponding Schema.

Dates use ISO `YYYY-MM-DD`; timestamps use RFC 3339. Boolean cells use actual Boolean values where supported. IDs are stable and must never be reassigned after citation or approval.

#### Verification Levels

`V0` unverified; `V1` title only; `V2` bibliographic metadata and DOI; `V3` abstract or record page; `V4` full-text page, section, figure, or table location; `V5` critical fact checked by a second source or a human. Core prose facts require at least V3. Mechanisms, quantitative comparisons, and figure/table data require at least V4.


<a id="module-references-source-record-schema-json"></a>
## Module: `references/source-record.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/source-record.schema.json",
  "title": "Source Record",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "source_id", "title", "authors", "year", "journal", "document_type", "doi", "url", "language", "database_sources", "record_version", "supersedes_source_id", "verification_level", "verification_date", "full_text_status", "screening_decision", "screening_reason", "materials", "substrates", "coatings", "deposition_routes", "interface_strategies", "optical_properties", "mechanical_properties", "environmental_properties", "manufacturing_properties", "characterization_methods", "themes", "research_stage", "intended_uses", "evidence_strength", "notes"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "source_id": {"$ref": "common.schema.json#/$defs/sourceId"},
    "title": {"type": ["string", "null"]},
    "authors": {"type": "array", "items": {"type": "string"}},
    "year": {"type": ["integer", "null"], "minimum": 1600, "maximum": 2200},
    "journal": {"type": ["string", "null"]},
    "document_type": {"enum": ["JOURNAL_ARTICLE", "REVIEW", "CONFERENCE_PAPER", "BOOK_CHAPTER", "STANDARD", "PATENT", "THESIS", "PREPRINT", "REPORT", "OTHER"]},
    "doi": {"type": ["string", "null"]},
    "url": {"type": ["string", "null"], "format": "uri"},
    "language": {"type": ["string", "null"]},
    "database_sources": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "record_version": {"type": "string", "minLength": 1},
    "supersedes_source_id": {"anyOf": [{"$ref": "common.schema.json#/$defs/sourceId"}, {"type": "null"}]},
    "verification_level": {"$ref": "common.schema.json#/$defs/verificationLevel"},
    "verification_date": {"type": ["string", "null"], "format": "date"},
    "full_text_status": {"enum": ["NOT_REQUESTED", "MISSING", "PARTIAL", "AVAILABLE", "UNREADABLE", "MISMATCHED"]},
    "screening_decision": {"enum": ["UNSCREENED", "INCLUDE", "EXCLUDE", "UNCERTAIN", "BACKGROUND_ONLY", "METHOD_ONLY"]},
    "screening_reason": {"type": ["string", "null"]},
    "materials": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "substrates": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "coatings": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "deposition_routes": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "interface_strategies": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "optical_properties": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "mechanical_properties": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "environmental_properties": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "manufacturing_properties": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "characterization_methods": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "themes": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "research_stage": {"type": ["string", "null"]},
    "intended_uses": {"type": "array", "items": {"enum": ["CORE", "SUPPORTING", "BACKGROUND", "METHOD", "CONFLICT"]}, "uniqueItems": true},
    "evidence_strength": {"enum": ["UNASSESSED", "WEAK", "MODERATE", "STRONG"]},
    "notes": {"type": ["string", "null"]}
  }
}
```

<a id="module-references-state-machine-md"></a>
## Module: `references/state-machine.md`

### Project State Machine

This reference is the normative execution contract for Step 00, Task 01-20, and Task 21A-21H. Persist every transition in `project_state.yaml`; never infer approval from conversational tone.

#### State Set

| State | Meaning |
|---|---|
| `NOT_STARTED` | No execution has begun. |
| `IN_PROGRESS` | The task owns the current working input and may write draft outputs. |
| `BLOCKED` | Progress requires external access, missing evidence, user action, or a resolved conflict. |
| `REVIEW_REQUIRED` | Outputs and quality-gate results are ready for an explicit user decision. |
| `APPROVED` | The user explicitly accepted the task result. |
| `REJECTED` | The user explicitly rejected the task result; revision is required. |
| `SKIPPED_WITH_RISK` | The user explicitly waived a gate and accepted a recorded risk. |
| `SUPERSEDED` | A previously approved or risk-waived result has a newer approved replacement. |
| `ARCHIVED` | A superseded record is retained only for audit and recovery. |

#### Legal Transitions

| From | To | Required evidence |
|---|---|---|
| `NOT_STARTED` | `IN_PROGRESS` | Prerequisites and current input validated. |
| `IN_PROGRESS` | `REVIEW_REQUIRED` | Independent output written and quality gate executed. |
| `NOT_STARTED`, `IN_PROGRESS`, `REVIEW_REQUIRED`, or `REJECTED` | `BLOCKED` | Blocking reason, prior state, owner, and recovery condition recorded. |
| `REVIEW_REQUIRED` | `APPROVED` | Explicit approval such as `确认通过` tied to the task ID. |
| `REVIEW_REQUIRED` | `REJECTED` | Explicit rejection or requested revision tied to the task ID. |
| `REVIEW_REQUIRED` | `IN_PROGRESS` | User explicitly requests revision or re-execution. |
| `REVIEW_REQUIRED` | `SKIPPED_WITH_RISK` | Explicit waiver plus a risk record and affected outputs. |
| `REJECTED` | `IN_PROGRESS` | Rework scope and new input recorded. |
| `BLOCKED` | recorded `blocked_from` state | Recovery condition has been satisfied and revalidated; then follow normal transitions. |
| `APPROVED` | `SUPERSEDED` | A replacement output has separately reached `APPROVED`. |
| `SKIPPED_WITH_RISK` | `SUPERSEDED` | A replacement output has separately reached `APPROVED`. |
| `SUPERSEDED` | `ARCHIVED` | Replacement linkage and retention path recorded. |

Any transition not listed above is illegal. A task must not jump from `NOT_STARTED` to `APPROVED`, from `IN_PROGRESS` to `APPROVED`, or from `BLOCKED` to `REVIEW_REQUIRED`.

#### Approval Gate

1. End every task at `REVIEW_REQUIRED` and pause.
2. Accept approval only when the user names the decision unambiguously, for example `确认通过`, `批准 Task 14`, or `进入下一步` when the immediately preceding message contains exactly one pending gate.
3. Treat acknowledgements such as “好的”, “可以看看”, “继续说”, or topic discussion as ambiguous. Ask for a decision and remain at `REVIEW_REQUIRED`.
4. Record `decision`, `decision_text`, `decided_by`, `decided_at`, and the approved output paths.
5. Never overwrite an approved output. Create a new version; after the replacement is approved, mark the old version `SUPERSEDED`.
6. `SKIPPED_WITH_RISK` is not approval. It requires the exact waived gate, consequence, mitigation, owner, and review point.

#### Execution Cycle

For each task or Task 21 subtask:

1. Read and validate `project_state.yaml` against `project-state.schema.json`.
2. Restore state in the required recovery order.
3. Check all prerequisite states and input file hashes.
4. Transition to `IN_PROGRESS` and persist before doing material work.
5. Write draft work to a task-specific path; retain source and evidence IDs.
6. Run the task quality gate and update risk, decision, evidence, and manual-check records.
7. Write a task result conforming to `task-result.schema.json`.
8. Transition to `REVIEW_REQUIRED`, write `stage_report.md`, and pause.

#### Step 00 Gate

Before Task 01, all required database access records must leave `UNVERIFIED`. A platform may be `NOT_REQUIRED_FOR_THIS_PROJECT` or `USER_WAIVED` only after explicit user confirmation. Login, VPN, CAPTCHA, or subscription barriers are recorded as access facts, not bypassed.

#### Task 21 Recovery

Task 21A-21H are independent state records. Persist `current_subtask`, inputs, outputs, quality-gate result, and approval record for each. Task 21B also persists the current chapter and pauses after every chapter. Approval of one subtask never implies approval of another.

#### Batch Mode

`stage_batch` may advance only through tasks whose prerequisites are already approved and whose gates do not require a new judgment. Immediately pause and persist state when any of the following occurs:

- permission, login, VPN, CAPTCHA, subscription, or browser handoff;
- metadata conflict, duplicate ambiguity, or version conflict;
- missing, unreadable, incomplete, or mismatched full text;
- scope, review-type, inclusion, mechanism, or other academic judgment;
- evidence below the required verification level;
- failed quality gate or unresolved manual check;
- conflict with an approved output;
- user cancellation or new instruction.

After a batch pause, set the affected task to `BLOCKED` or `REVIEW_REQUIRED` according to whether work can be reviewed, report the exact stop reason, and do not start another task.

#### Blocked, Skipped, and Superseded Records

- `BLOCKED`: include `blocker_id`, `blocked_from`, category, description, required action, owner, blocked_at, and resume_condition.
- `SKIPPED_WITH_RISK`: include `risk_id`, waived_gate, consequence, mitigation, owner, review_by, and user decision text.
- `SUPERSEDED`: include replacement task result ID, replacement path, approval timestamp, and archive location.

#### Recovery Order

On resume, read in this order and stop on inconsistency:

1. project state;
2. approved task and subtask records;
3. most recent approved outputs and their hashes;
4. risk register;
5. manual-check register;
6. current input and its hash;
7. the user's last formal decision.

If records disagree, preserve all files, set the current task to `BLOCKED`, and request a reconciliation decision. Do not select the newest timestamp as a substitute for approval.

#### Command Mapping

| User command | State effect |
|---|---|
| `确认通过` / `进入下一步` | `REVIEW_REQUIRED -> APPROVED`, then the next eligible task may start. |
| `修改：...` / `重新执行当前任务` | `REVIEW_REQUIRED` or `REJECTED -> IN_PROGRESS`. |
| `补充资料` | Attach input; resume only after validation. |
| `返回上一任务` | Open a new version; do not mutate an approved record. |
| `暂停项目` | Persist current state and set project pause metadata. |
| `恢复项目` | Execute the recovery order before any transition. |
| `批量执行当前阶段` | Set `execution_mode: stage_batch`; batch stop rules remain mandatory. |
| `取消批量执行` | Set `execution_mode: single_task_confirmation`. |
| `跳过当前门禁并记录风险` | `REVIEW_REQUIRED -> SKIPPED_WITH_RISK` only after risk details are recorded. |


<a id="module-references-systematic-review-branch-md"></a>
## Module: `references/systematic-review-branch.md`

### Systematic Review Strict Branch

#### Activation

Load this reference only when Task 02 explicitly approves `SYSTEMATIC_REVIEW`. If the project cannot meet the minimum controls below, recommend a transparent Narrative Review or a scoped review type; do not retain the Systematic label by weakening requirements silently.

#### Protocol Before Formal Screening

Freeze a dated protocol containing review questions, eligibility criteria, information sources, full search strategies, deduplication rules, reviewer roles, conflict resolution, extraction fields, quality/bias assessment, synthesis plan, deviations and amendment rules. Register when an appropriate registry accepts the topic; otherwise record the reason for non-registration and preserve a versioned local protocol.

#### Search Reproducibility

For each database retain platform and collection, full query, field tags, filters, coverage dates, run date/time, result count, export batches and file hashes. Document inaccessible databases and approved substitutes. Discovery-engine results may supplement but must not replace reproducible core database searches.

#### Screening Controls

Use two independent human reviewers for title/abstract and full-text screening where claimed. Record reviewer decisions separately, calculate or summarize agreement, and resolve disagreements through a predefined third-reviewer or consensus procedure. AI may prioritize or explain but cannot be represented as the second independent human reviewer.

If two human reviewers are unavailable, record the limitation and mitigation such as blinded duplicate sampling. The final manuscript must not state that dual screening occurred.

#### PRISMA Accounting

Maintain counts for identification, pre-deduplication, duplicates, records screened, records excluded, reports sought, reports not retrieved, full texts assessed, full-text exclusions by reason, and studies included. Counts must reconcile with import and screening logs; never invent a flow count to make the diagram balance.

#### Risk of Bias and Quality

Select a tool appropriate to study design and review question before assessment. Record domain judgments, rationale, reviewer and source location. Do not create a generic numeric “quality score” unless the selected method supports it. Use quality judgments in synthesis rather than excluding inconvenient findings post hoc.

#### Standardized Extraction

Pilot the extraction form on representative studies. Define units, missing-value rules, multiple reports per study, repeated samples, outcome time points, conversions and conflict resolution. Preserve raw extracted values and derived calculations separately.

#### Synthesis Plan

Predefine narrative grouping, effect direction, heterogeneity variables, subgroup logic and sensitivity checks. This Skill does not default to Meta-analysis. Statistical pooling requires compatible designs/outcomes, a separate approved analysis plan, reproducible calculations and appropriate statistical expertise.

#### Amendments and Deviations

Version every protocol amendment with date, rationale, affected records/tasks and approval. Distinguish planned analyses from post hoc exploration in both audit and manuscript versions.

#### Required Outputs

Protocol, registration record or reason, complete search appendix, deduplication log, dual-reviewer screening records, disagreement log, PRISMA count table/diagram, full-text exclusion list, risk-of-bias assessment, standardized extraction set, synthesis plan, amendments and limitations.

#### Blocking Gate

Block approval when counts do not reconcile, search strategies are incomplete, full-text exclusions lack reasons, claimed dual screening is absent, bias assessment is inappropriate, protocol deviations are hidden, or Meta-analysis is proposed without compatible data and a separate plan.

<a id="module-references-task-00-preflight-md"></a>
## Module: `references/task-00-preflight.md`

### Step 00 数据库与运行环境预检

#### 1. 任务名称和目标
在 Task 01 前核验数据库访问能力、本地文件与工具能力，形成真实能力边界，禁止把“网页可打开”当成“可检索、可导出或可访问全文”。

#### 2. 适用范围
所有 Narrative Review 与 Systematic Review 项目；数据库清单和状态定义以 v2 规格及 `optical-coating-integrated` 的学科需求为准。

#### 3. 前置条件
项目目录可写；用户已说明可能使用的机构账号、VPN 和本地软件。无前置任务，但状态必须从 `NOT_STARTED` 合法转换。

#### 4. 必需和可选输入
必需：课题、可用数据库、机构权限、浏览器状态、本地文件格式需求。可选：已有 PDF、RIS/BibTeX/EndNote/Zotero 导出、OCR 和版本控制环境。

#### 5. 执行步骤
逐项测试 WoS、Scopus、PubMed、Google Scholar、百度学术、Crossref、OpenAlex、GeoRef、Engineering Village、ScienceDirect、SpringerLink、CNKI、万方；登记 L0–L5、访问状态、测试日期、真实测试式和限制。随后检查 Markdown、CSV/XLSX、DOCX、JSON/YAML、PDF、OCR、脚本、联网、浏览器、持久目录、临时目录、版本控制和断点恢复。

#### 6. 应调用的 scripts、references 和 assets
读取 `state-machine.md`、`database-access-and-search.md`；复制 `assets/templates/preflight_and_roadmap.xlsx`。使用 `scripts/init_project.py` 进行无覆盖初始化，并用 `scripts/validate_project.py` 检查持久状态、目录、输出哈希和恢复约束。

#### 7. 文件操作
创建 `00_preflight/`，保存数据库访问表、环境检查表和受限能力说明。登录信息、Cookie、令牌和密码不得写入项目或日志。

#### 8. 文献与证据追踪要求
本步骤不创建虚假 Source_ID。测试检索若保留记录，标明仅为能力测试并登记真实来源、日期和结果数。

#### 9. 输出文件
`database_access_check.xlsx`、`environment_preflight.md`、风险与人工操作清单，以及更新后的 `project_state.yaml`。

#### 10. 质量检查和通过标准
进入 Task 01 前，必需平台不得保留 `UNVERIFIED`；每个平台记录字段完整；L4/L5 仅在实际导出/全文访问成功后赋值；项目需要的文件能力至少有一条可行路径。

#### 11. 阻断条件和风险
登录、VPN、验证码、订阅、地区限制或浏览器权限立即暂停；不得规避访问控制。项目关键平台不可用时设 `BLOCKED`，或由用户明确批准 `USER_WAIVED`/`NOT_REQUIRED_FOR_THIS_PROJECT`。

#### 12. 用户确认问题
“以上数据库与本地能力状态是否准确？请回复‘确认通过’，或指出需要重测、豁免或补充的平台。”

#### 13. 下一任务接口
向 Task 01 传递已批准的访问矩阵、环境能力、风险和人工操作要求；未获批准不得初始化正式项目。

#### 14. 最小示例
对 DLC—硫系玻璃课题实际测试 WoS、OpenAlex、CNKI 与 ScienceDirect；若 CNKI 需机构登录，则记录 `LOGIN_REQUIRED` 和当前 L1，而不是宣称已获得中文核心文献。

<a id="module-references-task-01-project-initialization-md"></a>
## Module: `references/task-01-project-initialization.md`

### Task 01 项目初始化

#### 1. 任务名称和目标
把用户课题、用途、期限、资源和 Step 00 能力固化为可恢复项目，分配稳定项目 ID 和控制文件。

#### 2. 适用范围
所有新项目；恢复既有项目时使用 `state-machine.md` 的恢复顺序，不重复初始化。

#### 3. 前置条件
Step 00 为 `APPROVED` 或 `SKIPPED_WITH_RISK`，且所有未核验平台已处理。

#### 4. 必需和可选输入
必需：题目、综述用途、目标读者、截止日期、可用人力和已批准预检。可选：目标期刊、已有大纲、文献库、团队分工和写作语言偏好。

#### 5. 执行步骤
生成项目 ID；复制状态和清单模板；建立 00–21 任务目录；记录研究目标、成功标准、范围假设、数据库能力、交付格式、时间约束和风险；将 Task 01 设为 `REVIEW_REQUIRED`。

#### 6. 应调用的 scripts、references 和 assets
读取 `state-machine.md`、`schema-and-template-map.md`；由 `scripts/init_project.py` 复制 `project_state.yaml`、`project_manifest.json`、`task_status.yaml`、`stage_report.md` 并执行确定性、无覆盖初始化。

#### 7. 文件操作
创建 `01_project_initialization/working|outputs|qa|logs` 及项目级 `working/outputs/qa/logs`；计算输入哈希；批准版本采用新文件名，不覆盖。

#### 8. 文献与证据追踪要求
导入的已有记录只登记原始文件和格式，不在本任务生成未经核验的 DOI、Source_ID 或全文状态。

#### 9. 输出文件
`project_brief.md`、`project_state.yaml`、`project_manifest.json`、任务登记、决策日志、风险清单和人工核查清单。

#### 10. 质量检查和通过标准
工作目录可写；项目 ID 唯一；题目、用途、期限、责任人和能力边界明确；控制文件可解析并符合 Schema；恢复入口明确。

#### 11. 阻断条件和风险
项目目标或交付物不明确、目录不可持久化、输入版本冲突或关键期限缺失时阻断。不得在临时目录中建立唯一项目副本。

#### 12. 用户确认问题
“请确认项目目标、截止日期、目录和能力边界是否正确；确认后进入综述类型判定。”

#### 13. 下一任务接口
向 Task 02 传递项目简报、资源边界和用户正式决策。

#### 14. 最小示例
项目题目登记为“红外硫系玻璃基底 DLC 薄膜：材料基础、制备技术与应用进展”，用途为中文学术综述，过程报告默认中文，但写作语言仍留待 Task 21A 决定。

<a id="module-references-task-02-review-type-md"></a>
## Module: `references/task-02-review-type.md`

### Task 02 综述类型判定

#### 1. 任务名称和目标
区分 Narrative Review 与 Systematic Review，避免因检索较广就错误使用“系统综述”名称。

#### 2. 适用范围
所有项目；选择 Systematic Review 时必须同时加载 `systematic-review-branch.md`。

#### 3. 前置条件
Task 01 已批准，项目目标、期限、资源和数据库能力明确。

#### 4. 必需和可选输入
必需：研究目的、问题类型、预期透明度、数据库能力、人力和期限。可选：注册平台、协议模板、双人筛选资源和偏倚评价工具。

#### 5. 执行步骤
比较两类综述在问题结构、协议、检索复现、筛选、偏倚风险和综合方法上的要求；评估项目是否能满足 Systematic Review 的最低条件；形成推荐与备选方案。

#### 6. 应调用的 scripts、references 和 assets
读取 `systematic-review-branch.md`、`state-machine.md`。输出使用项目 Markdown；用 `scripts/validate_project.py` 检查 review_type、状态与项目记录的一致性，Systematic Review 的学术合规仍按严格分支人工门禁。

#### 7. 文件操作
创建 `02_review_type/`，保存类型评估和用户决策；更新 `project_state.yaml.review_type`，保留变更历史。

#### 8. 文献与证据追踪要求
用于判断的同类综述或指南分配 Source_ID；政策和方法指南记录版本与访问日期。

#### 9. 输出文件
`review_type_assessment.md`、类型决策记录，以及 Systematic 分支所需的初始合规缺口清单。

#### 10. 质量检查和通过标准
推荐理由连接项目能力；若选 Systematic，协议、双人筛选、分歧处理、PRISMA、偏倚风险和标准化提取均有可行方案；否则明确采用 Narrative Review。

#### 11. 阻断条件和风险
用户坚持 Systematic 名称但资源无法满足最低要求时阻断；不得伪装注册、双人筛选或 Meta-analysis。

#### 12. 用户确认问题
“请明确批准 Narrative Review 或 Systematic Review；若批准后者，请同时确认协议和双人筛选安排。”

#### 13. 下一任务接口
向 Task 03 传递已批准类型、方法学义务和未解决风险。

#### 14. 最小示例
DLC—硫系玻璃主题若目标是材料与工艺进展综合、没有双人筛选资源，推荐 Narrative Review，并承诺公开检索式和筛选理由但不宣称 PRISMA 系统综述。

<a id="module-references-task-03-scope-and-questions-md"></a>
## Module: `references/task-03-scope-and-questions.md`

### Task 03 研究问题与边界

#### 1. 任务名称和目标
把宽泛主题收敛为可检索、可综合、可写作的研究问题与明确边界。

#### 2. 适用范围
所有项目；Systematic Review 需把问题转换为适用的 PICO、PECO、SPIDER 或等价结构。

#### 3. 前置条件
Task 02 已批准，综述类型和方法学义务明确。

#### 4. 必需和可选输入
必需：研究对象、材料、膜层、工艺、性能、应用、时间和语言偏好。可选：地域、标准、器件类型、波段、基底牌号和排除主题。

#### 5. 执行步骤
提出总问题和子问题；分别定义对象、干预/工艺、比较、结果和上下文；设置时间、语言、文献类型和灰色文献边界；用预检检索估计过宽/过窄风险；建立初始概念框架。

#### 6. 应调用的 scripts、references 和 assets
读取 `optical-coating-integrated.md` 的材料—工艺—结构—性能框架与领域门禁；使用 `project_diagnosis.md` 记录范围风险。

#### 7. 文件操作
创建 `03_scope_definition/`；保存范围声明、问题树和边界决策；范围变更必须新建版本并标记受影响任务。

#### 8. 文献与证据追踪要求
范围判断引用真实的先导检索和代表性 Source_ID；禁止用未检索的直觉声称“无文献”。

#### 9. 输出文件
`scope_statement.md`、`research_questions.md`、`initial_conceptual_framework.md` 和范围风险更新。

#### 10. 质量检查和通过标准
每个子问题都能映射到概念组、证据类型和计划交付物；范围没有明显遗漏或无法执行的无限扩张；排除项可解释。

#### 11. 阻断条件和风险
核心术语歧义、目标波段/基底/膜层未定、证据量明显不可管理或不足时阻断并返回用户决策。

#### 12. 用户确认问题
“请确认研究问题、纳入边界和明确排除项；批准后将调查已有综述。”

#### 13. 下一任务接口
向 Task 04 传递批准的问题树、概念框架、边界和先导检索线索。

#### 14. 最小示例
将“DLC 光学膜”限定为红外硫系玻璃基底上的 DLC/相关碳基防护膜，重点比较界面策略、低温制备、红外透过与机械环境可靠性，不把所有基底上的 DLC 生物医学应用纳入核心证据。

<a id="module-references-task-04-existing-reviews-md"></a>
## Module: `references/task-04-existing-reviews.md`

### Task 04 已有综述调查

#### 1. 任务名称和目标
系统比较已有综述的题目、范围、结构、贡献、时间覆盖与缺口，确定更新空间并登记可借鉴结构。

#### 2. 适用范围
所有项目；包括中文核心、SCI 综述、标准性报告和高质量领域专著章节。

#### 3. 前置条件
Task 03 已批准，研究问题和边界稳定。

#### 4. 必需和可选输入
必需：范围声明、问题树、数据库能力。可选：用户已知综述、课程结构、目标期刊近年综述和引文网络。

#### 5. 执行步骤
设计 review/survey/progress 等检索；跨中英文数据库执行并记录；核验题录和摘要；提取范围、分类法、结构、主要结论、截止年份和局限；比较与本项目的重合和差异；登记结构借鉴用途。

#### 6. 应调用的 scripts、references 和 assets
读取 `database-access-and-search.md`、`optical-coating-integrated.md`；使用文献库工作簿的 Source Registry；按需调用 `scripts/import_records.py`、`scripts/deduplicate_records.py` 和 `scripts/validate_metadata.py`。

#### 7. 文件操作
创建 `04_existing_reviews/`；保留原始导出、规范化记录、比较矩阵、覆盖图和检索日志。

#### 8. 文献与证据追踪要求
每篇综述分配 Source_ID，至少核验至 V3；结构借鉴标记 `STRUCTURAL_REFERENCE`，不得复制其论证或二次引用而不追原始来源。

#### 9. 输出文件
`existing_review_matrix.xlsx`、`review_coverage_map.md`、结构参考登记和更新空间说明。

#### 10. 质量检查和通过标准
中英文核心数据库均有合理覆盖或记录不可用原因；重合判断有真实 Source_ID；结构借鉴与事实证据分开；更新空间不是仅凭发表年份推断。

#### 11. 阻断条件和风险
核心数据库不可访问、综述全文不足以判断范围、或发现高度同题且更新价值不明时阻断。

#### 12. 用户确认问题
“已有综述的重合、可借鉴结构和更新空间是否判断合理？是否需要调整题目或范围？”

#### 13. 下一任务接口
向 Task 05 传递综述矩阵、覆盖缺口、结构参考 Source_ID 和潜在差异化方向。

#### 14. 最小示例
若现有综述聚焦通用 DLC 红外窗口但未区分硫系玻璃界面与低温工艺，本项目可把“基底相容性—过渡层—综合可靠性”作为候选差异化，但需在 Task 05 验证证据可得性。

<a id="module-references-task-05-topic-evaluation-md"></a>
## Module: `references/task-05-topic-evaluation.md`

### Task 05 创新性与可行性

#### 1. 任务名称和目标
比较至少三个候选题，基于已有综述、真实证据和期刊适配选择可执行且差异化明确的题目。

#### 2. 适用范围
所有项目；重大范围变更后重新执行并生成新版本项目诊断。

#### 3. 前置条件
Task 04 已批准，已有综述矩阵和范围风险可用。

#### 4. 必需和可选输入
必需：研究问题、已有综述矩阵、数据库能力、期限。可选：目标期刊层级、作者实验优势、预计图表和篇幅。

#### 5. 执行步骤
提出至少三个题目定位；按新颖性、重要性、证据量、全文可得性、方法可行性、作者优势和期刊适配评分；识别证据缺口和阻断项；推荐主方案和备选方案；首次生成研究路线图和项目化提示词库。

#### 6. 应调用的 scripts、references 和 assets
读取 `prompt-library-core.md`、`optical-coating-integrated.md`；复制 `project_diagnosis.md`、`prompt_library.md` 和 `preflight_and_roadmap.xlsx` 的 Research Roadmap Sheet。

#### 7. 文件操作
创建 `05_topic_evaluation/`；保存候选题评分矩阵、诊断、路线图 Markdown/XLSX 和提示词库；批准版本不可覆盖。

#### 8. 文献与证据追踪要求
每个新颖性或证据量判断连接检索日志和 Source_ID；目标期刊信息记录核验日期；不得把检索不到等同于不存在。

#### 9. 输出文件
`topic_scoring_matrix.xlsx`、`project_diagnosis.md`、推荐题目、`research_roadmap.md/.xlsx`、`prompt_library.md`。

#### 10. 质量检查和通过标准
至少三个候选定位可比较；推荐题差异化可被证据验证；每个核心问题连接至少一个证据任务和交付物；关键阻断项有处理方案。

#### 11. 阻断条件和风险
与已有综述高度重复、核心全文不可得、证据量不足或范围无法在期限内完成时阻断，不得仅靠改写标题掩盖重复。

#### 12. 用户确认问题
“请批准推荐题目、项目诊断、研究路线图和提示词库，或明确选择其他候选方案。”

#### 13. 下一任务接口
向 Task 06 传递批准题目、范围、研究问题、路线图、提示词库和关键领域概念。

#### 14. 最小示例
比较“材料基础全景”“界面与可靠性主线”“低温制备与工程放大”三个定位；若证据最完整且与已有综述差异最大的为界面主线，则题名与大纲优先围绕基底相容性和失效控制展开。

<a id="module-references-task-06-terminology-md"></a>
## Module: `references/task-06-terminology.md`

### Task 06 术语校准

#### 1. 任务名称和目标
建立中英文规范术语、缩写、旧称、商业名和易混词，防止机械翻译和检索漏检。

#### 2. 适用范围
所有项目；光学镀膜项目同时遵循 `optical-coating-integrated.md` 的物理量、工艺和表征命名规则。

#### 3. 前置条件
Task 05 已批准，题目、范围和研究路线图稳定。

#### 4. 必需和可选输入
必需：批准题目、研究问题、代表性文献和已有综述。可选：标准、材料牌号、专利术语、数据库主题词和作者关键词。

#### 5. 执行步骤
从题名、摘要、关键词、标准和数据库词表提取候选术语；核对中英文对应、缩写和上下位关系；标记歧义、旧称、拼写变体和排除语境；用先导检索验证召回与噪声。

#### 6. 应调用的 scripts、references 和 assets
读取 `optical-coating-integrated.md`、`database-access-and-search.md`；在项目中新建 `terminology_table.xlsx`。可使用 `scripts/import_records.py` 和 `scripts/validate_metadata.py` 规范化真实种子记录，但术语学术判断不得自动化替代。

#### 7. 文件操作
创建 `06_terminology/`，保存术语表、来源、版本、验证查询和变更记录；批准术语不得静默改名。

#### 8. 文献与证据追踪要求
每个专业术语至少登记定义来源或使用证据；材料牌号和工艺缩写连接 Source_ID 或标准；推测同义词不得直接作为等价词。

#### 9. 输出文件
`terminology_table.xlsx`、易混词与排除词清单、术语变更日志。

#### 10. 质量检查和通过标准
覆盖中文、标准英文、缩写、旧称和拼写变体；DLC、a-C:H、ta-C 等不被无条件等同；硫系玻璃类别和具体组成可区分。

#### 11. 阻断条件和风险
核心术语存在多义且无法通过标准或原文消解、商业名称成分不明、或用户研究对象与术语不一致时阻断。

#### 12. 用户确认问题
“请确认核心中英文术语、缩写和排除词，特别是 DLC 类型与硫系玻璃范围。”

#### 13. 下一任务接口
向 Task 07 传递批准术语、上下位关系、排除语境和验证查询结果。

#### 14. 最小示例
将 `diamond-like carbon`、`DLC`、`a-C:H`、`ta-C` 分别登记，并注明后两者是特定碳膜类别，不能在没有组成证据时全部归并为同一材料。

<a id="module-references-task-07-concept-groups-md"></a>
## Module: `references/task-07-concept-groups.md`

### Task 07 概念组

#### 1. 任务名称和目标
把批准术语组织为可解释的检索概念组、同义词组和排除组。

#### 2. 适用范围
所有数据库检索前；Systematic Review 的概念组必须进入协议和可复现检索附件。

#### 3. 前置条件
Task 06 已批准，术语表和歧义处理规则稳定。

#### 4. 必需和可选输入
必需：术语表、研究问题、范围声明。可选：数据库主题词、字段标签、通配符限制和先导检索噪声样本。

#### 5. 执行步骤
建立基底、膜层、制备、界面、光学、机械、环境和应用组；区分必选、扩展和排除项；定义组内 OR、组间 AND 与可选模块；用已知核心文献和噪声样本验证组合逻辑。

#### 6. 应调用的 scripts、references 和 assets
读取 `database-access-and-search.md` 和 `optical-coating-integrated.md`；输出项目化概念组表，不在 `SKILL.md` 堆积完整检索式。

#### 7. 文件操作
创建 `07_concept_groups/`；保存概念组、同义词、排除词、字段建议和验证结果，保留每次批准版本。

#### 8. 文献与证据追踪要求
记录每个概念词来自哪些 Source_ID、标准或数据库词表；用已知核心文献验证召回，不伪造检索命中。

#### 9. 输出文件
`concept_groups.xlsx`、`concept_logic.md`、已知文献召回检查表。

#### 10. 质量检查和通过标准
每个核心研究问题至少映射一个概念组合；组合逻辑可解释；材料、工艺与性能不被错误绑定为同义关系；排除词不误杀边界文献。

#### 11. 阻断条件和风险
核心组没有可验证术语、已知关键文献无法召回、或排除词导致系统性偏差时阻断。

#### 12. 用户确认问题
“概念组和组间组合是否符合研究边界？请确认后再规划数据库分工。”

#### 13. 下一任务接口
向 Task 08 传递概念组、数据库语法需求、召回检查和噪声风险。

#### 14. 最小示例
基底组包含 `chalcogenide glass`、具体玻璃体系与中文名称；膜层组包含 DLC 及经核验的类别；界面组作为可选模块，避免因所有文献都未写“interlayer”而漏掉核心论文。

<a id="module-references-task-08-database-plan-md"></a>
## Module: `references/task-08-database-plan.md`

### Task 08 数据库规划

#### 1. 任务名称和目标
依据 Step 00 的真实能力，为核心检索、补充发现、中文覆盖、元数据核验、引文追踪和全文获取分配平台职责。

#### 2. 适用范围
所有项目；不得把出版商全文平台当成唯一综合数据库。

#### 3. 前置条件
Task 07 已批准；Step 00 访问状态仍然有效，过期或变化的平台需重测。

#### 4. 必需和可选输入
必需：访问矩阵、概念组、综述类型、语言边界。可选：机构导出上限、引用管理器、团队账号和平台速率限制。

#### 5. 执行步骤
指定 WoS/Scopus 等核心库、CNKI/万方中文库、学科库、发现平台、Crossref/OpenAlex 核验平台和出版商全文平台；为每个平台定义问题、检索层级、字段、导出格式、时间点和引文追踪方向；制定不可用平台替代方案。

#### 6. 应调用的 scripts、references 和 assets
读取 `database-access-and-search.md` 与 Step 00 记录；使用 `preflight_and_roadmap.xlsx`、项目路线图和风险清单。

#### 7. 文件操作
创建 `08_database_plan/`；保存数据库分工表、引文追踪策略、导出命名规范和平台限制。

#### 8. 文献与证据追踪要求
所有数据库记录保留平台名、查询版本、日期和原始导出文件；同一文献后续合并但不丢来源平台。

#### 9. 输出文件
`database_role_matrix.xlsx`、`citation_chasing_plan.md`、`export_plan.md`。

#### 10. 质量检查和通过标准
核心、中文、发现、核验和全文职责都有可用路径或明确豁免；Systematic 分支覆盖所需数据库；计划与当前访问等级一致。

#### 11. 阻断条件和风险
核心范围仅能由不可访问平台覆盖、导出受限无法保证可追溯、或数据库组合明显造成语言/地区偏倚时阻断。

#### 12. 用户确认问题
“请确认数据库分工、替代路径和需人工登录的平台；批准后生成平台检索式。”

#### 13. 下一任务接口
向 Task 09 传递平台角色、语法约束、概念组、时间语言边界和导出要求。

#### 14. 最小示例
WoS/Scopus 负责英文核心检索，CNKI/万方负责中文核心与学位线索，OpenAlex/Crossref 核验 DOI，ScienceDirect/SpringerLink 仅用于合法全文和记录页补充。

<a id="module-references-task-09-search-strategies-md"></a>
## Module: `references/task-09-search-strategies.md`

### Task 09 三层检索式

#### 1. 任务名称和目标
为每个平台生成宽泛、适中和精准三层检索式，记录语法、字段、版本和预期噪声，使检索可复现。

#### 2. 适用范围
所有正式检索；Systematic Review 必须保存逐平台可复制完整式和执行日期。

#### 3. 前置条件
Task 08 已批准，平台分工与访问能力明确。

#### 4. 必需和可选输入
必需：概念组、平台语法、字段、时间语言边界。可选：已知文献、噪声样本、检索结果上限和引用追踪词。

#### 5. 执行步骤
先写平台中性逻辑；按平台翻译字段、通配符、邻近算符和短语规则；分别构建宽泛、适中、精准式；用已知文献测试召回并抽样噪声；记录每次修订原因，不使用未经平台支持的语法。

#### 6. 应调用的 scripts、references 和 assets
读取 `database-access-and-search.md`、`optical-coating-integrated.md` 和项目提示词库；使用检索日志文件。用 `scripts/version_output.py` 保存检索式版本；字段与数据库语法仍须在真实平台核验。

#### 7. 文件操作
创建 `09_search_strategies/`；每个平台独立保存查询文本、版本、字段、限制和测试记录；已执行查询不得被静默改写。

#### 8. 文献与证据追踪要求
检索测试命中的已知文献使用 Source_ID；结果数量仅记录实际界面或导出值；不得用模型估计冒充数据库结果。

#### 9. 输出文件
`search_strategy_master.md`、逐平台检索式、`search_string_test_log.xlsx` 和噪声说明。

#### 10. 质量检查和通过标准
三层检索式逻辑差异明确；平台语法已实际验证；核心已知文献可召回或有解释；查询、日期、字段和限制可复现。

#### 11. 阻断条件和风险
平台语法无法验证、查询被截断、结果上限不可管理、核心文献持续漏检或排除逻辑不稳定时阻断。

#### 12. 用户确认问题
“请确认三层检索式及噪声—召回权衡；批准后才执行正式检索。”

#### 13. 下一任务接口
向 Task 10 传递批准查询、平台顺序、导出格式、缓存与人工操作要求。

#### 14. 最小示例
宽泛式连接硫系玻璃与碳基膜层，适中式加入红外/防护语境，精准式再加入界面或制备模块；不得把精准式的较少命中解释为主题完整覆盖。

<a id="module-references-task-10-run-searches-md"></a>
## Module: `references/task-10-run-searches.md`

### Task 10 实际检索

#### 1. 任务名称和目标
合法执行批准的检索或指导用户导出，保存原始记录、真实结果数、查询版本和访问限制。

#### 2. 适用范围
所有数据库与发现平台；只在允许的自动化边界内操作。

#### 3. 前置条件
Task 09 已批准；所用平台访问状态未恶化；需要登录、VPN 或验证码时由用户操作。

#### 4. 必需和可选输入
必需：逐平台检索式、日期、字段、导出格式和目录。可选：结果分批规则、去重前标签、引用追踪种子和缓存设置。

#### 5. 执行步骤
按计划执行每个查询；记录开始/结束时间、真实结果数、排序和筛选；导出原始记录，不手工改写；对无法自动导出的库提供逐步人工导出说明；校验文件数量和格式；Task 10 后更新路线图中的真实检索结果与数据库缺口。

#### 6. 应调用的 scripts、references 和 assets
读取 `database-access-and-search.md`；保存到项目检索日志。使用 `scripts/import_records.py` 导入真实导出文件；不得模拟查询结果、记录数或导出内容。

#### 7. 文件操作
创建 `10_search_execution/raw/`、`exports/`、`logs/`；文件名包含平台、查询层级、版本和日期；原始导出只读保留。

#### 8. 文献与证据追踪要求
记录每批来源平台和查询 ID；导入前不擅自合并记录；引文追踪标记种子 Source_ID 和方向。

#### 9. 输出文件
`search_log.xlsx`、原始 CSV/XLSX/RIS/BibTeX/EndNote XML/JSON、失败日志和更新后的研究路线图。

#### 10. 质量检查和通过标准
每个批准平台有成功导出或明确失败状态；结果数来自真实界面；原始文件可打开；查询版本、日期、筛选和导出范围完整。

#### 11. 阻断条件和风险
验证码、登录失效、速率限制、条款禁止自动化、导出截断、平台异常或结果数与文件数无法解释时立即暂停。

#### 12. 用户确认问题
“请确认检索日志和原始导出完整；若有人工导出，请上传后再批准进入元数据清洗。”

#### 13. 下一任务接口
向 Task 11 传递只读原始导出、平台/查询标签、失败记录和用户补充文件。

#### 14. 最小示例
WoS 返回的结果数和实际导出批次数分别记录；CNKI 遇到验证码时暂停并让用户导出，而不是推测结果或绕过验证。

<a id="module-references-task-11-metadata-cleaning-md"></a>
## Module: `references/task-11-metadata-cleaning.md`

### Task 11 元数据清洗

#### 1. 任务名称和目标
规范 DOI、题名、作者、年份、期刊和版本关系，合并重复记录但保留来源、异常和决策链。

#### 2. 适用范围
Task 10 的全部原始导出及用户补充记录；支持 CSV、XLSX、RIS、BibTeX、EndNote XML、Zotero 映射和 JSON。

#### 3. 前置条件
Task 10 已批准，原始导出只读保存且平台/查询标签完整。

#### 4. 必需和可选输入
必需：全部原始记录、来源平台、查询 ID。可选：Crossref/OpenAlex 核验结果、Zotero 库、PDF 文件名和已有 DOI 清单。

#### 5. 执行步骤
解析格式并保留原始字段；规范空白、大小写、DOI URL 和作者；按 DOI、规范题名、作者年份和版本关系分层判重；区分预印本、会议文与正式版本；核验冲突；分配稳定 Source_ID；输出合并和异常决策。

#### 6. 应调用的 scripts、references 和 assets
读取 `source-record.schema.json`、`database-access-and-search.md`；使用 `literature_registry.xlsx`。依次调用 `scripts/import_records.py`、`scripts/deduplicate_records.py`、`scripts/validate_metadata.py`，保留导入、决策、冲突和外部核验状态。

#### 7. 文件操作
创建 `11_metadata_cleaning/working|outputs|qa|logs`；原始记录不改；规范库和决策日志版本化；被替代记录通过 `supersedes_source_id` 连接。

#### 8. 文献与证据追踪要求
Source_ID 一旦被引用不得重分配；V2 仅在题录和 DOI 已核验后赋值；元数据来源和核验日期必须保留。

#### 9. 输出文件
主文献库、Source Registry、重复决策日志、元数据异常清单和导入统计。

#### 10. 质量检查和通过标准
每条记录有唯一 Source_ID；重复决策可逆追踪；DOI 冲突未被静默覆盖；缺失字段明确为空；导入数、合并数、排除数和输出数守恒。

#### 11. 阻断条件和风险
同 DOI 不同题名、同题名不同版本、解析失败、编码损坏或计数不守恒时阻断；不得凭相似题名自动永久合并。

#### 12. 用户确认问题
“请确认重复与版本关系处理，特别是预印本/正式版和 DOI 冲突记录。”

#### 13. 下一任务接口
向 Task 12 传递规范主库、稳定 Source_ID、异常和未决版本关系。

#### 14. 最小示例
同一 DLC 论文的会议摘要与期刊全文分别保留 Source_ID，并用版本关系连接；期刊版作为主要证据，但不删除会议记录的来源轨迹。

<a id="module-references-task-12-eligibility-criteria-md"></a>
## Module: `references/task-12-eligibility-criteria.md`

### Task 12 纳入排除标准

#### 1. 任务名称和目标
在正式筛选前建立可执行、可复核的纳入排除标准和边界案例规则。

#### 2. 适用范围
所有项目；Systematic Review 同时遵循协议、双人筛选和分歧处理要求。

#### 3. 前置条件
Task 11 已批准，主文献库和元数据异常清单可用。

#### 4. 必需和可选输入
必需：范围声明、研究问题、综述类型、文献类型和时间语言边界。可选：全文可得性规则、质量阈值、灰色文献和标准处理方案。

#### 5. 执行步骤
把范围转换为对象、材料、工艺、性能、应用、文献类型、时间、语言和证据层级标准；规定题名、摘要和全文阶段的决定；建立排除码；抽样试筛并修正规则；记录边界案例与升级路径。

#### 6. 应调用的 scripts、references 和 assets
读取 `systematic-review-branch.md`、`optical-coating-integrated.md`；使用 `literature_registry.xlsx` 的 Screening Sheet。

#### 7. 文件操作
创建 `12_eligibility_criteria/`；保存筛选方案、排除码表、试筛结果和批准版本；正式筛选后规则变更必须记录影响并重审相关记录。

#### 8. 文献与证据追踪要求
每个筛选记录连接 Source_ID、阶段、决定、理由和审阅者；全文不可得不自动等同于主题不相关。

#### 9. 输出文件
`screening_protocol.md`、`exclusion_codebook.xlsx`、边界案例规则和试筛一致性记录。

#### 10. 质量检查和通过标准
标准可由不同审阅者一致执行；排除码互斥且可解释；边界文献有 `UNCERTAIN` 路径；标准在正式筛选前获批。

#### 11. 阻断条件和风险
标准依赖未定义概念、试筛分歧高、把全文缺失当主题排除、或批准后无记录改规则时阻断。

#### 12. 用户确认问题
“请批准纳入排除标准、排除码和边界案例处理；批准前不开始正式筛选。”

#### 13. 下一任务接口
向 Task 13 传递批准协议、排除码、边界升级规则和主文献库。

#### 14. 最小示例
只研究其他基底上的 DLC 可标为 `BACKGROUND_ONLY`；涉及硫系玻璃但没有 DLC/相关碳基膜证据的记录进入边界复核，而不是自动排除。

<a id="module-references-task-13-title-abstract-screening-md"></a>
## Module: `references/task-13-title-abstract-screening.md`

### Task 13 题名摘要筛选

#### 1. 任务名称和目标
按批准标准筛选题名和摘要，记录决定、理由、不确定性和全文需求，保护边界文献不被自动永久排除。

#### 2. 适用范围
主文献库全部未筛选记录；Systematic Review 使用双人独立筛选或明确记录无法执行的限制。

#### 3. 前置条件
Task 12 已批准，筛选协议和排除码冻结。

#### 4. 必需和可选输入
必需：Source_ID、题名、摘要、文献类型、筛选协议。可选：关键词、机构、引用上下文、第二审阅者结果。

#### 5. 执行步骤
先题名后摘要逐条判断；输出 `INCLUDE`、`EXCLUDE`、`UNCERTAIN`、`BACKGROUND_ONLY` 或 `METHOD_ONLY`；记录排除码、理由和置信度；摘要缺失或信息不足转全文判断；抽查一致性并解决分歧。

#### 6. 应调用的 scripts、references 和 assets
读取 `systematic-review-branch.md` 与筛选协议；使用 `literature_registry.xlsx` 的 Screening Sheet。筛选决定和漏项由本任务质量门禁检查；确定性脚本不得代替学术纳排判断或第二位人类审稿者。

#### 7. 文件操作
创建 `13_title_abstract_screening/`；保存筛选表、边界清单、分歧日志和阶段快照；不删除被排除记录。

#### 8. 文献与证据追踪要求
每个决定连接 Source_ID、筛选阶段、审阅者、日期和理由；AI 建议与人工最终决定分栏保存。

#### 9. 输出文件
`title_abstract_screening.xlsx`、`borderline_sources.xlsx`、分歧处理记录和全文获取清单。

#### 10. 质量检查和通过标准
所有目标记录有决定；摘要缺失不伪装已读；边界记录未自动永久排除；排除理由来自批准码；抽查未发现系统性误排。

#### 11. 阻断条件和风险
摘要语言无法理解、元数据错配、协议不足以处理新边界、双人结果无法协调或筛选状态丢失时阻断。

#### 12. 用户确认问题
“请确认题名摘要筛选统计、边界清单和全文获取范围。”

#### 13. 下一任务接口
向 Task 14 传递纳入/不确定记录、全文需求、边界理由和筛选审计链。

#### 14. 最小示例
题名只写“carbon coating on infrared glass”且摘要未给基底组成时标为 `UNCERTAIN` 并请求全文，不因缺少“chalcogenide”单词直接排除。

<a id="module-references-task-14-full-text-screening-md"></a>
## Module: `references/task-14-full-text-screening.md`

### Task 14 全文筛选分类

#### 1. 任务名称和目标
基于实际全文完成最终纳入、排除和二三级主题分类，并生成文献地图初版。

#### 2. 适用范围
Task 13 的 `INCLUDE` 与 `UNCERTAIN` 记录；无全文记录不得伪装全文筛选。

#### 3. 前置条件
Task 13 已批准；全文文件与 Source_ID 的初步映射可用。

#### 4. 必需和可选输入
必需：筛选协议、Source_ID、全文或明确缺失状态。可选：OCR 文本、补充材料、标准、专利和第二审阅者判断。

#### 5. 执行步骤
核对全文与题录；定位研究对象、材料、基底、膜层、工艺和结果；应用全文排除码；为纳入文献分配二三级主题和用途层级；记录边界与冲突；基于真实 Source_ID 建立文献地图节点和经证据支持的关系初版。

#### 6. 应调用的 scripts、references 和 assets
读取 `literature-map.schema.json`、`optical-coating-integrated.md`；使用 `literature_registry.xlsx` 和 `literature_map.xlsx`。调用 `scripts/build_literature_map.py` 生成仅含显式 Source_ID 和已核验关系的地图。

#### 7. 文件操作
创建 `14_full_text_screening/`；保存最终筛选表、排除日志、主题分类和地图初版；PDF 本体不移动时保存稳定相对路径与哈希。

#### 8. 文献与证据追踪要求
全文决定记录页码或章节；地图关系必须连接真实 Source_ID 和依据；不能凭题名相似创建 `SUPPORTS`、`CONTRADICTS` 或方法继承关系。

#### 9. 输出文件
最终纳入库、`full_text_exclusion_log.xlsx`、主题分类、`literature_map.xlsx/.md/.json` 初版。

#### 10. 质量检查和通过标准
每个决定说明是否实际读到全文；排除理由可定位；主题层级与研究问题相连；地图节点与 Source Registry 一致，关系有依据和核验等级。

#### 11. 阻断条件和风险
全文缺失、错配、扫描不可读、页码不稳定、协议无法处理新类型或关系证据不足时阻断或保留 `UNCERTAIN`。

#### 12. 用户确认问题
“请确认最终纳入排除、主题分类和文献地图初版；缺失全文如何处理也需明确决定。”

#### 13. 下一任务接口
向 Task 15 传递最终纳入库、全文映射、排除日志、主题和地图初版。

#### 14. 最小示例
全文确认使用 Ge-As-Se 基底和 DLC 过渡层后纳入界面工程主题；若 PDF 实际是同题名会议摘要，则标记 `MISMATCHED` 并阻断，不按全文纳入。

<a id="module-references-task-15-library-audit-md"></a>
## Module: `references/task-15-library-audit.md`

### Task 15 PDF 与文献库审计

#### 1. 任务名称和目标
核对 PDF、题录、缺页、OCR、DOI、附件归属和全文可读性，更新文献地图核验等级与精读优先级。

#### 2. 适用范围
最终纳入库的所有核心与支撑文献，以及将用于方法或图表证据的背景来源。

#### 3. 前置条件
Task 14 已批准，最终纳入库和文献地图初版存在。

#### 4. 必需和可选输入
必需：Source Registry、PDF 路径、文件哈希、题录和筛选决定。可选：OCR 输出、补充材料、机构下载记录和引用管理器附件。

#### 5. 执行步骤
逐一核对文件与 Source_ID；检查首页、末页、页数、文本层、图表、补充材料和 DOI；识别缺页、扫描、乱码和错配；记录 OCR 质量；按核心性、全文质量和证据需求排序精读；更新 V0–V4 和地图节点。

#### 6. 应调用的 scripts、references 和 assets
读取 `source-record.schema.json`、`literature-map.schema.json`；使用 Source Registry 与 Literature Map。调用 `scripts/validate_metadata.py` 和 `scripts/validate_project.py`，将外部失败、冲突和人工核查保持为显式状态。

#### 7. 文件操作
创建 `15_library_audit/`；保存审计表、哈希、OCR 清单、缺失全文清单和地图更新；不重命名或移动用户库中的外部文件，除非另有批准。

#### 8. 文献与证据追踪要求
V4 仅在定位到全文页码、章节、图或表后赋值；文件哈希和附件状态连接 Source_ID；OCR 文本不能替代原页定位。

#### 9. 输出文件
`library_audit_report.md`、`pdf_audit.xlsx`、精读优先级、缺失/错配清单和更新后的文献地图。

#### 10. 质量检查和通过标准
核心文献 PDF 完整可读或有明确风险决定；附件与题录一致；全文核验等级真实；地图和 Source Registry 同步；精读顺序连接研究问题。

#### 11. 阻断条件和风险
核心全文缺失、PDF 错配、关键页缺失、扫描无法 OCR 或 DOI 冲突时阻断，除非用户明确跳过门禁并记录影响。

#### 12. 用户确认问题
“请确认 PDF 审计、核心全文缺口和精读优先级；是否接受任何带风险继续项？”

#### 13. 下一任务接口
向 Task 16 传递可读全文、Source_ID、核验等级、精读顺序、主题和待人工核查项。

#### 14. 最小示例
核心论文 PDF 完整且已定位工艺表与透射谱，可升至 V4；只有数据库摘要的记录保持 V3，不能用于具体沉积参数或图表数据。

<a id="module-references-task-16-structured-reading-md"></a>
## Module: `references/task-16-structured-reading.md`

### Task 16 结构化精读

#### 1. 任务名称和目标
逐篇提取材料、工艺、条件、方法、定量结果、解释、局限和原文位置，区分事实层与解释层。

#### 2. 适用范围
Task 15 排定的核心、支撑、方法和冲突文献；综述文献使用领域地图式提取，原创研究使用结构化研究分析。

#### 3. 前置条件
Task 15 已批准，目标全文可读且 Source_ID、PDF 哈希和优先级明确。

#### 4. 必需和可选输入
必需：全文、题录、Source_ID、研究问题、领域字段。可选：补充材料、数据表、图像、OCR、作者更正和相关标准。

#### 5. 执行步骤
通读全文；记录问题、样品、材料、基底、膜层、界面、设备、工艺条件、表征、结果和局限；每个定量值保存单位、条件和原文位置；分开记录实验结果、作者解释、作者推测与 Skill 判断；标记跨文献比较条件。

#### 6. 应调用的 scripts、references 和 assets
读取 `evidence-card.schema.json`、`optical-coating-integrated.md`；复制 `reading_note.md`。可使用学术论文提取能力，但不得跳过全文定位。

#### 7. 文件操作
创建 `16_structured_reading/<Source_ID>/`；每篇保存独立笔记和必要截图索引，不改原 PDF；中断时持久化当前页和未完成字段。

#### 8. 文献与证据追踪要求
每条结果连接 Source_ID 和页码/章节/图/表；机制与定量比较要求 V4；二手引用标记待追原始来源；Raman 拟合不直接转换为精确 sp3 含量。

#### 9. 输出文件
逐篇 `reading_note.md`、定量结果表、原文位置索引、局限与人工核查清单。

#### 10. 质量检查和通过标准
必需领域字段已填写或写明“原文未报告”；结果/解释/推测/Skill 判断明确分层；定量值有条件、单位和位置；关键机制未由单一表征过度解释。

#### 11. 阻断条件和风险
全文错配、关键页缺失、OCR 影响数值、图表不可辨认、实验条件矛盾或二手引用无法追溯时阻断对应证据，不得补猜。

#### 12. 用户确认问题
“请确认本批精读笔记的事实—解释分层、原文位置和人工核查项；是否继续下一批或进入证据卡？”

#### 13. 下一任务接口
向 Task 17 传递已批准精读笔记、可支持主张、比较条件、图表候选和限制。

#### 14. 最小示例
记录“硬度 18 GPa”时同时记录压头、载荷、膜厚、基底和页码；作者将提高归因于 sp3 增加时另列为作者解释，若只有 Raman 证据则保留机制风险。

<a id="module-references-task-17-evidence-cards-md"></a>
## Module: `references/task-17-evidence-cards.md`

### Task 17 综述素材卡

#### 1. 任务名称和目标
把精读笔记转化为可直接服务主张、章节、比较、图表和研究空白的证据卡，同时限定使用边界。

#### 2. 适用范围
通过 Task 16 质量检查的文献；一篇文献可有一张主卡和多个主题子卡，但不得重复计为独立研究。

#### 3. 前置条件
Task 16 已批准，精读笔记含原文位置和核验等级。

#### 4. 必需和可选输入
必需：reading note、Source_ID、研究问题、计划章节。可选：候选 Claim_ID、比较组、图表设计和冲突来源。

#### 5. 执行步骤
概括该文献能回答的问题；提取材料—工艺—界面—性能上下文；列出可支持、限定或反驳的主张；登记比较用途、图表用途、原文位置、证据强度、局限和引用风险；识别不能支持的外推。

#### 6. 应调用的 scripts、references 和 assets
读取 `evidence-card.schema.json`、`claim.schema.json`、`optical-coating-integrated.md`；复制 `evidence_card.md`，并同步 `evidence_and_claims.xlsx`。

#### 7. 文件操作
创建 `17_evidence_cards/`；文件名含 Evidence_Card_ID 与 Source_ID；更新卡片生成新版本并保留旧版关系。

#### 8. 文献与证据追踪要求
每张卡有稳定 Evidence_Card_ID 和 Source_ID；支持的 Claim_ID 与原文位置双向可查；全文数据至少 V4；证据强度与核验等级分开。

#### 9. 输出文件
结构化证据卡、证据卡索引、引用风险和待补来源清单。

#### 10. 质量检查和通过标准
每张卡说明可用与不可用边界；关键结果可回到原文；作者解释与 Skill 判断分开；不存在把同一样品多篇论文当独立重复的错误。

#### 11. 阻断条件和风险
原文位置不完整、主张超出研究设计、版本/样品重复不明、单位不可比或版权用途不清时阻断相应卡片。

#### 12. 用户确认问题
“请确认证据卡的支持边界、强度和引用风险；批准后建立 Claim–Evidence Matrix。”

#### 13. 下一任务接口
向 Task 18 传递证据卡、Source_ID、候选 Claim_ID、支持/冲突关系和最低核验等级。

#### 14. 最小示例
某论文可支持“特定过渡层在给定沉积条件下提高划痕临界载荷”，但不能支持“该过渡层普遍解决所有硫系玻璃附着问题”。

<a id="module-references-task-18-claim-evidence-matrix-md"></a>
## Module: `references/task-18-claim-evidence-matrix.md`

### Task 18 主张—证据矩阵

#### 1. 任务名称和目标
建立 Claim_ID 与 Source_ID 的双向映射，确保正文核心主张在写作前具有足够、可定位且边界明确的证据。

#### 2. 适用范围
所有计划进入大纲和正文的背景、描述、比较、定量、机制、因果、共识、争议和研究空白主张。

#### 3. 前置条件
Task 17 已批准，证据卡和使用边界可用。

#### 4. 必需和可选输入
必需：证据卡、研究问题、章节意图、Source_ID。可选：候选图表、冲突证据、标准和人工复核结果。

#### 5. 执行步骤
为每个主张分配 `CLM-章节-序号`；写中英文主张；标记类型、来源、原文位置、关系、证据类型、强度、一致性、条件、局限、使用位置和人工状态；识别无证据、单一来源、冲突或过强措辞；建立来源到主张反向索引。

#### 6. 应调用的 scripts、references 和 assets
读取 `claim.schema.json`、`evidence-card.schema.json`、`schema-and-template-map.md`；使用 `evidence_and_claims.xlsx`。调用 `scripts/audit_claims.py` 检查 Source_ID、原文位置、V3/V4/V5 和领域越界。

#### 7. 文件操作
创建 `18_claim_evidence_matrix/`；保存矩阵、无证据主张、冲突和人工核查清单；Claim_ID 已在稿件使用后不得重分配。

#### 8. 文献与证据追踪要求
核心事实最低 V3；机制、定量比较和图表数据最低 V4；V5 表示第二来源或人工复核，不等同于证据强度；每个来源关系需有原文位置。

#### 9. 输出文件
`claim_evidence_matrix.xlsx`、Claim Registry、无证据主张清单和来源反向索引。

#### 10. 质量检查和通过标准
所有核心主张至少一条合格证据；关键比较包含可比条件；冲突未被多数表决掩盖；研究空白连接证据结构；人工状态明确。

#### 11. 阻断条件和风险
核心主张无证据、仅 V1/V2、机制仅由相关性支持、定量单位/条件不可比或 Source_ID 无法定位时阻断写作。

#### 12. 用户确认问题
“请确认核心主张、证据强度、冲突与待补证据；未关闭的核心缺口不得进入正文。”

#### 13. 下一任务接口
向 Task 19 传递通过门禁的主张、支持/冲突网络、条件、局限和证据缺口。

#### 14. 最小示例
`CLM-4.2-01` 比较两种低温沉积路线时，分别记录基底组成、偏压、膜厚和测试波段；条件不一致则标为条件性比较而非直接优劣排名。

<a id="module-references-task-19-evidence-synthesis-md"></a>
## Module: `references/task-19-evidence-synthesis.md`

### Task 19 证据综合

#### 1. 任务名称和目标
跨文献综合共识、冲突、条件、方法差异、阶段性结论和研究空白，更新文献地图的学术关系。

#### 2. 适用范围
通过 Task 18 的主张与证据；Narrative Review 采用结构化叙述综合，Systematic Review 遵循预先方案。

#### 3. 前置条件
Task 18 已批准，核心主张达到最低核验等级。

#### 4. 必需和可选输入
必需：Claim–Evidence Matrix、证据卡、文献地图、研究问题。可选：质量评价、标准、实验设计分层和统计综合计划。

#### 5. 执行步骤
按材料、工艺、结构、性能和应用聚类；比较方向与效应条件；解释样品、设备、测试和分析差异；区分共识、条件性结论、冲突和未知；为机制主张检查替代解释；从证据结构提炼空白；更新地图关系和路线图。

#### 6. 应调用的 scripts、references 和 assets
读取 `literature-map.schema.json`、`optical-coating-integrated.md`、`systematic-review-branch.md`；使用 `literature_map.xlsx` 与 Claim workbook。调用 `scripts/build_literature_map.py` 和 `scripts/audit_claims.py`，不得由标题相似性推断关系。

#### 7. 文件操作
创建 `19_evidence_synthesis/`；保存共识、争议、机制、条件和空白矩阵，以及地图更新前后差异。

#### 8. 文献与证据追踪要求
每条综合结论连接多个 Source_ID 或明确标为单一来源；冲突关系保留双方原文位置；研究空白连接缺失节点、薄弱关系或方法偏差。

#### 9. 输出文件
`consensus_matrix.xlsx`、`controversy_matrix.xlsx`、`mechanism_assessment.md`、`research_gap_matrix.xlsx` 和更新后的文献地图。

#### 10. 质量检查和通过标准
综合按问题而非作者流水账组织；差异原因有证据；相关性不升级为因果；单一表征不充当完整机制；地图关系均可核验。

#### 11. 阻断条件和风险
证据异质性无法解释、核心冲突缺全文、比较条件缺失、机制证据不足或空白仅凭“文献少”得出时阻断相应结论。

#### 12. 用户确认问题
“请确认共识、条件性争议、机制边界和研究空白；批准后据此搭建三级大纲。”

#### 13. 下一任务接口
向 Task 20 传递综合矩阵、通过的 Claim_ID、冲突、研究空白、地图和建议图表。

#### 14. 最小示例
不同研究对偏压与应力关系结论相反时，先分层基底温度、氢含量、膜厚和测量方法；无法统一则保留争议，不写成单调普遍规律。

<a id="module-references-task-20-outline-and-figures-md"></a>
## Module: `references/task-20-outline-and-figures.md`

### Task 20 三级大纲与图表

#### 1. 任务名称和目标
把研究问题和证据综合转化为三级大纲、论证路径和可追溯图表系统；大纲批准后才允许写作。

#### 2. 适用范围
所有项目；结构可适配目标期刊，但不得破坏证据链。

#### 3. 前置条件
Task 19 已批准，共识、争议、空白、Claim–Evidence Matrix 和文献地图可用。

#### 4. 必需和可选输入
必需：研究问题、综合矩阵、Claim_ID、Source_ID、计划篇幅。可选：目标期刊结构、课程框架、图表数量限制和作者偏好。

#### 5. 执行步骤
为每个一级/二级/三级标题定义问题和功能；每个三级标题配置中心命题、主要证据、跨研究比较、差异原因、适用条件、局限、阶段判断和图表；检查章节递进、平衡、证据密度和重复；建立图表 ID、元素、来源、转换、版权和核验记录；更新路线图。

#### 6. 应调用的 scripts、references 和 assets
读取 `figure-table-traceability.schema.json`、`optical-coating-integrated.md`；使用 `review_outline_template.docx`、`outline_review_report.md` 和 `evidence_and_claims.xlsx`。

#### 7. 文件操作
创建 `20_outline_and_figures/`；保存大纲、审查报告、图表计划、追踪矩阵和路线图新版本；批准大纲不得覆盖。

#### 8. 文献与证据追踪要求
每个三级标题至少连接一个通过门禁的 Claim_ID 和 Source_ID；每个图表元素有追踪 ID；再绘、数字化、计算和综合必须记录方法与版权状态。

#### 9. 输出文件
三级大纲 Markdown/DOCX、`outline_review_report.md`、图表系统、Figure–Table Traceability 和更新后的研究路线图。

#### 10. 质量检查和通过标准
论证不是作者流水账；章节平衡；核心主张和冲突均有位置；图表支持论证且可追溯；审查报告关键问题关闭；用户正式批准大纲。

#### 11. 阻断条件和风险
关键章节无证据、图表版权不明、核心 Claim 未通过、结构重复或用户仅模糊同意时阻断，不得进入 Task 21。

#### 12. 用户确认问题
“请明确批准三级大纲、图表计划和证据配置；只有回复‘确认通过’或等价明确批准后才进入写作。”

#### 13. 下一任务接口
向 Task 21A 传递批准大纲版本、Claim–Evidence Matrix、图表追踪、术语表、路线图和未关闭风险。

#### 14. 最小示例
“界面工程”三级标题分别配置附着证据、应力冲突、基底组成条件和一张材料—界面—失效机制图；若机制图只有推测关系，图例必须标注证据等级。

<a id="module-references-task-21-writing-submission-revision-md"></a>
## Module: `references/task-21-writing-submission-revision.md`

### Task 21 写作、核查、投稿与返修

#### 1. 任务名称和目标
按批准大纲完成写作语言决策、分章写作、全文整合、逐句核查、学术润色、期刊匹配、投稿材料和审稿回复。21A–21H 各有独立状态、输入、输出、质量门禁和批准记录。

#### 2. 适用范围
仅适用于 Task 20 已明确批准的项目。21F–21H 可在投稿或返修阶段单独恢复，但不得跳过其依赖的已批准稿件与审计记录。

#### 3. 前置条件
Task 20 为 `APPROVED` 或经明确风险豁免；批准大纲、术语表、Claim–Evidence Matrix、图表追踪和文献地图可用。`project_state.yaml.current_subtask` 必须指向唯一 21A–21H 状态。

#### 4. 必需和可选输入
必需：批准大纲、核心 Claim_ID/Source_ID、引用格式、图表追踪、用户决策。可选：目标期刊、作者指南、既有草稿、语言风格、作者贡献、利益冲突、基金、数据声明和审稿意见。

#### 5. 执行步骤

##### 21A 写作语言确认

记录中文或英文正文、摘要语言、术语保留规则和过程报告语言。默认过程报告中文，但不替用户选择最终稿语言。输出 `writing_language_decision.md`，明确批准后才能开始 21B。

##### 21B 分章节写作

按批准大纲逐章执行：读取该章 Claim–Evidence 子集；按“中心观点—主要证据—跨研究比较—差异原因—适用条件—局限—阶段性判断”组织段落；插入正式引用与图表引用；生成章节证据审计；将 `current_chapter` 设为待审章节并停在 `REVIEW_REQUIRED`。每章单独批准，禁止把一章批准扩展为后续章节批准。

##### 21C 全文整合

合并已批准章节；检查论证递进、重复、术语、章节平衡、交叉引用、摘要、结论和图表顺序；不得用整合改写绕过已批准主张。输出完整初稿和整合报告。

##### 21D 逐句核查

逐句识别事实、数字、比较、机制、因果、范围和引文；回查 Source_ID、DOI、原文位置、核验等级与支持关系；查找无来源数字、二次引用、引用漂移和过强措辞；输出 `citation_audit.xlsx`。核心未关闭项阻断后续清洁稿。

##### 21E 学术润色

在不改变事实和证据强度的前提下修正逻辑连接、术语、一致性、句法和学术语气；每项实质修改进入 `revision_recommendations.md`；润色后重新抽查引用与数字。

##### 21F 目标期刊匹配

联网核验期刊范围、文章类型、邀约要求、字数、图表、参考文献、APC、开放获取、AI 使用、版权和数据政策；记录官方 URL 与日期；比较适配、成本、风险和备选顺序。不得使用过期记忆替代当前官网。

##### 21G 投稿材料

基于已批准目标期刊和清洁稿生成 Cover Letter、Highlights、作者贡献、利益冲突、基金、数据/代码、伦理、AI 辅助声明、清单和投稿系统字段；所有作者与声明由用户确认，禁止代签或提交。

##### 21H 审稿回复

逐条登记意见、类别、严重度、响应策略、证据、修改文本和稿件位置；区分同意、部分同意和有证据的不同意；更新稿件、修改建议和引用审计；每条意见关闭后再形成 response letter。不得编造新实验或声称未完成的修改。

#### 6. 应调用的 scripts、references 和 assets
读取 `state-machine.md`、`claim.schema.json`、`figure-table-traceability.schema.json`、`optical-coating-integrated.md`、`prompt-library-core.md`；使用 `review_outline_template.docx`、`revision_recommendations.md`、证据与文献工作簿。可调用可用的学术写作、论文审查、文档和表格能力；使用 `scripts/audit_claims.py`、`scripts/audit_figures_tables.py` 和 `scripts/version_output.py` 执行确定性门禁和无覆盖版本化。

#### 7. 文件操作
创建 `21_writing/21A` 至 `21H` 独立目录；每个子任务保存 `working/outputs/qa/logs/task_status.yaml/stage_report.md`；21B 再按章节分目录。生成审计版和清洁投稿版，清洁版移除内部 ID 但保留正式引用和版权声明。批准文件不可覆盖。

#### 8. 文献与证据追踪要求
审计版保留 Claim_ID、Source_ID、原文位置、核验等级和风险；核心事实最低 V3，机制/定量/图表最低 V4；新写主张必须先回到 Task 18 建立证据，不得直接塞入正文。21F 政策信息记录官方来源和核验日期。

#### 9. 输出文件
21A 语言决策；21B 章节稿与章节审计；21C 完整初稿与整合报告；21D `citation_audit.xlsx`；21E 润色稿与修改建议；21F `journal_comparison.xlsx`；21G 投稿包；21H `reviewer_response_matrix.xlsx`、回复信和修订稿。

#### 10. 质量检查和通过标准
21A 有明确语言决策；21B 每章与批准大纲和证据一致；21C 无未解释重复或断裂；21D 核心逐句审计关闭；21E 未改变证据含义；21F 动态政策为当前官方信息；21G 所有作者声明人工确认；21H 意见—回复—修改—位置—证据闭环。每个子任务独立进入 `REVIEW_REQUIRED`。

#### 11. 阻断条件和风险
语言未定、章节大纲未批准、核心 Claim 无证据、DOI/引用冲突、图表版权不明、目标期刊政策无法核验、作者声明缺失、审稿意见含新实验需求或用户仅模糊批准时阻断对应子任务。

#### 12. 用户确认问题
21A：“请明确选择中文或英文正文。”21B：“请确认当前章节及证据审计后再写下一章。”21C–21H 分别要求对当前成果明确回复“确认通过”或提出修改，绝不批量推定。

#### 13. 下一任务接口
21A→21B 传语言规则；21B→21C 传全部已批准章节；21C→21D 传整合稿；21D→21E 传关闭后的审计；21E→21F 传清洁候选稿；21F→21G 传批准期刊和当前政策；21G→21H 传实际投稿稿件与材料。21H 完成后进入项目归档门禁，不自动上传或投稿。

#### 14. 最小示例
DLC—硫系玻璃中文综述在 21A 确认中文；21B 先写“材料基础”章并暂停，审计确认 Raman 相关措辞未把拟合等同精确 sp3；所有章节批准后才整合。21F 核验期刊官网当日 APC 与 AI 政策，21G 只生成投稿材料草稿，由用户亲自确认作者信息和实际提交。

<a id="module-references-task-result-schema-json"></a>
## Module: `references/task-result.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/build-optical-coating-review/task-result.schema.json",
  "title": "Task Result",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "result_id", "project_id", "task_id", "status", "started_at", "completed_at", "inputs", "outputs", "quality_gate", "evidence_updates", "risk_ids", "manual_check_ids", "approval"],
  "properties": {
    "schema_version": {"const": "1.0.0"},
    "result_id": {"type": ["string", "null"]},
    "project_id": {"type": ["string", "null"]},
    "task_id": {"$ref": "common.schema.json#/$defs/taskId"},
    "status": {"$ref": "common.schema.json#/$defs/status"},
    "started_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]},
    "completed_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]},
    "inputs": {"type": "array", "items": {"$ref": "common.schema.json#/$defs/fileRecord"}},
    "outputs": {"type": "array", "items": {"$ref": "common.schema.json#/$defs/fileRecord"}},
    "quality_gate": {
      "type": "object",
      "additionalProperties": false,
      "required": ["gate_id", "passed", "checks", "checked_at"],
      "properties": {
        "gate_id": {"type": ["string", "null"]},
        "passed": {"type": ["boolean", "null"]},
        "checks": {"type": "array", "items": {"type": "object", "required": ["check_id", "result", "detail"], "properties": {"check_id": {"type": "string"}, "result": {"enum": ["PASS", "FAIL", "NOT_APPLICABLE", "MANUAL_CHECK_REQUIRED"]}, "detail": {"type": ["string", "null"]}}, "additionalProperties": false}},
        "checked_at": {"anyOf": [{"$ref": "common.schema.json#/$defs/dateTime"}, {"type": "null"}]}
      }
    },
    "evidence_updates": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "risk_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "manual_check_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
    "approval": {"anyOf": [{"$ref": "common.schema.json#/$defs/approvalRecord"}, {"type": "null"}]}
  }
}
```

<a id="module-scripts-common-py"></a>
## Module: `scripts/_common.py`

```python
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from collections.abc import Iterable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_VALIDATION = 3
EXIT_CONFLICT = 4
EXIT_EXTERNAL = 5

SCHEMA_VERSION = "1.0.0"
VERIFICATION_RANK = {f"V{i}": i for i in range(6)}
SECRET_KEY = re.compile(
    r"(^|_)(password|passwd|secret|api_?key|access_?token|refresh_?token|cookie|session)(_|$)",
    re.IGNORECASE,
)
SECRET_VALUE = re.compile(
    r"(?:authorization\s*:\s*bearer\s+\S+|(?:password|api[_-]?key|token|cookie)\s*[=:]\s*\S+)",
    re.IGNORECASE,
)


class ScriptError(RuntimeError):
    def __init__(self, message: str, exit_code: int = EXIT_VALIDATION):
        super().__init__(message)
        self.exit_code = exit_code


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_bytes(path: Path, data: bytes, *, overwrite: bool = True) -> None:
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise ScriptError(f"Refusing to overwrite existing file: {path}", EXIT_CONFLICT)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def atomic_write_text(path: Path, text: str, *, overwrite: bool = True) -> None:
    atomic_write_bytes(path, text.encode("utf-8"), overwrite=overwrite)


def write_json(path: Path, value: Any, *, overwrite: bool = True) -> None:
    assert_no_secrets(value)
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n", overwrite=overwrite)


def load_yaml_support():
    try:
        import yaml
    except ImportError as exc:
        raise ScriptError("PyYAML is required for YAML files. Install pyyaml.", EXIT_USAGE) from exc
    return yaml


def load_data(path: Path) -> Any:
    path = path.resolve()
    if not path.is_file():
        raise ScriptError(f"Input file does not exist: {path}", EXIT_USAGE)
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    if path.suffix.lower() in {".yaml", ".yml"}:
        return load_yaml_support().safe_load(text)
    raise ScriptError(f"Unsupported structured file: {path}", EXIT_USAGE)


def write_data(path: Path, value: Any, *, overwrite: bool = True) -> None:
    assert_no_secrets(value)
    if path.suffix.lower() == ".json":
        write_json(path, value, overwrite=overwrite)
        return
    if path.suffix.lower() in {".yaml", ".yml"}:
        text = load_yaml_support().safe_dump(value, sort_keys=False, allow_unicode=True)
        atomic_write_text(path, text, overwrite=overwrite)
        return
    raise ScriptError(f"Unsupported structured output: {path}", EXIT_USAGE)


def assert_no_secrets(value: Any, location: str = "root") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if SECRET_KEY.search(str(key)):
                raise ScriptError(f"Sensitive field is forbidden at {location}.{key}", EXIT_CONFLICT)
            assert_no_secrets(item, f"{location}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            assert_no_secrets(item, f"{location}[{index}]")
    elif isinstance(value, str) and SECRET_VALUE.search(value):
        raise ScriptError(f"Possible credential material is forbidden at {location}", EXIT_CONFLICT)


def schema_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "references"


def validate_against_schema(instance: Any, schema_name: str) -> list[str]:
    try:
        from jsonschema import Draft202012Validator, FormatChecker, RefResolver
    except ImportError as exc:
        raise ScriptError("jsonschema is required for Schema validation.", EXIT_USAGE) from exc

    root = schema_dir()
    schema_path = root / schema_name
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    common = json.loads((root / "common.schema.json").read_text(encoding="utf-8"))
    store = {
        common["$id"]: common,
        "common.schema.json": common,
        (root / "common.schema.json").resolve().as_uri(): common,
    }
    resolver = RefResolver(base_uri=schema_path.resolve().as_uri(), referrer=schema, store=store)
    validator = Draft202012Validator(schema, resolver=resolver, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    return [f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}" for error in errors]


def normalize_doi(value: Any) -> str | None:
    if value is None:
        return None
    doi = str(value).strip()
    if not doi:
        return None
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi\s*:\s*", "", doi, flags=re.IGNORECASE)
    return doi.strip().lower() or None


def normalize_title(value: Any) -> str:
    text = str(value or "").casefold()
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def split_semicolon(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return unique_strings(value)
    text = str(value)
    parts = re.split(r"(?<!\\);", text)
    return unique_strings(part.replace(r"\;", ";").strip() for part in parts if part.strip())


def unique_strings(values: Iterable[Any]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        item = str(value).strip()
        if item and item not in seen:
            result.append(item)
            seen.add(item)
    return result


def records_from_payload(payload: Any, key: str = "records") -> list[dict[str, Any]]:
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict) and isinstance(payload.get(key), list):
        records = payload[key]
    else:
        raise ScriptError(f"Expected a JSON array or object containing '{key}'", EXIT_USAGE)
    if not all(isinstance(item, dict) for item in records):
        raise ScriptError("Every record must be a JSON object", EXIT_USAGE)
    return records


def verification_at_least(value: str, required: str) -> bool:
    return VERIFICATION_RANK.get(value, -1) >= VERIFICATION_RANK[required]


def append_jsonl_atomic(path: Path, entry: dict[str, Any]) -> None:
    assert_no_secrets(entry)
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    line = json.dumps(entry, ensure_ascii=False, sort_keys=True)
    atomic_write_text(path, existing + line + "\n")


def print_report(report: Any) -> None:
    print(json.dumps(report, ensure_ascii=False, indent=2))


def run_cli(function) -> None:
    try:
        code = function()
    except ScriptError as exc:
        print_report({"status": "ERROR", "error": str(exc), "exit_code": exc.exit_code})
        raise SystemExit(exc.exit_code) from exc
    except (json.JSONDecodeError, ValueError) as exc:
        print_report({"status": "ERROR", "error": str(exc), "exit_code": EXIT_VALIDATION})
        raise SystemExit(EXIT_VALIDATION) from exc
    raise SystemExit(EXIT_OK if code is None else code)
```

<a id="module-scripts-distribution-py"></a>
## Module: `scripts/_distribution.py`

```python
from __future__ import annotations

import hashlib
from pathlib import Path

TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".mjs", ".txt", ".csv", ".tsv"}


def canonical_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return data
    text = data.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    return text.encode("utf-8")


def source_files(skill_root: Path) -> list[Path]:
    skill_root = skill_root.resolve()
    files = [skill_root / "SKILL.md", skill_root / "agents" / "openai.yaml"]
    files.extend(sorted((skill_root / "references").glob("*"), key=lambda item: item.name.casefold()))
    files.extend(sorted((skill_root / "scripts").glob("*"), key=lambda item: item.name.casefold()))
    files.extend(sorted((skill_root / "assets" / "templates").glob("*"), key=lambda item: item.name.casefold()))
    return [path for path in files if path.is_file() and "__pycache__" not in path.parts]


def source_manifest(skill_root: Path) -> list[dict[str, object]]:
    skill_root = skill_root.resolve()
    result = []
    for path in source_files(skill_root):
        data = canonical_bytes(path)
        result.append(
            {
                "path": path.relative_to(skill_root).as_posix(),
                "sha256": hashlib.sha256(data).hexdigest(),
                "size": len(data),
            }
        )
    return result


def source_hash(skill_root: Path) -> str:
    digest = hashlib.sha256()
    for entry in source_manifest(skill_root):
        digest.update(str(entry["path"]).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(entry["sha256"]).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()
```

<a id="module-scripts-audit-claims-py"></a>
## Module: `scripts/audit_claims.py`

```python
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
```

<a id="module-scripts-audit-figures-tables-py"></a>
## Module: `scripts/audit_figures_tables.py`

```python
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
```

<a id="module-scripts-build-core-workbooks-mjs"></a>
## Module: `scripts/build_core_workbooks.mjs`

```javascript
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { FileBlob, SpreadsheetFile, Workbook } = require("@oai/artifact-tool");

const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outputDir = path.join(skillRoot, "assets", "templates");
const qaDir = path.resolve(skillRoot, "..", "qa", "stage2", "xlsx");

const STATUS = ["NOT_STARTED", "IN_PROGRESS", "BLOCKED", "REVIEW_REQUIRED", "APPROVED", "REJECTED", "SKIPPED_WITH_RISK", "SUPERSEDED", "ARCHIVED"];
const VERIFY = ["V0", "V1", "V2", "V3", "V4", "V5"];
const HUMAN = ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REVISE", "REJECTED"];
const STRENGTH = ["UNASSESSED", "WEAK", "MODERATE", "STRONG"];
const BOOLEAN = ["TRUE", "FALSE"];

const colors = {
  header: "#174A5B",
  headerText: "#FFFFFF",
  guideHeader: "#365B4A",
  border: "#B8C2C8",
  required: "#E8F1ED",
  optional: "#F3F5F6",
};

const databaseRows = [
  ["Web of Science Core Collection", "COMPREHENSIVE"],
  ["Scopus", "COMPREHENSIVE"],
  ["PubMed", "DISCIPLINE"],
  ["Google Scholar", "DISCOVERY"],
  ["百度学术", "DISCOVERY"],
  ["Crossref", "METADATA_VERIFICATION"],
  ["OpenAlex", "METADATA_VERIFICATION"],
  ["GeoRef", "DISCIPLINE"],
  ["Engineering Village", "DISCIPLINE"],
  ["ScienceDirect", "PUBLISHER_FULL_TEXT"],
  ["SpringerLink", "PUBLISHER_FULL_TEXT"],
  ["CNKI", "CHINESE_DATABASE"],
  ["万方", "CHINESE_DATABASE"],
].map(([database_name, database_category]) => ({ database_name, database_category, access_status: "UNVERIFIED", access_level: "L0" }));

const specs = [
  {
    file: "preflight_and_roadmap.xlsx",
    sheets: [
      {
        name: "Database Access",
        fields: [
          ["database_name", "string", true, "平台名称"], ["database_category", "enum", true, "平台类别"], ["access_status", "enum", true, "访问状态"], ["access_level", "enum", true, "L0-L5 能力等级"],
          ["access_route", "string", false, "机构、VPN 或公开访问路径"], ["test_date", "date", false, "ISO 日期"], ["institutional_login", "boolean", true, "是否使用机构登录"], ["vpn_required", "boolean", true, "是否需要 VPN"],
          ["search_available", "boolean", true, "是否可检索"], ["record_page_available", "boolean", true, "是否可查看题录页"], ["abstract_available", "boolean", true, "是否可查看摘要"], ["full_text_available", "boolean", true, "是否可合法访问全文"],
          ["citation_export_available", "boolean", true, "是否可导出引文"], ["supported_export_formats", "array<string>", true, "分号分隔"], ["test_query", "string", false, "实际测试检索式"], ["test_result_count", "integer", false, "真实结果数量"],
          ["automation_restrictions", "string", false, "验证码、速率或条款限制"], ["known_limitations", "string", false, "已知限制"], ["user_confirmed", "boolean", true, "用户是否确认"], ["notes", "string", false, "补充说明"]
        ],
        rows: databaseRows,
        validations: { access_status: ["ACCESSIBLE", "PARTIALLY_ACCESSIBLE", "VPN_REQUIRED", "LOGIN_REQUIRED", "NO_SUBSCRIPTION", "CAPTCHA_OR_MANUAL_OPERATION_REQUIRED", "TEMPORARILY_UNAVAILABLE", "REGION_RESTRICTED", "NOT_REQUIRED_FOR_THIS_PROJECT", "USER_WAIVED", "UNVERIFIED"], access_level: ["L0", "L1", "L2", "L3", "L4", "L5"], institutional_login: BOOLEAN, vpn_required: BOOLEAN, search_available: BOOLEAN, record_page_available: BOOLEAN, abstract_available: BOOLEAN, full_text_available: BOOLEAN, citation_export_available: BOOLEAN, user_confirmed: BOOLEAN }
      },
      {
        name: "Research Roadmap",
        fields: [
          ["schema_version", "string", true, "固定为 1.0.0"], ["roadmap_item_id", "id", true, "RM-000 格式稳定 ID"], ["research_question", "string", true, "核心研究问题"], ["stage", "enum", true, "STEP_00 或 STAGE_1-4"],
          ["task", "task_id", true, "STEP-00 或 TASK-01...TASK-21H"], ["prerequisites", "array<string>", true, "分号分隔"], ["evidence_needed", "array<string>", true, "至少一项，分号分隔"], ["preferred_sources", "array<string>", true, "分号分隔"],
          ["planned_deliverable", "string", true, "计划交付物"], ["decision_gate", "string", true, "批准条件"], ["risk", "string|null", false, "主要风险"], ["status", "enum", true, "任务状态"], ["owner", "string|null", false, "责任人"], ["last_updated", "date|null", false, "ISO 日期"]
        ],
        validations: { stage: ["STEP_00", "STAGE_1", "STAGE_2", "STAGE_3", "STAGE_4"], status: STATUS }
      }
    ]
  },
  {
    file: "literature_registry.xlsx",
    sheets: [
      {
        name: "Master Literature",
        fields: [
          ["schema_version", "string", true, "固定为 1.0.0"], ["source_id", "id", true, "SRC- 前缀稳定 ID"], ["title", "string|null", true, "原文题名"], ["authors", "array<string>", true, "分号分隔"], ["year", "integer|null", true, "出版年份"],
          ["journal", "string|null", true, "期刊或来源"], ["document_type", "enum", true, "文献类型"], ["doi", "string|null", false, "规范化 DOI"], ["url", "uri|null", false, "记录页或全文 URL"], ["language", "string|null", false, "语言"],
          ["database_sources", "array<string>", true, "分号分隔"], ["record_version", "string", true, "题录版本"], ["supersedes_source_id", "source_id|null", false, "被替代版本"], ["verification_level", "enum", true, "V0-V5"], ["verification_date", "date|null", false, "ISO 日期"],
          ["full_text_status", "enum", true, "全文状态"], ["screening_decision", "enum", true, "筛选决定"], ["screening_reason", "string|null", false, "筛选理由"], ["materials", "array<string>", true, "分号分隔"], ["substrates", "array<string>", true, "分号分隔"],
          ["coatings", "array<string>", true, "分号分隔"], ["deposition_routes", "array<string>", true, "分号分隔"], ["interface_strategies", "array<string>", true, "分号分隔"], ["optical_properties", "array<string>", true, "分号分隔"], ["mechanical_properties", "array<string>", true, "分号分隔"],
          ["environmental_properties", "array<string>", true, "分号分隔"], ["manufacturing_properties", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["themes", "array<string>", true, "分号分隔"], ["research_stage", "string|null", false, "研究阶段"],
          ["intended_uses", "array<enum>", true, "CORE/SUPPORTING/BACKGROUND/METHOD/CONFLICT"], ["evidence_strength", "enum", true, "证据强度"], ["notes", "string|null", false, "补充说明"]
        ],
        validations: { document_type: ["JOURNAL_ARTICLE", "REVIEW", "CONFERENCE_PAPER", "BOOK_CHAPTER", "STANDARD", "PATENT", "THESIS", "PREPRINT", "REPORT", "OTHER"], verification_level: VERIFY, full_text_status: ["NOT_REQUESTED", "MISSING", "PARTIAL", "AVAILABLE", "UNREADABLE", "MISMATCHED"], screening_decision: ["UNSCREENED", "INCLUDE", "EXCLUDE", "UNCERTAIN", "BACKGROUND_ONLY", "METHOD_ONLY"], evidence_strength: STRENGTH },
        wholeNumbers: { year: [1600, 2200] }
      },
      {
        name: "Screening",
        fields: [["screening_id", "id", true, "筛选记录 ID"], ["source_id", "source_id", true, "稳定来源 ID"], ["screening_stage", "enum", true, "筛选阶段"], ["decision", "enum", true, "决定"], ["exclusion_reason", "string|null", false, "排除理由"], ["uncertainty", "enum", true, "不确定性"], ["full_text_used", "boolean", true, "是否实际使用全文"], ["reviewer", "string|null", false, "筛选者"], ["reviewed_at", "date|null", false, "ISO 日期"], ["notes", "string|null", false, "补充说明"]],
        validations: { screening_stage: ["TITLE", "ABSTRACT", "FULL_TEXT"], decision: ["INCLUDE", "EXCLUDE", "UNCERTAIN", "BACKGROUND_ONLY", "METHOD_ONLY"], uncertainty: ["LOW", "MEDIUM", "HIGH"], full_text_used: BOOLEAN }
      },
      {
        name: "Source Registry",
        fields: [["source_id", "source_id", true, "稳定来源 ID"], ["canonical_title", "string|null", true, "规范题名"], ["doi", "string|null", false, "规范化 DOI"], ["record_version", "string", true, "记录版本"], ["supersedes_source_id", "source_id|null", false, "替代关系"], ["verification_level", "enum", true, "V0-V5"], ["metadata_sources", "array<string>", true, "分号分隔"], ["pdf_path", "string|null", false, "项目内 PDF 路径"], ["pdf_sha256", "sha256|null", false, "PDF 哈希"], ["attachment_status", "enum", true, "附件状态"], ["manual_check_status", "enum", true, "人工核查状态"], ["notes", "string|null", false, "补充说明"]],
        validations: { verification_level: VERIFY, attachment_status: ["NONE", "AVAILABLE", "MISSING", "MISMATCHED", "UNREADABLE"], manual_check_status: HUMAN }
      }
    ]
  },
  {
    file: "evidence_and_claims.xlsx",
    sheets: [
      {
        name: "Claims",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["claim_id", "claim_id", true, "CLM-章节-序号"], ["claim_text_zh", "string|null", true, "中文主张"], ["claim_text_en", "string|null", true, "英文主张"], ["claim_type", "enum", true, "主张类型"], ["source_ids", "array<source_id>", true, "分号分隔"], ["original_locations", "array<string>", true, "与来源顺序对应"], ["relations", "array<enum>", true, "SUPPORTS/CONTRADICTS/QUALIFIES/BACKGROUND_ONLY"], ["evidence_type", "enum", true, "证据类型"], ["evidence_strength", "enum", true, "证据强度"], ["consistency", "enum", true, "一致性"], ["applicability_conditions", "array<string>", true, "分号分隔"], ["limitations", "array<string>", true, "分号分隔"], ["intended_section", "string|null", false, "计划章节"], ["human_status", "enum", true, "人工状态"], ["minimum_verification_level", "enum", true, "最低核验等级"], ["notes", "string|null", false, "补充说明"]],
        validations: { claim_type: ["BACKGROUND", "DESCRIPTIVE", "COMPARATIVE", "QUANTITATIVE", "MECHANISTIC", "CAUSAL", "METHOD", "CONSENSUS", "CONTROVERSY", "RESEARCH_GAP", "APPLICATION"], evidence_type: ["METADATA", "ABSTRACT", "FULL_TEXT_STATEMENT", "TABLE", "FIGURE", "SUPPLEMENT", "STANDARD", "DERIVED_CALCULATION", "SYNTHESIS"], evidence_strength: STRENGTH, consistency: ["UNASSESSED", "CONSISTENT", "MIXED", "CONTRADICTORY", "SINGLE_SOURCE"], human_status: HUMAN, minimum_verification_level: VERIFY }
      },
      {
        name: "Evidence Cards",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["evidence_card_id", "id", true, "EC- 前缀稳定 ID"], ["source_id", "source_id", true, "稳定来源 ID"], ["citation", "string|null", false, "规范引文"], ["research_question", "string|null", false, "对应研究问题"], ["material_system", "string|null", false, "材料体系"], ["substrate", "string|null", false, "基底"], ["coating", "string|null", false, "膜层"], ["deposition_method", "string|null", false, "沉积方法"], ["interface_strategy", "string|null", false, "界面策略"], ["process_conditions", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["key_results", "array<structured>", true, "指标|值|单位|条件|位置，多条用分号"], ["author_interpretation", "array<string>", true, "分号分隔"], ["skill_assessment", "array<string>", true, "分号分隔"], ["supported_claim_ids", "array<claim_id>", true, "分号分隔"], ["comparison_uses", "array<string>", true, "分号分隔"], ["figure_table_uses", "array<string>", true, "分号分隔"], ["original_locations", "array<string>", true, "分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["evidence_strength", "enum", true, "证据强度"], ["limitations", "array<string>", true, "分号分隔"], ["citation_risks", "array<string>", true, "分号分隔"], ["human_status", "enum", true, "人工状态"]],
        validations: { verification_level: VERIFY, evidence_strength: STRENGTH, human_status: HUMAN }
      },
      {
        name: "Figure-Table Trace",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["trace_id", "id", true, "TRC- 前缀稳定 ID"], ["artifact_id", "id", true, "FIG- 或 TAB- 前缀"], ["artifact_type", "enum", true, "图、图元素、表或单元格"], ["element_id", "string|null", false, "元素 ID"], ["target_location", "string|null", false, "稿件位置"], ["source_id", "source_id", true, "稳定来源 ID"], ["original_location", "string", true, "页码、章节、图或表"], ["transformation", "enum", true, "转换方式"], ["calculation", "string|null", false, "计算过程"], ["copyright_status", "enum", true, "版权状态"], ["permission_reference", "string|null", false, "许可记录"], ["verification_level", "enum", true, "V0-V5"], ["human_status", "enum", true, "人工状态"], ["notes", "string|null", false, "补充说明"]],
        validations: { artifact_type: ["FIGURE", "FIGURE_ELEMENT", "TABLE", "TABLE_CELL"], transformation: ["DIRECT_REUSE", "REDRAWN", "ADAPTED", "DIGITIZED", "CALCULATED", "SYNTHESIZED"], copyright_status: ["UNASSESSED", "ORIGINAL", "LICENSED", "PERMISSION_REQUIRED", "PERMISSION_OBTAINED", "FAIR_USE_ASSESSED", "NOT_REUSABLE"], verification_level: VERIFY, human_status: HUMAN }
      }
    ]
  },
  {
    file: "literature_map.xlsx",
    sheets: [
      {
        name: "Nodes",
        fields: [["source_id", "source_id", true, "稳定来源 ID"], ["title", "string|null", true, "题名"], ["year", "integer|null", true, "年份"], ["journal", "string|null", true, "期刊"], ["document_type", "string|null", true, "文献类型"], ["materials", "array<string>", true, "分号分隔"], ["substrates", "array<string>", true, "分号分隔"], ["coatings", "array<string>", true, "分号分隔"], ["deposition_routes", "array<string>", true, "分号分隔"], ["interface_strategies", "array<string>", true, "分号分隔"], ["optical_properties", "array<string>", true, "分号分隔"], ["mechanical_properties", "array<string>", true, "分号分隔"], ["environmental_properties", "array<string>", true, "分号分隔"], ["manufacturing_properties", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["evidence_types", "array<string>", true, "分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["themes", "array<string>", true, "分号分隔"], ["research_stage", "string|null", false, "研究阶段"], ["intended_uses", "array<enum>", true, "CORE/SUPPORTING/BACKGROUND/METHOD/CONFLICT"], ["evidence_strength", "enum", true, "证据强度"]],
        validations: { verification_level: VERIFY, evidence_strength: STRENGTH },
        wholeNumbers: { year: [1600, 2200] }
      },
      {
        name: "Edges",
        fields: [["edge_id", "id", true, "EDGE- 前缀稳定 ID"], ["from_source_id", "source_id", true, "起点 Source_ID"], ["to_source_id", "source_id", true, "终点 Source_ID"], ["relation", "enum", true, "学术关系"], ["basis", "string", true, "关系依据，禁止仅凭标题相似"], ["original_locations", "array<string>", true, "原文位置，分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["human_status", "enum", true, "人工状态"]],
        validations: { relation: ["SUPPORTS", "CONTRADICTS", "EXTENDS", "USES_METHOD_FROM", "SHARES_MATERIAL_SYSTEM", "SHARES_DEPOSITION_ROUTE", "REPORTS_COMPARABLE_METRIC", "STRUCTURAL_REFERENCE", "BACKGROUND_ONLY"], verification_level: VERIFY, human_status: ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REJECTED"] }
      },
      {
        name: "Views",
        fields: [["view_type", "enum", true, "必需视图"], ["status", "enum", true, "构建状态"], ["scope", "string|null", false, "视图范围"], ["output_path", "string|null", false, "导出路径"], ["last_updated", "date|null", false, "ISO 日期"], ["notes", "string|null", false, "补充说明"]],
        rows: ["TIME_EVOLUTION", "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE", "THEME_CLUSTER", "METHOD_CHARACTERIZATION_MATRIX", "CONSENSUS_CONTROVERSY", "EVIDENCE_LAYER"].map((view_type) => ({ view_type, status: "NOT_STARTED" })),
        validations: { view_type: ["TIME_EVOLUTION", "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE", "THEME_CLUSTER", "METHOD_CHARACTERIZATION_MATRIX", "CONSENSUS_CONTROVERSY", "EVIDENCE_LAYER"], status: STATUS }
      }
    ]
  }
];

function columnLetter(index) {
  let n = index + 1;
  let out = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    out = String.fromCharCode(65 + r) + out;
    n = Math.floor((n - 1) / 26);
  }
  return out;
}

function rowsToMatrix(fields, rows = []) {
  return rows.map((record) => fields.map(([name]) => Object.hasOwn(record, name) ? record[name] : null));
}

function defaultWidth(name, type) {
  if (name.includes("title") || name.includes("question") || name.includes("basis") || name.includes("reason") || name.includes("notes")) return 30;
  if (type.startsWith("array") || name.includes("conditions") || name.includes("limitations")) return 24;
  if (type.includes("date") || name.includes("status") || name.includes("level")) return 18;
  if (name.includes("id")) return 20;
  return 17;
}

function writeDataSheet(workbook, spec) {
  const sheet = workbook.worksheets.add(spec.name);
  const headers = spec.fields.map(([name]) => name);
  const end = columnLetter(headers.length - 1);
  sheet.getRange(`A1:${end}1`).values = [headers];
  const matrix = rowsToMatrix(spec.fields, spec.rows);
  if (matrix.length) sheet.getRange(`A2:${end}${matrix.length + 1}`).values = matrix;
  const header = sheet.getRange(`A1:${end}1`);
  header.format = { fill: colors.header, font: { bold: true, color: colors.headerText }, wrapText: true, verticalAlignment: "center", horizontalAlignment: "center", borders: { preset: "all", style: "thin", color: colors.border } };
  header.format.rowHeight = 34;
  spec.fields.forEach(([name, type], i) => {
    sheet.getRange(`${columnLetter(i)}:${columnLetter(i)}`).format.columnWidth = defaultWidth(name, type);
  });
  sheet.freezePanes.freezeRows(1);
  for (const [field, values] of Object.entries(spec.validations || {})) {
    const idx = headers.indexOf(field);
    if (idx >= 0) sheet.getRange(`${columnLetter(idx)}2:${columnLetter(idx)}500`).dataValidation = { rule: { type: "list", values } };
  }
  for (const [field, [min, max]] of Object.entries(spec.wholeNumbers || {})) {
    const idx = headers.indexOf(field);
    if (idx >= 0) sheet.dataValidations.add({ range: `${columnLetter(idx)}2:${columnLetter(idx)}500`, rule: { type: "whole", operator: "between", formula1: min, formula2: max } });
  }
  if (matrix.length) {
    const body = sheet.getRange(`A2:${end}${matrix.length + 1}`);
    body.format = { wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: colors.border } };
    body.format.rowHeight = 28;
  }
  return sheet;
}

function writeFieldGuide(workbook, sheetSpecs) {
  const sheet = workbook.worksheets.add("Field Guide");
  const rows = [["sheet", "field", "type", "required", "description", "allowed_values"]];
  for (const spec of sheetSpecs) {
    for (const [field, type, required, description] of spec.fields) {
      rows.push([spec.name, field, type, required ? "YES" : "NO", description, (spec.validations?.[field] || []).join(";")]);
    }
  }
  sheet.getRange(`A1:F${rows.length}`).values = rows;
  sheet.getRange("A1:F1").format = { fill: colors.guideHeader, font: { bold: true, color: colors.headerText }, wrapText: true, horizontalAlignment: "center", borders: { preset: "all", style: "thin", color: colors.border } };
  sheet.getRange(`A2:F${rows.length}`).format = { wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: colors.border } };
  [18, 28, 18, 12, 36, 42].forEach((width, i) => { sheet.getRange(`${columnLetter(i)}:${columnLetter(i)}`).format.columnWidth = width; });
  sheet.freezePanes.freezeRows(1);
  return sheet;
}

function safeName(name) {
  return name.replace(/[^A-Za-z0-9_-]+/g, "_");
}

async function buildWorkbook(spec) {
  const workbook = Workbook.create();
  for (const sheetSpec of spec.sheets) writeDataSheet(workbook, sheetSpec);
  writeFieldGuide(workbook, spec.sheets);

  const workbookQaDir = path.join(qaDir, path.basename(spec.file, ".xlsx"));
  await fs.mkdir(workbookQaDir, { recursive: true });
  const inspections = [];
  for (const sheetSpec of [...spec.sheets, { name: "Field Guide" }]) {
    const inspected = await workbook.inspect({ kind: "table", sheetId: sheetSpec.name, range: "A1:Z20", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 26, maxChars: 6000 });
    inspections.push({ sheet: sheetSpec.name, inspect: inspected.ndjson ?? String(inspected) });
    const preview = await workbook.render({ sheetName: sheetSpec.name, autoCrop: "all", scale: 1, format: "png" });
    await fs.writeFile(path.join(workbookQaDir, `${safeName(sheetSpec.name)}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
  const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
  await fs.writeFile(path.join(workbookQaDir, "inspection.json"), JSON.stringify({ workbook: spec.file, inspections, formula_errors: errors.ndjson ?? String(errors) }, null, 2), "utf8");
  const outputPath = path.join(outputDir, spec.file);
  const out = await SpreadsheetFile.exportXlsx(workbook);
  await out.save(outputPath);
  const reopened = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
  for (const sheetSpec of spec.sheets) {
    const expected = sheetSpec.fields.map(([name]) => name);
    const end = columnLetter(expected.length - 1);
    const actual = reopened.worksheets.getItem(sheetSpec.name).getRange(`A1:${end}1`).values[0];
    if (JSON.stringify(actual) !== JSON.stringify(expected)) {
      throw new Error(`Exported header mismatch in ${spec.file}/${sheetSpec.name}`);
    }
  }
}

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });
for (const spec of specs) await buildWorkbook(spec);
console.log(JSON.stringify({ outputDir, qaDir, workbooks: specs.map((s) => s.file) }, null, 2));
```

<a id="module-scripts-build-full-skill-py"></a>
## Module: `scripts/build_full_skill.py`

```python
from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
from datetime import datetime, timezone
from pathlib import Path

from _common import ScriptError, atomic_write_text, run_cli
from _distribution import TEXT_SUFFIXES, source_files, source_hash, source_manifest


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Build a deterministic portable SKILL_FULL.md from the modular Skill sources.")
    result.add_argument("skill_root", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--generated-at", help="RFC 3339 timestamp for reproducible builds; otherwise SOURCE_DATE_EPOCH or current UTC")
    return result


def generated_at(explicit: str | None) -> str:
    if explicit:
        try:
            datetime.fromisoformat(explicit.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ScriptError("--generated-at must be an RFC 3339 timestamp", 2) from exc
        return explicit
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.fromtimestamp(int(epoch), timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def demote_markdown(text: str) -> str:
    result = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#{1,6}\s", line):
            hashes, rest = line.split(" ", 1)
            line = "#" * min(6, len(hashes) + 2) + " " + rest
        result.append(line)
    return "\n".join(result)


def fence_for(path: Path) -> str:
    return {".py": "python", ".mjs": "javascript", ".json": "json", ".yaml": "yaml", ".yml": "yaml"}.get(path.suffix.lower(), "text")


def module_anchor(relative: str) -> str:
    return "module-" + re.sub(r"[^a-z0-9]+", "-", relative.casefold()).strip("-")


def rewrite_local_links(text: str, current_relative: str, known_paths: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if target.startswith(("#", "http://", "https://", "mailto:")):
            return match.group(0)
        path_part = target.split("#", 1)[0]
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(current_relative), path_part))
        if resolved not in known_paths:
            return match.group(0)
        return f"](#{module_anchor(resolved)})"

    return re.sub(r"\]\(([^)]+)\)", replace, text)


def main() -> int:
    args = parser().parse_args()
    root = args.skill_root.resolve()
    if not (root / "SKILL.md").is_file():
        raise ScriptError(f"Not a Skill root: {root}", 2)
    output = args.output.resolve()
    if output.exists():
        raise ScriptError(f"Refusing to overwrite generated distribution: {output}", 4)
    stamp = generated_at(args.generated_at)
    digest = source_hash(root)
    manifest = source_manifest(root)
    files = source_files(root)
    known_paths = {path.relative_to(root).as_posix() for path in files}
    content_hash_placeholder = "__PORTABLE_CONTENT_SHA256__"
    sections = [
        f"Portable Content SHA-256: `{content_hash_placeholder}`",
        "<!-- GENERATED FILE: DO NOT EDIT. Rebuild with scripts/build_full_skill.py. -->",
        "# Build Optical Coating Review - Portable Full Skill",
        "",
        f"Generated at: `{stamp}`  ",
        f"Source SHA-256: `{digest}`",
        "",
        "This portable document mirrors the modular Skill. The modular Codex Skill remains the authoritative runtime form.",
        "",
        "## Module Index",
        "",
    ]
    sections.extend(
        f"- [`{path.relative_to(root).as_posix()}`](#{module_anchor(path.relative_to(root).as_posix())})"
        for path in files
    )
    for path in files:
        relative = path.relative_to(root).as_posix()
        sections.extend(["", f"<a id=\"{module_anchor(relative)}\"></a>", f"## Module: `{relative}`", ""])
        if path.suffix.lower() not in TEXT_SUFFIXES:
            item = next(entry for entry in manifest if entry["path"] == relative)
            sections.append(f"Binary asset: `{relative}`; SHA-256 `{item['sha256']}`; size `{item['size']}` bytes.")
            continue
        text = path.read_text(encoding="utf-8-sig")
        if path.suffix.lower() == ".md":
            sections.append(demote_markdown(rewrite_local_links(text, relative, known_paths)))
        else:
            sections.extend([f"```{fence_for(path)}", text.rstrip(), "```"])
    sections.extend(["", "## Source Manifest", "", "```json", json.dumps(manifest, ensure_ascii=False, indent=2), "```", ""])
    unhashed_content = "\n".join(sections)
    content_digest = hashlib.sha256(unhashed_content.encode("utf-8")).hexdigest()
    content = unhashed_content.replace(content_hash_placeholder, content_digest, 1)
    atomic_write_text(output, content, overwrite=False)
    print(json.dumps({"status": "OK", "output": str(output), "source_sha256": digest, "content_sha256": content_digest, "files": len(manifest), "generated_at": stamp}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
```

<a id="module-scripts-build-literature-map-py"></a>
## Module: `scripts/build_literature_map.py`

```python
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
```

<a id="module-scripts-build-outline-template-py"></a>
## Module: `scripts/build_outline_template.py`

```python
from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

SKILL_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = SKILL_ROOT / "assets" / "templates" / "review_outline_template.docx"
PRESET = "compact_reference_guide"
CONTENT_DXA = 9360
TABLE_INDENT_DXA = 120
CELL_MARGINS = {"top": 80, "bottom": 80, "start": 120, "end": 120}


def set_east_asia_font(style_or_run, name: str = "Microsoft YaHei") -> None:
    style_or_run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), name)


def set_style_font(style, latin: str, size: float, color: str | None = None, bold: bool | None = None) -> None:
    style.font.name = latin
    style.font.size = Pt(size)
    if color:
        style.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        style.font.bold = bold
    style._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), latin)
    style._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), latin)
    style._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")


def add_bottom_border(paragraph, color: str = "AAB7BE", size: str = "6") -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn("w:pBdr"))
    if p_bdr is None:
        p_bdr = OxmlElement("w:pBdr")
        p_pr.append(p_bdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), color)
    p_bdr.append(bottom)


def add_page_field(paragraph) -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, separate, text, end])


def add_multilevel_heading_numbering(document: Document) -> int:
    numbering = document.part.numbering_part.element
    abstract_id = 42
    num_id = 42
    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    multi = OxmlElement("w:multiLevelType")
    multi.set(qn("w:val"), "multilevel")
    abstract.append(multi)
    for level, text in enumerate(["%1", "%1.%2", "%1.%2.%3"]):
        lvl = OxmlElement("w:lvl")
        lvl.set(qn("w:ilvl"), str(level))
        start = OxmlElement("w:start")
        start.set(qn("w:val"), "1")
        num_fmt = OxmlElement("w:numFmt")
        num_fmt.set(qn("w:val"), "decimal")
        lvl_text = OxmlElement("w:lvlText")
        lvl_text.set(qn("w:val"), text)
        suff = OxmlElement("w:suff")
        suff.set(qn("w:val"), "space")
        p_pr = OxmlElement("w:pPr")
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), "0")
        ind.set(qn("w:hanging"), "0")
        p_pr.append(ind)
        lvl.extend([start, num_fmt, lvl_text, suff, p_pr])
        abstract.append(lvl)
    numbering.append(abstract)
    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(num_id))
    abstract_ref = OxmlElement("w:abstractNumId")
    abstract_ref.set(qn("w:val"), str(abstract_id))
    num.append(abstract_ref)
    numbering.append(num)
    return num_id


def apply_heading_number(paragraph, num_id: int, level: int) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    num_pr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), str(level))
    num = OxmlElement("w:numId")
    num.set(qn("w:val"), str(num_id))
    num_pr.extend([ilvl, num])
    p_pr.insert(0, num_pr)


def set_cell_margins(cell) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for edge, value in CELL_MARGINS.items():
        node = tc_mar.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_cell_width(cell, width_dxa: int) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn("w:tcW"))
    if tc_w is None:
        tc_w = OxmlElement("w:tcW")
        tc_pr.append(tc_w)
    tc_w.set(qn("w:w"), str(width_dxa))
    tc_w.set(qn("w:type"), "dxa")


def set_cell_fill(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_table_geometry(table, widths: list[int]) -> None:
    if sum(widths) != CONTENT_DXA:
        raise ValueError("Table widths must sum to 9360 DXA")
    table.autofit = False
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl_pr = table._tbl.tblPr
    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(CONTENT_DXA))
    tbl_w.set(qn("w:type"), "dxa")
    tbl_ind = tbl_pr.find(qn("w:tblInd"))
    if tbl_ind is None:
        tbl_ind = OxmlElement("w:tblInd")
        tbl_pr.append(tbl_ind)
    tbl_ind.set(qn("w:w"), str(TABLE_INDENT_DXA))
    tbl_ind.set(qn("w:type"), "dxa")
    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)
    for row in table.rows:
        for index, cell in enumerate(row.cells):
            set_cell_width(cell, widths[index])
            set_cell_margins(cell)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def format_table_text(table, header: bool = False) -> None:
    for row_index, row in enumerate(table.rows):
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(4)
                paragraph.paragraph_format.line_spacing = 1.0
                for run in paragraph.runs:
                    run.font.name = "Calibri"
                    run.font.size = Pt(10)
                    set_east_asia_font(run)
                    if header and row_index == 0:
                        run.bold = True
            if header and row_index == 0:
                set_cell_fill(cell, "E8EEF5")


def add_heading(document: Document, text: str, level: int, num_id: int) -> None:
    paragraph = document.add_paragraph(text, style=f"Heading {level}")
    apply_heading_number(paragraph, num_id, level - 1)


def add_prompt(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    label = paragraph.add_run("写作与证据要求：")
    label.bold = True
    body = paragraph.add_run(text)
    for run in (label, body):
        run.font.name = "Calibri"
        set_east_asia_font(run)
    paragraph.paragraph_format.keep_together = True


def build_document() -> Document:
    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.right_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)

    normal = document.styles["Normal"]
    set_style_font(normal, "Calibri", 11, "1F2933")
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25

    heading_tokens = {
        1: (16, "2E74B5", 18, 10),
        2: (13, "2E74B5", 14, 7),
        3: (12, "1F4D78", 10, 5),
    }
    for level, (size, color, before, after) in heading_tokens.items():
        style = document.styles[f"Heading {level}"]
        set_style_font(style, "Calibri", size, color, True)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True

    header = section.header.paragraphs[0]
    header.text = "Optical Coating Literature Review | Audit Template"
    header.alignment = WD_ALIGN_PARAGRAPH.LEFT
    header.paragraph_format.space_after = Pt(4)
    for run in header.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor.from_string("5F6B73")
    add_bottom_border(header)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.paragraph_format.space_before = Pt(4)
    run = footer.add_run("Page ")
    run.font.name = "Calibri"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor.from_string("5F6B73")
    add_page_field(footer)

    title = document.add_paragraph()
    title.paragraph_format.space_before = Pt(0)
    title.paragraph_format.space_after = Pt(12)
    title.paragraph_format.keep_with_next = True
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = title.add_run("红外硫系玻璃基底 DLC 薄膜\n三级大纲与审计写作骨架")
    run.font.name = "Calibri"
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor.from_string("174A5B")
    set_east_asia_font(run)

    subtitle = document.add_paragraph("材料基础、制备技术与应用进展 | Evidence-traceable review outline")
    subtitle.paragraph_format.space_after = Pt(12)
    for run in subtitle.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor.from_string("5F6B73")
        set_east_asia_font(run)

    meta = document.add_table(rows=6, cols=2)
    meta.style = "Table Grid"
    meta_data = [
        ("项目 ID", "初始化项目时填写；与 project_state.yaml 一致"),
        ("综述类型", "在 Task 02 批准 Narrative Review 或 Systematic Review 后填写"),
        ("大纲版本", "批准版本不得覆盖；新版本通过 SUPERSEDED 关系连接"),
        ("证据门禁", "核心事实 ≥ V3；机制、定量比较与图表数据 ≥ V4"),
        ("Style preset", PRESET),
        ("Named override", "中文字符使用 Microsoft YaHei 作为 East Asian fallback；标题 20 pt #174A5B"),
    ]
    for row, values in zip(meta.rows, meta_data):
        row.cells[0].text, row.cells[1].text = values
        set_cell_fill(row.cells[0], "E8EEF5")
        row.cells[0].paragraphs[0].runs[0].bold = True
    set_table_geometry(meta, [2700, 6660])
    format_table_text(meta)

    document.add_paragraph()
    gate = document.add_table(rows=1, cols=1)
    gate.style = "Table Grid"
    gate.cell(0, 0).text = "状态门禁：本模板只能在 Task 20 的三级大纲获明确批准后用于 Task 21B 写作。每章结束后暂停；未经批准不得继续下一章。"
    set_cell_fill(gate.cell(0, 0), "F4F6F9")
    set_table_geometry(gate, [9360])
    format_table_text(gate)

    num_id = add_multilevel_heading_numbering(document)
    sections = [
        ("引言与综述边界", [
            ("红外窗口的防护需求与应用背景", "把服役环境、透过波段和失效模式连接到涂层需求；用 Source_ID 区分工程背景与直接证据。"),
            ("综述范围、术语和证据方法", "明确硫系玻璃、DLC 类型、工艺、性能、应用、时间与语言边界；说明 Narrative 或 Systematic 分支。")
        ]),
        ("红外硫系玻璃基底的材料基础", [
            ("组成—结构—红外性能关系", "比较玻璃组成、声子吸收、折射率、软化温度与环境稳定性；定量值必须带条件和原文位置。"),
            ("表面加工损伤与镀膜相容性", "综合粗糙度、缺陷、热膨胀、温度上限和清洗敏感性，避免把单一基底结论外推到全部硫系玻璃。")
        ]),
        ("DLC 膜层的结构与光学基础", [
            ("键合结构、缺陷与应力", "区分 sp2/sp3、氢含量、密度和应力的测量与推断；Raman 拟合不得直接等同于精确 sp3 含量。"),
            ("光学常数与红外响应", "在波长、角度、偏振、膜厚和模型条件下比较 n、k、透射、反射和吸收，记录拟合模型与不确定性。")
        ]),
        ("制备技术与工艺窗口", [
            ("PECVD、磁控溅射与离子辅助路线", "比较能量输入、温度、沉积速率、均匀性、应力和基底损伤；把设备差异作为跨研究比较条件。"),
            ("FCVA、PLD 与复合沉积路线", "评估高离化率、颗粒缺陷、过滤、放大和复杂曲面适用性；工程结论需要规模证据。")
        ]),
        ("界面工程与失效控制", [
            ("清洗、活化与过渡层", "追踪表面化学、等离子活化、Si/Ge 等过渡层及梯度设计对附着和光学损耗的影响。"),
            ("残余应力、裂纹与剥落机制", "分别陈述观察结果、作者解释和跨文献判断；因果表述需排除膜厚、温度和缺陷等混杂因素。")
        ]),
        ("综合性能与评价方法", [
            ("光学、机械与环境性能", "按相同测试条件比较透射、硬度、模量、附着、磨损、湿热、盐雾、风沙与热循环，禁止无条件横向排名。"),
            ("表征方法与证据质量", "建立光谱、椭偏、Raman、XPS、SEM、AFM、压痕和划痕的证据矩阵，说明方法局限与互证关系。")
        ]),
        ("应用进展与工程化", [
            ("红外成像、探测与航天窗口", "连接真实器件指标、服役条件和标准要求；实验室样片结果不能直接替代系统级寿命证据。"),
            ("大口径、曲面、均匀性与成本", "综合装夹、温控、过程监控、一致性、良率和产业化成本；明确公开证据不足之处。")
        ]),
        ("共识、争议与研究空白", [
            ("跨文献共识和条件性争议", "按材料、工艺、测试和表征条件解释一致与冲突；所有关系必须连接真实 Source_ID。"),
            ("证据缺口与研究路线图", "从 Claim–Evidence Matrix 和 Literature Map 提炼标准、寿命、界面直接证据及工程放大缺口。")
        ]),
        ("结论", [
            ("材料—工艺—界面—性能综合判断", "只总结正文已建立且达到门禁的主张，保留适用条件、局限和证据强度。"),
            ("未来优先研究方向", "按证据缺口、可验证问题、所需方法和预期工程价值排序，避免空泛展望。")
        ]),
    ]

    for h1, children in sections:
        add_heading(document, h1, 1, num_id)
        for index, (h2, prompt) in enumerate(children, start=1):
            add_heading(document, h2, 2, num_id)
            add_heading(document, "核心命题、证据配置与边界", 3, num_id)
            add_prompt(document, prompt)

    document.add_page_break()
    add_heading(document, "三级标题证据配置表", 1, num_id)
    caption = document.add_paragraph("表前说明：每个三级标题至少连接一个核心命题、一个可核验来源和一个质量门禁。")
    caption.paragraph_format.space_before = Pt(4)
    caption.paragraph_format.space_after = Pt(4)
    caption.paragraph_format.keep_with_next = True
    table = document.add_table(rows=5, cols=4)
    table.style = "Table Grid"
    headers = ["三级标题", "核心命题 / Claim_ID", "Source_ID 与原文位置", "冲突、局限与图表"]
    for cell, value in zip(table.rows[0].cells, headers):
        cell.text = value
    for row in table.rows[1:]:
        row.cells[0].text = "填写已批准标题"
        row.cells[1].text = "登记命题及最低核验等级"
        row.cells[2].text = "登记来源和页码、章节、图或表"
        row.cells[3].text = "登记冲突证据、边界和追踪 ID"
    set_table_geometry(table, [1800, 2700, 2700, 2160])
    format_table_text(table, header=True)

    add_heading(document, "参考文献", 1, num_id)
    add_prompt(document, "仅纳入正文实际引用且题录已核验的来源；提交版移除内部 ID，但保留正式引文和必要版权声明。")

    core = document.core_properties
    core.title = "红外硫系玻璃基底 DLC 薄膜三级大纲与审计写作骨架"
    core.subject = f"Preset: {PRESET}; evidence-traceable review template"
    core.author = "build-optical-coating-review"
    core.keywords = "DLC, chalcogenide glass, optical coating, literature review, evidence traceability"
    return document


def audit_docx(path: Path) -> None:
    with ZipFile(path) as archive:
        document_xml = archive.read("word/document.xml").decode("utf-8")
        styles_xml = archive.read("word/styles.xml").decode("utf-8")
        numbering_xml = archive.read("word/numbering.xml").decode("utf-8")
        settings_xml = archive.read("word/settings.xml").decode("utf-8")
    checks = {
        "letter_page": 'w:w="12240"' in document_xml and 'w:h="15840"' in document_xml,
        "one_inch_margins": all(token in document_xml for token in ['w:top="1440"', 'w:right="1440"', 'w:bottom="1440"', 'w:left="1440"']),
        "table_width": 'w:tblW w:type="dxa" w:w="9360"' in document_xml or 'w:tblW w:w="9360" w:type="dxa"' in document_xml,
        "table_indent": 'w:tblInd w:w="120" w:type="dxa"' in document_xml or 'w:tblInd w:type="dxa" w:w="120"' in document_xml,
        "multilevel_numbering": 'w:multiLevelType w:val="multilevel"' in numbering_xml,
        "body_line_spacing": 'w:line="300"' in styles_xml,
        "update_fields": "w:updateFields" in settings_xml,
    }
    failed = [name for name, passed in checks.items() if not passed and name != "update_fields"]
    if failed:
        raise RuntimeError(f"DOCX preset audit failed: {failed}")


def enable_field_updates(document: Document) -> None:
    settings = document.settings._element
    update = settings.find(qn("w:updateFields"))
    if update is None:
        update = OxmlElement("w:updateFields")
        settings.append(update)
    update.set(qn("w:val"), "true")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = build_document()
    enable_field_updates(document)
    document.save(OUTPUT)
    audit_docx(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
```

<a id="module-scripts-check-distribution-parity-py"></a>
## Module: `scripts/check_distribution_parity.py`

```python
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
```

<a id="module-scripts-deduplicate-records-py"></a>
## Module: `scripts/deduplicate_records.py`

```python
from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from _common import (
    ScriptError,
    normalize_doi,
    normalize_title,
    records_from_payload,
    run_cli,
    unique_strings,
    utc_now,
    validate_against_schema,
    write_json,
)

ARRAY_FIELDS = {
    "authors", "database_sources", "materials", "substrates", "coatings", "deposition_routes",
    "interface_strategies", "optical_properties", "mechanical_properties", "environmental_properties",
    "manufacturing_properties", "characterization_methods", "themes", "intended_uses",
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Deduplicate Source Records while preserving identifiers, conflicts, and version candidates.")
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--decision-log", type=Path)
    return result


def merge_into(canonical: dict[str, Any], duplicate: dict[str, Any]) -> list[dict[str, Any]]:
    conflicts = []
    for key, value in duplicate.items():
        if key in {"source_id", "schema_version", "supersedes_source_id"}:
            continue
        if key in ARRAY_FIELDS:
            canonical[key] = unique_strings(list(canonical.get(key, [])) + list(value or []))
        elif canonical.get(key) in (None, "", "UNASSESSED", "V0", "NOT_REQUESTED", "UNSCREENED") and value not in (None, ""):
            canonical[key] = value
        elif value not in (None, "") and canonical.get(key) != value:
            conflicts.append({"field": key, "kept": canonical.get(key), "other": value})
    return conflicts


def choose_canonical(records: list[dict[str, Any]]) -> dict[str, Any]:
    return min(records, key=lambda item: (0 if normalize_doi(item.get("doi")) else 1, item["source_id"]))


def main() -> int:
    args = parser().parse_args()
    records = records_from_payload(json.loads(args.input.read_text(encoding="utf-8-sig")))
    errors = []
    ids = set()
    for index, record in enumerate(records):
        errors.extend(f"record[{index}] {item}" for item in validate_against_schema(record, "source-record.schema.json"))
        if record.get("source_id") in ids:
            errors.append(f"record[{index}] repeats Source_ID {record.get('source_id')}")
        ids.add(record.get("source_id"))
    if errors:
        raise ScriptError("Input validation failed: " + " | ".join(errors), 3)

    active = {record["source_id"]: dict(record) for record in records}
    relations: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []

    doi_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        doi = normalize_doi(record.get("doi"))
        if doi:
            doi_groups[doi].append(record)
    for doi, group in sorted(doi_groups.items()):
        if len(group) < 2:
            continue
        canonical = choose_canonical(group)
        for duplicate in sorted(group, key=lambda item: item["source_id"]):
            if duplicate["source_id"] == canonical["source_id"] or duplicate["source_id"] not in active:
                continue
            conflicts = merge_into(active[canonical["source_id"]], duplicate)
            del active[duplicate["source_id"]]
            relations.append({"from_source_id": duplicate["source_id"], "to_source_id": canonical["source_id"], "relation": "DUPLICATE_OF", "basis": f"Exact normalized DOI: {doi}"})
            decisions.append({"decision": "AUTO_MERGE", "method": "DOI_EXACT", "canonical": canonical["source_id"], "removed": duplicate["source_id"], "conflicts": conflicts})

    title_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in active.values():
        title = normalize_title(record.get("title"))
        if title:
            title_groups[title].append(record)
    for title, group in sorted(title_groups.items()):
        if len(group) < 2:
            continue
        doi_values = {normalize_doi(item.get("doi")) for item in group if normalize_doi(item.get("doi"))}
        years = {item.get("year") for item in group if item.get("year") is not None}
        if len(doi_values) > 1:
            issue = {
                "status": "MANUAL_REVIEW_REQUIRED",
                "reason": "EXACT_TITLE_DIFFERENT_DOI",
                "source_ids": sorted(item["source_id"] for item in group),
                "doi_values": sorted(doi_values),
                "normalized_title": title,
            }
            unresolved.append(issue)
            decisions.append({"decision": "KEEP_SEPARATE", **issue})
            continue
        if len(years) > 1:
            issue = {
                "status": "MANUAL_REVIEW_REQUIRED",
                "reason": "EXACT_TITLE_YEAR_CONFLICT",
                "source_ids": sorted(item["source_id"] for item in group),
                "years": sorted(years),
                "normalized_title": title,
            }
            unresolved.append(issue)
            decisions.append({"decision": "KEEP_SEPARATE", **issue})
            continue
        canonical = choose_canonical(group)
        for duplicate in sorted(group, key=lambda item: item["source_id"]):
            if duplicate["source_id"] == canonical["source_id"] or duplicate["source_id"] not in active:
                continue
            candidate = copy.deepcopy(active[canonical['source_id']])
            conflicts = merge_into(candidate, duplicate)
            if conflicts:
                unresolved.append({"status": "MANUAL_REVIEW_REQUIRED", "reason": "TITLE_MATCH_FIELD_CONFLICT", "source_ids": [canonical["source_id"], duplicate["source_id"]], "conflicts": conflicts})
                decisions.append({"decision": "KEEP_SEPARATE", "method": "TITLE_EXACT", "source_ids": [canonical["source_id"], duplicate["source_id"]], "conflicts": conflicts})
                continue
            active[canonical['source_id']] = candidate
            del active[duplicate["source_id"]]
            relations.append({"from_source_id": duplicate["source_id"], "to_source_id": canonical["source_id"], "relation": "DUPLICATE_OF", "basis": "Exact normalized title with no DOI/year conflict"})
            decisions.append({"decision": "AUTO_MERGE", "method": "TITLE_EXACT", "canonical": canonical["source_id"], "removed": duplicate["source_id"], "conflicts": []})

    for record in records:
        if record.get("supersedes_source_id"):
            relations.append({"from_source_id": record["source_id"], "to_source_id": record["supersedes_source_id"], "relation": "SUPERSEDES", "basis": "Explicit source-record version link"})

    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "records": sorted(active.values(), key=lambda item: item["source_id"]),
        "relations": relations,
        "decision_log": decisions,
        "unresolved": unresolved,
        "counts": {"input": len(records), "retained": len(active), "merged": len(records) - len(active), "manual_review": len(unresolved)},
    }
    write_json(args.output, output, overwrite=False)
    if args.decision_log:
        write_json(args.decision_log, decisions, overwrite=False)
    print(json.dumps({"status": "REVIEW_REQUIRED" if unresolved else "OK", **output["counts"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
```

<a id="module-scripts-import-records-py"></a>
## Module: `scripts/import_records.py`

```python
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from _common import (
    SCHEMA_VERSION,
    ScriptError,
    normalize_doi,
    normalize_title,
    run_cli,
    split_semicolon,
    utc_now,
    validate_against_schema,
    write_json,
)

ARRAY_FIELDS = {
    "authors",
    "database_sources",
    "materials",
    "substrates",
    "coatings",
    "deposition_routes",
    "interface_strategies",
    "optical_properties",
    "mechanical_properties",
    "environmental_properties",
    "manufacturing_properties",
    "characterization_methods",
    "themes",
    "intended_uses",
}
ALIASES = {
    "source id": "source_id",
    "source_id": "source_id",
    "title": "title",
    "article title": "title",
    "authors": "authors",
    "author": "authors",
    "year": "year",
    "publication year": "year",
    "journal": "journal",
    "publication title": "journal",
    "document type": "document_type",
    "item type": "document_type",
    "doi": "doi",
    "url": "url",
    "language": "language",
    "database sources": "database_sources",
    "database": "database_sources",
    "record version": "record_version",
    "supersedes source id": "supersedes_source_id",
    "verification level": "verification_level",
    "verification date": "verification_date",
    "full text status": "full_text_status",
    "screening decision": "screening_decision",
    "screening reason": "screening_reason",
    "materials": "materials",
    "substrates": "substrates",
    "coatings": "coatings",
    "deposition routes": "deposition_routes",
    "interface strategies": "interface_strategies",
    "optical properties": "optical_properties",
    "mechanical properties": "mechanical_properties",
    "environmental properties": "environmental_properties",
    "manufacturing properties": "manufacturing_properties",
    "characterization methods": "characterization_methods",
    "themes": "themes",
    "research stage": "research_stage",
    "intended uses": "intended_uses",
    "evidence strength": "evidence_strength",
    "notes": "notes",
}
DOCUMENT_TYPES = {
    "journalarticle": "JOURNAL_ARTICLE",
    "journal article": "JOURNAL_ARTICLE",
    "article": "JOURNAL_ARTICLE",
    "jour": "JOURNAL_ARTICLE",
    "review": "REVIEW",
    "conferencepaper": "CONFERENCE_PAPER",
    "conference paper": "CONFERENCE_PAPER",
    "conf": "CONFERENCE_PAPER",
    "bookchapter": "BOOK_CHAPTER",
    "book chapter": "BOOK_CHAPTER",
    "standard": "STANDARD",
    "patent": "PATENT",
    "thesis": "THESIS",
    "preprint": "PREPRINT",
    "report": "REPORT",
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Import bibliographic exports into Schema-conformant Source Records.")
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--format", choices=["csv", "tsv", "xlsx", "json", "ris", "bibtex", "endnote-xml"])
    result.add_argument("--sheet", help="XLSX sheet name; defaults to Source Registry, Master Literature, or the active sheet")
    result.add_argument("--database", help="Source database name recorded on every imported record")
    result.add_argument("--query-id", help="Executed query identifier recorded in notes")
    result.add_argument("--log", type=Path, help="Import log path; defaults beside output")
    return result


def clean_header(value: Any) -> str:
    text = re.sub(r"[_\-]+", " ", str(value or "").strip().casefold())
    return " ".join(text.split())


def canonical_row(row: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in row.items():
        canonical = ALIASES.get(clean_header(key), clean_header(key).replace(" ", "_"))
        result[canonical] = value
    return result


def read_delimited(path: Path, delimiter: str) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter=delimiter)]


def read_xlsx(path: Path, sheet_name: str | None) -> list[dict[str, Any]]:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise ScriptError("openpyxl is required for XLSX imports", 2) from exc
    workbook = load_workbook(path, read_only=True, data_only=True)
    candidates = [sheet_name] if sheet_name else ["Source Registry", "Master Literature"]
    worksheet = next((workbook[name] for name in candidates if name and name in workbook.sheetnames), workbook.active)
    rows = worksheet.iter_rows(values_only=True)
    try:
        headers = [str(value or "").strip() for value in next(rows)]
    except StopIteration:
        return []
    return [dict(zip(headers, values)) for values in rows if any(value not in (None, "") for value in values)]


def read_ris(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    current: dict[str, list[str]] = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = re.match(r"^([A-Z0-9]{2})\s*-\s*(.*)$", line)
        if not match:
            continue
        tag, value = match.groups()
        if tag == "ER":
            records.append(
                {
                    "title": (current.get("TI") or current.get("T1") or [None])[0],
                    "authors": current.get("AU") or current.get("A1") or [],
                    "year": (current.get("PY") or current.get("Y1") or [None])[0],
                    "journal": (current.get("JO") or current.get("JF") or current.get("T2") or [None])[0],
                    "document_type": (current.get("TY") or [None])[0],
                    "doi": (current.get("DO") or [None])[0],
                    "url": (current.get("UR") or [None])[0],
                }
            )
            current = {}
        else:
            current.setdefault(tag, []).append(value.strip())
    return records


def read_bibtex(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8-sig")
    starts = list(re.finditer(r"@(\w+)\s*\{", text))
    records: list[dict[str, Any]] = []
    for index, match in enumerate(starts):
        block = text[match.end() : starts[index + 1].start() if index + 1 < len(starts) else len(text)]
        fields = {}
        block = re.sub(r',\s*(?=\w+\s*=)', '\n', block)
        for field in re.finditer(r"(?ms)^\s*(\w+)\s*=\s*(?:\{(.*?)\}|\"(.*?)\")\s*,?", block):
            fields[field.group(1).casefold()] = (field.group(2) if field.group(2) is not None else field.group(3)).strip()
        records.append(
            {
                "title": fields.get("title"),
                "authors": re.split(r"\s+and\s+", fields.get("author", ""), flags=re.IGNORECASE),
                "year": fields.get("year"),
                "journal": fields.get("journal") or fields.get("booktitle"),
                "document_type": match.group(1),
                "doi": fields.get("doi"),
                "url": fields.get("url"),
            }
        )
    return records


def first_text(element: ET.Element, paths: list[str]) -> str | None:
    for path in paths:
        found = element.find(path)
        if found is not None and found.text:
            return found.text.strip()
    return None


def read_endnote_xml(path: Path) -> list[dict[str, Any]]:
    root = ET.parse(path).getroot()
    records = []
    for record in root.findall(".//record"):
        authors = [item.text.strip() for item in record.findall(".//contributors/authors/author") if item.text]
        records.append(
            {
                "title": first_text(record, [".//titles/title", ".//title"]),
                "authors": authors,
                "year": first_text(record, [".//dates/year", ".//year"]),
                "journal": first_text(record, [".//periodical/full-title", ".//secondary-title"]),
                "document_type": first_text(record, [".//ref-type"]),
                "doi": first_text(record, [".//electronic-resource-num", ".//doi"]),
                "url": first_text(record, [".//urls/related-urls/url", ".//url"]),
            }
        )
    return records


def read_json_records(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        payload = payload["records"]
    if not isinstance(payload, list):
        raise ScriptError("JSON import must be an array or contain a records array", 2)
    result = []
    for item in payload:
        data = item.get("data", item) if isinstance(item, dict) else None
        if not isinstance(data, dict):
            raise ScriptError("Every JSON record must be an object", 2)
        if "creators" in data and "authors" not in data:
            authors = []
            for creator in data.get("creators", []):
                name = creator.get("name") or " ".join(filter(None, [creator.get("firstName"), creator.get("lastName")]))
                if name:
                    authors.append(name)
            data = {**data, "authors": authors}
        result.append(data)
    return result


def parse_year(value: Any) -> int | None:
    if value in (None, ""):
        return None
    match = re.search(r"(?:16|17|18|19|20|21)\d{2}", str(value))
    return int(match.group(0)) if match else None


def document_type(value: Any) -> str:
    text = str(value or "").strip()
    if text in {
        "JOURNAL_ARTICLE", "REVIEW", "CONFERENCE_PAPER", "BOOK_CHAPTER", "STANDARD",
        "PATENT", "THESIS", "PREPRINT", "REPORT", "OTHER",
    }:
        return text
    return DOCUMENT_TYPES.get(text.casefold(), "OTHER")


def stable_source_id(row: dict[str, Any]) -> str:
    if row.get("source_id"):
        return str(row["source_id"]).strip().upper()
    identity = normalize_doi(row.get("doi")) or "|".join(
        [normalize_title(row.get("title")), str(parse_year(row.get("year")) or ""), ";".join(split_semicolon(row.get("authors")))]
    )
    if not identity.strip("|"):
        raise ScriptError("Cannot assign Source_ID without a title, DOI, year, or author", 3)
    return "SRC-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12].upper()


def normalize_record(raw: dict[str, Any], database: str | None, query_id: str | None) -> dict[str, Any]:
    row = canonical_row(raw)
    notes = str(row.get("notes") or "").strip() or None
    if query_id:
        notes = "; ".join(filter(None, [notes, f"query_id={query_id}"]))
    result = {
        "schema_version": SCHEMA_VERSION,
        "source_id": stable_source_id(row),
        "title": str(row.get("title") or "").strip() or None,
        "authors": split_semicolon(row.get("authors")),
        "year": parse_year(row.get("year")),
        "journal": str(row.get("journal") or "").strip() or None,
        "document_type": document_type(row.get("document_type")),
        "doi": normalize_doi(row.get("doi")),
        "url": str(row.get("url") or "").strip() or None,
        "language": str(row.get("language") or "").strip() or None,
        "database_sources": split_semicolon(row.get("database_sources")),
        "record_version": str(row.get("record_version") or "1").strip(),
        "supersedes_source_id": str(row.get("supersedes_source_id") or "").strip() or None,
        "verification_level": str(row.get("verification_level") or "V0").strip().upper(),
        "verification_date": str(row.get("verification_date") or "").strip() or None,
        "full_text_status": str(row.get("full_text_status") or "NOT_REQUESTED").strip().upper(),
        "screening_decision": str(row.get("screening_decision") or "UNSCREENED").strip().upper(),
        "screening_reason": str(row.get("screening_reason") or "").strip() or None,
        "materials": split_semicolon(row.get("materials")),
        "substrates": split_semicolon(row.get("substrates")),
        "coatings": split_semicolon(row.get("coatings")),
        "deposition_routes": split_semicolon(row.get("deposition_routes")),
        "interface_strategies": split_semicolon(row.get("interface_strategies")),
        "optical_properties": split_semicolon(row.get("optical_properties")),
        "mechanical_properties": split_semicolon(row.get("mechanical_properties")),
        "environmental_properties": split_semicolon(row.get("environmental_properties")),
        "manufacturing_properties": split_semicolon(row.get("manufacturing_properties")),
        "characterization_methods": split_semicolon(row.get("characterization_methods")),
        "themes": split_semicolon(row.get("themes")),
        "research_stage": str(row.get("research_stage") or "").strip() or None,
        "intended_uses": [value.upper() for value in split_semicolon(row.get("intended_uses"))],
        "evidence_strength": str(row.get("evidence_strength") or "UNASSESSED").strip().upper(),
        "notes": notes,
    }
    if database and database not in result["database_sources"]:
        result["database_sources"].append(database)
    return result


def detect_format(path: Path) -> str:
    suffix = path.suffix.casefold()
    return {
        ".csv": "csv", ".tsv": "tsv", ".xlsx": "xlsx", ".json": "json",
        ".ris": "ris", ".bib": "bibtex", ".xml": "endnote-xml",
    }.get(suffix) or ""


def main() -> int:
    args = parser().parse_args()
    path = args.input.resolve()
    if not path.is_file():
        raise ScriptError(f"Input file does not exist: {path}", 2)
    format_name = args.format or detect_format(path)
    readers = {
        "csv": lambda: read_delimited(path, ","),
        "tsv": lambda: read_delimited(path, "\t"),
        "xlsx": lambda: read_xlsx(path, args.sheet),
        "json": lambda: read_json_records(path),
        "ris": lambda: read_ris(path),
        "bibtex": lambda: read_bibtex(path),
        "endnote-xml": lambda: read_endnote_xml(path),
    }
    if format_name not in readers:
        raise ScriptError("Cannot detect input format; use --format", 2)
    raw_records = readers[format_name]()
    records = [normalize_record(row, args.database, args.query_id) for row in raw_records]
    id_counts: dict[str, int] = {}
    for raw_record, record in zip(raw_records, records):
        if canonical_row(raw_record).get('source_id'):
            continue
        base_id = record['source_id']
        id_counts[base_id] = id_counts.get(base_id, 0) + 1
        if id_counts[base_id] > 1:
            record['source_id'] = f'{base_id}-R{id_counts[base_id]}'
    errors = []
    seen_ids = set()
    for index, record in enumerate(records):
        if record["source_id"] in seen_ids:
            errors.append(f"record[{index}] duplicates Source_ID {record['source_id']}; run deduplicate_records.py after assigning distinct raw IDs")
        seen_ids.add(record["source_id"])
        errors.extend(f"record[{index}] {item}" for item in validate_against_schema(record, "source-record.schema.json"))
    if errors:
        raise ScriptError("Import validation failed: " + " | ".join(errors), 3)
    write_json(args.output, records, overwrite=False)
    log_path = args.log or args.output.with_suffix(".import-log.json")
    log = {
        "status": "OK",
        "input": str(path),
        "input_format": format_name,
        "database": args.database,
        "query_id": args.query_id,
        "imported_records": len(records),
        "output": str(args.output.resolve()),
        "run_at": utc_now(),
        "limitations": ["No external metadata was inferred or verified during import."],
    }
    write_json(log_path, log, overwrite=False)
    print(json.dumps(log, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
```

<a id="module-scripts-init-project-py"></a>
## Module: `scripts/init_project.py`

```python
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
```

<a id="module-scripts-transition-state-py"></a>
## Module: `scripts/transition_state.py`

```python
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
```

<a id="module-scripts-validate-metadata-py"></a>
## Module: `scripts/validate_metadata.py`

```python
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

from _common import (
    EXIT_EXTERNAL,
    ScriptError,
    normalize_doi,
    normalize_title,
    records_from_payload,
    run_cli,
    utc_now,
    validate_against_schema,
    write_json,
)

DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Validate source metadata locally and optionally cross-check DOI records with Crossref.")
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--crossref", action="store_true", help="Opt in to lawful, rate-limited Crossref DOI checks")
    result.add_argument("--cache", type=Path, default=Path(".metadata-cache"))
    result.add_argument("--rate-limit", type=float, default=1.0, help="Minimum seconds between network requests")
    result.add_argument("--timeout", type=float, default=15.0)
    result.add_argument("--mailto", help="Contact email for Crossref polite identification; never written into project output")
    result.add_argument("--max-records", type=int, help="Bound external checks")
    return result


def cache_file(directory: Path, doi: str) -> Path:
    return directory / (hashlib.sha256(doi.encode("utf-8")).hexdigest() + ".json")


def crossref_lookup(doi: str, args: argparse.Namespace) -> tuple[dict | None, str, str | None]:
    cache = cache_file(args.cache.resolve(), doi)
    if cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8")), "CACHE_HIT", None
    query = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{query}"
    agent = "build-optical-coating-review/1.0"
    if args.mailto:
        agent += f" (mailto:{args.mailto})"
    request = urllib.request.Request(url, headers={"User-Agent": agent, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, "EXTERNAL_CHECK_FAILED", str(exc)
    cache.parent.mkdir(parents=True, exist_ok=True)
    write_json(cache, payload, overwrite=False)
    return payload, "NETWORK_OK", None


def crossref_year(message: dict) -> int | None:
    for field in ["published-print", "published-online", "issued", "created"]:
        parts = message.get(field, {}).get("date-parts", [])
        if parts and parts[0]:
            return int(parts[0][0])
    return None


def main() -> int:
    args = parser().parse_args()
    if args.rate_limit < 0.5:
        raise ScriptError("--rate-limit must be at least 0.5 seconds", 2)
    records = records_from_payload(json.loads(args.input.read_text(encoding="utf-8-sig")))
    results = []
    external_failures = 0
    network_count = 0
    last_request = 0.0
    for index, record in enumerate(records):
        local_errors = validate_against_schema(record, "source-record.schema.json")
        doi = normalize_doi(record.get("doi"))
        if doi and not DOI_PATTERN.match(doi):
            local_errors.append("doi: invalid DOI syntax")
        result = {
            "source_id": record.get("source_id"),
            "doi": doi,
            "local_status": "INVALID" if local_errors else "VALID",
            "local_errors": local_errors,
            "external_status": "NOT_REQUESTED",
            "external_error": None,
            "title_similarity": None,
            "year_match": None,
            "crossref_title": None,
            "crossref_year": None,
            "checked_at": utc_now(),
        }
        if args.crossref:
            if not doi:
                result["external_status"] = "NOT_CHECKED_NO_DOI"
            elif args.max_records is not None and network_count >= args.max_records:
                result["external_status"] = "NOT_CHECKED_LIMIT_REACHED"
            else:
                cache_exists = cache_file(args.cache.resolve(), doi).is_file()
                if not cache_exists:
                    elapsed = time.monotonic() - last_request
                    if elapsed < args.rate_limit:
                        time.sleep(args.rate_limit - elapsed)
                    last_request = time.monotonic()
                    network_count += 1
                payload, status, error = crossref_lookup(doi, args)
                result["external_status"] = status
                result["external_error"] = error
                if payload is None:
                    external_failures += 1
                else:
                    message = payload.get("message", {})
                    title_values = message.get("title") or []
                    title = title_values[0] if title_values else None
                    year = crossref_year(message)
                    result["crossref_title"] = title
                    result["crossref_year"] = year
                    if title and record.get("title"):
                        result["title_similarity"] = round(
                            SequenceMatcher(None, normalize_title(record["title"]), normalize_title(title)).ratio(), 4
                        )
                    if year and record.get("year"):
                        result["year_match"] = year == record["year"]
                    if result["title_similarity"] is not None and result["title_similarity"] < 0.85 or result["year_match"] is False:
                        result["external_status"] = "METADATA_CONFLICT"
                    else:
                        result["external_status"] = "VERIFIED_MATCH"
        results.append(result)

    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "network_enabled": args.crossref,
        "legal_boundary": "Crossref public API only; no authentication, CAPTCHA, subscription, or access-control bypass.",
        "results": results,
        "counts": {
            "records": len(records),
            "local_invalid": sum(item["local_status"] == "INVALID" for item in results),
            "external_failures": external_failures,
            "metadata_conflicts": sum(item["external_status"] == "METADATA_CONFLICT" for item in results),
        },
    }
    write_json(args.output, output, overwrite=False)
    print(json.dumps({"status": "EXTERNAL_CHECK_FAILED" if external_failures else "OK", **output["counts"]}, ensure_ascii=False, indent=2))
    return EXIT_EXTERNAL if external_failures else 0


if __name__ == "__main__":
    run_cli(main)
```

<a id="module-scripts-validate-project-py"></a>
## Module: `scripts/validate_project.py`

```python
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
```

<a id="module-scripts-version-output-py"></a>
## Module: `scripts/version_output.py`

```python
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import (
    ScriptError,
    append_jsonl_atomic,
    atomic_write_bytes,
    run_cli,
    sha256_file,
    utc_now,
)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Create an immutable, hash-recorded output version without overwriting prior files.")
    result.add_argument("source", type=Path)
    result.add_argument("output_directory", type=Path)
    result.add_argument("--version", help="Explicit version label such as v003; otherwise choose the next numeric version")
    result.add_argument("--role", default="task_output")
    result.add_argument("--note")
    return result


def next_version(directory: Path, stem: str, suffix: str) -> str:
    pattern = re.compile(rf"^{re.escape(stem)}\.v(\d{{3,}}){re.escape(suffix)}$")
    numbers = []
    if directory.exists():
        for item in directory.iterdir():
            match = pattern.match(item.name)
            if match:
                numbers.append(int(match.group(1)))
    return f"v{max(numbers, default=0) + 1:03d}"


def main() -> int:
    args = parser().parse_args()
    source = args.source.resolve()
    if not source.is_file():
        raise ScriptError(f"Source file does not exist: {source}", 2)
    output_directory = args.output_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    version = args.version or next_version(output_directory, source.stem, source.suffix)
    if not re.fullmatch(r"v[0-9]{3,}", version):
        raise ScriptError("Version must match vNNN with at least three digits", 2)
    target = output_directory / f"{source.stem}.{version}{source.suffix}"
    if target.exists():
        raise ScriptError(f"Version already exists: {target}", 4)
    data = source.read_bytes()
    atomic_write_bytes(target, data, overwrite=False)
    entry = {
        "version": version,
        "path": target.name,
        "role": args.role,
        "sha256": sha256_file(target),
        "source_path": str(source),
        "source_sha256": sha256_file(source),
        "created_at": utc_now(),
        "note": args.note,
    }
    append_jsonl_atomic(output_directory / "version_manifest.jsonl", entry)
    print(json.dumps({"status": "OK", **entry}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    run_cli(main)
```

<a id="module-assets-templates-evidence-and-claims-xlsx"></a>
## Module: `assets/templates/evidence_and_claims.xlsx`

Binary asset: `assets/templates/evidence_and_claims.xlsx`; SHA-256 `402de1de5091ed2569f000ba99c0f7e6c9bd47b6daeddee38d53c2157a667d6b`; size `9785` bytes.

<a id="module-assets-templates-evidence-card-md"></a>
## Module: `assets/templates/evidence_card.md`

---
schema_version: 1.0.0
evidence_card_id: null
source_id: null
verification_level: V0
evidence_strength: UNASSESSED
human_status: UNREVIEWED
---

### 证据卡

#### 引文与研究问题

记录规范引文、Source_ID，以及该文献对当前研究问题的直接贡献。

#### 材料与工艺上下文

记录材料体系、基底、膜层、制备方法、界面策略、工艺条件和表征方法。

#### 关键结果

每条结果包含指标、值、单位、条件和原文位置。无法定位全文位置的结果不得标为 V4。

#### 解释分层

分别记录实验结果、作者解释、作者推测和 Skill 综合判断。

#### 主张与写作用途

登记支持的 Claim_ID、比较对象、适用章节、图表用途及证据关系。

#### 局限与引用风险

记录适用条件、相互冲突的证据、二次引用风险、数据换算风险和需人工复核项。

<a id="module-assets-templates-literature-map-xlsx"></a>
## Module: `assets/templates/literature_map.xlsx`

Binary asset: `assets/templates/literature_map.xlsx`; SHA-256 `5e0121d66c0d01d7f2e6ad2282da2ff08b5ba7757f29a2b67ea08564da8bbd00`; size `8427` bytes.

<a id="module-assets-templates-literature-registry-xlsx"></a>
## Module: `assets/templates/literature_registry.xlsx`

Binary asset: `assets/templates/literature_registry.xlsx`; SHA-256 `6a0f81caa735a184fcc098c7c76bc7987249f99759ebf33813aa4f0e57ff69f1`; size `9404` bytes.

<a id="module-assets-templates-outline-review-report-md"></a>
## Module: `assets/templates/outline_review_report.md`

### 三级大纲反馈报告

#### 审查对象与版本

记录大纲文件、版本、审批状态和关联研究路线图。

#### 范围与论证递进

检查每个三级标题是否回答明确问题，章节之间是否形成材料—工艺—结构—性能—应用的递进。

#### 章节平衡与证据密度

记录章节篇幅、核心 Source_ID 数量、Claim_ID 数量、冲突证据和核验等级分布。

#### 作者流水账风险

标出按论文逐篇罗列而缺少跨文献比较的部分，并给出综合单元。

#### 图表与研究空白

核查每个关键图表的证据来源和追踪 ID；核查研究空白是否来自证据矩阵与文献地图。

#### 关键问题关闭条件

逐项记录问题、严重度、影响章节、所需修改、责任人、状态和复核结果。关键问题关闭前 Task 20 不得批准。

<a id="module-assets-templates-preflight-and-roadmap-xlsx"></a>
## Module: `assets/templates/preflight_and_roadmap.xlsx`

Binary asset: `assets/templates/preflight_and_roadmap.xlsx`; SHA-256 `b2097d8cc2a1ef21c8e03c17bf2071183b12666f42c86a4c636ed6790971797f`; size `8707` bytes.

<a id="module-assets-templates-project-diagnosis-md"></a>
## Module: `assets/templates/project_diagnosis.md`

### 项目诊断

#### 问题定义

记录研究对象、核心问题、综述类型、使用场景、时间范围和语言范围。

#### 现有资源与数据库能力

汇总文献、PDF、实验材料、机构权限、数据库能力等级和自动化限制。

#### 题目风险与已有综述重合

基于真实检索结果说明范围过宽、过窄、概念混淆和与既有综述重合的风险。

#### 创新机会与证据可得性

比较至少三个候选定位，分别说明可验证的差异化、所需证据和证据缺口。

#### 目标期刊层级

记录候选期刊层级、范围适配及仍需联网核验的动态政策。

#### 阻断项与推荐结论

列出阻断项、责任人、解除条件，并给出带边界的推荐题目与后续路线。

<a id="module-assets-templates-project-manifest-json"></a>
## Module: `assets/templates/project_manifest.json`

```json
{
  "schema_version": "1.0.0",
  "project_id": null,
  "project_title": null,
  "review_type": "UNDECIDED",
  "language": null,
  "created_at": null,
  "updated_at": null,
  "state_file": "project_state.yaml",
  "task_register": "task_register.xlsx",
  "decision_log": "decision_log.md",
  "risk_register": "risk_register.xlsx",
  "manual_checklist": "manual_checklist.xlsx",
  "research_roadmap": "research_roadmap.xlsx",
  "schema_directory": "references",
  "directories": {
    "working": "working",
    "outputs": "outputs",
    "qa": "qa",
    "logs": "logs"
  },
  "approved_outputs": [],
  "file_hashes": {}
}
```

<a id="module-assets-templates-project-state-yaml"></a>
## Module: `assets/templates/project_state.yaml`

```yaml
schema_version: 1.0.0
project_id: null
project_title: null
review_type: UNDECIDED
execution_mode: single_task_confirmation
project_status: NOT_STARTED
current_stage: STEP_00
current_task: STEP-00
current_subtask: null
current_chapter: null
paused: false
pause_reason: null
tasks:
  - {task_id: STEP-00, status: NOT_STARTED, prerequisites: [], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-01, status: NOT_STARTED, prerequisites: [STEP-00], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-02, status: NOT_STARTED, prerequisites: [TASK-01], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-03, status: NOT_STARTED, prerequisites: [TASK-02], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-04, status: NOT_STARTED, prerequisites: [TASK-03], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-05, status: NOT_STARTED, prerequisites: [TASK-04], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-06, status: NOT_STARTED, prerequisites: [TASK-05], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-07, status: NOT_STARTED, prerequisites: [TASK-06], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-08, status: NOT_STARTED, prerequisites: [TASK-07], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-09, status: NOT_STARTED, prerequisites: [TASK-08], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-10, status: NOT_STARTED, prerequisites: [TASK-09], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-11, status: NOT_STARTED, prerequisites: [TASK-10], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-12, status: NOT_STARTED, prerequisites: [TASK-11], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-13, status: NOT_STARTED, prerequisites: [TASK-12], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-14, status: NOT_STARTED, prerequisites: [TASK-13], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-15, status: NOT_STARTED, prerequisites: [TASK-14], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-16, status: NOT_STARTED, prerequisites: [TASK-15], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-17, status: NOT_STARTED, prerequisites: [TASK-16], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-18, status: NOT_STARTED, prerequisites: [TASK-17], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-19, status: NOT_STARTED, prerequisites: [TASK-18], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-20, status: NOT_STARTED, prerequisites: [TASK-19], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
task_21_subtasks:
  - {task_id: TASK-21A, status: NOT_STARTED, prerequisites: [TASK-20], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21B, status: NOT_STARTED, prerequisites: [TASK-21A], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21C, status: NOT_STARTED, prerequisites: [TASK-21B], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21D, status: NOT_STARTED, prerequisites: [TASK-21C], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21E, status: NOT_STARTED, prerequisites: [TASK-21D], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21F, status: NOT_STARTED, prerequisites: [TASK-21E], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21G, status: NOT_STARTED, prerequisites: [TASK-21F], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
  - {task_id: TASK-21H, status: NOT_STARTED, prerequisites: [TASK-21G], input_paths: [], output_paths: [], quality_gate_passed: null, approval: null, blocker_id: null, result_id: null, updated_at: null}
approved_task: null
last_approved_output: null
risk_ids: []
manual_check_ids: []
current_inputs: []
last_user_decision: null
created_at: null
updated_at: null
```

<a id="module-assets-templates-prompt-library-md"></a>
## Module: `assets/templates/prompt_library.md`

---
schema_version: 1.0.0
project_id: null
generated_after_task: TASK-05
last_updated: null
---

### 项目化提示词库

每条提示使用以下字段：`prompt_id`、`phase`、`intent`、`when_to_use`、`required_inputs`、`tool_or_database_prerequisites`、`prompt_text`、`expected_outputs`、`stop_conditions`、`quality_checks`。

#### 选题诊断

基于已批准的研究边界与已有综述矩阵，比较候选题的新颖性、证据可得性和目标期刊适配。缺少真实检索结果时停止，不生成确定性的新颖性结论。

#### 术语与检索式

围绕基底、膜层、工艺、界面、光学、机械、环境和应用建立概念组，分别生成宽泛、适中和精准检索式，并说明数据库语法差异和噪声来源。

#### 筛选解释

根据已批准的纳入排除标准判断题名、摘要或全文；输出决定、理由、不确定性和所需全文信息。边界文献不得自动永久排除。

#### 全文精读与证据卡

区分结果、作者解释、推测和 Skill 判断；为所有定量结果记录条件、单位和原文位置，并生成 Source_ID、Claim_ID 与 Evidence_Card_ID 关联。

#### 争议、共识与研究空白

按材料、工艺、测试条件和方法差异解释不一致结果。研究空白必须来自证据结构，不能仅由“研究较少”推断。

#### 大纲审查与段落写作

检查论证递进、章节平衡、证据密度和图表支撑。段落按“中心观点—主要证据—跨研究比较—差异原因—适用条件—局限—阶段性判断”组织。

#### 引用核查、期刊匹配与审稿回复

核对 DOI、事实支持关系、因果强度、无来源数字、期刊动态政策和逐条审稿意见。动态信息必须记录核验日期和来源。

<a id="module-assets-templates-reading-note-md"></a>
## Module: `assets/templates/reading_note.md`

---
schema_version: 1.0.0
source_id: null
verification_level: V0
human_status: UNREVIEWED
---

### 结构化精读笔记

#### 题录与版本

记录题名、作者、年份、期刊、DOI、版本关系、数据库来源、全文文件与 Source_ID。

#### 研究问题与对象

区分论文明确提出的问题与本综述使用该论文回答的问题。

#### 材料—基底—膜层—界面

记录材料体系、硫系玻璃组成、DLC 类型、过渡层或梯度层，以及样品前处理。

#### 制备方法与条件

记录沉积方法、设备、气氛、功率、偏压、温度、时间、膜厚和关键工艺窗口。缺失字段明确写“原文未报告”。

#### 表征与结果

逐项记录表征方法、指标、数值、单位、试验条件和原文页码、章节、图或表。

#### 作者解释

只记录作者明确给出的解释，并保留限定语。

#### Skill 判断

将跨文献推断、方法学评价和可能解释与作者解释分开；未经证据支持不得升级为机制事实。

#### 局限与适用边界

记录样本、方法、对照、统计、外推范围、工程规模和未解决问题。

#### 可支持的主张与用途

列出 Claim_ID、支持或冲突关系、计划章节、比较用途、图表用途和最低核验等级。

#### 人工复核

记录需核对的定量值、机制表述、Raman 拟合解释、版权或元数据冲突。

<a id="module-assets-templates-review-outline-template-docx"></a>
## Module: `assets/templates/review_outline_template.docx`

Binary asset: `assets/templates/review_outline_template.docx`; SHA-256 `32bd2c36a9b72eeead96b79e1356d60309e295711d52746bfee0054f2cb73cd1`; size `42087` bytes.

<a id="module-assets-templates-revision-recommendations-md"></a>
## Module: `assets/templates/revision_recommendations.md`

### 修改建议登记

| 建议 ID | 优先级 | 问题位置 | 问题类型 | 证据 | 建议修改 | 影响章节 | 处理状态 | 复核结果 |
|---|---|---|---|---|---|---|---|---|

处理状态使用 `OPEN`、`IN_PROGRESS`、`RESOLVED`、`WONT_FIX_WITH_RATIONALE`。证据栏关联 Source_ID、Claim_ID、审计记录或期刊政策来源；涉及事实与定量值的建议不得仅凭语言偏好关闭。

<a id="module-assets-templates-stage-report-md"></a>
## Module: `assets/templates/stage_report.md`

---
schema_version: 1.0.0
project_id: null
task_id: STEP-00
status: REVIEW_REQUIRED
report_date: null
---

### 阶段报告

#### 当前任务

记录任务名称、目标、当前状态和本次执行边界。

#### 输入

登记输入文件、版本、哈希和用户正式决策。

#### 执行过程

概述已执行步骤、调用的工具与数据库，以及任何人工操作。

#### 成果与文件

列出新生成或更新的文件、版本、用途和审计状态。批准文件不得覆盖。

#### 文献与证据更新

列出新增或变更的 Source_ID、Claim_ID、Evidence_Card_ID、图表追踪 ID 和核验等级。

#### 质量检查

逐项记录检查名称、`PASS`、`FAIL`、`NOT_APPLICABLE` 或 `MANUAL_CHECK_REQUIRED`、证据与结果。

#### 风险与待人工核查

记录风险 ID、影响、缓解措施、责任人和复核时点；记录人工核查 ID 与触发原因。

#### 待补材料

列出继续工作所需的文件、访问权限、实验信息或用户判断。没有待补材料时写“无”。

#### 下一步

说明下一任务、前置条件和预计输出，但在当前门禁获批前不执行。

#### 用户决策

等待用户明确回复“确认通过”、提出修改、补充资料，或明确要求跳过门禁并记录风险。

<a id="module-assets-templates-task-status-yaml"></a>
## Module: `assets/templates/task_status.yaml`

```yaml
schema_version: 1.0.0
result_id: null
project_id: null
task_id: STEP-00
status: NOT_STARTED
started_at: null
completed_at: null
inputs: []
outputs: []
quality_gate:
  gate_id: null
  passed: null
  checks: []
  checked_at: null
evidence_updates: []
risk_ids: []
manual_check_ids: []
approval: null
```

## Source Manifest

```json
[
  {
    "path": "SKILL.md",
    "sha256": "8b6bda8d402356a46e8f86114ce73570a7f20e4a048365044cde6419d7621359",
    "size": 9952
  },
  {
    "path": "agents/openai.yaml",
    "sha256": "8406fabf3f42c1909c07d3cad5db6691d49e312298090b0df70e7aa33c1b2c09",
    "size": 315
  },
  {
    "path": "references/claim.schema.json",
    "sha256": "e5217d39761a1067e9c8673406cb4e3f830d35fb0c506914bf1e5d332b28ccce",
    "size": 2296
  },
  {
    "path": "references/common.schema.json",
    "sha256": "27fdfb4da890bcb406796fa3af56c8d5ea91a16e7abfa88ceff2d86f468d2b70",
    "size": 1954
  },
  {
    "path": "references/database-access-and-search.md",
    "sha256": "c42e083fbcf0d774ae84db590d54493307787d1090e182e0c2b353f6cc6f59fe",
    "size": 5069
  },
  {
    "path": "references/evidence-card.schema.json",
    "sha256": "9abd3c33490be4b6a280195829840165eb445902767eac5e7e9f318891fa1474",
    "size": 2858
  },
  {
    "path": "references/figure-table-traceability.schema.json",
    "sha256": "7f338d6adf9404cfc557ca97bba1163fb93681b7d8e6a994b52356f14f752dae",
    "size": 1672
  },
  {
    "path": "references/literature-map.schema.json",
    "sha256": "44e85a8686a8e81c95a8bf49c261efa7ab4cdaca8fcf65093d136785e2c28d45",
    "size": 4056
  },
  {
    "path": "references/optical-coating-integrated.md",
    "sha256": "e31061758c85824c67e8a8741b88b839757f70231c193809d7614a52b02358b3",
    "size": 13302
  },
  {
    "path": "references/project-state.schema.json",
    "sha256": "cf306ab9b3c9029dd4def016fa844c1f6c465657fc12b697886cf7761d135016",
    "size": 3362
  },
  {
    "path": "references/prompt-library-core.md",
    "sha256": "99feef0270b432f5c21ec8882deb37c3c2d8a4b847a866c2b2739f7fae5fb53f",
    "size": 19265
  },
  {
    "path": "references/roadmap-item.schema.json",
    "sha256": "726a76e4f7462227da4389be03d1ff351a70c1256e0afbb9dc564ac3a7639b4e",
    "size": 1366
  },
  {
    "path": "references/schema-and-template-map.md",
    "sha256": "b9674909768ed09d307e4488f6d97e837ad8b0f00a2a435f287076cc7e173282",
    "size": 1953
  },
  {
    "path": "references/source-record.schema.json",
    "sha256": "a906441e83485bd7ab7478ea8bbb83c96b74a937fa0807ede82c3adb97ffd2f8",
    "size": 3530
  },
  {
    "path": "references/state-machine.md",
    "sha256": "0d2201947a4f9f1550f813edf5aacadea865f394f8ab4f0f7b097406d3ad15ff",
    "size": 7045
  },
  {
    "path": "references/systematic-review-branch.md",
    "sha256": "5c95247f07bae4877c12d76d93363bbf5aea12c2fafc5e457820c83c96ebc1d1",
    "size": 3839
  },
  {
    "path": "references/task-00-preflight.md",
    "sha256": "d52fdbe073517b597a404a50e9849f38dd44a8d6e8bd27f50887b273be954936",
    "size": 3118
  },
  {
    "path": "references/task-01-project-initialization.md",
    "sha256": "43ad30eef548bb0549b90ad1706325e4cd2a52861398c40dadd177a8b4a87275",
    "size": 2522
  },
  {
    "path": "references/task-02-review-type.md",
    "sha256": "d6f0d194a673f002ec7d80548aac958871ef0ff85f1b0ddc49e966d614ba0b14",
    "size": 2389
  },
  {
    "path": "references/task-03-scope-and-questions.md",
    "sha256": "c4eb64f040c2d0536c018b33bb981b18f1682c295f397eb256c3577f211cc85f",
    "size": 2291
  },
  {
    "path": "references/task-04-existing-reviews.md",
    "sha256": "71cf4a4bc2c76128ffad15097587a00de2ed32d4dbd6494de21b31210156b975",
    "size": 2442
  },
  {
    "path": "references/task-05-topic-evaluation.md",
    "sha256": "47f416f9e9ab97ebf42ebe7c510a63b2797ef1f437be9f5baa4c003b120e3789",
    "size": 2490
  },
  {
    "path": "references/task-06-terminology.md",
    "sha256": "ab6e524832ae90bdcf062fbddd26c097e9928c630dd6e5bc999b7ee861f6c4d9",
    "size": 2387
  },
  {
    "path": "references/task-07-concept-groups.md",
    "sha256": "d8deab67ca36c68d104d8807721617300e626b192f48024ee5264fbe62de8207",
    "size": 2194
  },
  {
    "path": "references/task-08-database-plan.md",
    "sha256": "e9a953c832f0e288bb72db2f324ea7877d49fbadbfc6d36f199fbcf5945dd107",
    "size": 2316
  },
  {
    "path": "references/task-09-search-strategies.md",
    "sha256": "fa3482c7d00190980580a43e3079ab61628ba7198c2397e1e48f4a2c2c11772d",
    "size": 2386
  },
  {
    "path": "references/task-10-run-searches.md",
    "sha256": "c1dc3152c0521fbb5badd1254f274b6a64d9a61b854bfe747156c016695f6c22",
    "size": 2412
  },
  {
    "path": "references/task-11-metadata-cleaning.md",
    "sha256": "da605e4b650419e59c46b167cf9161ada82fceca984d73a49719fe1629ed87b9",
    "size": 2493
  },
  {
    "path": "references/task-12-eligibility-criteria.md",
    "sha256": "a201477eb6b47ac0b0c5c871ac9a1aac61af0959ef760833b70900b529caa132",
    "size": 2240
  },
  {
    "path": "references/task-13-title-abstract-screening.md",
    "sha256": "1e4e71c978ed75cbf717eaf86e845c629921042609d3da4154c9011e4b62e214",
    "size": 2337
  },
  {
    "path": "references/task-14-full-text-screening.md",
    "sha256": "596c03a6eb6ac1bb80b36722e2b462d874a659ebed9714434983b309cd25dfa5",
    "size": 2486
  },
  {
    "path": "references/task-15-library-audit.md",
    "sha256": "55aacdf41fdec34ae341aa65d8127d36a3f70a98ce033ff445c59032aad7f814",
    "size": 2530
  },
  {
    "path": "references/task-16-structured-reading.md",
    "sha256": "eed4b9c5c047af54eabfe81b60187b3f33576fe25d1e5889ab59328514f13527",
    "size": 2585
  },
  {
    "path": "references/task-17-evidence-cards.md",
    "sha256": "41d98c01d814c48d83bfa6d074702f0797fcdb4d997188d5346a6f6be5968545",
    "size": 2349
  },
  {
    "path": "references/task-18-claim-evidence-matrix.md",
    "sha256": "312ae95cb443e23016578b136249ffb10f62e8d6254bb10f9a96ce4e872d31a1",
    "size": 2498
  },
  {
    "path": "references/task-19-evidence-synthesis.md",
    "sha256": "fdaa0261ab1a51df7dd8ea7e8755b6c9b9c5af4b28b8499abd0974488fb5ef8b",
    "size": 2565
  },
  {
    "path": "references/task-20-outline-and-figures.md",
    "sha256": "e0d973b1cf3c7ec61bf28f53b1a7441d2631579533546d0b76c5d53d2ddd6ba1",
    "size": 2637
  },
  {
    "path": "references/task-21-writing-submission-revision.md",
    "sha256": "afa557503e79fb331d1fa461ea86d25e6bcad9bf796e974b183060374bd285b6",
    "size": 6342
  },
  {
    "path": "references/task-result.schema.json",
    "sha256": "d94ab424691b9750b27482fb5abd8c1aae678a8536b1699a0aafb7d731026f50",
    "size": 2169
  },
  {
    "path": "scripts/_common.py",
    "sha256": "6f9c2f0d1d49959957db20726b118d83ebe4d28983852c82258c1ff8b0720f11",
    "size": 7917
  },
  {
    "path": "scripts/_distribution.py",
    "sha256": "4e1990b854029476ccf0896cf0e5066c8746a8e3639319cfffdf87ef30574de9",
    "size": 1757
  },
  {
    "path": "scripts/audit_claims.py",
    "sha256": "973fe33366c5fad1c3a39fc0e441c1f32b12720242fcb9106455a297f84d24c7",
    "size": 5531
  },
  {
    "path": "scripts/audit_figures_tables.py",
    "sha256": "917e79d158ae1ed2d541a1d3293f46a2a8094b3538b7271064ef69920b03e3e2",
    "size": 4497
  },
  {
    "path": "scripts/build_core_workbooks.mjs",
    "sha256": "ce842fcc62d595fa0aaae9e2a57f7f52cb35a48fc6b2e71b1cb46af4818fb230",
    "size": 22417
  },
  {
    "path": "scripts/build_full_skill.py",
    "sha256": "a499a7041ee1e35419b31bfbf9e43ad0512ada30694dd109f3e2639f594bef0b",
    "size": 5306
  },
  {
    "path": "scripts/build_literature_map.py",
    "sha256": "64b799c4d9037ed4d8e23be493deb7bac181119f2a50627c09132a8457b95e4f",
    "size": 3772
  },
  {
    "path": "scripts/build_outline_template.py",
    "sha256": "97d7c1297707b6de81d1422f604f76f62c1d935ab295f7d4b02ea69f6869735c",
    "size": 18850
  },
  {
    "path": "scripts/check_distribution_parity.py",
    "sha256": "4eed9c9728c057508c754d457e0d8e39f3625deb2e53d2f1d89e507943c42e45",
    "size": 3390
  },
  {
    "path": "scripts/deduplicate_records.py",
    "sha256": "f8515a5bb1cfe9764cf101ddd660aa146f434b56b1c7068071ad06053a32f430",
    "size": 7484
  },
  {
    "path": "scripts/import_records.py",
    "sha256": "0590cad31bb4dc2e2bd58ff341f887108ed736352667e8ccd2cb501ca0412a0e",
    "size": 15795
  },
  {
    "path": "scripts/init_project.py",
    "sha256": "b4b5e2ae968350bd20693e9b6c230e51a9e797d40c9999c7f14c5957f0fed6a6",
    "size": 5997
  },
  {
    "path": "scripts/transition_state.py",
    "sha256": "ea1f2383aa791a15a5c9ff7a364db6a918dcb6b4980ab81c7aa5d4b4189b6884",
    "size": 10056
  },
  {
    "path": "scripts/validate_metadata.py",
    "sha256": "45054fa275a1a9b84173f391e59773a13b3e873fe627f988f6e8203bd91f30c7",
    "size": 6765
  },
  {
    "path": "scripts/validate_project.py",
    "sha256": "63e3ea40b2e277a5c0bea32b44ced92aeba5ea178441f031a438a7f7cea37ab4",
    "size": 7161
  },
  {
    "path": "scripts/version_output.py",
    "sha256": "35e70f59e17ab32ec0451d2cfc4d0da52658f46c904dca1ba27545e7bb375279",
    "size": 2416
  },
  {
    "path": "assets/templates/evidence_and_claims.xlsx",
    "sha256": "402de1de5091ed2569f000ba99c0f7e6c9bd47b6daeddee38d53c2157a667d6b",
    "size": 9785
  },
  {
    "path": "assets/templates/evidence_card.md",
    "sha256": "78cfd76cdbba2dd7d3685d44802fa58edce77fb054b7d6876f5a4567cc7658bc",
    "size": 890
  },
  {
    "path": "assets/templates/literature_map.xlsx",
    "sha256": "5e0121d66c0d01d7f2e6ad2282da2ff08b5ba7757f29a2b67ea08564da8bbd00",
    "size": 8427
  },
  {
    "path": "assets/templates/literature_registry.xlsx",
    "sha256": "6a0f81caa735a184fcc098c7c76bc7987249f99759ebf33813aa4f0e57ff69f1",
    "size": 9404
  },
  {
    "path": "assets/templates/outline_review_report.md",
    "sha256": "0553e53d251377e5f47c195b1d301e4674fc502cd7d1d4621321b2e83bc66d99",
    "size": 848
  },
  {
    "path": "assets/templates/preflight_and_roadmap.xlsx",
    "sha256": "b2097d8cc2a1ef21c8e03c17bf2071183b12666f42c86a4c636ed6790971797f",
    "size": 8707
  },
  {
    "path": "assets/templates/project_diagnosis.md",
    "sha256": "d53081174644e082910b0fb0b0af836d9bef2525b6697a21145d04e704b32053",
    "size": 768
  },
  {
    "path": "assets/templates/project_manifest.json",
    "sha256": "0e876726d15f74dd803bf1f1b104dafba742845b0495c5d0bcf65345f0bd8910",
    "size": 618
  },
  {
    "path": "assets/templates/project_state.yaml",
    "sha256": "5c5a4a391fb1e2e279e8b9390a0eb68b9e2598a1525c91ff2aaa24805c5dd68d",
    "size": 6294
  },
  {
    "path": "assets/templates/prompt_library.md",
    "sha256": "95eb1f84e7580f96f50e4224e5dc20ddcc743a6539bc9d368535e92c3a166d52",
    "size": 1782
  },
  {
    "path": "assets/templates/reading_note.md",
    "sha256": "1db7990ed8c15c3d2f09ee3eea5afa363f3f560b7c8672e64604f47a81f92cf6",
    "size": 1397
  },
  {
    "path": "assets/templates/review_outline_template.docx",
    "sha256": "32bd2c36a9b72eeead96b79e1356d60309e295711d52746bfee0054f2cb73cd1",
    "size": 42087
  },
  {
    "path": "assets/templates/revision_recommendations.md",
    "sha256": "09ee63f7b025f172050c0d4842e433ad85ae6ea374b31265a749288cd1b4209b",
    "size": 413
  },
  {
    "path": "assets/templates/stage_report.md",
    "sha256": "061229a9b6254c9b87f072643e726ce7395fb4a2420232d5591dc153c4c1f0a4",
    "size": 1277
  },
  {
    "path": "assets/templates/task_status.yaml",
    "sha256": "c978a220a98a2d5d7f6b27e3e9b53d23df739312aaf10ffc5f31137213764fd4",
    "size": 298
  }
]
```
