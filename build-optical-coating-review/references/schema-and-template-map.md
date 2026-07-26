# Schema and Template Map

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

## Flat-Table Encoding

XLSX cells cannot directly store JSON arrays. Encode arrays as semicolon-delimited values in workbooks, preserving semicolons inside a value by escaping them as `\;`. Import scripts must split and unescape these fields. Empty cells normalize to empty arrays or `null` according to the corresponding Schema.

Dates use ISO `YYYY-MM-DD`; timestamps use RFC 3339. Boolean cells use actual Boolean values where supported. IDs are stable and must never be reassigned after citation or approval.

## Verification Levels

`V0` unverified; `V1` title only; `V2` bibliographic metadata and DOI; `V3` abstract or record page; `V4` full-text page, section, figure, or table location; `V5` critical fact checked by a second source or a human. Core prose facts require at least V3. Mechanisms, quantitative comparisons, and figure/table data require at least V4.

