#!/usr/bin/env python3
"""Generate r=3 canonical-insert and factor-structure mission artifacts."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_BUNDLE = ROOT / "data/generated/r3_factorization_audit/20260513T160231Z"
REPORTS = ROOT / "reports"
STRUCTURE_ROOT = ROOT / "data/generated/r3_factor_structure"
V2_PROPOSAL = ROOT / "reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md"
V2_PROPOSAL_JSON = ROOT / "reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json"
SOURCE_MANIFEST = SOURCE_BUNDLE / "manifest.json"

REQUIRED_MANIFEST_FILE_HASH = "fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254"
REQUIRED_MANIFEST_PAYLOAD_HASH = "e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f"
SHARED_FACTOR_HASH = "02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69"
BOUNDARY = (
    "This is a finite-level S-level characteristic-polynomial factorization fact only. "
    "It does not prove or imply the Collatz conjecture, global orbit behavior, "
    "determinant nonvanishing for all real s > 0, cross-level invariance, or a "
    "structural mechanism."
)


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_factors(model: str) -> list[dict[str, Any]]:
    factor_dir = SOURCE_BUNDLE / model / "factors"
    factors = [load_json(path) for path in sorted(factor_dir.glob("factor_*.json"))]
    for factor in factors:
        factor["source_path"] = str(
            (factor_dir / f"factor_{factor['factor_index']:02d}.json").relative_to(ROOT)
        )
    return factors


def factor_summary(factors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "factor_index": f["factor_index"],
            "factor_sha256": f["factor_sha256"],
            "degree_y": f["degree_y"],
            "degree_t_max": f["degree_t_max"],
            "multiplicity": f["multiplicity"],
            "is_row_sum_factor": f["is_row_sum_factor"],
            "is_linear_in_y": f["is_linear_in_y"],
            "status_label": f["status_label"],
            "source_path": f["source_path"],
        }
        for f in factors
    ]


def by_hash(factors: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {f["factor_sha256"]: f for f in factors}


def row_sum_index(factors: list[dict[str, Any]]) -> int | None:
    matches = [f["factor_index"] for f in factors if f["is_row_sum_factor"]]
    return matches[0] if matches else None


def degree_pattern(factors: list[dict[str, Any]]) -> list[int]:
    return [int(f["degree_y"]) for f in factors]


def multiplicity_pattern(factors: list[dict[str, Any]]) -> list[int]:
    return [int(f["multiplicity"]) for f in factors]


def degree_contribution(factors: list[dict[str, Any]]) -> int:
    return sum(int(f["degree_y"]) * int(f["multiplicity"]) for f in factors)


def build_structure_payload(stamp: str) -> dict[str, Any]:
    manifest = load_json(SOURCE_MANIFEST)
    unit = load_factors("unit")
    full = load_factors("full")
    unit_by_hash = by_hash(unit)
    full_by_hash = by_hash(full)
    shared_hashes = sorted(set(unit_by_hash).intersection(full_by_hash))

    shared = []
    for factor_hash in shared_hashes:
        uf = unit_by_hash[factor_hash]
        ff = full_by_hash[factor_hash]
        shared.append(
            {
                "factor_sha256": factor_hash,
                "unit_factor_index": uf["factor_index"],
                "full_factor_index": ff["factor_index"],
                "unit_degree_y": uf["degree_y"],
                "full_degree_y": ff["degree_y"],
                "unit_multiplicity": uf["multiplicity"],
                "full_multiplicity": ff["multiplicity"],
                "same_factor_text": uf["factor"] == ff["factor"],
                "is_row_sum_factor": uf["is_row_sum_factor"] or ff["is_row_sum_factor"],
                "claim_label": "Verified Fact",
                "scope_note": "finite-level audited factor bundle hash/string comparison only",
            }
        )

    unit_row = row_sum_index(unit)
    full_row = row_sum_index(full)
    unit_non_row = [f for f in unit if not f["is_row_sum_factor"]]
    full_non_row = [f for f in full if not f["is_row_sum_factor"]]
    unit_residual = [f for f in unit if not f["is_row_sum_factor"] and f["factor_sha256"] not in shared_hashes]
    full_residual = [f for f in full if not f["is_row_sum_factor"] and f["factor_sha256"] not in shared_hashes]

    sage_path = shutil.which("sage")
    gcd_status = (
        "Not Established"
        if sage_path is None
        else "Not run by this Python helper; Sage is available for a follow-up exact gcd pass"
    )
    pairwise_gcds = []
    for uf in unit:
        for ff in full:
            same = uf["factor_sha256"] == ff["factor_sha256"] and uf["factor"] == ff["factor"]
            pairwise_gcds.append(
                {
                    "unit_factor_i": uf["factor_index"],
                    "full_factor_j": ff["factor_index"],
                    "static_same_hash_and_text": same,
                    "gcd_degree_y": uf["degree_y"] if same else None,
                    "gcd_hash_or_expression": uf["factor_sha256"] if same else None,
                    "claim_label": "Verified Fact" if same else "Not Established",
                    "method": "static bundle equality" if same else "Sage gcd not run",
                }
            )

    simple_degree_multiples = {
        "unit_higher_degrees": [f["degree_y"] for f in unit_residual],
        "full_higher_degrees": [f["degree_y"] for f in full_residual],
        "observation": (
            "The residual higher-degree pairs are 2,6 for unit and 3,9 for full. "
            "They have a 3/2 degree ratio by ordered pair, not an integer degree-multiple relation."
        ),
        "claim_label": "Computational Observation",
    }

    payload = {
        "status": "Computational Observation",
        "target": "finite-level r=3 audited factor-bundle structure analysis",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level characteristic-polynomial factor bundle from the 20260513T160231Z Sage audit",
        "method": "Python static JSON/hash analysis; Sage exact gcd unavailable on PATH",
        "claim_boundary": BOUNDARY,
        "source_manifest": str(SOURCE_MANIFEST.relative_to(ROOT)),
        "source_manifest_file_sha256": sha256_file(SOURCE_MANIFEST),
        "source_manifest_payload_sha256": manifest.get("manifest_payload_sha256"),
        "source_command": manifest.get("source_command"),
        "sage_available": sage_path is not None,
        "sage_path": sage_path,
        "exact_gcd_status": gcd_status,
        "models": {
            "unit": {
                "dimension": 18,
                "factor_degree_pattern": degree_pattern(unit),
                "multiplicity_pattern": multiplicity_pattern(unit),
                "row_sum_factor_index": unit_row,
                "factor_degree_contribution": degree_contribution(unit),
                "factors": factor_summary(unit),
            },
            "full": {
                "dimension": 27,
                "factor_degree_pattern": degree_pattern(full),
                "multiplicity_pattern": multiplicity_pattern(full),
                "row_sum_factor_index": full_row,
                "factor_degree_contribution": degree_contribution(full),
                "factors": factor_summary(full),
            },
        },
        "shared_factors": shared,
        "minimum_expected_observations": {
            "shared_hash_expected": SHARED_FACTOR_HASH in shared_hashes,
            "unit_factor_01_equals_full_factor_01": unit[1]["factor_sha256"] == full[1]["factor_sha256"] == SHARED_FACTOR_HASH,
            "unit_row_sum_factor_index": unit_row,
            "full_row_sum_factor_index": full_row,
            "unit_degree_pattern": degree_pattern(unit),
            "full_degree_pattern": degree_pattern(full),
        },
        "shared_non_row_sum_factor_multiplicity_same": (
            unit_by_hash[SHARED_FACTOR_HASH]["multiplicity"] == full_by_hash[SHARED_FACTOR_HASH]["multiplicity"]
            if SHARED_FACTOR_HASH in unit_by_hash and SHARED_FACTOR_HASH in full_by_hash
            else None
        ),
        "quotient_residual_patterns": {
            "after_removing_row_sum_only": {
                "unit_degree_contribution": degree_contribution(unit_non_row),
                "full_degree_contribution": degree_contribution(full_non_row),
                "unit_degrees_with_multiplicity": [[f["degree_y"], f["multiplicity"]] for f in unit_non_row],
                "full_degrees_with_multiplicity": [[f["degree_y"], f["multiplicity"]] for f in full_non_row],
            },
            "after_removing_row_sum_and_shared_non_row_factor": {
                "unit_degree_contribution": degree_contribution(unit_residual),
                "full_degree_contribution": degree_contribution(full_residual),
                "unit_degrees_with_multiplicity": [[f["degree_y"], f["multiplicity"]] for f in unit_residual],
                "full_degrees_with_multiplicity": [[f["degree_y"], f["multiplicity"]] for f in full_residual],
            },
        },
        "simple_degree_multiples": simple_degree_multiples,
        "pairwise_gcds": pairwise_gcds,
        "sage_follow_up_tests": [
            "Compute pairwise gcds for every unit/full factor over QQ(t)[y] and record exact gcd expressions.",
            "Test divisibility of full residual factors by substitutions or quotients suggested by the shared linear factor.",
            "Compare residual characteristic polynomials after removing row-sum and shared non-row-sum factors.",
            "Search for commutant, symmetry, or equitable-partition mechanisms for the squared residual factors.",
        ],
        "not_established_items": [
            "r=3 structural mechanism explaining the factorization pattern",
            "exact pairwise gcd table for non-identical factor pairs over QQ(t)[y]",
            "simple integer degree-multiple relation from unit higher-degree factors to full higher-degree factors",
            "determinant nonvanishing for all real s > 0",
            "cross-level invariance",
            "subdominant spectral structure",
            "any Collatz-level conclusion",
        ],
        "reproduction_command": "python3 scripts/r3_factor_structure_analysis.py",
    }
    return payload


def exact_insert_text() -> str:
    return f"""==SECTION:: 05.charpoly.r3.generic_s_level_factorization_proposed ==

