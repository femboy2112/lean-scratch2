#!/usr/bin/env python3
"""Placeholder for cross-level invariance searches.

Codex target: turn this into a precise invariant comparison only after reading
canonical files 06-08. Default status remains Not Established.
"""

from __future__ import annotations

from pathlib import Path

from collatz_codex_harness.reports import write_markdown_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    out = ROOT / "reports" / "cross_level_invariance_plan.md"
    write_markdown_report(
        out,
        "Cross-Level Invariance Search Plan",
        [
            (
                "Status",
                "status: Not Established\n\nNo cross-level r=2/r=3 spectral invariance is claimed by this placeholder.",
            ),
            (
                "Next exact tasks",
                "1. Define the candidate invariant.\n2. Specify normalization.\n3. Test at r=2 and r=3 separately.\n4. Check against file 06 over-upgrade guards.",
            ),
        ],
    )
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
