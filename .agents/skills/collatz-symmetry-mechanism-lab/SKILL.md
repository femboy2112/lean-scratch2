---
name: collatz-symmetry-mechanism-lab
description: Structural-mechanism discovery skill for the Collatz r=3 finite-level matrix program. Use for commutants, automorphisms, equitable partitions, projectors, idempotents, block decompositions, quotient matrices, specialization-based mechanism hints, and structural-mechanism candidate reports.
---

# Collatz Symmetry Mechanism Lab

Use this skill to search for exact finite-level structural mechanisms behind repeated factors, residual blocks, and invariant decompositions.

## Mission

Search for:

- commutants;
- automorphisms;
- equitable partitions;
- projectors and idempotents;
- block decompositions;
- quotient matrices;
- representation-like finite decompositions.

## Evidence ladder

Distinguish strictly between:

1. exact specialization fact;
2. generic exact fact;
3. pattern across samples;
4. structural mechanism candidate;
5. structural mechanism proof.

## Standard outputs

```text
data/generated/r3_deep_program/<timestamp>/commutant/*.json
data/generated/r3_deep_program/<timestamp>/automorphisms/*.json
data/generated/r3_deep_program/<timestamp>/partitions/*.json
reports/<timestamp>_r3_commutant_specialization_analysis.md
reports/<timestamp>_r3_equitable_partition_search.md
reports/<timestamp>_r3_automorphism_search.md
reports/<timestamp>_r3_mechanism_candidates.md
```

## Guardrail

Always state:

```text
No structural mechanism is established unless an exact generic witness is produced and audited.
```

## Claim labels

- Exact fixed-specialization commutant dimension: `Verified Fact` for that specialization.
- Pattern across several specializations: `Computational Observation`.
- Generic commutant over `QQ(t)`: `Verified Fact` only if exact.
- Structural mechanism: `Not Established` until exact generic witness.

## Completion criteria

The pass is complete only when every candidate mechanism includes ring/domain, specialization or generic scope, supporting artifact paths, and missing proof steps.