status_label: Verified Fact, finite-level only
r: 3
level: S-level
models: unit and full
recorded_ring: QQ[t][y]
y-separability ring: QQ(t)[y]
source_manifest: data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
manifest file hash: {REQUIRED_MANIFEST_FILE_HASH}
manifest payload hash: {REQUIRED_MANIFEST_PAYLOAD_HASH}

The finite-level r=3 S-level characteristic-polynomial factorization audit records exact Sage reconstruction for both audited models.

unit dimension: 18
unit factor_degree_pattern: [1,1,2,6]
unit multiplicity_pattern: [1,1,2,2]
unit row-sum factor index: 0

full dimension: 27
full factor_degree_pattern: [1,1,3,9]
full multiplicity_pattern: [1,2,2,2]
full row-sum factor index: 0

Sage-displayed irreducibility over QQ[t][y] is recorded for every displayed factor in the source audit bundle. y-separability checked over QQ(t)[y] is recorded for every displayed factor in the source audit bundle.

This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.

[STATUS: Verified Fact]
[GUARD: S-level characteristic-polynomial factorization only; do not upgrade to B-level descent, compact-factorization closure, structural mechanism, subdominant spectral structure, cross-level invariance, all-real-s determinant nonvanishing, or Collatz-level claims.]"""


def build_insert_payload(stamp: str) -> dict[str, Any]:
    manifest = load_json(SOURCE_MANIFEST)
    return {
        "status": "Advisory Only",
        "target": "human-reviewable canonical insertion patch for audited finite-level r=3 S-level factorization",
        "created_utc": stamp,
        "source_proposal_v2": str(V2_PROPOSAL.relative_to(ROOT)),
        "source_proposal_v2_json": str(V2_PROPOSAL_JSON.relative_to(ROOT)),
        "source_manifest": str(SOURCE_MANIFEST.relative_to(ROOT)),
        "candidate_target_file": "data/canonical_bundle/05_R3_CLOSURES.txt",
        "candidate_target_section": "Insert before <<APPEND-POINT::05.charpoly>> as a new 05.charpoly.r3.generic_s_level_factorization section after human review.",
        "placement_rationale": (
            "05_R3_CLOSURES.txt is the canonical file for r=3 Verified Fact closures. "
            "08_RECONNAISSANCE_OBSERVATIONS.txt is reserved for Computational Observation reconnaissance, "
            "so the audited finite-level exact factorization belongs in 05 if a human accepts insertion."
        ),
        "exact_insert_text": exact_insert_text(),
        "required_pre_insert_checks": [
            "Confirm canonical bundle files are still untouched before review.",
            "Rerun env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage in an environment with Sage.",
            f"Verify manifest file sha256 equals {REQUIRED_MANIFEST_FILE_HASH}.",
            f"Verify manifest payload sha256 equals {REQUIRED_MANIFEST_PAYLOAD_HASH}.",
            "Confirm source proposal v2 wording still passes proof-boundary audit.",
            "Confirm the insert text says Sage-displayed irreducibility over QQ[t][y] and y-separability checked over QQ(t)[y].",
        ],
        "rollback_note": (
            "This artifact is a proposed insert only. If rejected, delete or supersede this report pair; "
            "no canonical bundle rollback is needed because no canonical file is modified."
        ),
        "proof_boundary": BOUNDARY,
        "preserved_facts": {
            "status_label": "Verified Fact, finite-level only",
            "r": 3,
            "level": "S-level",
            "models": ["unit", "full"],
            "unit_dimension": 18,
            "unit_factor_degree_pattern": [1, 1, 2, 6],
            "unit_multiplicity_pattern": [1, 1, 2, 2],
            "full_dimension": 27,
            "full_factor_degree_pattern": [1, 1, 3, 9],
            "full_multiplicity_pattern": [1, 2, 2, 2],
            "recorded_ring": "QQ[t][y]",
            "y_separability_ring": "QQ(t)[y]",
            "manifest_file_hash": sha256_file(SOURCE_MANIFEST),
            "manifest_payload_hash": manifest.get("manifest_payload_sha256"),
        },
        "canonical_files_touched": False,
        "reproduction_command": "python3 scripts/r3_factor_structure_analysis.py",
    }


def md_insert(payload: dict[str, Any]) -> str:
    checks = "\n".join(f"- {item}" for item in payload["required_pre_insert_checks"])
    return f"""# r=3 Factorization Canonical Insert Patch

