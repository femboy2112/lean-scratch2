# Matrix Construction Contract

## Source of truth

Use the canonical bundle and existing `src/collatz_codex_harness/construct.py`.

## Do not guess

If a construction rule is not stated or implemented, do not invent one. Mark the task blocked.

## Required identifiers

Every constructed matrix or derived artifact must identify:

```text
r:
model: unit | full | other explicit model
level:
slice_or_parameter:
matrix_family:
source_rule:
input_hash:
```

## Cross-checks

Whenever feasible:

1. Check row sums / Perron expectations.
2. Check rank/kernel against canonical closure claims.
3. Compare Python-generated data to Sage-generated exact data.
4. Store hashes of inputs and outputs.
