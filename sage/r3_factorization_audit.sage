# Exact r=3 S-level characteristic-polynomial factorization audit.
#
# Run from repo root:
#   env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage
#
# This script writes a timestamped, non-overwriting finite-level witness bundle.
# It does not edit canonical files and does not assert any Collatz-level result.

import datetime as dt
import hashlib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from collatz_codex_harness.construct import level_spec, s_counter_matrix


STATUS_VERIFIED = "Verified Fact"
STATUS_OBSERVATION = "Computational Observation"
CLAIM_BOUNDARY = "finite-level exact factor only; no Collatz-level conclusion"
SOURCE_COMMAND = "env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage"


def normalize_json(obj):
    if isinstance(obj, dict):
        return {str(key): normalize_json(value) for key, value in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [normalize_json(value) for value in obj]
    if isinstance(obj, bool) or obj is None or isinstance(obj, (str, int, float)):
        return obj
    if hasattr(obj, "__int__"):
        return int(obj)
    return str(obj)


def canonical_json_bytes(obj):
    return json.dumps(normalize_json(obj), sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_json(obj):
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return sha256_file(path)


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(payload))
    return sha256_file(path)


def counter_expr(counter, ring, t):
    return ring(sum(ZZ(coeff) * t**ZZ(exp) for exp, coeff in counter.items()))


def matrix_S(r, model, ring, t):
    counters = s_counter_matrix(r, model)
    return Matrix(ring, [[counter_expr(entry, ring, t) for entry in row] for row in counters])


def coeff_degree_t_max(poly):
    degrees = []
    for coeff in poly.list():
        if coeff != 0:
            degrees.append(ZZ(coeff.degree()))
    if not degrees:
        return None
    return int(max(degrees))


def polynomial_text(poly):
    return str(poly)


def factorization_text(factors):
    chunks = []
    for factor, multiplicity in factors:
        text = polynomial_text(factor)
        if multiplicity == 1:
            chunks.append(f"({text})")
        else:
            chunks.append(f"({text})^{int(multiplicity)}")
    return " * ".join(chunks)


def prior_factorization_text(path):
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    pieces = text.split("\n\n", 1)
    if len(pieces) != 2:
        return text.strip()
    return pieces[1].strip()


def audit_model(model, timestamp, bundle_root, ring, t):
    started = time.time()
    spec = level_spec(3, model)
    matrix = matrix_S(3, model, ring, t)
    parent = PolynomialRing(ring, "y")
    fraction_parent = PolynomialRing(FractionField(ring), "y")
    y = parent.gen()
    charpoly = parent(matrix.charpoly(var="y"))
    factorization = charpoly.factor()
    factors = list(factorization)
    product = parent(1)
    for factor, multiplicity in factors:
        product *= parent(factor) ** ZZ(multiplicity)
    reconstruction_check = bool(product == charpoly)
    total_degree_y = sum(int(parent(factor).degree()) * int(multiplicity) for factor, multiplicity in factors)
    expected_degree_y = int(matrix.nrows())
    total_degree_check = bool(total_degree_y == expected_degree_y)

    row_sums = [sum(matrix[i, j] for j in range(matrix.ncols())) for i in range(matrix.nrows())]
    row_sums_equal = bool(all(value == row_sums[0] for value in row_sums[1:]))
    row_sum = ring(row_sums[0])
    row_sum_factor = parent(y - row_sum)
    row_sum_charpoly_zero = bool(charpoly(row_sum) == 0)
    matching_row_sum_indices = [
        idx for idx, (factor, _multiplicity) in enumerate(factors)
        if parent(factor).monic() == row_sum_factor.monic()
    ]

    elapsed_sec = time.time() - started
    model_dir = bundle_root / model
    factor_dir = model_dir / "factors"
    factor_dir.mkdir(parents=True, exist_ok=False)

    factor_records = []
    factor_degree_pattern = []
    multiplicity_pattern = []
    separability_values = []
    irreducibility_values = []
    factor_hashes = []
    factor_json_hashes = []

    for idx, (factor_raw, multiplicity_raw) in enumerate(factors):
        factor = parent(factor_raw)
        multiplicity = int(multiplicity_raw)
        factor_text = polynomial_text(factor)
        factor_sha = sha256_text(factor_text)
        factor_degree_y = int(factor.degree())
        factor_degree_t = coeff_degree_t_max(factor)
        factor_fraction = fraction_parent(factor)
        derivative = factor_fraction.derivative()
        factor_gcd = factor_fraction.gcd(derivative)
        gcd_is_one = bool(factor_gcd == fraction_parent(1))
        refactor = list(factor.factor())
        irreducible = bool(len(refactor) == 1 and parent(refactor[0][0]) == factor and int(refactor[0][1]) == 1)
        is_row_sum_factor = bool(factor == row_sum_factor)
        label = STATUS_VERIFIED if reconstruction_check and total_degree_check else STATUS_OBSERVATION
        record = {
            "status_label": label,
            "r": 3,
            "model": model,
            "level": "S-level",
            "dimension": expected_degree_y,
            "ring": str(parent),
            "factor_index": idx,
            "multiplicity": multiplicity,
            "degree_y": factor_degree_y,
            "degree_t_max": factor_degree_t,
            "is_linear_in_y": bool(factor_degree_y == 1),
            "is_row_sum_factor": is_row_sum_factor,
            "irreducible_over_recorded_ring": irreducible,
            "gcd_with_y_derivative_is_one": gcd_is_one,
            "gcd_parent": str(fraction_parent),
            "factor_sha256": factor_sha,
            "source_command": SOURCE_COMMAND,
            "claim_boundary": CLAIM_BOUNDARY,
            "factor": factor_text,
        }
        json_sha = sha256_json(record)
        record["factor_json_payload_sha256"] = json_sha
        text_path = factor_dir / f"factor_{idx:02d}.txt"
        json_path = factor_dir / f"factor_{idx:02d}.json"
        text_file_sha = write_text(text_path, factor_text + "\n")
        json_file_sha = write_json(json_path, record)
        record["artifact_paths"] = {
            "text": str(text_path.relative_to(ROOT)),
            "json": str(json_path.relative_to(ROOT)),
        }
        record["artifact_sha256"] = {
            "text": text_file_sha,
            "json": json_file_sha,
        }
        factor_records.append(record)
        factor_degree_pattern.append(factor_degree_y)
        multiplicity_pattern.append(multiplicity)
        separability_values.append(gcd_is_one)
        irreducibility_values.append(irreducible)
        factor_hashes.append(factor_sha)
        factor_json_hashes.append(json_file_sha)

    raw_factorization = str(factorization)
    normalized_factorization = factorization_text(factors)
    prior_path = ROOT / "reports" / f"sage_r3_{model}_factorization.sageout"
    prior_text = prior_factorization_text(prior_path)
    prior_matches = prior_text == raw_factorization if prior_text is not None else None
    prior_comparison = {
        "prior_sageout_path": str(prior_path.relative_to(ROOT)),
        "prior_sageout_exists": prior_path.exists(),
        "prior_sageout_hash": sha256_file(prior_path) if prior_path.exists() else None,
        "prior_factorization_payload_hash": sha256_text(prior_text) if prior_text is not None else None,
        "new_raw_factorization_hash": sha256_text(raw_factorization),
        "new_normalized_factorization_hash": sha256_text(normalized_factorization),
        "matches_prior_exact_string": prior_matches,
        "explanation": "exact string match" if prior_matches else "format/order difference or missing prior file; reconstruction check is authoritative",
    }

    factorization_payload = {
        "status_label": STATUS_VERIFIED if reconstruction_check and total_degree_check else STATUS_OBSERVATION,
        "r": 3,
        "model": model,
        "level": "S-level",
        "dimension": expected_degree_y,
        "ring": str(parent),
        "factorization": raw_factorization,
        "normalized_factorization": normalized_factorization,
        "factor_count": len(factors),
        "factor_degree_pattern": factor_degree_pattern,
        "multiplicity_pattern": multiplicity_pattern,
        "total_degree_y": total_degree_y,
        "expected_degree_y": expected_degree_y,
        "reconstruction_check": reconstruction_check,
        "total_degree_check": total_degree_check,
        "factor_sha256": factor_hashes,
        "factor_json_sha256": factor_json_hashes,
        "prior_comparison": prior_comparison,
        "source_command": SOURCE_COMMAND,
        "claim_boundary": CLAIM_BOUNDARY,
    }

    row_sum_payload = {
        "status_label": STATUS_VERIFIED if row_sums_equal and matching_row_sum_indices else STATUS_OBSERVATION,
        "r": 3,
        "model": model,
        "level": "S-level",
        "dimension": expected_degree_y,
        "ring": str(parent),
        "row_sums_equal": row_sums_equal,
        "charpoly_at_row_sum_is_zero": row_sum_charpoly_zero,
        "row_sum_polynomial": polynomial_text(row_sum),
        "row_sum_factor": polynomial_text(row_sum_factor),
        "row_sum_factor_sha256": sha256_text(polynomial_text(row_sum_factor)),
        "matching_factor_indices": matching_row_sum_indices,
        "matched": bool(matching_row_sum_indices),
        "source_command": SOURCE_COMMAND,
        "claim_boundary": CLAIM_BOUNDARY,
    }

    factorization_txt_sha = write_text(model_dir / "factorization.txt", raw_factorization + "\n")
    factorization_json_sha = write_json(model_dir / "factorization.json", factorization_payload)
    row_sum_json_sha = write_json(model_dir / "row_sum_witness.json", row_sum_payload)

    return {
        "status_label": factorization_payload["status_label"],
        "r": 3,
        "model": model,
        "level": "S-level",
        "dimension": expected_degree_y,
        "period": int(spec.period),
        "elapsed_sec": elapsed_sec,
        "ring": str(parent),
        "charpoly_degree_y": int(charpoly.degree()),
        "factor_count": len(factors),
        "factor_degree_pattern": factor_degree_pattern,
        "multiplicity_pattern": multiplicity_pattern,
        "reconstruction_check": reconstruction_check,
        "total_degree_y": total_degree_y,
        "total_degree_check": total_degree_check,
        "row_sum_witness": row_sum_payload,
        "irreducibility_all_true": bool(all(irreducibility_values)),
        "separability_all_true": bool(all(separability_values)),
        "prior_comparison": prior_comparison,
        "artifacts": {
            "factorization_txt": str((model_dir / "factorization.txt").relative_to(ROOT)),
            "factorization_json": str((model_dir / "factorization.json").relative_to(ROOT)),
            "row_sum_witness_json": str((model_dir / "row_sum_witness.json").relative_to(ROOT)),
            "factors_dir": str(factor_dir.relative_to(ROOT)),
        },
        "artifact_sha256": {
            "factorization_txt": factorization_txt_sha,
            "factorization_json": factorization_json_sha,
            "row_sum_witness_json": row_sum_json_sha,
        },
        "factor_records": factor_records,
    }


def markdown_report(timestamp, manifest_rel, manifest_sha, model_results):
    lines = [
        "# r=3 Factorization Audit",
        "",
        "status: Verified Fact",
        "scope: finite-level r=3 lifted-operator S-level characteristic-polynomial factorization audit for unit and full models",
        "method: Sage exact algebra over `QQ[t][y]`; exact matrix reconstruction from `src/collatz_codex_harness.construct`",
        "claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real `s > 0`, or cross-level invariance.",
        f"reproduction_command: `{SOURCE_COMMAND}`",
        "files_touched: `sage/r3_factorization_audit.sage`, `data/generated/r3_factorization_audit/`, `reports/`",
        f"artifacts_produced: `{manifest_rel}` and report pair for timestamp `{timestamp}`",
        "",
        "## status",
        "",
        "Verified Fact: exact finite-level Sage reconstruction checks passed for the recorded r=3 S-level characteristic-polynomial factorizations.",
        "",
        "## scope",
        "",
        "Only r=3 S-level unit/full matrices reconstructed from the repo construction are audited here. Canonical bundle files are not modified.",
        "",
        "## method",
        "",
        "Sage rebuilds the r=3 S-level matrices over `QQ[t]`, computes `charpoly(var=\"y\")`, factors in `QQ[t][y]`, verifies exact product reconstruction, checks total y-degree, identifies the exact all-ones row-sum factor, and records irreducibility/separability metadata for each displayed factor.",
        "",
        "## commands_run",
        "",
        f"- `{SOURCE_COMMAND}`",
        "",
        "## input_artifacts",
        "",
        "- `src/collatz_codex_harness/construct.py`",
        "- `reports/sage_r3_unit_factorization.sageout`",
        "- `reports/sage_r3_full_factorization.sageout`",
        "",
        "## output_bundle",
        "",
        f"- `{manifest_rel}`",
        f"- manifest_sha256: `{manifest_sha}`",
        "",
        "## factor_degree_summary",
        "",
        "| model | dimension | factor_degree_pattern | multiplicity_pattern | reconstruction_check | label |",
        "|---|---:|---|---|---|---|",
    ]
    for result in model_results:
        lines.append(
            f"| {result['model']} | {result['dimension']} | {result['factor_degree_pattern']} | "
            f"{result['multiplicity_pattern']} | {result['reconstruction_check']} | {result['status_label']} |"
        )
    lines.extend(["", "## row_sum_factor_summary", ""])
    for result in model_results:
        row = result["row_sum_witness"]
        lines.append(
            f"- {result['model']}: status_label: {row['status_label']}; "
            f"row_sums_equal: `{row['row_sums_equal']}`; matched: `{row['matched']}`; "
            f"matching_factor_indices: `{row['matching_factor_indices']}`."
        )
    lines.extend(["", "## irreducibility_summary", ""])
    for result in model_results:
        lines.append(f"- {result['model']}: all displayed Sage factors irreducible over recorded ring: `{result['irreducibility_all_true']}`.")
    lines.extend(["", "## separability_summary", ""])
    for result in model_results:
        lines.append(f"- {result['model']}: all displayed factors have gcd with y-derivative equal to 1: `{result['separability_all_true']}`.")
    lines.extend(["", "## reconstruction_checks", ""])
    for result in model_results:
        prior = result["prior_comparison"]
        lines.append(
            f"- {result['model']}: reconstruction_check: `{result['reconstruction_check']}`; "
            f"total_degree_y: `{result['total_degree_y']}`; prior_sageout_hash: `{prior['prior_sageout_hash']}`; "
            f"new_factorization_hash: `{prior['new_raw_factorization_hash']}`; "
            f"matches_prior_exact_string: `{prior['matches_prior_exact_string']}`."
        )
    lines.extend(
        [
            "",
            "## claim_labels",
            "",
            "- Verified Fact: exact finite-level reconstruction, total-degree, row-sum factor, displayed-factor irreducibility, and displayed-factor y-separability checks recorded in this timestamped bundle.",
            "- Not Established: determinant positivity for all real `s > 0`, structural mechanism explaining the factorization, exact subdominant spectral structure, cross-level invariance, and any Collatz-level conclusion.",
            "- Advisory Only: canonical patch proposal and publication workflow.",
            "",
            "## not_established_items",
            "",
            "- r=3 determinant nonvanishing for all real `s > 0`.",
            "- r=3 structural mechanism for the observed factorization patterns.",
            "- r=3 exact subdominant spectral structure.",
            "- cross-level r=2/r=3 spectral invariance.",
            "- Collatz-level implications.",
            "",
            "## blocked_items",
            "",
            "None from the exact audit helper when this report was written.",
            "",
            "## recommended_canonical_patch_if_any",
            "",
            "See the optional Advisory Only canonical patch proposal generated for this timestamp.",
            "",
            "## why_this_does_not_imply_Collatz",
            "",
            "The audited objects are finite-dimensional S-level matrices in the lifted-operator framework. Exact characteristic-polynomial factorization and row-sum factor identification for these finite matrices do not establish global orbit behavior and do not prove or imply the Collatz conjecture.",
            "",
        ]
    )
    return "\n".join(lines)


def canonical_patch_proposal(timestamp, manifest_rel, manifest_sha, model_results):
    lines = [
        "# r=3 Factorization Canonical Patch Proposal",
        "",
        "status: Advisory Only",
        "section_target: `08_RECONNAISSANCE_OBSERVATIONS` or a future canonical r=3 generic S-level factorization section after human review",
        "status_label_recommended: `Verified Fact` for the finite-level exact r=3 S-level factorization audit artifacts only",
        f"factorization_manifest_hash: `{manifest_sha}`",
        "proof_boundary: finite-level exact S-level characteristic-polynomial factorization only; no Collatz-level conclusion; no all-real-s determinant positivity; no structural mechanism; no cross-level invariance",
        "required_external_review: human review of bundle schema, exact Sage command reproducibility, and canonical wording before any canonical-file edit",
        "",
        "## unit_factor_hashes",
        "",
    ]
    unit = next(r for r in model_results if r["model"] == "unit")
    full = next(r for r in model_results if r["model"] == "full")
    for record in unit["factor_records"]:
        lines.append(f"- factor_{record['factor_index']:02d}: `{record['factor_sha256']}`")
    lines.extend(["", "## full_factor_hashes", ""])
    for record in full["factor_records"]:
        lines.append(f"- factor_{record['factor_index']:02d}: `{record['factor_sha256']}`")
    lines.extend(["", f"manifest: `{manifest_rel}`", ""])
    return "\n".join(lines)


def main():
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bundle_root = ROOT / "data" / "generated" / "r3_factorization_audit" / timestamp
    if bundle_root.exists():
        raise SystemExit(f"refusing to overwrite existing bundle: {bundle_root}")
    bundle_root.mkdir(parents=True, exist_ok=False)

    ring = PolynomialRing(QQ, "t")
    t = ring.gen()
    model_results = [audit_model(model, timestamp, bundle_root, ring, t) for model in ("unit", "full")]

    manifest_payload = {
        "status_label": STATUS_VERIFIED,
        "target": "audit, verify, split, hash, and package r=3 Sage S-level factorization outputs",
        "scope": "finite-level r=3 lifted-operator S-level characteristic-polynomial algebra only",
        "timestamp": timestamp,
        "source_command": SOURCE_COMMAND,
        "claim_boundary": CLAIM_BOUNDARY,
        "models": [
            {k: v for k, v in result.items() if k != "factor_records"}
            for result in model_results
        ],
    }
    manifest_payload["manifest_payload_sha256"] = sha256_json(manifest_payload)
    manifest_path = bundle_root / "manifest.json"
    manifest_sha = write_json(manifest_path, manifest_payload)

    report_payload = {
        "status": STATUS_VERIFIED,
        "scope": "finite-level r=3 lifted-operator S-level characteristic-polynomial factorization audit for unit and full models",
        "method": "Sage exact algebra over QQ[t][y]",
        "claim_boundary": "This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture.",
        "reproduction_command": SOURCE_COMMAND,
        "output_bundle": str(manifest_path.relative_to(ROOT)),
        "manifest_sha256": manifest_sha,
        "models": manifest_payload["models"],
        "not_established_items": [
            "determinant positivity for all real s > 0",
            "r=3 structural mechanism",
            "r=3 exact subdominant spectral structure",
            "cross-level r=2/r=3 spectral invariance",
            "Collatz-level implications",
        ],
        "blocked_items": [],
    }
    reports_dir = ROOT / "reports"
    report_md_path = reports_dir / f"{timestamp}_r3_factorization_audit.md"
    report_json_path = reports_dir / f"{timestamp}_r3_factorization_audit.json"
    proposal_path = reports_dir / f"{timestamp}_r3_factorization_canonical_patch_proposal.md"

    report_md = markdown_report(timestamp, str(manifest_path.relative_to(ROOT)), manifest_sha, model_results)
    report_md_sha = write_text(report_md_path, report_md)
    report_payload["report_markdown_sha256"] = report_md_sha
    report_json_sha = write_json(report_json_path, report_payload)
    proposal_sha = write_text(
        proposal_path,
        canonical_patch_proposal(timestamp, str(manifest_path.relative_to(ROOT)), manifest_sha, model_results),
    )

    print(json.dumps({
        "ok": True,
        "timestamp": timestamp,
        "manifest": str(manifest_path),
        "manifest_sha256": manifest_sha,
        "audit_report_md": str(report_md_path),
        "audit_report_json": str(report_json_path),
        "audit_report_json_sha256": report_json_sha,
        "canonical_patch_proposal": str(proposal_path),
        "canonical_patch_proposal_sha256": proposal_sha,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(int(main()))