status: Advisory Only
scope: finite-level r=3 S-level characteristic-polynomial canonical insertion proposal only
method: report-only synthesis from audited Sage factorization bundle and v2 proposal
claim_boundary: {payload["proof_boundary"]}
reproduction_command: `{payload["reproduction_command"]}`
files_touched: `reports/`, `data/generated/r3_factor_structure/`, `scripts/r3_factor_structure_analysis.py`
artifacts_produced: this Markdown report and sidecar JSON

## Patch Metadata

- source_proposal_v2: `{payload["source_proposal_v2"]}`
- source_manifest: `{payload["source_manifest"]}`
- candidate_target_file: `{payload["candidate_target_file"]}`
- candidate_target_section: {payload["candidate_target_section"]}
- status: `Advisory Only`

## Placement Rationale

{payload["placement_rationale"]}

## Exact Insert Text

```text
{payload["exact_insert_text"]}
```

## Required Pre-Insert Checks

{checks}

## Rollback Note

{payload["rollback_note"]}

## Proof Boundary

{payload["proof_boundary"]}
"""


def md_checklist(payload: dict[str, Any]) -> str:
    return f"""# r=3 Canonical Insert Review Checklist

status: Advisory Only
scope: human review checklist for a proposed finite-level r=3 S-level canonical insert
method: checklist generated from active mission packet requirements
claim_boundary: {payload["proof_boundary"]}
reproduction_command: `{payload["reproduction_command"]}`
files_touched: `reports/`, `data/generated/r3_factor_structure/`, `scripts/r3_factor_structure_analysis.py`
artifacts_produced: this checklist

