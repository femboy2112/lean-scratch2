---
name: collatz-factor-structure-lab
description: Exact factor-structure analysis skill for r=3 Collatz S-level artifacts. Use for factor registries, residual characteristic polynomials, pairwise gcds, resultants, discriminants, quotient/residual relations, substitution searches, and factor-network graph artifacts over QQ[t][y] and QQ(t)[y].
---

# Collatz Factor Structure Lab

Use this skill for exact finite-level factor algebra around audited r=3 S-level characteristic-polynomial artifacts.

## Mission

Analyze factor registries, residuals, factor graphs, gcd tables, resultants, discriminants, substitution tests, and quotient/residual relations.

## Sage rule

Every Sage command must use the repo-local Sage binary:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage <script>
```

Do not rely on bare `sage` being on PATH.

## Standard outputs

```text
data/generated/r3_factor_structure/<timestamp>/factor_relation_manifest.json
data/generated/r3_deep_program/<timestamp>/factor_registry.json
data/generated/r3_deep_program/<timestamp>/factor_graph/factor_graph.json
data/generated/r3_deep_program/<timestamp>/residuals/residual_manifest.json
reports/<timestamp>_r3_factor_structure_analysis.md
reports/<timestamp>_r3_residual_factor_analysis.md
reports/<timestamp>_r3_factor_relation_expansion.md
```

## Claim logic

- Exact gcd: `Verified Fact`.
- Exact residual construction: `Verified Fact`.
- Exact resultant/discriminant computation: `Verified Fact` for that named polynomial only.
- Substitution pattern without exact identity: `Computational Observation`.
- Structural mechanism: `Not Established` unless an exact mechanism witness exists.

## Required report fields

```text
status:
scope:
ring:
model:
level:
method:
source_artifacts:
claim_boundary:
not_established_items:
```

## Completion criteria

The pass is complete only when exact computations include ring/domain, input artifact hashes, output hashes, and proof-boundary-safe labels.
