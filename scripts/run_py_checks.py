#!/usr/bin/env python3
"""Fast sanity gates for the canonical construction."""

from __future__ import annotations

import json
from pathlib import Path

from collatz_codex_harness.construct import (
    R2_FULL_LEAF_EXPONENT_ROWS,
    R2_UNIT_EXPONENT_TABLE,
    all_row_sums_equal,
    exponent_table,
    full_rows,
    level_spec,
    live_columns,
    multiplicative_order_2,
    odd_multiples_of_3_representatives,
    source_zero_columns,
    unit_rows,
)
from collatz_codex_harness.hashes import sha256_json
from collatz_codex_harness.reports import write_json_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        checks.append({"name": name, "passed": bool(condition), "detail": detail})
        if not condition:
            raise AssertionError(f"failed check: {name}; detail={detail!r}")

    check("P_2 = 18", multiplicative_order_2(3**3) == 18)
    check("P_3 = 54", multiplicative_order_2(3**4) == 54)

    check("unit r=2 rows", unit_rows(2) == (1, 2, 4, 5, 7, 8))
    check("full r=2 rows", full_rows(2) == (1, 2, 4, 5, 7, 8, 3, 9, 15))
    check("unit r=3 row count", len(unit_rows(3)) == 18, unit_rows(3))
    check("full r=3 row count", len(full_rows(3)) == 27, full_rows(3))

    check("live columns r=2 count", len(live_columns(2)) == 18)
    check("live columns r=3 count", len(live_columns(3)) == 54)
    check("zero source columns r=2 count", len(source_zero_columns(2)) == 9)
    check("zero source columns r=3 count", len(source_zero_columns(3)) == 27)

    r2_unit = exponent_table(2, "unit")
    r2_full = exponent_table(2, "full")
    check("r=2 unit exponent table matches canonical", r2_unit == R2_UNIT_EXPONENT_TABLE)
    check(
        "r=2 full leaf rows match canonical",
        r2_full[6:] == R2_FULL_LEAF_EXPONENT_ROWS,
    )

    for r in (2, 3):
        for model in ("unit", "full"):
            spec = level_spec(r, model)
            table = exponent_table(r, model)
            check(f"r={r} {model} table row count", len(table) == len(spec.rows))
            check(f"r={r} {model} table column count", all(len(row) == len(spec.live_columns) for row in table))
            check(f"r={r} {model} row sums equal", all_row_sums_equal(r, model))

    payload = {
        "claim_status": "Verified Fact sanity gates only; no Collatz-level conclusion",
        "checks": checks,
    }
    report = ROOT / "reports" / "py_sanity_checks.json"
    write_json_report(report, payload)
    digest = sha256_json(payload)
    print(json.dumps({"ok": True, "report": str(report), "payload_sha256": digest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
