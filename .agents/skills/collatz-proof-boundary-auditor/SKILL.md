---
name: collatz-proof-boundary-auditor
description: Proof-boundary and formalization audit skill for the Collatz spectral project. Use to classify claims, prevent false Collatz-level conclusions, review computational witnesses, generate Lean theorem stubs, and verify finite spectral results stay inside proven scope.
---

# Collatz Proof-Boundary Auditor

This skill is the repo's mathematical immune system.

## Mission

Audit reports, scripts, theorem candidates, and generated artifacts for:

1. unsupported theorem upgrades;
2. finite-level-to-Collatz overreach;
3. missing hypotheses;
4. weak evidence labels;
5. Lean-formalization readiness.

## Required first read

Read:

```text
AGENTS.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
data/canonical_bundle/07_INTERPRETATION_AND_BOUNDARIES.txt
```

## Main commands

Audit one file:

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<file>.md
```

Audit all reports:

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
```

Extract theorem candidates:

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/extract_theorem_candidates.py reports/<file>.md
```

Generate Lean stub:

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/generate_lean_stub.py --name <TheoremName> --statement "<finite-level statement>"
```

## Claim classification

Classify each claim as exactly one of:

- `Verified Fact`
- `Computational Observation`
- `Not Established`
- `Withdrawn`
- `Patched`
- `Contradiction Detected`
- `Over-Upgraded`
- `Advisory Only`

## Reject immediately

Reject or downgrade any claim that says or implies:

- finite spectral closure proves Collatz;
- determinant positivity was proved from samples;
- numerical eigenvalue multiplicity is algebraic proof;
- r=2 mechanism automatically transfers to r=3;
- modular nonzero witness proves real positivity;
- one slice proves generic all-s behavior.

## Lean readiness test

A theorem candidate is Lean-ready only if it has:

1. all quantified variables;
2. finite-level scope;
3. specified r/model/slice/matrix family;
4. exact domain/ring;
5. no hidden appeal to numerical evidence;
6. no Collatz-level conclusion.

## Output

Produce:

```text
reports/<slug>_audit.md
reports/<slug>_audit.json
```

Use dispositions:

- `PASS`
- `PASS_WITH_PATCHES`
- `BLOCKED`
- `REJECT`
