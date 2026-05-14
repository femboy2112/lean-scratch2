# r=3 Canonical Insert Review Checklist

status: Advisory Only
scope: human review checklist for a proposed finite-level r=3 S-level canonical insert
method: checklist generated from active mission packet requirements
claim_boundary: This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_factor_structure_analysis.py`
files_touched: `reports/`, `data/generated/r3_factor_structure/`, `scripts/r3_factor_structure_analysis.py`
artifacts_produced: this checklist

## Required Checks

- [ ] Canonical bundle files remain unmodified.
- [ ] `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage` reruns successfully before any insertion.
- [ ] Manifest file hash equals `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254`.
- [ ] Manifest payload hash equals `e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f`.
- [ ] Insert target is `data/canonical_bundle/05_R3_CLOSURES.txt`, not the Computational Observation file.
- [ ] Insert text includes `status_label: Verified Fact, finite-level only`.
- [ ] Insert text includes r=3, S-level, unit/full dimensions, degree patterns, and multiplicity patterns.
- [ ] Insert text uses `Sage-displayed irreducibility over QQ[t][y]`.
- [ ] Insert text uses `y-separability checked over QQ(t)[y]`.
- [ ] Insert text does not say simply that irreducible factors are proved irreducible.
- [ ] Insert text includes the finite-level proof boundary sentence exactly.
- [ ] No Collatz-level implication, all-real-s determinant nonvanishing claim, cross-level invariance claim, or structural-mechanism claim is introduced.
