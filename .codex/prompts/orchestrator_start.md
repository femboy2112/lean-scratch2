Use `$collatz-research-orchestrator`.

Target: identify the most valuable next finite-level r=3 research step in this repo.

Instructions:
1. Read `CODEX.md`, `CLAIM_GUARDRAILS.md`, and `CODEX_TASKS.md`.
2. Run `bash scripts/bootstrap_codex.sh`.
3. Produce a plan using `PLANS.md`.
4. Spawn subagents if useful:
   - algebra_explorer
   - experiment_runner
   - proof_auditor
5. Return a consolidated report with commands, artifacts, claim labels, and blockers.
