# Publication Addendum — r=3 Next Finite-Level Research Cycle

- **addendum_id:** `2026-05-13_r3_next_research_cycle_publish_addendum`
- **status:** `Advisory Only`
- **applies_to:** `plans/codex/2026-05-13_r3_next_research_cycle.md`
- **purpose:** make result publication explicit

## Mandatory override

This addendum overrides the earlier ambiguity in the mission packet. Codex must not stop after producing local reports. If the work is safe to commit, Codex must also push the resulting commit to GitHub.

## Publication Phase I — Commit and push results

Run this only after the final report, witness manifest, and final proof-boundary validation have been generated.

### I.1 Inspect status

```bash
git status --short
```

If there are no changes, write a short terminal summary saying no new commit is needed.

### I.2 Review changed files

```bash
git diff --stat
git diff -- reports plans data/generated .agents scripts sage lean || true
```

Do not commit files outside the intended result set unless they are required harness fixes.

Allowed commit paths:

```text
reports/
data/generated/
plans/
lean/
sage/
scripts/
.agents/
.codex/
```

Do not commit:

```text
.venv/
.sage-conda/
__pycache__/
.pytest_cache/
.mypy_cache/
.DS_Store
large temporary logs outside reports/
```

### I.3 Final validation before commit

Run:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_pre_push_claim_ladder_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

If a proof-boundary blocker appears, do not commit. Patch the offending report or stop with a blocker summary.

### I.4 Commit

Use:

```bash
git add reports data/generated plans lean sage scripts .agents .codex
git status --short
git commit -m "Run r3 finite-level reconnaissance cycle"
```

If only plan/status files changed, use:

```bash
git commit -m "Update r3 Codex research cycle status"
```

### I.5 Push

Push to the current branch:

```bash
git push
```

If Git says the branch has no upstream, run:

```bash
git push -u origin HEAD
```

### I.6 Report pushed commit

After pushing, Codex must print:

```text
pushed_commit: <commit hash>
branch: <branch name>
final_report: reports/<timestamp>_r3_next_cycle_final.md
witness_manifest: reports/witness_manifest.json
proof_boundary_validation: reports/<timestamp>_pre_push_claim_ladder_validation.json
```

## If push fails

If `git push` fails, Codex must not silently stop. It must report:

```text
push_status: failed
failure_command: git push
stderr_summary: <short summary>
local_commit: <commit hash if created>
manual_recovery:
  git status
  git log --oneline -5
  git push -u origin HEAD
```

## Boundary

This publication addendum changes only repository workflow. It does not change any mathematical claim labels and does not permit any Collatz-level conclusion.
