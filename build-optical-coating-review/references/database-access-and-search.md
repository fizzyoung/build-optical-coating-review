# Database Access and Search Operations

## Purpose

Use this reference in Step 00 and Tasks 04, 08, 09, and 10. Treat access, search, metadata, export, and full text as separate capabilities. Never bypass authentication, CAPTCHA, subscriptions, robots restrictions, or platform terms.

## Platform Roles

| Role | Platforms | Primary use | Not sufficient alone for |
|---|---|---|---|
| Comprehensive index | Web of Science Core Collection, Scopus | Core multidisciplinary retrieval, cited/citing links, exports | Guaranteed full text |
| Discipline index | PubMed, GeoRef, Engineering Village | Topic-specific terminology and engineering coverage | Complete optical-coating coverage by itself |
| Chinese database | CNKI, 万方 | Chinese journals, theses, standards and local engineering work | English SCI coverage |
| Discovery | Google Scholar, 百度学术 | Seed finding, citation discovery, hard-to-find records | Reproducible exhaustive counts or clean bulk export |
| Metadata verification | Crossref, OpenAlex | DOI, title, author, venue and relationship checks | Subscription full text or definitive indexing status |
| Publisher full text | ScienceDirect, SpringerLink | Record pages, abstracts, supplements and lawful full text | Comprehensive cross-publisher search |

## Access Record

For every platform record `database_name`, `database_category`, `access_status`, `access_level`, `access_route`, `test_date`, login/VPN requirements, search/record/abstract/full-text/export availability, export formats, test query, real result count, automation restrictions, limitations and user confirmation.

Access states are `ACCESSIBLE`, `PARTIALLY_ACCESSIBLE`, `VPN_REQUIRED`, `LOGIN_REQUIRED`, `NO_SUBSCRIPTION`, `CAPTCHA_OR_MANUAL_OPERATION_REQUIRED`, `TEMPORARILY_UNAVAILABLE`, `REGION_RESTRICTED`, `NOT_REQUIRED_FOR_THIS_PROJECT`, `USER_WAIVED`, and `UNVERIFIED`. Capability levels are L0 closed, L1 homepage, L2 search, L3 record/abstract, L4 export, and L5 lawful required full text.

Before Task 01, no required platform may remain `UNVERIFIED`. `NOT_REQUIRED_FOR_THIS_PROJECT` and `USER_WAIVED` require explicit user approval.

## Browser and Account Boundary

- Ask the user to complete login, institutional SSO, VPN, CAPTCHA, MFA, consent, download approval, or subscription decisions.
- Do not capture passwords, tokens, cookies, session storage, or private account data in project files or logs.
- Do not automate bulk access when platform terms or visible restrictions prohibit it.
- Use rate limits, bounded pages, and caching when automation is permitted.
- Record a failed access attempt as a status; do not fabricate results or silently substitute a different database.

## Three-Layer Search Design

1. Broad: maximize recall with substrate/coating concepts and verified synonyms.
2. Balanced: add optical, protection, interface, or manufacturing context to reduce unrelated uses.
3. Precise: add a specific process, mechanism, performance, or application group for focused questions.

Write platform-neutral Boolean logic first. Translate only after verifying field names, phrase rules, wildcard behavior, proximity syntax, query length, language handling and date filters on the live platform. Keep exclusion clauses narrow and test them against known relevant records.

## Query Record

Every executed query records a stable query ID, platform, database collection, query tier, exact string, fields, filters, date/time, result count, sort order, export range, export format, file path, operator, version, and error or restriction. Results counts must come from the live interface or exported file.

## Export and Provenance

- Preserve raw exports as read-only inputs.
- Include platform, query ID, tier, version, date and batch in filenames.
- Tag each imported record with all source platforms and queries before deduplication.
- Accept CSV, XLSX, RIS, BibTeX, EndNote XML, Zotero mappings and JSON only through format-aware parsers.
- Reconcile `reported result count`, `exported rows`, `parse failures`, `duplicates`, `retained records` and `unresolved records`.

## Citation Chasing

Record seed Source_ID, direction (`BACKWARD`, `FORWARD`, `RELATED`), platform, date and inclusion reason. Citation connection is a discovery path, not proof that two papers agree. Create literature-map relations only after reading evidence that supports the relation.

## Metadata Verification

Normalize DOI by removing resolver prefixes and lowercasing for matching while preserving the display form. Cross-check title, author, year and venue before V2. When Crossref, OpenAlex, publisher and PDF disagree, retain all values, identify their sources, and create a manual conflict rather than selecting the most convenient field.

## Stop Conditions

Pause on login/VPN/CAPTCHA, unexpected download prompts, export truncation, result-count drift without explanation, syntax rejection, platform outage, source conflicts, full-text mismatch or any instruction that would bypass access controls. Resume only after state and access records are updated.
