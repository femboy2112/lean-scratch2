# r=3 Factor Structure Next Targets

status: Advisory Only
scope: next-packet recommendation after finite-level r=3 factor-structure static analysis
method: report-only recommendation from audited factor bundle relationships
claim_boundary: This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_factor_structure_analysis.py`
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
