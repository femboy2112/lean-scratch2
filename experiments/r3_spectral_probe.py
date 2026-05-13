#!/usr/bin/env python3
"""Numerical r=3 spectral reconnaissance.

Status: Computational Observation only.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from collatz_codex_harness.construct import level_spec, s_numeric_matrix
from collatz_codex_harness.reports import utc_now_iso

ROOT = Path(__file__).resolve().parents[1]


def run(models: list[str], slices: list[float]) -> Path:
    out = ROOT / "reports" / "r3_spectral_probe.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "generated_at_utc",
                "status",
                "r",
                "model",
                "s",
                "dimension",
                "perron_row_sum_S",
                "max_abs_eigen_S",
                "second_abs_eigen_S",
                "spectral_gap_S",
                "claim_boundary",
            ],
        )
        writer.writeheader()
        for model in models:
            spec = level_spec(3, model)  # type: ignore[arg-type]
            for s in slices:
                M = s_numeric_matrix(3, model, s)  # type: ignore[arg-type]
                evals = np.linalg.eigvals(M)
                abs_sorted = sorted((abs(complex(x)) for x in evals), reverse=True)
                row_sum = float(np.sum(M[0, :]))
                second = float(abs_sorted[1]) if len(abs_sorted) > 1 else 0.0
                writer.writerow(
                    {
                        "generated_at_utc": utc_now_iso(),
                        "status": "Computational Observation",
                        "r": 3,
                        "model": model,
                        "s": s,
                        "dimension": len(spec.rows),
                        "perron_row_sum_S": row_sum,
                        "max_abs_eigen_S": float(abs_sorted[0]),
                        "second_abs_eigen_S": second,
                        "spectral_gap_S": float(abs_sorted[0] - second),
                        "claim_boundary": "Numerical S-level probe only; no exact closure and no Collatz-level conclusion.",
                    }
                )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="+", default=["unit", "full"], choices=["unit", "full"])
    parser.add_argument("--slices", nargs="+", type=float, default=[0.50, 0.55, 0.60])
    args = parser.parse_args()
    out = run(args.models, args.slices)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
