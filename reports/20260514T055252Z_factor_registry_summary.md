# r=3 Factor Registry Summary

status: Verified Fact
scope: finite-level r=3 S-level factor registry from audited Sage factorization and exact gcd artifacts
method: Python normalization of audited factor JSON and exact gcd manifest
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp 20260514T055252Z`
files_touched: `reports/`, `data/generated/r3_deep_program/20260514T055252Z/`
artifacts_produced: `data/generated/r3_deep_program/20260514T055252Z/factor_registry.json`, `data/generated/r3_deep_program/20260514T055252Z/factor_registry.csv`

## Verification Checks

- unit factor degree contribution: `18`
- full factor degree contribution: `27`
- unit row-sum factor index: `[0]`
- full row-sum factor index: `[0]`
- shared unit/full factor hash present: `True`
