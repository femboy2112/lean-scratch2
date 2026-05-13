#!/usr/bin/env python3
"""Python-side r=3 factor-search scaffold.

For serious exact characteristic polynomials, prefer Sage scripts in ../sage.
This script is intentionally conservative to avoid accidental long SymPy runs.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from collatz_codex_harness.construct import level_spec
from collatz_codex_harness.reports import write_markdown_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("model", choices=["unit", "full"])
    parser.add_argument("--allow-heavy", action="store_true")
    args = parser.parse_args()
    spec = level_spec(3, args.model)
    out = ROOT / "reports" / f"r3_{args.model}_factor_search_plan.md"

    if not args.allow_heavy:
        write_markdown_report(
            out,
            f"r=3 {args.model} Factor Search Plan",
            [
                ("Status", "status: Not Established"),
                (
                    "Reason Python exact charpoly is blocked by default",
                    f"Dimension is {len(spec.rows)}. Use Sage for exact charpoly/factorization unless a smaller invariant subspace has been isolated.",
                ),
                (
                    "Recommended command",
                    f"```bash\nsage sage/r3_factorization_search.sage {args.model}\n```",
                ),
            ],
        )
        print(f"wrote {out}")
        return 0

    raise SystemExit("Heavy SymPy path intentionally not implemented. Use Sage or add a bounded method.")


if __name__ == "__main__":
    raise SystemExit(main())
