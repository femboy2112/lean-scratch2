# Proof Boundary Rules

## Finite theorem boundary

A valid finite-level theorem must specify:

```text
r:
model:
level:
slice/parameter:
matrix family:
domain/ring:
construction rule:
hypotheses:
conclusion:
```

## Global Collatz boundary

A finite-level theorem may support structure inside the lifted-operator framework. It does not by itself prove:

- all integer orbits converge;
- absence of divergent trajectories;
- absence of nontrivial cycles;
- global monotonic descent;
- the Collatz conjecture.

## Evidence-to-claim mapping

| Evidence | Maximum label |
|---|---|
| plot / float eigenvalues | Computational Observation |
| modular sample | Computational Observation |
| exact finite script output | Verified Fact, if reproducible and scoped |
| proof sketch with full hypotheses | Not Established or candidate theorem |
| Lean-checked finite theorem | Verified Fact, finite only |