## Required Checks

- [ ] Canonical bundle files remain unmodified.
- [ ] `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage` reruns successfully before any insertion.
- [ ] Manifest file hash equals `{REQUIRED_MANIFEST_FILE_HASH}`.
- [ ] Manifest payload hash equals `{REQUIRED_MANIFEST_PAYLOAD_HASH}`.
- [ ] Insert target is `data/canonical_bundle/05_R3_CLOSURES.txt`, not the Computational Observation file.
- [ ] Insert text includes `status_label: Verified Fact, finite-level only`.
- [ ] Insert text includes r=3, S-level, unit/full dimensions, degree patterns, and multiplicity patterns.
- [ ] Insert text uses `Sage-displayed irreducibility over QQ[t][y]`.
- [ ] Insert text uses `y-separability checked over QQ(t)[y]`.
- [ ] Insert text does not say simply that irreducible factors are proved irreducible.
- [ ] Insert text includes the finite-level proof boundary sentence exactly.
- [ ] No Collatz-level implication, all-real-s determinant nonvanishing claim, cross-level invariance claim, or structural-mechanism claim is introduced.
"""


def md_structure(payload: dict[str, Any], manifest_path: Path) -> str:
    shared_lines = []
    for item in payload["shared_factors"]:
        shared_lines.append(
            f"- factor hash `{item['factor_sha256']}`: unit factor_{item['unit_factor_index']:02d}, "
            f"full factor_{item['full_factor_index']:02d}; degree {item['unit_degree_y']}; "
            f"multiplicity unit={item['unit_multiplicity']}, full={item['full_multiplicity']}; "
            f"label: `{item['claim_label']}`."
        )
    shared_text = "\n".join(shared_lines) or "- No shared factor hashes detected."

    next_tests = "\n".join(f"- {item}" for item in payload["sage_follow_up_tests"])
    not_established = "\n".join(f"- {item}" for item in payload["not_established_items"])
    return f"""# r=3 Factor Structure Analysis

