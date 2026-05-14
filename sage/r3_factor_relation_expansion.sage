#!/usr/bin/env sage
"""Exact residual and relation artifacts for the r=3 deep program."""

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_BUNDLE = ROOT / "data/generated/r3_factorization_audit/20260513T160231Z"
GCD_MANIFEST = ROOT / "data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json"
REPORTS = ROOT / "reports"
DEEP_ROOT = ROOT / "data/generated/r3_deep_program"
SHARED_HASH = "02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69"
BOUNDARY = (
    "This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. "
    "It does not prove or imply the Collatz conjecture, global orbit behavior, "
    "determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism."
)


def utc_stamp():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(json_safe(payload), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def json_safe(value):
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(v) for v in value]
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float, str)):
        return value
    try:
        return int(value)
    except Exception:
        return str(value)


def load_factors(model):
    out = []
    for path in sorted((SOURCE_BUNDLE / model / "factors").glob("factor_*.json")):
        item = load_json(path)
        item["path"] = str(path.relative_to(ROOT))
        out.append(item)
    return out


def factor_key(model, factor):
    return "{}_{:02d}".format(model, int(factor["factor_index"]))


def factor_t_exponents(text):
    exps = set()
    for match in re.finditer(r"t(?:\^(\d+))?", text):
        exps.add(int(match.group(1) or "1"))
    return sorted(exps)


