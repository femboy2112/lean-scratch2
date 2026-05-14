# r=3 Factorization Canonical Insert Patch

status: Advisory Only
scope: finite-level r=3 S-level characteristic-polynomial canonical insertion proposal only
method: report-only synthesis from audited Sage factorization bundle and v2 proposal
claim_boundary: This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_factor_structure_analysis.py`
files_touched: `reports/`, `data/generated/r3_factor_structure/`, `scripts/r3_factor_structure_analysis.py`
artifacts_produced: this Markdown report and sidecar JSON

## Patch Metadata

- source_proposal_v2: `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
- source_manifest: `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json`
- candidate_target_file: `data/canonical_bundle/05_R3_CLOSURES.txt`
- candidate_target_section: Insert before <<APPEND-POINT::05.charpoly>> as a new 05.charpoly.r3.generic_s_level_factorization section after human review.
- status: `Advisory Only`

## Placement Rationale

05_R3_CLOSURES.txt is the canonical file for r=3 Verified Fact closures. 08_RECONNAISSANCE_OBSERVATIONS.txt is reserved for Computational Observation reconnaissance, so the audited finite-level exact factorization belongs in 05 if a human accepts insertion.

## Exact Insert Text

```text
==SECTION:: 05.charpoly.r3.generic_s_level_factorization_proposed ==

status_label: Verified Fact, finite-level only
r: 3
level: S-level
models: unit and full
recorded_ring: QQ[t][y]
y-separability ring: QQ(t)[y]
source_manifest: data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
manifest file hash: fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254
manifest payload hash: e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f

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
[GUARD: S-level characteristic-polynomial factorization only; do not upgrade to B-level descent, compact-factorization closure, structural mechanism, subdominant spectral structure, cross-level invariance, all-real-s determinant nonvanishing, or Collatz-level claims.]
```

## Required Pre-Insert Checks

- Confirm canonical bundle files are still untouched before review.
- Rerun env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage in an environment with Sage.
- Verify manifest file sha256 equals fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254.
- Verify manifest payload sha256 equals e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f.
- Confirm source proposal v2 wording still passes proof-boundary audit.
- Confirm the insert text says Sage-displayed irreducibility over QQ[t][y] and y-separability checked over QQ(t)[y].

## Rollback Note

This artifact is a proposed insert only. If rejected, delete or supersede this report pair; no canonical bundle rollback is needed because no canonical file is modified.

## Proof Boundary

This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
