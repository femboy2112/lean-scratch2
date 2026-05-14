---
name: collatz-provenance-reproducibility-lab
description: Artifact provenance, reproducibility, hash verification, manifest validation, artifact indexing, and rerun-script skill for the Collatz finite-level research repo. Use for generated data bundles, SHA-256 checks, witness manifests, reproduction commands, and audit-noise control.
---

# Collatz Provenance Reproducibility Lab

Use this skill whenever Codex needs generated research artifacts to be durable, hash-addressed, reproducible, and human-queryable.

## Mission

Maintain artifact integrity for finite-level Collatz research:

- SHA-256 verification
- manifest validation
- generated artifact indexes
- reproduction command files
- timestamped bundle comparison
- witness-manifest hygiene
- audit-noise control

## Required first reads

```text
AGENTS.md
CLAIM_GUARDRAILS.md
reports/witness_manifest.json
```

Read the relevant `data/generated/.../manifest.json` files for the active mission.

## Standard outputs

```text
data/generated/<program>/<timestamp>/artifact_index.json
data/generated/<program>/<timestamp>/reproduction_commands.txt
reports/<timestamp>_artifact_index.md
reports/<timestamp>_reproducibility_notes.md
reports/<timestamp>_manifest_hash_audit.md
```

## Required rules

- Do not alter mathematical artifacts to make hashes match.
- Do not delete generated artifacts unless the active plan explicitly authorizes deletion.
- Hash consistency authenticates artifacts only; it does not upgrade mathematical claims.
- Every artifact index entry must include `path`, `kind`, `sha256`, `producer_phase`, `status_label`, and `claim_boundary`.
- If a hash mismatch appears, label it `Contradiction Detected` for artifact integrity, not automatically for mathematics.

## Preferred workflow

1. Locate the target bundle.
2. Recompute file hashes using Python stdlib.
3. Compare against manifests and reports.
4. Write a machine-readable hash audit.
5. Write a human-readable reproducibility note.
6. Update or request update of `reports/witness_manifest.json`.
7. Route any mathematical claim language to `$collatz-proof-boundary-auditor`.

## Completion criteria

The pass is complete only when all generated artifacts are indexed, the command needed to reproduce the bundle is recorded, and every mismatch or missing artifact is explicitly labelled.
