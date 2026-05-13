#!/usr/bin/env python3
"""Generate a Lean theorem stub for a finite-level candidate."""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "lean").exists():
            return q
    return p


def clean_name(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_]", "_", name)
    if not name or name[0].isdigit():
        name = "candidate_" + name
    return name


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--statement", required=True)
    parser.add_argument("--namespace", default="CollatzSpectral.Candidates")
    args = parser.parse_args()

    root = repo_root()
    name = clean_name(args.name)
    ns = args.namespace
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = root / "lean" / f"{stamp}_{name}.lean"

    content = f"""/-
Generated finite-level theorem stub.

Status: Not Established
Claim boundary: This skeleton does not prove or imply the Collatz conjecture.
Instruction: Replace `True` with a fully formal finite-level statement only
after all hypotheses are explicit and audited.
Original statement:
{args.statement}
-/

namespace {ns}

theorem {name} :
    True := by
  trivial

end {ns}
"""
    out.write_text(content, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
