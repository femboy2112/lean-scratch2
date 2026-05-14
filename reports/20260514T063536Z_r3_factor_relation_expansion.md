# r=3 Factor Relation Expansion

status: Advisory Only
scope: finite-level r=3 S-level audited factor relation expansion
method: Sage exact gcd/support extraction; bounded discriminants; explicit classification for deferred resultants
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
reproduction_command: `env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage --timestamp 20260514T063536Z`
files_touched: `sage/r3_factor_relation_expansion.sage`, `reports/`, `data/generated/r3_deep_program/20260514T063536Z/factor_relations/`
artifacts_produced: `data/generated/r3_deep_program/20260514T063536Z/factor_relations/gcd_table.json`, `data/generated/r3_deep_program/20260514T063536Z/factor_relations/resultant_table.json`, `data/generated/r3_deep_program/20260514T063536Z/factor_relations/discriminant_table.json`, `data/generated/r3_deep_program/20260514T063536Z/factor_relations/coefficient_support.json`, `data/generated/r3_deep_program/20260514T063536Z/factor_relations/substitution_profiles.json`

## Exact Relations

Verified Fact: exact pairwise gcd table over `QQ(t)[y]` and residual cross-gcd degree zero.

Computational Observation: bounded/low-cost discriminant extraction results, where applicable.

## Deferred Targets

Not Established: generic high-degree resultants and high-degree discriminant expansions.

Advisory Only: defer these expansions to a selected target pass because expression swell is expected.
