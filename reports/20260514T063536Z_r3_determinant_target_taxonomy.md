# r3 determinant target taxonomy

status: Advisory Only
scope: finite-level r=3 S-level deep-program support report
method: bounded program generation and explicit blocker classification
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp 20260514T063536Z`
files_touched: `reports/`
artifacts_produced: this report pair

Advisory Only: determinant targets are charpoly evaluations, `det(S)`, `det(I-S)`, residual-factor determinants, and compact determinant objects from prior constraints if later explicitly defined; all-real-s nonvanishing remains Not Established.
