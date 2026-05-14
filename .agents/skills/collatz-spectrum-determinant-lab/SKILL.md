---
name: collatz-spectrum-determinant-lab
description: Determinant and spectrum analysis skill for finite-level Collatz matrix artifacts. Use for determinant target taxonomy, root-isolation attempts, Sturm/sign-chart work, factor-root tracking, subdominant spectral experiments, specialization sweeps, and strict separation of numerical observations from exact claims.
---

# Collatz Spectrum Determinant Lab

Use this skill for determinant targets, exact root-isolation attempts, spectral tracking, and specialization sweeps.

## Mission

Separate numerical, modular, and exact evidence for:

- subdominant spectral structure;
- determinant target taxonomy;
- exact root isolation;
- Sturm/sign-chart attempts;
- factor-root tracking;
- specialization sweeps.

## Standard outputs

```text
reports/<timestamp>_r3_determinant_target_taxonomy.md
reports/<timestamp>_r3_determinant_root_isolation_attempt.md
reports/<timestamp>_r3_subdominant_factor_tracking.md
data/generated/r3_deep_program/<timestamp>/determinant_targets/*.json
data/generated/r3_deep_program/<timestamp>/spectral_tracking/*.json
```

## Claim discipline

- Numerical eigenvalue order: `Computational Observation`.
- Modular sample: `Computational Observation`.
- Root isolation for a named polynomial: `Verified Fact` for that polynomial only.
- All-real-s determinant nonvanishing: `Not Established` unless exact positivity/nonvanishing proof is complete.

## Determinant taxonomy rule

Before trying positivity, name the determinant object precisely:

```text
charpoly evaluated at a target y
det(S)
det(I - S)
determinant of a residual factor
compact determinant from prior constraints
```

## Completion criteria

The pass is complete only when all numerical outputs are clearly separated from exact algebra, and every determinant/nonvanishing claim states the exact polynomial and domain.
