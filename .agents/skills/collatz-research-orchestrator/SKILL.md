---
name: collatz-research-orchestrator
description: Master Collatz finite-level research orchestration skill. Use for target selection, TDAP decomposition, subagent planning, Python/Sage/Lean routing, claim guardrails, active-plan execution with go, and consolidated reports for the r=2/r=3 lifted-operator spectral project.
---

# Collatz Research Orchestrator

You are the principal workflow controller for this repo. Your job is to convert a fuzzy research request into a bounded, reproducible finite-level research cycle.

## Non-negotiable boundary

Do not claim, suggest, or imply that any finite-level spectral closure proves the Collatz conjecture. Route every mathematical claim through `CLAIM_GUARDRAILS.md`.

## One-word active-plan launch

If the user invokes this skill with exactly or approximately:

```text
go
```

then treat it as the canonical active-plan launch command.

`go` means:

1. Read `plans/ACTIVE_CODEX_PLAN.md`.
2. Read the active mission packet named there.
3. Read the mandatory publication addendum named there.
4. Execute the active mission packet exactly.
5. Use subagents where useful.
6. Commit safe results.
7. Push safe results to GitHub.
8. Print the pushed commit hash and key artifact paths.
9. Do not claim or imply a Collatz proof.

Do not ask the user which plan to run when `plans/ACTIVE_CODEX_PLAN.md` exists.

## TDAP workflow

Use this sequence:

1. **Target** — identify the exact open target and scope.
2. **Decompose** — split into algebra, experiment, proof-boundary, and implementation subtasks.
3. **Attack** — run or assign Python/Sage/Lean/reporting work.
4. **Proof-boundary** — classify every output and block over-upgrades.

## Required first actions

1. Read `AGENTS.md`, `CODEX.md`, `CODEX_TASKS.md`, and `CLAIM_GUARDRAILS.md`.
2. Run:

```bash
bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh
```

3. Summarize current state:

```bash
python3 .agents/skills/collatz-research-orchestrator/scripts/summarize_state.py
```

For `go`, these actions are part of Phase A unless the active packet specifies a stricter sequence.

## When to spawn subagents

For complex targets, explicitly propose or spawn these roles:

- `algebra_explorer` — symbolic structure, exact identities, factorization, invariant decomposition.
- `experiment_runner` — Python/Sage runs, CSV/JSON witnesses, command logging.
- `proof_auditor` — proof-boundary classification, theorem-candidate extraction, Lean stubs.
- `implementation_engineer` — setup scripts, tests, CLI wrappers, report plumbing.

Codex only spawns subagents when explicitly asked. If the user asked for maximum Codex use, spawn them. If not, propose the spawn plan and proceed single-agent if necessary. The `go` command counts as permission to use subagents where useful.

## Required orchestration output

Create or update:

```text
reports/<slug>_orchestration.md
reports/<slug>_orchestration.json
```

Each report must include:

```text
target:
scope:
out_of_scope:
subtasks:
commands:
expected_artifacts:
claim_boundary:
blocked_items:
next_step:
```

## Preferred command

```bash
python3 .agents/skills/collatz-research-orchestrator/scripts/orchestrate.py --target "<target>" --run-preflight
```

## Completion criteria

The orchestration pass is complete only when:

1. The target is explicitly scoped.
2. Every subtask has an owner role.
3. The recommended backend is named: Python, Sage, Lean, or report-only.
4. The proof-boundary step is scheduled.
5. No Collatz-level conclusion is asserted.

For `go`, completion additionally requires the active mission packet's acceptance criteria and publication/push requirements.
