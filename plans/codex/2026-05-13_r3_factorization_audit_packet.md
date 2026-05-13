# Codex Mission Packet — r=3 Factorization Audit and Packaging

- **plan_id:** `2026-05-13_r3_factorization_audit_packet`
- **status:** `Advisory Only`
- **target:** audit, verify, split, hash, and package the r=3 Sage S-level factorization outputs
- **scope:** finite-level r=3 lifted-operator S-level characteristic-polynomial algebra only
- **publication:** obey `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md`
- **guardrail:** no finite-level factorization, determinant, spectral, rank, or kernel result may be upgraded into a Collatz-level theorem

## Go command

This mission must be launchable with:

```text
$collatz-research-orchestrator go
```

When invoked with `go`, Codex must:

1. read `plans/ACTIVE_CODEX_PLAN.md`;
2. read this packet;
3. read the publication addendum;
4. execute the mission phases below;
5. commit and push safe results.

## Required reads

```text
AGENTS.md
CODEX.md
CODEX_TASKS.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
PLANS.md
plans/ACTIVE_CODEX_PLAN.md
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
reports/20260513T152905Z_r3_next_cycle_final.md
reports/20260513T152358Z_r3_recon_triage.md
reports/20260513T152815Z_theorem_candidates.md
reports/sage_r3_unit_factorization.sageout
reports/sage_r3_full_factorization.sageout
sage/r3_factorization_search.sage
src/collatz_codex_harness/construct.py
scripts/run_py_checks.py
```

## Non-goals

Do not assert:

1. a proof of Collatz;
2. global orbit behavior;
3. determinant nonvanishing for all real `s > 0`;
4. cross-level r=2/r=3 invariance;
5. structural mechanism unless a separate exact witness is generated;
6. canonical-file changes;
7. Lean stubs for exploratory claims.

## Claim-label rules

Use the labels in `CLAIM_GUARDRAILS.md`.

Default labels:

```text
Advisory Only — plans/workflow/publication notes.
Computational Observation — current r=3 Sage outputs until independently audited.
Verified Fact — only exact finite-level checks with machine-verifiable witness artifacts generated in this mission.
Not Established — determinant positivity, structural mechanism, cross-level invariance, Collatz implications.
Patched — harness/provenance fixes only.
Over-Upgraded — any claim exceeding evidence.
Contradiction Detected — conflict with canonical data or exact recomputation.
```

Even if a factorization is promoted to `Verified Fact`, that applies only to the finite-dimensional S-level characteristic-polynomial factorization inside this repo construction.

## Required output bundle

Create a timestamped bundle:

```text
data/generated/r3_factorization_audit/<timestamp>/
  manifest.json
  unit/
    factorization.txt
    factorization.json
    row_sum_witness.json
    factors/factor_00.txt
    factors/factor_00.json
    ...
  full/
    factorization.txt
    factorization.json
    row_sum_witness.json
    factors/factor_00.txt
    factors/factor_00.json
    ...
```

Also create:

```text
reports/<timestamp>_r3_factorization_audit.md
reports/<timestamp>_r3_factorization_audit.json
reports/<timestamp>_r3_factorization_audit_claim_validation.json
```

Optional, only if all checks pass:

```text
reports/<timestamp>_r3_factorization_canonical_patch_proposal.md
```

The optional canonical patch proposal is `Advisory Only`; do not edit canonical files.

## Phase A — Baseline validation

Run:

