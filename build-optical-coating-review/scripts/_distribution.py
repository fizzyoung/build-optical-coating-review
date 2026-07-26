from __future__ import annotations

import hashlib
from pathlib import Path

TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".mjs", ".txt", ".csv", ".tsv"}


def source_files(skill_root: Path) -> list[Path]:
    skill_root = skill_root.resolve()
    files = [skill_root / "SKILL.md", skill_root / "agents" / "openai.yaml"]
    files.extend(sorted((skill_root / "references").glob("*"), key=lambda item: item.name.casefold()))
    files.extend(sorted((skill_root / "scripts").glob("*"), key=lambda item: item.name.casefold()))
    files.extend(sorted((skill_root / "assets" / "templates").glob("*"), key=lambda item: item.name.casefold()))
    return [path for path in files if path.is_file() and "__pycache__" not in path.parts]


def source_manifest(skill_root: Path) -> list[dict[str, object]]:
    result = []
    for path in source_files(skill_root):
        data = path.read_bytes()
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
