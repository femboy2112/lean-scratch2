#!/usr/bin/env python3
"""Audit all generated reports for claim-ladder and forbidden-language issues."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "reports").exists():
            return q
    raise SystemExit("Could not locate repo root")


def main() -> int:
    root = repo_root()
    audit = root / ".agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py"
    files = [
        p
        for p in sorted((root / "reports").glob("*"))
        if p.is_file()
        and p.suffix.lower() in {".md", ".txt", ".json", ".log"}
        and not p.stem.endswith("_audit")
    ]
    results = []
    worst = 0
    for p in files:
        proc = subprocess.run([sys.executable, str(audit), str(p.relative_to(root))], cwd=root, text=True, capture_output=True)
        try:
            payload = json.loads(proc.stdout)
        except Exception:
            payload = {"ok": False, "stdout": proc.stdout, "stderr": proc.stderr}
        results.append({"file": str(p.relative_to(root)), "returncode": proc.returncode, "payload": payload})
        worst = max(worst, proc.returncode)

    out = {
        "ok": worst == 0,
        "count": len(results),
        "results": results,
        "claim_boundary": "This validates report language only; it does not prove mathematical claims.",
    }
    print(json.dumps(out, indent=2))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
