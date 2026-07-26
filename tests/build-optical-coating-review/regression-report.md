# build-optical-coating-review Regression Report

- Generated: 2026-07-26T13:32:23Z
- Status: PASS
- Tests: 17 total; 17 passed; 0 failed; 0 errors; 0 skipped
- Duration: 19.703 seconds
- Isolation: all mutable fixtures were created under system temporary directories
- Approved example project modified: no

## Coverage

- CLI help and dependency loading for all 12 deterministic scripts
- Initialization, safe resume, overwrite refusal, state transitions, validation, and Task 21B gate
- CSV, RIS, BibTeX, EndNote XML, and XLSX import; DOI deduplication and conflict retention
- Local metadata validation and simulated external verification failure
- Explicit map edges plus self-edge and unknown Source_ID rejection
- V3-V5 claim gates, original locations, substantive support, and Raman-sp3 overclaim blocking
- Figure/table provenance, calculations, copyright, permission, and verification gates
- Immutable versioning, reproducible portable build, tamper detection, and installed-copy parity

## Results

| Test | Status | Seconds |
|---|---:|---:|
| test_all_scripts_support_help | PASS | 2.333 |
| test_claim_audit_passes_v4_and_blocks_overclaim | PASS | 1.16 |
| test_external_metadata_failure_returns_explicit_status_without_network | PASS | 0.039 |
| test_figure_audit_checks_v4_calculation_and_copyright | PASS | 0.816 |
| test_import_csv_and_deduplicate_exact_doi | PASS | 0.833 |
| test_import_rejects_reused_explicit_source_id | PASS | 0.413 |
| test_import_ris_bibtex_endnote_and_xlsx | PASS | 2.339 |
| test_literature_map_uses_only_explicit_edges | PASS | 0.788 |
| test_local_metadata_validation_does_not_infer_external_values | PASS | 0.416 |
| test_portable_builder_is_reproducible_and_parity_detects_tampering | PASS | 1.09 |
| test_project_state_transitions_validation_and_versioning | PASS | 4.885 |
| test_task_21b_requires_current_chapter | PASS | 1.181 |
| test_title_conflict_keeps_both_records_unmodified | PASS | 0.406 |
| test_claim_gate_rejects_missing_v4_location_and_background_only | PASS | 0.811 |
| test_initialize_resume_and_reject_unsafe_overwrite | PASS | 1.144 |
| test_literature_map_rejects_self_edge_and_unknown_source | PASS | 0.766 |
| test_source_distribution_and_installed_copy_match | PASS | 0.282 |
