# AGENTS.md — Collatz finite-level spectral research harness

## Repository mission

This repo is a computational research harness for the finite-level lifted-operator Collatz program. It is not a proof of the Collatz conjecture. Use it to build, run, audit, and report exact finite-level algebra and carefully labelled computational reconnaissance.

## Start every session

1. Read `CODEX.md`.
2. Read `CLAIM_GUARDRAILS.md`.
3. Run the fast sanity gate before changing math code:

```bash
bash scripts/bootstrap_codex.sh
```

If the task requires exact Sage algebra:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

## Repo map

- `data/canonical_bundle/` — canonical project state and prompt.
- `src/collatz_codex_harness/` — construction, hashing, reporting, guardrails.
- `experiments/` — Python reconnaissance scripts.
- `sage/` — exact-algebra Sage scripts.
- `lean/` — formalization stubs only.
- `reports/` — generated reports and witness artifacts.
- `.agents/skills/` — reusable Codex skills.
- `.codex/` — optional project-scoped Codex configuration, agent roles, prompts, and review notes.

## Mandatory claim boundary

Never claim that finite-level matrix facts prove, imply, nearly prove, or essentially solve the Collatz conjecture.

Use exactly scoped language:

```text
This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework.
```

Forbidden claim shapes:

```text
This proves Collatz.
This essentially proves Collatz.
This shows no divergent Collatz orbits exist.
The spectral radius bound solves the conjecture.
```

## Required labels

Every mathematical or computational claim must be labelled as one of:

- `Verified Fact`
- `Computational Observation`
- `Not Established`
- `Withdrawn`
- `Patched`
- `Contradiction Detected`
- `Over-Upgraded`
- `Advisory Only`

Do not invent new labels without explicitly updating `CLAIM_GUARDRAILS.md`.

## Evidence standard

For every nontrivial output, record:

```text
status:
scope:
method:
claim_boundary:
reproduction_command:
files_touched:
artifacts_produced:
```

For computation reports, include input hashes whenever possible.

## Exactness rules

- Use Sage for exact rational/polynomial matrix algebra when available.
- Python/SymPy may orchestrate, prototype, and run smaller exact checks.
- Floating-point eigenvalue data is never proof.
- Modular probes may prove nonzero-polynomial facts only when the evaluation map is explicitly specified and checked.
- Numerical positivity samples never prove all-real positivity.

## Subagent policy

Use subagents for hard or parallel tasks. Spawn only when the prompt explicitly asks for multi-agent work or when a skill instructs you to propose a spawn plan and the user accepts.

Default subagent roles:

1. `algebra_explorer` — search symbolic structures and exact identities.
2. `experiment_runner` — run Python/Sage probes and produce witnesses.
3. `proof_auditor` — classify claims and block overreach.
4. `implementation_engineer` — maintain scripts, tests, Makefile, setup, and reports.

## Review policy

Before finalizing meaningful changes:

```text
Run tests/sanity gates.
Run the proof-boundary auditor on new reports.
Use /review on uncommitted changes when available.
```

Review against `REVIEW_RULES.md`.

## Done means

A task is not done until:

1. The relevant command was run or a clear blocker is documented.
2. Artifacts are written under `reports/` or the target directory.
3. Claims are labelled.
4. False Collatz-level escalation is absent.
5. The reproduction command is included.
