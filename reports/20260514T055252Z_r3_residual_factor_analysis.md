# r=3 Residual Factor Analysis

status: Verified Fact
scope: finite-level r=3 S-level audited factor residual algebra
method: Sage exact products over QQ(t)[y] from audited factor JSON and exact gcd manifest
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage --timestamp 20260514T055252Z`
files_touched: `sage/r3_factor_relation_expansion.sage`, `reports/`, `data/generated/r3_deep_program/20260514T055252Z/residuals/`
artifacts_produced: `data/generated/r3_deep_program/20260514T055252Z/residuals/residual_manifest.json`

## Residual Checks

- unit residual degree in y: `16`
- full residual degree in y: `24`
- unit charpoly reconstruction after removing row/shared factors: `True`
- full charpoly reconstruction after removing row/shared factors: `True`
- residual cross-gcd degree in y: `0`
- residual cross-gcd method: derived from exact pairwise gcd manifest over `QQ(t)[y]`

## Not Established

Not Established: resultants and determinant positivity over all real `s > 0` are not established by this residual pass.
