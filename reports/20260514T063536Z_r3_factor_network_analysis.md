# r=3 Factor Network Analysis

status: Verified Fact
scope: finite-level r=3 S-level factor graph from audited factor and gcd artifacts
method: graph projection of factor hashes, row-sum roles, shared-factor roles, and residual nodes
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp 20260514T063536Z`
files_touched: `reports/`, `data/generated/r3_deep_program/20260514T063536Z/factor_graph/`
artifacts_produced: `data/generated/r3_deep_program/20260514T063536Z/factor_graph/factor_graph.json`, `data/generated/r3_deep_program/20260514T063536Z/factor_graph/factor_graph.dot`
