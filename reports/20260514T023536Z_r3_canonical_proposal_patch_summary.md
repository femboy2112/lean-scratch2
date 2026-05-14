# r=3 Canonical Proposal Patch Summary

status: Advisory Only
scope: report-only patch of the r=3 factorization canonical patch proposal
method: incorporated Claude PASS_WITH_PATCHES findings into a new v2 proposal artifact
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
files_touched: `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`, `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json`, `reports/20260514T023536Z_r3_canonical_proposal_patch_summary.md`
artifacts_produced: v2 proposal Markdown, v2 proposal JSON, patch summary

## Patch Items

- Added per-model dimension, degree pattern, multiplicity pattern, reconstruction check, row-sum factor index, and finite-level status label.
- Added `manifest_payload_sha256` while preserving the manifest file hash.
- Added recorded ring `QQ[t][y]` and y-separability ring `QQ(t)[y]`.
- Reworded irreducibility as Sage-displayed irreducibility over QQ[t][y].
- Added the human-side Sage rerun caveat before canonical-file insertion.
- Kept proposal status `Advisory Only`.
- Kept canonical bundle files untouched.

## Not Established

- determinant nonvanishing for all real s > 0
- structural mechanism explaining factorization
- exact subdominant spectral structure
- cross-level invariance
- Collatz-level implications
- independent human proof of irreducibility beyond Sage-displayed factorization

## Output Artifacts

- `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
- `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json`
- `reports/20260514T023536Z_r3_canonical_proposal_patch_summary.md`
