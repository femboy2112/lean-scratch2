# r=3 Deep Program Theorem Candidates

status: Advisory Only
scope: finite-level r=3 S-level theorem-candidate triage
method: classification of exact artifacts and blocked targets
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp 20260514T063536Z`
files_touched: `reports/`
artifacts_produced: theorem-candidate Markdown and JSON

- Verified Fact: finite-level r=3 S-level unit/full characteristic-polynomial factorization over `QQ[t][y]`, with the recorded degree and multiplicity patterns in `data/generated/r3_factorization_audit/20260513T160231Z/manifest.json`; this does not establish structural mechanism, all-real-s determinant nonvanishing, cross-level invariance, or any Collatz-level conclusion.
- Verified Fact: over `QQ(t)[y]`, the finite-level r=3 S-level unit residual product of degree 16 and full residual product of degree 24 have residual cross-gcd degree zero, derived from the exact pairwise residual-factor gcd manifest.
- Not Established: structural mechanism.
- Not Established: determinant nonvanishing for all real `s > 0`.
