# r=3 Factorization Audit

status: Verified Fact
scope: finite-level r=3 lifted-operator S-level characteristic-polynomial factorization audit for unit and full models
method: Sage exact algebra over `QQ[t][y]`; exact matrix reconstruction from `src/collatz_codex_harness.construct`
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real `s > 0`, or cross-level invariance.
reproduction_command: `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage`
files_touched: `sage/r3_factorization_audit.sage`, `data/generated/r3_factorization_audit/`, `reports/`
artifacts_produced: `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json` and report pair for timestamp `20260513T160231Z`

## status

Verified Fact: exact finite-level Sage reconstruction checks passed for the recorded r=3 S-level characteristic-polynomial factorizations.

## scope

Only r=3 S-level unit/full matrices reconstructed from the repo construction are audited here. Canonical bundle files are not modified.

## method

Sage rebuilds the r=3 S-level matrices over `QQ[t]`, computes `charpoly(var="y")`, factors in `QQ[t][y]`, verifies exact product reconstruction, checks total y-degree, identifies the exact all-ones row-sum factor, and records irreducibility/separability metadata for each displayed factor.

## commands_run

- `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage`

## input_artifacts

- `src/collatz_codex_harness/construct.py`
- `reports/sage_r3_unit_factorization.sageout`
- `reports/sage_r3_full_factorization.sageout`

## output_bundle

- `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json`
- manifest_sha256: `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254`

## factor_degree_summary

| model | dimension | factor_degree_pattern | multiplicity_pattern | reconstruction_check | label |
|---|---:|---|---|---|---|
| unit | 18 | [1, 1, 2, 6] | [1, 1, 2, 2] | True | Verified Fact |
| full | 27 | [1, 1, 3, 9] | [1, 2, 2, 2] | True | Verified Fact |

## row_sum_factor_summary

- unit: status_label: Verified Fact; row_sums_equal: `True`; matched: `True`; matching_factor_indices: `[0]`.
- full: status_label: Verified Fact; row_sums_equal: `True`; matched: `True`; matching_factor_indices: `[0]`.

## irreducibility_summary

- unit: all displayed Sage factors irreducible over recorded ring: `True`.
- full: all displayed Sage factors irreducible over recorded ring: `True`.

## separability_summary

- unit: all displayed factors have gcd with y-derivative equal to 1: `True`.
- full: all displayed factors have gcd with y-derivative equal to 1: `True`.

## reconstruction_checks

- unit: reconstruction_check: `True`; total_degree_y: `18`; prior_sageout_hash: `f341ce713b73a759e7a970f23178ea71047eb0821cf1b373ca3401ad38abf07c`; new_factorization_hash: `d3bab9ded8ed111d524d2e5ab1ff110cc8c1a8d29122dce129cfdc2d26c651c1`; matches_prior_exact_string: `True`.
- full: reconstruction_check: `True`; total_degree_y: `27`; prior_sageout_hash: `fe1477297a2a807520390978a2dc3ea259e403698c420e1ecff74df16b68e71a`; new_factorization_hash: `ad1b0e02663f15b77fd2dda9c9e20ef9f71aaab2810b485f1709ea8d1a21ae58`; matches_prior_exact_string: `True`.

## claim_labels

- Verified Fact: exact finite-level reconstruction, total-degree, row-sum factor, displayed-factor irreducibility, and displayed-factor y-separability checks recorded in this timestamped bundle.
- Not Established: determinant positivity for all real `s > 0`, structural mechanism explaining the factorization, exact subdominant spectral structure, cross-level invariance, and any Collatz-level conclusion.
- Advisory Only: canonical patch proposal and publication workflow.

## not_established_items

- r=3 determinant nonvanishing for all real `s > 0`.
- r=3 structural mechanism for the observed factorization patterns.
- r=3 exact subdominant spectral structure.
- cross-level r=2/r=3 spectral invariance.
- Collatz-level implications.

## blocked_items

None from the exact audit helper when this report was written.

## recommended_canonical_patch_if_any

See the optional Advisory Only canonical patch proposal generated for this timestamp.

## why_this_does_not_imply_Collatz

The audited objects are finite-dimensional S-level matrices in the lifted-operator framework. Exact characteristic-polynomial factorization and row-sum factor identification for these finite matrices do not establish global orbit behavior and do not prove or imply the Collatz conjecture.
