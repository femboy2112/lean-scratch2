#!/usr/bin/env python3
"""Collect report artifacts into a hash manifest."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "reports").exists():
            return q
    raise SystemExit("Could not locate repo root")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = repo_root()
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    manifest_path = reports / "witness_manifest.json"

    entries = []
    for p in sorted(reports.glob("*")):
        if p.is_file() and p.name != "witness_manifest.json":
            entries.append({
                "path": str(p.relative_to(root)),
                "bytes": p.stat().st_size,
                "sha256": sha256(p),
            })

    manifest = {
        "status": "Advisory Only",
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "scope": "finite-level Collatz harness report artifacts",
        "claim_boundary": "Hashes authenticate artifacts only; they do not upgrade mathematical claims.",
        "entries": entries,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps({"ok": True, "manifest": str(manifest_path), "count": len(entries)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
