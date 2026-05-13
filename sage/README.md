# Sage Exact Algebra Scripts

Run from repo root.

```bash
sage sage/r2_verify_factorization.sage
sage sage/r3_factorization_search.sage unit
sage sage/r3_factorization_search.sage full
```

If `sage` is missing:

```bash
bash scripts/setup_linux_mint.sh --sage auto
```

If the local conda environment was created but `sage` is not on PATH:

```bash
.sage-conda/bin/sage sage/r2_verify_factorization.sage
```

All r=3 exact results remain **Computational Observation** until separately audited and promoted with a witness package.
