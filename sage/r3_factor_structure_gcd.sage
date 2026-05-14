#!/usr/bin/env sage
"""Exact pairwise gcd pass for the r=3 audited factor bundle."""

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_BUNDLE = ROOT / "data/generated/r3_factorization_audit/20260513T160231Z"
REPORTS = ROOT / "reports"
STRUCTURE_ROOT = ROOT / "data/generated/r3_factor_structure"
BOUNDARY = (
    "This is a finite-level S-level characteristic-polynomial factorization fact only. "
    "It does not prove or imply the Collatz conjecture, global orbit behavior, "
    "determinant nonvanishing for all real s > 0, cross-level invariance, or a "
    "structural mechanism."
)


def utc_stamp():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_factors(model):
    factor_dir = SOURCE_BUNDLE / model / "factors"
    return [load_json(path) for path in sorted(factor_dir.glob("factor_*.json"))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", default=None)
    args = parser.parse_args()

    stamp = args.timestamp or utc_stamp()
    structure_dir = STRUCTURE_ROOT / stamp
    manifest_path = structure_dir / "factor_gcd_manifest.json"
    report_json = REPORTS / f"{stamp}_r3_factor_structure_gcd.json"
    report_md = REPORTS / f"{stamp}_r3_factor_structure_gcd.md"

    R = PolynomialRing(QQ, "t")
    K = FractionField(R)
    Y = PolynomialRing(K, "y")

    unit = load_factors("unit")
    full = load_factors("full")
    unit_polys = [(factor, Y(factor["factor"])) for factor in unit]
    full_polys = [(factor, Y(factor["factor"])) for factor in full]

    pairwise = []
    nonconstant = []
    for uf, upoly in unit_polys:
        for ff, fpoly in full_polys:
            gcd_poly = upoly.gcd(fpoly).monic()
            gcd_expr = str(gcd_poly)
            gcd_degree_y = int(gcd_poly.degree())
            row = {
                "unit_factor_i": int(uf["factor_index"]),
                "full_factor_j": int(ff["factor_index"]),
                "unit_factor_sha256": uf["factor_sha256"],
                "full_factor_sha256": ff["factor_sha256"],
                "unit_degree_y": int(uf["degree_y"]),
                "full_degree_y": int(ff["degree_y"]),
                "gcd_degree_y": gcd_degree_y,
                "gcd_expression": gcd_expr,
                "gcd_expression_sha256": sha256_text(gcd_expr),
                "claim_label": "Verified Fact",
                "scope_note": "exact pairwise gcd over QQ(t)[y] for audited finite-level r=3 S-level factors",
            }
            pairwise.append(row)
            if gcd_degree_y > 0:
                nonconstant.append(row)

    payload = {
        "status": "Verified Fact",
        "target": "previously blocked r=3 factor-structure exact gcd pass",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level audited unit/full characteristic-polynomial factors from 20260513T160231Z",
        "method": "Sage exact pairwise gcd over QQ(t)[y]",
        "ring": "QQ(t)[y]",
        "claim_boundary": BOUNDARY,
        "source_bundle": str(SOURCE_BUNDLE.relative_to(ROOT)),
        "reproduction_command": "env DOT_SAGE=$PWD/.codex/sage .sage-conda/bin/sage sage/r3_factor_structure_gcd.sage",
        "files_touched": [
            "sage/r3_factor_structure_gcd.sage",
            "reports/",
            "data/generated/r3_factor_structure/",
        ],
        "artifacts_produced": {
            "factor_gcd_manifest": str(manifest_path.relative_to(ROOT)),
            "report_json": str(report_json.relative_to(ROOT)),
            "report_md": str(report_md.relative_to(ROOT)),
        },
        "previous_blocker_resolved": "Sage exact gcd work was previously marked Not Established because Sage was unavailable on PATH.",
        "unit_factor_count": len(unit),
        "full_factor_count": len(full),
        "pairwise_gcd_count": len(pairwise),
        "nonconstant_gcds": nonconstant,
        "pairwise_gcds": pairwise,
        "not_established_items": [
            "r=3 structural mechanism explaining the factorization pattern",
            "determinant nonvanishing for all real s > 0",
            "cross-level invariance",
            "subdominant spectral structure",
            "any Collatz-level conclusion",
        ],
    }

    nonconstant_lines = []
    for row in nonconstant:
        nonconstant_lines.append(
            "- unit factor_{:02d} with full factor_{:02d}: gcd_degree_y={}, gcd_expression_sha256={}, label=`Verified Fact`".format(
                row["unit_factor_i"],
                row["full_factor_j"],
                row["gcd_degree_y"],
                row["gcd_expression_sha256"],
            )
        )
    if not nonconstant_lines:
        nonconstant_lines.append("- No nonconstant gcds were detected.")

    table_lines = [
        "| unit factor | full factor | gcd degree in y | gcd expression sha256 | label |",
        "|---:|---:|---:|---|---|",
    ]
    for row in pairwise:
        table_lines.append(
            "| {unit_factor_i:02d} | {full_factor_j:02d} | {gcd_degree_y} | `{gcd_expression_sha256}` | Verified Fact |".format(
                **row
            )
        )

    md = """# r=3 Factor Structure Exact GCD Pass

status: Verified Fact
scope: {scope}
method: {method}
claim_boundary: {claim_boundary}
reproduction_command: `{reproduction_command}`
files_touched: `sage/r3_factor_structure_gcd.sage`, `reports/`, `data/generated/r3_factor_structure/`
artifacts_produced: `{manifest_path}`, `{report_json}`, `{report_md}`

## Previous Failed Part

Patched: the prior factor-structure artifact marked exact gcd work `Not Established` because Sage was unavailable on PATH. This pass reruns only that Sage-dependent part with the repo-local Sage binary.

## Nonconstant GCDs

{nonconstant}

## Pairwise GCD Table

{table}

## Remaining Not Established Items

- r=3 structural mechanism explaining the factorization pattern
- determinant nonvanishing for all real s > 0
- cross-level invariance
- subdominant spectral structure
- any Collatz-level conclusion
""".format(
        scope=payload["scope"],
        method=payload["method"],
        claim_boundary=payload["claim_boundary"],
        reproduction_command=payload["reproduction_command"],
        manifest_path=payload["artifacts_produced"]["factor_gcd_manifest"],
        report_json=payload["artifacts_produced"]["report_json"],
        report_md=payload["artifacts_produced"]["report_md"],
        nonconstant="\n".join(nonconstant_lines),
        table="\n".join(table_lines),
    )

    write_json(manifest_path, payload)
    write_json(report_json, payload)
    write_text(report_md, md)
    print(json.dumps({"ok": True, "outputs": payload["artifacts_produced"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(int(main()))
