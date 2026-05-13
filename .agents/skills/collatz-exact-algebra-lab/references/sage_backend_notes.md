# Sage Backend Notes

## Use Sage when exact algebra matters

Preferred Sage targets:

```bash
sage sage/r2_verify_factorization.sage
sage sage/r3_factorization_search.sage unit
sage sage/r3_factorization_search.sage full
sage sage/r3_determinant_polynomial.sage
```

## If Sage is missing

Run:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

If installation is blocked, downgrade the task to Python-only reconnaissance and clearly mark Sage-dependent exact claims as blocked.

## Performance policy

For expensive full-model computations:

1. Try unit model first.
2. Try modular/specialized probes.
3. Try quotient/invariant decomposition.
4. Record timeout/blocker.
5. Do not silently reduce the problem and report it as the original target.
