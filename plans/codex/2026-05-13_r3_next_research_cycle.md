# Codex Mission Packet — r=3 Next Finite-Level Research Cycle

- **plan_id:** `2026-05-13_r3_next_research_cycle`
- **status:** `Advisory Only`
- **target:** r=3 compact factorization + determinant nonvanishing triage
- **scope:** finite-level lifted-operator Collatz research only
- **owner:** Codex using repo skills and subagents where available
- **required guardrail:** no finite-level spectral, determinant, rank, kernel, or factorization result may be upgraded into a Collatz-level theorem

## 0. Start prompt for Codex

Use this exact task prompt from repo root:

```text
$collatz-research-orchestrator read plans/ACTIVE_CODEX_PLAN.md and execute it exactly. Use subagents where useful. Run Python reconnaissance first, collect witnesses, audit proof boundaries, and promote to Sage exact algebra only when the plan's promotion rules are satisfied. Commit only scripts, reports, witness data, theorem-candidate notes, and safe plan-status updates. Do not claim or imply a Collatz proof.
```

## 1. Required reads before action

Codex must read these files before modifying or running research logic:

```text
AGENTS.md
CODEX.md
CODEX_TASKS.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
PLANS.md
.agents/skills/collatz-research-orchestrator/SKILL.md
.agents/skills/collatz-exact-algebra-lab/SKILL.md
.agents/skills/collatz-proof-boundary-auditor/SKILL.md
data/canonical_bundle/PROMPT.md
data/canonical_bundle/05_R3_CLOSURES.txt
data/canonical_bundle/06_MATHEMATICAL_CONSTRAINTS.txt
data/canonical_bundle/07_INTERPRETATION_AND_BOUNDARIES.txt
```

## 2. Non-goals

Do **not** attempt or assert any of the following:

1. A proof of the Collatz conjecture.
2. A claim that finite-level spectral closure implies global orbit behavior.
3. A claim that determinant samples prove all-real-s nonvanishing.
4. A claim that numerical eigenvalue multiplicity proves algebraic multiplicity.
5. A claim that an r=2 mechanism automatically transfers to r=3.
6. A canonical-bundle patch unless the change is explicitly classified as `Patched` and audited.
7. Lean formalization of exploratory claims.

## 3. Claim labels

Every mathematical or computational claim must use exactly one of the project labels:

```text
Verified Fact
Computational Observation
Not Established
Withdrawn
Patched
Contradiction Detected
Over-Upgraded
Advisory Only
```

Use the weakest label supported by evidence.

## 4. Execution phases

### Phase A — Environment and skill validation

Run from repo root:

```bash
bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-research-orchestrator/scripts/summarize_state.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_state_summary.json
```

Expected:

```text
preflight exits 0
check_codex_skills.py exits 0
run_py_checks.py exits 0
state summary includes the canonical bundle and three skills
```

If any command fails, stop and patch only the minimum setup defect. Do not proceed into math experiments until Phase A passes.

### Phase B — Create orchestration report

Run:

```bash
python3 .agents/skills/collatz-research-orchestrator/scripts/orchestrate.py \
  --target "r=3 compact factorization and determinant nonvanishing triage" \
  --run-preflight \
  --out-prefix r3_next_research_cycle
```

Expected artifacts:

```text
reports/*_r3_next_research_cycle_orchestration.md
reports/*_r3_next_research_cycle_orchestration.json
```

The orchestration report must name all subtasks, backends, expected artifacts, claim boundary, and blocked items.

### Phase C — Tier 1 Python reconnaissance

Run exactly these wrapper targets first:

```bash
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-unit-fast
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-full-fast
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py factor-python
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py cross-level
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

Expected artifacts:

```text
reports/*_spectral-fast.log
reports/*_spectral-fast_analysis.md
reports/*_spectral-fast_witness.json
reports/*_modular-unit-fast.log
reports/*_modular-unit-fast_analysis.md
reports/*_modular-unit-fast_witness.json
reports/*_modular-full-fast.log
reports/*_modular-full-fast_analysis.md
reports/*_modular-full-fast_witness.json
reports/*_factor-python.log
reports/*_factor-python_analysis.md
reports/*_factor-python_witness.json
reports/*_cross-level.log
reports/*_cross-level_analysis.md
reports/*_cross-level_witness.json
reports/witness_manifest.json
```

All Phase C outputs are `Computational Observation` unless independently upgraded by exact algebra and audit.

### Phase D — First proof-boundary audit

Run:

```bash
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_claim_ladder_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

If the validator reports `Over-Upgraded`, `Contradiction Detected`, or forbidden Collatz-level language, stop and patch reports before running more experiments.

### Phase E — Triage Python results

Codex must inspect the Phase C reports and answer these questions in a new report:

```text
reports/<timestamp>_r3_recon_triage.md
reports/<timestamp>_r3_recon_triage.json
```

Required questions:

1. Did spectral-fast reveal repeated unit/full structure across s = 0.50, 0.55, 0.60?
2. Did modular-unit-fast or modular-full-fast produce a stable nonzero determinant witness pattern?
3. Did factor-python reveal any candidate compact factors, repeated factor templates, quotient decompositions, or residual decompositions?
4. Did cross-level reveal any invariant pattern worth exact testing?
5. Which exact Sage target, if any, is justified next?
6. Which claims remain `Not Established`?
7. Which claims should be explicitly rejected or downgraded?

The triage report must include a table with columns:

```text
candidate | evidence | label | exact_next_test | risk
```

### Phase F — Sage promotion rules

Only run Sage after Phase E chooses a concrete exact target.

Before Sage:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

Sanity check:

```bash
timeout 900 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r2
```

Then choose the smallest justified r=3 exact target:

```bash
timeout 1800 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r3-unit
```

Run full r=3 only if at least one of these is true:

1. `sage-r3-unit` identifies a concrete factor/determinant target needing full-model confirmation.
2. Phase E identifies a specific full-model candidate already visible in Python reconnaissance.
3. The user explicitly instructs Codex to spend the runtime.

If justified:

```bash
timeout 3600 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r3-full
```

After every Sage run:

```bash
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_post_sage_claim_ladder_validation.json
```

### Phase G — Theorem-candidate extraction

Only after exact evidence exists, write:

```text
reports/<timestamp>_theorem_candidates.md
reports/<timestamp>_theorem_candidates.json
```

Each theorem candidate must include:

```text
name:
status_label:
quantified_variables:
r:
model:
slice_or_parameter:
level:
matrix_family:
domain_or_ring:
statement:
evidence_artifacts:
missing_proof_steps:
why_this_does_not_imply_Collatz:
```

Generate Lean stubs only for candidates labelled `Verified Fact` or exact finite-level theorem candidates with all hypotheses specified.

### Phase H — Final report and commit

Create:

```text
reports/<timestamp>_r3_next_cycle_final.md
reports/<timestamp>_r3_next_cycle_final.json
```

Final report must include:

```text
commands_run:
artifacts_created:
claim_labels:
exact_results:
computational_observations:
not_established_items:
blocked_items:
recommended_next_plan:
```

Then run:

```bash
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_final_claim_ladder_validation.json
pytest -q || true
python3 scripts/run_py_checks.py
```

Commit only if Phase A passed and no proof-boundary blocker remains.

Suggested commit message:

```text
Run r3 finite-level reconnaissance cycle
```

## 5. Subagent plan

If Codex supports subagents in the local setup, spawn:

```text
algebra_explorer
experiment_runner
proof_auditor
implementation_engineer
```

### algebra_explorer

Task:

```text
Read the r=3 closure files and Phase C outputs. Identify exact symbolic structures, factorization hypotheses, quotient/residual decompositions, determinant candidates, and invariant decompositions worth Sage testing. Return only finite-level claims with explicit evidence labels.
```

### experiment_runner

Task:

```text
Run the Phase A through Phase C commands. Preserve logs, witnesses, and failed probes. Never overwrite prior artifacts without a new timestamp.
```

### proof_auditor

Task:

```text
Audit all generated reports and witness summaries. Reject finite-level-to-Collatz escalation. Produce patch instructions for any over-upgraded language.
```

### implementation_engineer

Task:

```text
Fix only harness defects blocking execution: Python command mismatch, missing executable bits, missing directories, bad report paths, or broken wrappers. Do not alter mathematical definitions unless explicitly directed by the proof auditor.
```

## 6. Acceptance criteria

The mission is complete when all are true:

1. `scripts/check_codex_skills.py` passes.
2. `scripts/run_py_checks.py` passes.
3. Tier 1 reconnaissance artifacts exist.
4. `reports/witness_manifest.json` is updated.
5. Proof-boundary validation has been run after reconnaissance and after any Sage step.
6. Final report exists in both Markdown and JSON.
7. Every mathematical claim has a project claim label.
8. No Collatz-level conclusion is asserted.
9. Any Sage execution failure is recorded as a blocker, not hidden.
10. Next exact target is clearly recommended.

## 7. What to bring back to ChatGPT

After Codex finishes, provide ChatGPT with:

```text
latest commit hash
reports/<timestamp>_r3_next_cycle_final.md
reports/witness_manifest.json
any theorem_candidates files
any failed command logs
```

The next ChatGPT task should be:

```text
Audit Codex's r=3 next-cycle outputs for mathematical soundness, claim-boundary correctness, and next-step quality.
```
