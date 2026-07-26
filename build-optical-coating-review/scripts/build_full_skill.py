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
