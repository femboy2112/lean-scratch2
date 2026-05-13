# TDAP Workflow

TDAP means:

```text
Target → Decompose → Attack → Proof-boundary
```

## Target

Write the target as a finite-level problem.

Bad:

```text
Solve Collatz.
```

Good:

```text
Find or rule out a compact factorization pattern for the r=3 full S-level characteristic polynomial at s=0.55 within the currently constructed finite lifted-operator model.
```

## Decompose

Split into independent work units:

- construction verification;
- exact algebra;
- numerical reconnaissance;
- modular probes;
- invariant search;
- proof-boundary audit;
- report generation.

## Attack

Choose backend by task:

- Python: orchestration, data parsing, graph/invariant search, reports.
- Sage: exact rational/polynomial matrices, rank/kernel, determinant, charpoly.
- Lean: formalization only after exact statements stabilize.

## Proof-boundary

Every output gets classified. The auditor must state what was not proved.
