#!/usr/bin/env python3
"""Extract theorem-candidate-like lines from a report and package them for review."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


KEYWORDS = re.compile(r"\b(theorem|lemma|proposition|candidate|conjecture|verified fact)\b", re.IGNORECASE)


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "reports").exists():
            return q
    return p


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    root = repo_root()
    path = Path(args.path)
    if not path.is_absolute():
        path = root / path
    text = path.read_text(encoding="utf-8", errors="replace")

    candidates = []
    for i, line in enumerate(text.splitlines(), start=1):
        if KEYWORDS.search(line):
            candidates.append({
                "line": i,
                "text": line.strip(),
                "status": "Not Established",
                "required_boundary": "finite-level lifted-operator statement only; no Collatz-level conclusion",
            })

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_json = root / "reports" / f"{stamp}_{path.stem}_theorem_candidates.json"
    out_md = root / "reports" / f"{stamp}_{path.stem}_theorem_candidates.md"

    payload = {
        "source": str(path.relative_to(root) if path.is_relative_to(root) else path),
        "created_utc": stamp,
        "candidates": candidates,
        "claim_boundary": "Extraction is heuristic and does not validate theorem truth.",
    }
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md = [
        f"# Theorem Candidate Extraction — {path.name}",
        "",
        "- status: `Advisory Only`",
        "- claim_boundary: heuristic extraction only; no candidate is proved",
        "",
        "| Line | Candidate text | Initial status |",
        "|---:|---|---|",
    ]
    for c in candidates:
        text_cell = c["text"].replace("|", "\\|")
        md.append(f"| {c['line']} | {text_cell} | {c['status']} |")
    out_md.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({"ok": True, "count": len(candidates), "json": str(out_json), "markdown": str(out_md)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
