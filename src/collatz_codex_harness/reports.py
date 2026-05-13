"""Report writers for research runs."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .hashes import canonical_json_bytes, sha256_json


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json_report(path: str | Path, payload: dict[str, Any]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    enriched = {
        "generated_at_utc": utc_now_iso(),
        **payload,
    }
    p.write_bytes(canonical_json_bytes(enriched))
    return p


def write_markdown_report(path: str | Path, title: str, sections: list[tuple[str, str]]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", f"Generated: {utc_now_iso()}", ""]
    for heading, body in sections:
        lines.extend([f"## {heading}", "", body.rstrip(), ""])
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def report_hash(path: str | Path) -> str:
    return sha256_json(json.loads(Path(path).read_text(encoding="utf-8")))