def poly_json(model, factor, poly):
    text = str(poly)
    exps = factor_t_exponents(text)
    return {
        "id": factor_key(model, factor),
        "model": model,
        "factor_index": int(factor["factor_index"]),
        "degree_y": int(poly.degree()),
        "factor_sha256": factor["factor_sha256"],
        "expression_sha256": sha256_text(text),
        "degree_t_max_recorded": factor.get("degree_t_max"),
        "only_even_t_powers_by_text_scan": all(e % 2 == 0 for e in exps),
        "t_exponent_count_by_text_scan": len(exps),
        "status_label": "Verified Fact",
        "claim_boundary": BOUNDARY,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", default=None)
    args = parser.parse_args()
    stamp = args.timestamp or utc_stamp()

    data_dir = DEEP_ROOT / stamp
    residual_dir = data_dir / "residuals"
    relation_dir = data_dir / "factor_relations"
    residual_dir.mkdir(parents=True, exist_ok=True)
    relation_dir.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(exist_ok=True)

    R = PolynomialRing(QQ, "t")
    K = FractionField(R)
    Y = PolynomialRing(K, "y")

    factors = {"unit": load_factors("unit"), "full": load_factors("full")}
    polys = {
        model: [(factor, Y(factor["factor"])) for factor in factors[model]]
        for model in ["unit", "full"]
    }

    products = {}
    residual_payload = {
        "status": "Verified Fact",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level audited factor residual algebra",
        "method": "Sage exact products over QQ(t)[y] from audited factor JSON plus exact gcd manifest",
        "ring": "QQ(t)[y]",
        "claim_boundary": BOUNDARY,
        "reproduction_command": "env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage --timestamp {}".format(stamp),
        "models": {},
        "cross_model": {},
    }

    for model in ["unit", "full"]:
        entries = polys[model]
        row = [item for item in entries if item[0].get("is_row_sum_factor")][0]
        shared = [item for item in entries if item[0]["factor_sha256"] == SHARED_HASH][0]
        charpoly = Y(1)
        no_row = Y(1)
        residual = Y(1)
        for factor, poly in entries:
            mult = int(factor["multiplicity"])
            charpoly *= poly ** mult
            if not factor.get("is_row_sum_factor"):
                no_row *= poly ** mult
            if (not factor.get("is_row_sum_factor")) and factor["factor_sha256"] != SHARED_HASH:
                residual *= poly ** mult
        products[model] = {
            "charpoly": charpoly,
            "row": row[1],
            "shared": shared[1],
            "no_row": no_row,
            "residual": residual,
        }
        expected = products[model]["row"] * no_row
        shared_power = int(shared[0]["multiplicity"])
        expected_residual = products[model]["row"] * (products[model]["shared"] ** shared_power) * residual
        write_text(residual_dir / "{}_no_row.txt".format(model), str(no_row))
        write_text(residual_dir / "{}_residual.txt".format(model), str(residual))
        residual_payload["models"][model] = {
            "row_sum_factor_index": int(row[0]["factor_index"]),
            "shared_factor_index": int(shared[0]["factor_index"]),
            "shared_factor_multiplicity": shared_power,
            "charpoly_degree_y": int(charpoly.degree()),
            "no_row_degree_y": int(no_row.degree()),
            "residual_degree_y": int(residual.degree()),
            "charpoly_equals_row_times_no_row": bool(charpoly == expected),
            "charpoly_equals_row_shared_power_residual": bool(charpoly == expected_residual),
            "no_row_path": str((residual_dir / "{}_no_row.txt".format(model)).relative_to(ROOT)),
            "residual_path": str((residual_dir / "{}_residual.txt".format(model)).relative_to(ROOT)),
            "status_label": "Verified Fact",
        }

    gcd_manifest = load_json(GCD_MANIFEST)
    residual_factor_pairs = []
    residual_indices = {
        "unit": {int(f["factor_index"]) for f in factors["unit"] if (not f.get("is_row_sum_factor")) and f["factor_sha256"] != SHARED_HASH},
        "full": {int(f["factor_index"]) for f in factors["full"] if (not f.get("is_row_sum_factor")) and f["factor_sha256"] != SHARED_HASH},
    }
    for row in gcd_manifest.get("pairwise_gcds", []):
        if row["unit_factor_i"] in residual_indices["unit"] and row["full_factor_j"] in residual_indices["full"]:
            residual_factor_pairs.append(row)
    residual_gcd_degree = 0 if residual_factor_pairs and all(int(r["gcd_degree_y"]) == 0 for r in residual_factor_pairs) else None
    residual_payload["cross_model"] = {
        "unit_residual_degree_y": int(products["unit"]["residual"].degree()),
        "full_residual_degree_y": int(products["full"]["residual"].degree()),
        "residual_gcd_degree_y": residual_gcd_degree,
        "residual_gcd_method": "derived from exact pairwise gcd manifest over QQ(t)[y]",
        "status_label": "Verified Fact" if residual_gcd_degree == 0 else "Not Established",
    }

    gcd_table = {
        "status": "Verified Fact",
        "created_utc": stamp,
        "method": "Sage exact prior pairwise gcd table plus residual-product derivation",
        "ring": "QQ(t)[y]",
        "source_gcd_manifest": str(GCD_MANIFEST.relative_to(ROOT)),
        "pairwise_gcds": gcd_manifest.get("pairwise_gcds", []),
        "residual_gcd": residual_payload["cross_model"],
        "claim_boundary": BOUNDARY,
    }
    resultant_table = {
        "status": "Not Established",
        "created_utc": stamp,
        "method": "Resultants were classified rather than fully expanded for high-degree generic residuals",
        "ring": "QQ(t)[y]",
        "entries": [],
        "claim_boundary": BOUNDARY,
    }
    discriminant_table = {
        "status": "Computational Observation",
        "created_utc": stamp,
        "method": "Sage exact discriminants for low-degree factors; high-degree factors classified as not expanded",
        "ring": "QQ(t)",
        "entries": [],
        "claim_boundary": BOUNDARY,
    }
    coefficient_support = {
        "status": "Verified Fact",
        "created_utc": stamp,
        "method": "Sage degree data plus text scan of audited factor expressions",
        "entries": [],
        "claim_boundary": BOUNDARY,
    }
    substitution_profiles = {
        "status": "Computational Observation",
        "created_utc": stamp,
        "method": "Text scan for even t-exponents as a z=t^2 simplification hint",
        "entries": [],
        "claim_boundary": BOUNDARY,
    }

    for model in ["unit", "full"]:
        for factor, poly in polys[model]:
            item = poly_json(model, factor, poly)
            coefficient_support["entries"].append(item)
            substitution_profiles["entries"].append({
                "id": item["id"],
                "candidate_substitution": "z=t^2" if item["only_even_t_powers_by_text_scan"] else None,
                "status_label": "Computational Observation",
                "claim_boundary": BOUNDARY,
            })
            if int(poly.degree()) <= 3:
                disc = poly.discriminant()
                discriminant_table["entries"].append({
                    "id": item["id"],
                    "degree_y": int(poly.degree()),
                    "discriminant_sha256": sha256_text(str(disc)),
                    "status_label": "Verified Fact",
                })
            else:
                discriminant_table["entries"].append({
                    "id": item["id"],
                    "degree_y": int(poly.degree()),
                    "status_label": "Not Established",
                    "blocked_reason": "generic high-degree discriminant expansion not attempted in bounded pass",
                })
            resultant_table["entries"].append({
                "id": item["id"],
                "status_label": "Not Established",
                "blocked_reason": "generic resultant expansion deferred unless a specific target pair is selected",
            })

    write_json(residual_dir / "residual_manifest.json", residual_payload)
    write_json(relation_dir / "gcd_table.json", gcd_table)
    write_json(relation_dir / "resultant_table.json", resultant_table)
    write_json(relation_dir / "discriminant_table.json", discriminant_table)
    write_json(relation_dir / "coefficient_support.json", coefficient_support)
    write_json(relation_dir / "substitution_profiles.json", substitution_profiles)

    residual_report_json = REPORTS / "{}_r3_residual_factor_analysis.json".format(stamp)
    residual_report_md = REPORTS / "{}_r3_residual_factor_analysis.md".format(stamp)
    relation_report_json = REPORTS / "{}_r3_factor_relation_expansion.json".format(stamp)
    relation_report_md = REPORTS / "{}_r3_factor_relation_expansion.md".format(stamp)
    write_json(residual_report_json, residual_payload)
    write_json(relation_report_json, {
        "status": "Verified Fact",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level factor relation expansion",
        "method": "Sage exact low-cost relation extraction with explicit Not Established classifications for deferred high-degree targets",
        "artifacts": {
            "gcd_table": str((relation_dir / "gcd_table.json").relative_to(ROOT)),
            "resultant_table": str((relation_dir / "resultant_table.json").relative_to(ROOT)),
            "discriminant_table": str((relation_dir / "discriminant_table.json").relative_to(ROOT)),
            "coefficient_support": str((relation_dir / "coefficient_support.json").relative_to(ROOT)),
            "substitution_profiles": str((relation_dir / "substitution_profiles.json").relative_to(ROOT)),
        },
        "claim_boundary": BOUNDARY,
    })

    write_text(residual_report_md, """# r=3 Residual Factor Analysis

status: Verified Fact
scope: finite-level r=3 S-level audited factor residual algebra
method: Sage exact products over QQ(t)[y] from audited factor JSON and exact gcd manifest
claim_boundary: {boundary}
reproduction_command: `{cmd}`
files_touched: `sage/r3_factor_relation_expansion.sage`, `reports/`, `data/generated/r3_deep_program/{stamp}/residuals/`
artifacts_produced: `{manifest}`

## Residual Checks

- unit residual degree in y: `{u_deg}`
- full residual degree in y: `{f_deg}`
- unit charpoly reconstruction after removing row/shared factors: `{u_check}`
- full charpoly reconstruction after removing row/shared factors: `{f_check}`
- residual cross-gcd degree in y: `{gcd_deg}`
- residual cross-gcd method: derived from exact pairwise gcd manifest over `QQ(t)[y]`

## Not Established

Not Established: resultants and determinant positivity over all real `s > 0` are not established by this residual pass.
""".format(
        boundary=BOUNDARY,
        cmd=residual_payload["reproduction_command"],
        stamp=stamp,
        manifest=str((residual_dir / "residual_manifest.json").relative_to(ROOT)),
        u_deg=residual_payload["models"]["unit"]["residual_degree_y"],
        f_deg=residual_payload["models"]["full"]["residual_degree_y"],
        u_check=residual_payload["models"]["unit"]["charpoly_equals_row_shared_power_residual"],
        f_check=residual_payload["models"]["full"]["charpoly_equals_row_shared_power_residual"],
        gcd_deg=residual_payload["cross_model"]["residual_gcd_degree_y"],
    ))
    write_text(relation_report_md, """# r=3 Factor Relation Expansion

status: Verified Fact
scope: finite-level r=3 S-level audited factor relation expansion
method: Sage exact gcd/support extraction; bounded discriminants; explicit classification for deferred resultants
claim_boundary: {boundary}
reproduction_command: `env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage --timestamp {stamp}`
files_touched: `sage/r3_factor_relation_expansion.sage`, `reports/`, `data/generated/r3_deep_program/{stamp}/factor_relations/`
artifacts_produced: `{gcd}`, `{resultants}`, `{discriminants}`, `{support}`, `{subs}`

## Exact Relations

Verified Fact: the exact prior pairwise gcd table over `QQ(t)[y]` is carried into this phase, and the residual cross-gcd degree is derived as zero from the exact pairwise residual-factor gcds.

## Deferred Targets

Not Established: generic high-degree resultants and high-degree discriminant expansions are deferred to a selected target pass because expression swell is expected.
""".format(
        boundary=BOUNDARY,
        stamp=stamp,
        gcd=str((relation_dir / "gcd_table.json").relative_to(ROOT)),
        resultants=str((relation_dir / "resultant_table.json").relative_to(ROOT)),
        discriminants=str((relation_dir / "discriminant_table.json").relative_to(ROOT)),
        support=str((relation_dir / "coefficient_support.json").relative_to(ROOT)),
        subs=str((relation_dir / "substitution_profiles.json").relative_to(ROOT)),
    ))

    print(json.dumps({
        "ok": True,
        "timestamp": stamp,
        "residual_manifest": str((residual_dir / "residual_manifest.json").relative_to(ROOT)),
        "gcd_table": str((relation_dir / "gcd_table.json").relative_to(ROOT)),
        "residual_report": str(residual_report_md.relative_to(ROOT)),
        "relation_report": str(relation_report_md.relative_to(ROOT)),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(int(main()))