```bash
git pull --ff-only || true
bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

If this fails, patch only the minimum harness/environment issue, label it `Patched`, rerun Phase A, and continue only after success.

## Phase B — Implement exact audit helper

Create one helper, preferably Sage:

```text
sage/r3_factorization_audit.sage
```

The helper must:

1. rebuild r=3 unit and full S-level matrices from `src/collatz_codex_harness/construct.py`;
2. compute characteristic polynomials over `QQ[t]` with variable `y`;
3. factor the polynomials using Sage exact algebra;
4. extract factor strings and multiplicities;
5. verify product reconstruction equals the characteristic polynomial;
6. check total y-degree: unit `18`, full `27`;
7. split factors into text/JSON artifacts;
8. hash factor strings, factor JSON objects, raw factorization strings, and final manifest;
9. write all artifacts under `data/generated/r3_factorization_audit/<timestamp>/`;
10. not overwrite existing timestamped bundles.

## Phase C — Factor metadata schema

Each factor JSON must include at least:

```json
{
  "status_label": "Verified Fact or Computational Observation",
  "r": 3,
  "model": "unit or full",
  "level": "S-level",
  "dimension": 18,
  "ring": "QQ[t][y] or exact Sage parent",
  "factor_index": 0,
  "multiplicity": 1,
  "degree_y": 1,
  "degree_t_max": 108,
  "is_linear_in_y": true,
  "is_row_sum_factor": false,
  "irreducible_over_recorded_ring": true,
  "gcd_with_y_derivative_is_one": true,
  "factor_sha256": "...",
  "source_command": "...",
  "claim_boundary": "finite-level exact factor only; no Collatz-level conclusion"
}
```

Use `null` instead of guessing.

## Phase D — Row-sum/Perron factor identification

For each model:

1. compute the exact common row-sum polynomial from the constructed S-level matrix;
2. verify all row sums are equal over the recorded ring;
3. check whether `y - row_sum(t)` appears as a factor;
4. mark the matching factor `is_row_sum_factor: true`;
5. write `row_sum_witness.json`.

If no match is found, label it `Contradiction Detected` only if it conflicts with exact expected row-sum behavior; otherwise label it `Not Established` and explain.

## Phase E — Irreducibility and y-separability

For each factor:

1. record Sage’s factorization over the stated ring;
2. record whether Sage treats the displayed factor as irreducible in that factorization;
3. compute `gcd(f, ∂f/∂y)` in the exact parent or a stated fraction-field parent;
4. record whether the gcd is `1`;
5. do not confuse characteristic-polynomial multiplicity with internal inseparability.

## Phase F — Prior-output comparison

Compare new exact outputs against:

```text
reports/sage_r3_unit_factorization.sageout
reports/sage_r3_full_factorization.sageout
```

The final report must include:

```text
prior_unit_sageout_hash:
new_unit_factorization_hash:
unit_reconstruction_check:
unit_matches_prior_or_explains_format_difference:
prior_full_sageout_hash:
new_full_factorization_hash:
full_reconstruction_check:
full_matches_prior_or_explains_format_difference:
```

Formatting/order differences are acceptable only if exact reconstruction/equality checks pass.

## Phase G — Final audit report

Create:

```text
reports/<timestamp>_r3_factorization_audit.md
reports/<timestamp>_r3_factorization_audit.json
```

Required sections:

```text
status
scope
method
commands_run
input_artifacts
output_bundle
factor_degree_summary
row_sum_factor_summary
irreducibility_summary
separability_summary
reconstruction_checks
claim_labels
not_established_items
blocked_items
recommended_canonical_patch_if_any
why_this_does_not_imply_Collatz
```

The factor-degree summary must include:

```text
model | dimension | factor_degree_pattern | multiplicity_pattern | reconstruction_check | label
unit  | 18        | ...                   | ...                  | pass/fail             | ...
full  | 27        | ...                   | ...                  | pass/fail             | ...
```

## Phase H — Proof-boundary validation

Run:

```bash
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<timestamp>_r3_factorization_audit.md
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/<timestamp>_r3_factorization_audit_claim_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

Patch any proof-boundary blocker before committing.

## Phase I — Optional canonical patch proposal

If all exact audit gates pass, write:

```text
reports/<timestamp>_r3_factorization_canonical_patch_proposal.md
```

Required fields:

```text
status: Advisory Only
section_target:
status_label_recommended:
factorization_manifest_hash:
unit_factor_hashes:
full_factor_hashes:
proof_boundary:
required_external_review:
```

Do not modify canonical bundle files.

## Phase J — Publication

Obey the publication addendum:

```text
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
```

Commit message:

```text
Audit r3 Sage factorization artifacts
```

After pushing, Codex must print:

```text
pushed_commit: <commit hash>
branch: <branch name>
audit_report: reports/<timestamp>_r3_factorization_audit.md
manifest: data/generated/r3_factorization_audit/<timestamp>/manifest.json
claim_validation: reports/<timestamp>_r3_factorization_audit_claim_validation.json
canonical_patch_proposal: reports/<timestamp>_r3_factorization_canonical_patch_proposal.md or none
```

## Subagent plan

If available, use:

```text
algebra_explorer — inspect factors, row-sum factors, multiplicities, structure.
experiment_runner — run Sage helper, preserve logs/witnesses, update manifest.
proof_auditor — audit report/proposal/factor metadata for overreach.
implementation_engineer — implement only minimal reproducible helper scripts.
```

## Acceptance criteria

Mission is complete only when:

1. environment and skill checks pass;
2. r=3 unit and full charpolys are recomputed exactly or prior outputs are verified by exact reconstruction;
3. factor artifacts are split and hash-addressed;
4. multiplicities and total degrees are recorded;
5. row-sum/Perron factor identification is attempted and reported;
6. irreducibility and `gcd(f, ∂f/∂y)` checks are attempted and reported;
7. reconstruction checks pass or failure is explicitly labelled;
8. final audit report exists in Markdown and JSON;
9. proof-boundary validation runs;
10. witness manifest is updated;
11. safe results are committed and pushed;
12. no Collatz-level conclusion is asserted.
