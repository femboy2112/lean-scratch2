# r=3 Factorization Canonical Patch Proposal v2

status: Advisory Only
source_audit_report: `reports/20260513T160231Z_r3_factorization_audit.md`
source_manifest: `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json`
original_proposal: `reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md`
factorization_manifest_file_sha256: `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254`
manifest_payload_sha256: `e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f`
recorded_ring: `QQ[t][y]`, represented by Sage as `Univariate Polynomial Ring in y over Univariate Polynomial Ring in t over Rational Field`
y_separability_ring: `QQ(t)[y]`, represented by a polynomial ring over `FractionField(QQ[t])`
irreducibility_wording: Sage-displayed irreducibility over QQ[t][y]
reproduction_caveat: Human-side rerun of `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage` is required before canonical-file insertion.
proof_boundary: This proposal supports only a finite-level exact S-level characteristic-polynomial factorization claim for the r=3 unit/full matrices reconstructed in this repo. It does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.
required_external_review: Human review of bundle schema, exact Sage command reproducibility, manifest payload hashing, and canonical wording before any canonical-file edit.

## Evidence

status: Advisory Only
scope: finite-level r=3 lifted-operator S-level characteristic-polynomial factorization proposal refinement
method: report-only patch from exact Sage audit manifest and Claude PASS_WITH_PATCHES findings
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. This proposal does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
files_touched: `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`, `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json`, `reports/20260514T023536Z_r3_canonical_proposal_patch_summary.md`
artifacts_produced: this v2 proposal and sidecar JSON

## Factorization Summary

| model | dimension | factor_degree_pattern | multiplicity_pattern | reconstruction_check | row_sum_factor_index | status_label |
|---|---:|---|---|---|---:|---|
| unit | 18 | [1,1,2,6] | [1,1,2,2] | True | 0 | Verified Fact, finite-level only |
| full | 27 | [1,1,3,9] | [1,2,2,2] | True | 0 | Verified Fact, finite-level only |

## Factor Hashes

unit factor hashes:

- factor_00: `fb4cc15db6c76dea45ece185f3a2808bc519f4183864a7124646a32588376aec`
- factor_01: `02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69`
- factor_02: `3860a125d1de0df7c0cf81fb47a2164c29760a73f7c70eef58ce54b5099fb3e7`
- factor_03: `a6d3d2b27ed7a8d34fc651677ffa1a58b8e70744c0bf1fc576c0118d1555fc1d`

full factor hashes:

- factor_00: `a44fcd571bbd816ac64489d88a87cd35f967e14d04e2ee88a1b0af98454c1b14`
- factor_01: `02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69`
- factor_02: `d201683ad25dacc610b24120a0f1ddd4e051442771b803bdeda1ab7d532fd42a`
- factor_03: `498455175f2d2defadc095649900160284cec3b6c69f63bc639d187b0271c9a5`

## Claim Labels

Verified Fact: exact finite-level reconstruction, total-degree, row-sum factor, displayed Sage factorization, and y-separability checks recorded in the source audit bundle.

Advisory Only: this v2 canonical patch proposal and publication workflow.

Not Established:

- determinant nonvanishing for all real s > 0
- structural mechanism explaining factorization
- exact subdominant spectral structure
- cross-level invariance
- Collatz-level implications
- independent human proof of irreducibility beyond Sage-displayed factorization

## Boundary

This proposal supports only a finite-level exact S-level characteristic-polynomial factorization claim for the r=3 unit/full matrices reconstructed in this repo. It does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.

Canonical bundle files must remain untouched unless a separate human review explicitly authorizes insertion.
