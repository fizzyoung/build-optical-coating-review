# build-optical-coating-review

Evidence-traceable Codex Skill for optical-coating literature reviews, with an integrated domain pack for infrared chalcogenide-glass substrates and diamond-like carbon (DLC) films.

## Capabilities

- Approval-gated workflow from database preflight through review planning, search, screening, full-paper reading, evidence synthesis, writing, submission, and revision.
- Stable `Source_ID`, `Claim_ID`, evidence-card, literature-map, and figure/table provenance contracts.
- Narrative Review and strict Systematic Review branches.
- Deterministic scripts for project initialization, state transitions, validation, record import, deduplication, metadata checks, evidence audits, immutable versioning, and distribution parity.
- Chinese-first process reports while preserving English titles, terms, formulas, and citations.

The Skill records actual database access levels and never bypasses subscriptions, authentication, VPN requirements, CAPTCHA, or publisher access controls.

## Install In Codex

Ask Codex to install the Skill from:

```text
https://github.com/fizzyoung/build-optical-coating-review/tree/main/build-optical-coating-review
```

The installable Skill is the `build-optical-coating-review/` directory. Restart or open a new Codex task after installation so Skill discovery reloads.

## Example Requests

```text
围绕红外硫系玻璃基底 DLC 薄膜建立一个可追溯的 SCI 综述项目。
```

```text
检索并筛选 DLC 红外保护膜的中英文文献，先完成数据库预检并逐阶段等待确认。
```

```text
审计这些综述主张是否有 V3/V4 证据和原文位置支持。
```

## Repository Layout

- `build-optical-coating-review/`: installable Codex Skill.
- `dist/SKILL_FULL.md`: generated portable single-file representation.
- `tests/build-optical-coating-review/`: release regression runner and latest report.
- `qa/stage4/test_scripts.py`: reusable core-script test cases.

## Validate

Python 3.11 or newer is recommended. With `uv` installed:

```powershell
uv run --with PyYAML --with jsonschema --with openpyxl python tests/build-optical-coating-review/run_regression.py --installed-skill-root build-optical-coating-review
```

The current release passes 17 regression tests covering all 12 deterministic scripts, success paths, expected failures, immutable outputs, and source/distribution parity.

## License

MIT License. See [LICENSE](LICENSE).
