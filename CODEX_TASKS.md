# Codex Research Tasks

## Tier -2 — specialized capability validation

Run after any skills/agents change:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
```

Expected: all core and specialized skills are discoverable, all configured agent role files exist, and no role file uses unsupported `model_context`.

## Tier -1 — active-plan orchestration

Use:

```text
$collatz-research-orchestrator go
```

This launches the active packet in `plans/ACTIVE_CODEX_PLAN.md` and may use specialized skills/agents.

## Tier 0 — environment and sanity gates

```bash
bash scripts/bootstrap_codex.sh
python3 scripts/run_py_checks.py
```

For Sage work, prefer repo-local Sage:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage --version
```

## Tier 1 — provenance and artifact hygiene

Use `$collatz-provenance-reproducibility-lab` for:

```text
hash audits
artifact indexes
reproduction commands
bundle comparisons
witness manifest hygiene
```

## Tier 2 — cheap reconnaissance

```bash
python3 experiments/r3_spectral_probe.py --slices 0.50 0.55 0.60 --models unit full
python3 experiments/r3_modular_determinant_probe.py --model unit --samples 20
python3 experiments/r3_modular_determinant_probe.py --model full --samples 20
```

Outputs are **Computational Observation** only.

## Tier 3 — exact Sage and factor-structure work

Use `$collatz-factor-structure-lab` and local Sage for:

```text
residual factors
pairwise gcds
resultants
discriminants
factor graphs
substitution searches
quotient/residual relations
```

Example:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_structure_gcd.sage
```

## Tier 4 — mechanism search

Use `$collatz-symmetry-mechanism-lab` for:

```text
commutants
automorphisms
equitable partitions
projectors/idempotents
block decompositions
```

Specialization evidence is not generic proof.

## Tier 5 — spectrum and determinant work

Use `$collatz-spectrum-determinant-lab` for:

```text
determinant target taxonomy
root isolation
Sturm/sign charts
factor-root tracking
subdominant spectral experiments
```

Numerical eigenvalues remain **Computational Observation**.

## Tier 6 — canonical curation

Use `$collatz-canonical-curator` for insertion previews and human checklists. Do not edit canonical files unless an active packet explicitly authorizes it.

## Tier 7 — proof-boundary and red-team review

Use:

```text
$collatz-proof-boundary-auditor
$collatz-red-team-reviewer
```

The proof auditor checks claim scope; the red-team reviewer checks evidence/source consistency.

## Tier 8 — formalization readiness

Use `$collatz-lean-formalization-bridge` only after exact finite theorem candidates have:

```text
explicit hypotheses
exact ring/domain
finite matrix family
artifact hashes
no numerical dependence
no Collatz-level conclusion
```

## Global boundary

No finite-level spectral, determinant, factorization, rank, kernel, or matrix fact may be upgraded into a Collatz-level theorem.
