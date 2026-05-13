#!/usr/bin/env python3
"""Modular determinant nonzero reconnaissance for r=3 S(t).

A nonzero determinant at one finite-field specialization can witness that a
symbolic determinant is not the zero polynomial, assuming construction and
specialization are correct. It does NOT prove positivity/nonvanishing for all
real s>0.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from collatz_codex_harness.construct import det_mod_prime, s_matrix_mod
from collatz_codex_harness.reports import write_json_report

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PRIMES = [1000003, 1000033, 1000037, 1000039, 1000081]


def run(model: str, samples: int, seed: int) -> Path:
    rng = random.Random(seed)
    rows = []
    nonzero_count = 0
    for _ in range(samples):
        p = rng.choice(DEFAULT_PRIMES)
        t = rng.randrange(2, p - 1)
        M = s_matrix_mod(3, model, t, p)  # type: ignore[arg-type]
        det = det_mod_prime(M, p)
        if det % p:
            nonzero_count += 1
        rows.append({"prime": p, "t_value": t, "det_mod_prime": det, "nonzero": bool(det % p)})
    payload = {
        "status": "Computational Observation",
        "r": 3,
        "model": model,
        "samples": samples,
        "seed": seed,
        "nonzero_count": nonzero_count,
        "claim_boundary": "Finite-field samples only; no all-real-s determinant nonvanishing proof and no Collatz-level conclusion.",
        "rows": rows,
    }
    out = ROOT / "reports" / f"r3_{model}_modular_det_probe.json"
    write_json_report(out, payload)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=["unit", "full"], required=True)
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260513)
    args = parser.parse_args()
    out = run(args.model, args.samples, args.seed)
    print(json.dumps({"wrote": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
