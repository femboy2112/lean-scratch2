# Exact Algebra Protocol

## Claim-grade backend

Use Sage for:

- polynomial rings over `QQ`, finite fields, or specified exact domains;
- exact matrices;
- characteristic polynomials;
- determinants;
- rank/kernel;
- factorization over declared rings.

Use Python/SymPy for:

- small exact calculations;
- command orchestration;
- parsing canonical files;
- report generation;
- modular and numerical reconnaissance.

## Floating-point quarantine

If a computation uses floating point:

- status must be `Computational Observation`;
- do not use theorem language;
- do not infer algebraic multiplicity;
- do not infer all-real positivity.

## Modular-probe quarantine

A modular nonzero determinant witness can support only this kind of claim:

```text
The determinant polynomial is not identically zero under the specified evaluation map.
```

It does not prove:

```text
determinant > 0 for all real s > 0
```
