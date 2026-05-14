# r=3 Canonical Proposal Patch Orchestration

target: patch the r=3 factorization canonical patch proposal using Claude audit findings
scope: report/proposal refinement only; no canonical bundle modification
out_of_scope: canonical bundle edits, new Sage algebra, determinant nonvanishing for all real s > 0, structural-mechanism claims, exact subdominant spectral claims, cross-level invariance, Collatz-level implications
claim_boundary: This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.

## subtasks

| role | subtask | backend | status |
|---|---|---|---|
| collatz-research-orchestrator | read active plan, mission packet, publication addendum, and canonical guardrails | report-only | complete |
| implementation_engineer | create v2 proposal Markdown/JSON and patch summary without touching canonical files | report-only | complete |
| proof_auditor | run report audit and claim ladder validation | Python | scheduled |
| experiment_runner | collect witness manifest after report patch | Python | scheduled |

## commands

- `bash scripts/bootstrap_codex.sh`
- `bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh`
- `python3 .agents/skills/collatz-research-orchestrator/scripts/summarize_state.py`
- `python3 scripts/check_codex_skills.py`
- `python3 scripts/run_py_checks.py`
- `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
- `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/20260514T023536Z_r3_canonical_proposal_patch_claim_validation.json`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py`

## expected_artifacts

- `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md`
- `reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json`
- `reports/20260514T023536Z_r3_canonical_proposal_patch_summary.md`
- `reports/20260514T023536Z_r3_canonical_proposal_patch_claim_validation.json`
- `reports/witness_manifest.json`

## blocked_items

None at orchestration time.

## next_step

Run proof-boundary validation, final sanity gates, collect witnesses, then commit and push safe result artifacts.
