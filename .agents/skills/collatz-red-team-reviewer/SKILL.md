---
name: collatz-red-team-reviewer
description: Adversarial verification skill for Collatz research artifacts. Use to red-team reports, recompute hashes, compare claims against source artifacts, scan for contradictions, identify unsupported proof bridges, and produce independent review reports.
---

# Collatz Red Team Reviewer

Use this skill for independent adversarial review of reports, scripts, generated data, and theorem candidates.

## Mission

Try to falsify or downgrade unsupported claims by checking:

- source artifacts;
- hashes;
- scripts;
- generated reports;
- proof bridges;
- canonical boundaries;
- contradiction patterns.

## Distinction from proof-boundary auditor

```text
proof-boundary-auditor = language / claim-scope audit
red-team-reviewer = adversarial evidence / source-consistency audit
```

## Standard outputs

```text
reports/<timestamp>_red_team_review.md
reports/<timestamp>_red_team_review.json
data/generated/red_team/<timestamp>/hash_audit.json
```

## Required behavior

- Recompute hashes where feasible.
- Compare report claims directly against source artifacts.
- Flag unsupported theorem upgrades.
- Treat missing source evidence as `Not Established`.
- Do not repair claims silently; report required patches.

## Completion criteria

A red-team pass is complete only when the report has a disposition, finding table, source-artifact comparison, unsafe-claim list, and strongest safe finite-level claim statement.
