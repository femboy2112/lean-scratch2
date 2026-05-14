---
name: collatz-canonical-curator
description: Canonical insertion preview and human-review curation skill. Use to prepare canonical patch proposals, diff previews, insertion checklists, canonical wording checks, rollback notes, and proof-boundary-safe canonical review packets without modifying canonical bundle files.
---

# Collatz Canonical Curator

Use this skill when preparing a canonical insertion proposal, canonical diff preview, or human-review checklist.

## Mission

Prepare canonical-review artifacts without editing canonical bundle files.

## Required first reads

```text
AGENTS.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
data/canonical_bundle/01_FRAMEWORK_AND_CONVENTIONS.txt
data/canonical_bundle/05_R3_CLOSURES.txt
data/canonical_bundle/07_INTERPRETATION_AND_BOUNDARIES.txt
```

## Core behavior

1. Read canonical bundle files only for placement and wording compatibility.
2. Prepare insertion previews and `.patch` preview artifacts.
3. Generate human review checklists and rollback notes.
4. Audit proof-boundary wording before publishing a proposal.
5. Refuse direct canonical edits unless the active mission explicitly authorizes them.

## Standard outputs

```text
reports/<timestamp>_canonical_insert_preview.md
reports/<timestamp>_canonical_insert_preview.json
reports/<timestamp>_canonical_insert_diff_preview.patch
reports/<timestamp>_canonical_insert_human_checklist.md
```

## Required language

Every preview must include:

```text
This is a proposed canonical insertion only. It does not modify canonical files.
```

## Forbidden language

Do not write that finite S-level factorization proves or implies Collatz, global orbit behavior, all-real-s determinant nonvanishing, or structural mechanism.

## Completion criteria

A curation pass is complete only when the insert text, target section, placement rationale, rollback note, proof boundary, and human checklist are all present.
