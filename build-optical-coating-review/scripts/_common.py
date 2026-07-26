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
