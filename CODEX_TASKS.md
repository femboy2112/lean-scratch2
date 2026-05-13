# Codex Research Tasks


## Tier -1 — Codex skill validation

```bash
python3 scripts/check_codex_skills.py
```

Use the skills in this order for serious work:

```text
$collatz-research-orchestrator
$collatz-exact-algebra-lab
$collatz-proof-boundary-auditor
```


## Tier 0 — environment and sanity gates

```bash
bash scripts/bootstrap_codex.sh
pytest -q
python3 scripts/run_py_checks.py
```

Expected: all construction sanity checks pass.

## Tier 1 — cheap reconnaissance

```bash
python3 experiments/r3_spectral_probe.py --slices 0.50 0.55 0.60 --models unit full
python3 experiments/r3_modular_determinant_probe.py --model unit --samples 20
python3 experiments/r3_modular_determinant_probe.py --model full --samples 20
```

Outputs are **Computational Observation** only.

## Tier 2 — exact Sage work

```bash
sage sage/r2_verify_factorization.sage
sage sage/r3_factorization_search.sage unit
sage sage/r3_factorization_search.sage full
```

The r=3 full factorization may be expensive. If it is too slow, switch to determinant-only, modular specialization, or smaller factor-invariant searches.

## Tier 3 — hypothesis generation

Use reports from Tier 1 and Tier 2 to propose exact targets. Do not upgrade labels without exact witnesses.

Recommended hypothesis spaces:

1. automorphism/equitable-partition search on r=3 `S(t)` label structure;
2. quotient/residual decompositions for r=3;
3. common invariant subspaces visible at s=0.50 but absent at s=0.55/0.60;
4. determinant positivity mechanisms after substituting `u=t+t^{-1}` or parity-respecting variables;
5. modular factor patterns stable across primes.

## Tier 4 — proof-boundary preparation

Only after exact patterns stabilize:

1. write theorem candidates with explicit hypotheses;
2. separate finite-level theorem from Collatz-level theorem;
3. create Lean skeletons for definitions/finite lemmas only;
4. do not formalize exploratory claims.
