---
name: collatz-exact-algebra-lab
description: Exact algebra and data-analysis skill for the Collatz spectral harness. Use for Python/Sage experiments, characteristic polynomials, determinants, factor searches, rank/kernel scans, spectrum analysis, witness JSON/CSV generation, and reproducible computation reports.
---

# Collatz Exact Algebra Lab

This skill runs disciplined computation for the finite-level lifted-operator Collatz project.

## Core rule

Use the weakest label supported by the evidence. Numerical output is `Computational Observation`, not proof. Exact Sage/SymPy output is finite-level only unless a separately audited proof bridge exists.

## Backend selection

Use this backend order:

1. **Sage** for exact rational/polynomial matrices, determinant, characteristic polynomial, rank/kernel, factorization, exact fields/rings.
2. **Python/SymPy** for orchestration, small exact checks, modular sampling, report generation, and fallback reconnaissance.
3. **NumPy** only for numerical reconnaissance, never theorem-grade claims.
4. **Lean** only after the proof-boundary auditor has produced a fully scoped theorem candidate.

## Required first commands

```bash
bash scripts/bootstrap_codex.sh
python scripts/run_py_checks.py
```

If Sage is needed:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

## Main wrapper

Use:

```bash
python .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py <target>
```

Known targets:

```text
spectral-fast
modular-unit-fast
modular-full-fast
factor-python
cross-level
sage-r2
sage-r3-unit
sage-r3-full
```

Then collect witnesses:

```bash
python .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

## Required report fields

Every report must state:

```text
status:
scope:
method:
claim_boundary:
reproduction_command:
input_hashes:
output_artifacts:
known_limitations:
```

## Exactness checks

Before calling a result exact:

1. State the ring/domain.
2. State r, model, slice/parameter, level, and matrix family.
3. Save the command and artifact hash.
4. Run an independent comparison where feasible.
5. Send the output to `$collatz-proof-boundary-auditor`.

## Completion criteria

The lab pass is complete only when:

1. Commands have been run or blockers are documented.
2. Witness artifacts exist under `reports/` or `data/generated/`.
3. Claims are labelled.
4. `collect_witnesses.py` has updated the witness manifest.
5. Proof-boundary audit has been requested or run.