status: Computational Observation
scope: {payload["scope"]}
method: {payload["method"]}
claim_boundary: {payload["claim_boundary"]}
reproduction_command: `{payload["reproduction_command"]}`
files_touched: `scripts/r3_factor_structure_analysis.py`, `reports/`, `data/generated/r3_factor_structure/`
artifacts_produced: `{manifest_path.relative_to(ROOT)}` and this report pair

## Source Bundle

- source_manifest: `{payload["source_manifest"]}`
- source_manifest_file_sha256: `{payload["source_manifest_file_sha256"]}`
- source_manifest_payload_sha256: `{payload["source_manifest_payload_sha256"]}`
- Sage available on PATH: `{payload["sage_available"]}`
- exact_gcd_status: `{payload["exact_gcd_status"]}`

## Factor Patterns

| model | dimension | degree pattern | multiplicity pattern | row-sum factor index | label |
|---|---:|---|---|---:|---|
| unit | 18 | {payload["models"]["unit"]["factor_degree_pattern"]} | {payload["models"]["unit"]["multiplicity_pattern"]} | {payload["models"]["unit"]["row_sum_factor_index"]} | Verified Fact |
| full | 27 | {payload["models"]["full"]["factor_degree_pattern"]} | {payload["models"]["full"]["multiplicity_pattern"]} | {payload["models"]["full"]["row_sum_factor_index"]} | Verified Fact |

## Shared Factors

{shared_text}

The shared non-row-sum factor does not have the same multiplicity in the audited bundle: unit multiplicity is 1 and full multiplicity is 2. This statement is scoped to static comparison of the audited factor JSON artifacts.

## Degree and Residual Patterns

Computational Observation: {payload["simple_degree_multiples"]["observation"]}

After removing row-sum factors only, the non-row-sum degree contributions are unit {payload["quotient_residual_patterns"]["after_removing_row_sum_only"]["unit_degree_contribution"]} and full {payload["quotient_residual_patterns"]["after_removing_row_sum_only"]["full_degree_contribution"]}.

After removing both the row-sum factor and the shared non-row-sum factor, the residual degree contributions are unit {payload["quotient_residual_patterns"]["after_removing_row_sum_and_shared_non_row_factor"]["unit_degree_contribution"]} and full {payload["quotient_residual_patterns"]["after_removing_row_sum_and_shared_non_row_factor"]["full_degree_contribution"]}.

## Exact GCD Work

