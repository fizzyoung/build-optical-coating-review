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
