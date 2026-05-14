#!/usr/bin/env python3
"""Audit generated reports for claim-ladder and forbidden-language issues."""
from __future__ import annotations

import argparse
import datetime as dt
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


def parse_stamp(name: str) -> str | None:
    stem = Path(name).stem
    first = stem.split("_", 1)[0]
    if (
        len(first) == 16
        and first.endswith("Z")
        and first[8] == "T"
        and first[:8].isdigit()
        and first[9:15].isdigit()
    ):
        return first
    return None


def is_audit_artifact(path: Path) -> bool:
    stem = path.stem
    return (
        stem.endswith("_audit")
        or stem.endswith("_claim_validation")
        or stem.endswith("_claim_ladder_validation")
        or "claim_ladder_validation" in stem
        or path.name == "witness_manifest.json"
        or "witness_manifest" in stem
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", default=None, help="Only audit timestamped reports at or after YYYYMMDDTHHMMSSZ.")
    parser.add_argument("--exclude-audits", action="store_true", help="Skip audit/validation/manifest reports.")
    parser.add_argument("--output", default=None, help="Write validation JSON to this path as well as stdout.")
    args = parser.parse_args()

    root = repo_root()
    audit = root / ".agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py"
    files = [
        p
        for p in sorted((root / "reports").glob("*"))
        if p.is_file()
        and p.suffix.lower() in {".md", ".txt", ".json", ".log"}
        and not p.stem.endswith("_audit")
    ]
    if args.exclude_audits:
        files = [p for p in files if not is_audit_artifact(p)]
    if args.since:
        files = [p for p in files if (parse_stamp(p.name) or "") >= args.since]

    results = []
    worst = 0
    for p in files:
        proc = subprocess.run([sys.executable, str(audit), str(p.relative_to(root)), "--no-write"], cwd=root, text=True, capture_output=True)
        try:
            payload = json.loads(proc.stdout)
        except Exception:
            payload = {"ok": False, "stdout": proc.stdout, "stderr": proc.stderr}
        results.append({"file": str(p.relative_to(root)), "returncode": proc.returncode, "payload": payload})
        worst = max(worst, proc.returncode)

    out = {
        "status": "Advisory Only",
        "ok": worst == 0,
        "count": len(results),
        "created_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "since": args.since,
        "exclude_audits": args.exclude_audits,
        "results": results,
        "claim_boundary": "This validates report language only; it does not prove mathematical claims.",
    }
    text = json.dumps(out, indent=2)
    if args.output:
        output = Path(args.output)
        if not output.is_absolute():
            output = root / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