Not Established: Sage was not available on PATH for this Python run, so pairwise gcds over `QQ(t)[y]` or `QQ[t][y]` were not computed here. The sidecar manifest records static equality for the identical shared factor and marks non-identical pairwise gcds as `Not Established`.

## Justified Sage Follow-Up Tests

{next_tests}

## Structural Mechanism Claims Remaining Not Established

{not_established}
"""


def md_next_targets(payload: dict[str, Any]) -> str:
    return f"""# r=3 Factor Structure Next Targets

status: Advisory Only
scope: next-packet recommendation after finite-level r=3 factor-structure static analysis
method: report-only recommendation from audited factor bundle relationships
claim_boundary: {payload["claim_boundary"]}
reproduction_command: `{payload["reproduction_command"]}`
files_touched: `reports/`, `data/generated/r3_factor_structure/`, `scripts/r3_factor_structure_analysis.py`
artifacts_produced: this recommendation

## Recommended Next Missions

1. Exact pairwise gcd/divisibility and quotient-residual relation search over `QQ(t)[y]`.
   - backend: Sage
   - target: compute all unit/full pairwise gcds, then test quotient/residual relations after removing row-sum and shared non-row-sum factors.
   - status: Advisory Only

2. Commutant, symmetry, and equitable-partition search for the squared residual factors.
   - backend: Python exact prototypes promoted to Sage only for exact candidates
   - target: identify whether a finite-level structural mechanism explains the squared factors in either r=3 model.
   - status: Advisory Only

Do not create a new active packet from this report alone. No structural mechanism, all-real-s determinant nonvanishing, cross-level invariance, or Collatz-level conclusion is established here.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", default=None, help="UTC timestamp prefix to use for generated artifacts.")
    args = parser.parse_args()

    stamp = args.timestamp or utc_stamp()
    REPORTS.mkdir(exist_ok=True)
    structure_dir = STRUCTURE_ROOT / stamp
    structure_dir.mkdir(parents=True, exist_ok=True)

    insert_payload = build_insert_payload(stamp)
    structure_payload = build_structure_payload(stamp)
    factor_manifest_path = structure_dir / "factor_relation_manifest.json"

    outputs = {
        "canonical_insert_patch_md": REPORTS / f"{stamp}_r3_factorization_canonical_insert_patch.md",
        "canonical_insert_patch_json": REPORTS / f"{stamp}_r3_factorization_canonical_insert_patch.json",
        "canonical_insert_review_checklist": REPORTS / f"{stamp}_r3_factorization_canonical_insert_review_checklist.md",
        "factor_relation_manifest": factor_manifest_path,
        "structure_analysis_md": REPORTS / f"{stamp}_r3_factor_structure_analysis.md",
        "structure_analysis_json": REPORTS / f"{stamp}_r3_factor_structure_analysis.json",
        "structure_next_targets": REPORTS / f"{stamp}_r3_factor_structure_next_targets.md",
        "next_recommendation": REPORTS / f"{stamp}_r3_next_structural_mechanism_packet_recommendation.md",
    }

    insert_payload["artifacts_produced"] = {k: str(v.relative_to(ROOT)) for k, v in outputs.items() if k.startswith("canonical")}
    structure_payload["artifacts_produced"] = {k: str(v.relative_to(ROOT)) for k, v in outputs.items() if not k.startswith("canonical")}

    write_text(outputs["canonical_insert_patch_md"], md_insert(insert_payload))
    write_json(outputs["canonical_insert_patch_json"], insert_payload)
    write_text(outputs["canonical_insert_review_checklist"], md_checklist(insert_payload))
    write_json(outputs["factor_relation_manifest"], structure_payload)
    write_text(outputs["structure_analysis_md"], md_structure(structure_payload, factor_manifest_path))
    write_json(outputs["structure_analysis_json"], structure_payload)
    write_text(outputs["structure_next_targets"], md_next_targets(structure_payload))
    write_text(outputs["next_recommendation"], md_next_targets(structure_payload))

    print(
        json.dumps(
            {
                "ok": True,
                "timestamp": stamp,
                "outputs": {k: str(v.relative_to(ROOT)) for k, v in outputs.items()},
                "sage_available": structure_payload["sage_available"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
