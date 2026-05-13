#!/usr/bin/env python3
"""Summarize the Collatz harness state for Codex orchestration."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


OPEN_TARGETS = [
    "r=3 compact factorization",
    "r=3 structural mechanism",
    "r=3 subdominant spectral structure",
    "r=3 determinant nonvanishing for all real s > 0",
    "r=3 exact determinant polynomials",
    "cross-level r=2/r=3 spectral invariance",
    "proof-boundary clarification for finite-level implications",
]


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "data/canonical_bundle").exists():
            return q
    return p


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = repo_root()
    bundle = root / "data/canonical_bundle"
    files = []
    for p in sorted(bundle.glob("*")):
        if p.is_file():
            files.append({
                "name": p.name,
                "bytes": p.stat().st_size,
                "sha256": sha256(p),
            })

    payload = {
        "repo_root": str(root),
        "canonical_file_count": len(files),
        "canonical_files": files,
        "open_targets": OPEN_TARGETS,
        "skills": sorted(str(p.relative_to(root)) for p in (root / ".agents/skills").glob("*/SKILL.md")),
        "guardrail": "No finite-level matrix fact may be upgraded to a Collatz-level proof.",
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
