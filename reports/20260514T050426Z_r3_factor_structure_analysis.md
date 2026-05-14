# r=3 Factor Structure Analysis

status: Computational Observation
scope: finite-level r=3 S-level characteristic-polynomial factor bundle from the 20260513T160231Z Sage audit
method: Python static JSON/hash analysis; Sage exact gcd unavailable on PATH
claim_boundary: This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_factor_structure_analysis.py`
files_touched: `scripts/r3_factor_structure_analysis.py`, `reports/`, `data/generated/r3_factor_structure/`
artifacts_produced: `data/generated/r3_factor_structure/20260514T050426Z/factor_relation_manifest.json` and this report pair

## Source Bundle

- source_manifest: `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json`
- source_manifest_file_sha256: `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254`
- source_manifest_payload_sha256: `e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f`
- Sage available on PATH: `False`
- exact_gcd_status: `Not Established`

## Factor Patterns

| model | dimension | degree pattern | multiplicity pattern | row-sum factor index | label |
|---|---:|---|---|---:|---|
| unit | 18 | [1, 1, 2, 6] | [1, 1, 2, 2] | 0 | Verified Fact |
| full | 27 | [1, 1, 3, 9] | [1, 2, 2, 2] | 0 | Verified Fact |

## Shared Factors

- factor hash `02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69`: unit factor_01, full factor_01; degree 1; multiplicity unit=1, full=2; label: `Verified Fact`.

The shared non-row-sum factor does not have the same multiplicity in the audited bundle: unit multiplicity is 1 and full multiplicity is 2. This statement is scoped to static comparison of the audited factor JSON artifacts.

## Degree and Residual Patterns

Computational Observation: The residual higher-degree pairs are 2,6 for unit and 3,9 for full. They have a 3/2 degree ratio by ordered pair, not an integer degree-multiple relation.

After removing row-sum factors only, the non-row-sum degree contributions are unit 17 and full 26.

After removing both the row-sum factor and the shared non-row-sum factor, the residual degree contributions are unit 16 and full 24.

## Exact GCD Work

Not Established: Sage was not available on PATH for this Python run, so pairwise gcds over `QQ(t)[y]` or `QQ[t][y]` were not computed here. The sidecar manifest records static equality for the identical shared factor and marks non-identical pairwise gcds as `Not Established`.

## Justified Sage Follow-Up Tests

- Compute pairwise gcds for every unit/full factor over QQ(t)[y] and record exact gcd expressions.
- Test divisibility of full residual factors by substitutions or quotients suggested by the shared linear factor.
- Compare residual characteristic polynomials after removing row-sum and shared non-row-sum factors.
- Search for commutant, symmetry, or equitable-partition mechanisms for the squared residual factors.

## Structural Mechanism Claims Remaining Not Established

- r=3 structural mechanism explaining the factorization pattern
- exact pairwise gcd table for non-identical factor pairs over QQ(t)[y]
- simple integer degree-multiple relation from unit higher-degree factors to full higher-degree factors
- determinant nonvanishing for all real s > 0
- cross-level invariance
- subdominant spectral structure
- any Collatz-level conclusion
