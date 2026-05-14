---
name: collatz-lean-formalization-bridge
description: Lean formalization bridge for audited finite-level Collatz theorem candidates. Use to convert exact finite-level statements into Lean stubs, proof-obligation tables, dependency maps, and formalization-readiness reports. Do not use for exploratory or numerical claims.
---

# Collatz Lean Formalization Bridge

Use this skill only after theorem candidates are exact, finite-level, audited, and fully scoped.

## Mission

Convert audited finite-level statements into:

- Lean theorem stubs;
- proof-obligation tables;
- dependency maps;
- formalization-readiness reports.

## Activation rule

Activate only when a theorem candidate has:

```text
all variables quantified
finite-level scope
exact ring/domain
model/level/matrix family
evidence artifact hashes
no numerical dependence
no Collatz-level conclusion
```

## Standard outputs

```text
lean/generated/<TheoremName>.lean
reports/<timestamp>_lean_readiness.md
reports/<timestamp>_proof_obligations.md
```

## Forbidden uses

Do not generate Lean stubs for:

- numerical observations;
- modular samples;
- under-specified determinant positivity claims;
- structural mechanism guesses;
- any Collatz-level theorem.

## Completion criteria

A bridge pass is complete only when each generated stub has explicit hypotheses, exact domain/ring, finite matrix family, evidence artifacts, and a list of missing formal definitions.
