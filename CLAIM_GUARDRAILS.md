# Claim Guardrails

## Non-negotiable boundary

Do not claim that finite-level matrix facts prove, imply, or nearly prove the Collatz conjecture.

Allowed wording:

```text
This is a finite-level structural / spectral / determinant fact inside the lifted-operator framework.
```

Forbidden wording:

```text
This proves Collatz.
This essentially proves Collatz.
This shows no divergent Collatz orbits exist.
The spectral radius bound solves the conjecture.
```

## Status labels

Use exactly one label per claim:

| Label | Use |
|---|---|
| Verified Fact | Exact witness present and canonical or newly witnessable. |
| Computational Observation | Numerical, modular, solver-derived, or exploratory. |
| Not Established | Open; no exact witness. |
| Withdrawn | Known bad claim. Never resurrect silently. |
| Patched | Earlier artifact corrected. |
| Contradiction Detected | Conflicts with locked fact. Halt. |
| Over-Upgraded | Claim exceeds evidence. Downgrade. |
| Advisory Only | Process note, not mathematics. |

## Known over-upgrade traps

- Compact S-level factorization does not imply B-level descent-to-Q.
- Shared factor at one slice does not close general compact factorization.
- r=2 structural mechanisms do not transfer to r=3 without independent witness.
- Numerical eigenvalue multiplicity does not prove algebraic multiplicity.
- Positive numerical determinant samples do not prove all-real-s determinant nonvanishing.
- A modular nonzero determinant witness proves only that the symbolic determinant is not the zero polynomial if the evaluation map is correctly specified; it does not prove positivity for all real `s > 0`.
