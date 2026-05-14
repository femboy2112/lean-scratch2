# r=3 Factor Structure Exact GCD Pass

status: Verified Fact
scope: finite-level r=3 S-level audited unit/full characteristic-polynomial factors from 20260513T160231Z
method: Sage exact pairwise gcd over QQ(t)[y]
claim_boundary: This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `env DOT_SAGE=$PWD/.codex/sage .sage-conda/bin/sage sage/r3_factor_structure_gcd.sage`
files_touched: `sage/r3_factor_structure_gcd.sage`, `reports/`, `data/generated/r3_factor_structure/`
artifacts_produced: `data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json`, `reports/20260514T052552Z_r3_factor_structure_gcd.json`, `reports/20260514T052552Z_r3_factor_structure_gcd.md`

## Previous Failed Part

Patched: the prior factor-structure artifact marked exact gcd work `Not Established` because Sage was unavailable on PATH. This pass reruns only that Sage-dependent part with the repo-local Sage binary.

## Nonconstant GCDs

- unit factor_01 with full factor_01: gcd_degree_y=1, gcd_expression_sha256=02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69, label=`Verified Fact`

## Pairwise GCD Table

| unit factor | full factor | gcd degree in y | gcd expression sha256 | label |
|---:|---:|---:|---|---|
| 00 | 00 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 00 | 01 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 00 | 02 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 00 | 03 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 01 | 00 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 01 | 01 | 1 | `02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69` | Verified Fact |
| 01 | 02 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 01 | 03 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 02 | 00 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 02 | 01 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 02 | 02 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 02 | 03 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 03 | 00 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 03 | 01 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 03 | 02 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |
| 03 | 03 | 0 | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | Verified Fact |

## Remaining Not Established Items

- r=3 structural mechanism explaining the factorization pattern
- determinant nonvanishing for all real s > 0
- cross-level invariance
- subdominant spectral structure
- any Collatz-level conclusion
