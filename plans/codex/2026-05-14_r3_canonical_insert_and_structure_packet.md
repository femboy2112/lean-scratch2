# Codex Mission Packet — r=3 Canonical Insert Prep + Factor-Structure Work

- **plan_id:** `2026-05-14_r3_canonical_insert_and_structure_packet`
- **status:** `Advisory Only`
- **target:** prepare a human-reviewable canonical insertion patch for the verified finite-level r=3 factorization bundle, then run additional finite-level factor-structure analysis
- **scope:** finite-level r=3 S-level characteristic-polynomial artifacts and derived factor-structure reports only
- **publication:** obey `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md`
- **hard guardrail:** do not edit canonical bundle files; do not claim or imply a Collatz proof

## One-word launch

This mission must launch with:

```text
$collatz-research-orchestrator go
```

When invoked with `go`, Codex must read `plans/ACTIVE_CODEX_PLAN.md`, this packet, the publication addendum, and then execute all phases below. It must commit and push safe results.

## Required inputs

Read before acting:

```text
AGENTS.md
CODEX.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
plans/ACTIVE_CODEX_PLAN.md
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
reports/20260513T160231Z_r3_factorization_audit.md
reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md
reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.json
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md
reports/20260513T152905Z_r3_next_cycle_final.md
reports/20260513T163247Z_claude_r3_factorization_audit.md if present locally, otherwise continue from v2 proposal
```

Also inspect canonical files only for placement and wording compatibility:

```text
data/canonical_bundle/05_R3_CLOSURES.txt
data/canonical_bundle/08_RECONNAISSANCE_OBSERVATIONS.txt
```

Do **not** modify canonical files.

## Non-goals

Do not assert or attempt:

1. proof of the Collatz conjecture;
2. global orbit behavior;
3. determinant nonvanishing for all real `s > 0`;
4. structural mechanism unless exact new witnesses are produced in this run;
5. cross-level invariance;
6. direct canonical-file edits;
7. Lean formalization;
8. any status stronger than the evidence allows.

## Part 1 — Canonical insertion prep

Create a human-reviewable canonical insertion patch artifact. Do not apply it.

Required outputs:

```text
reports/<timestamp>_r3_factorization_canonical_insert_patch.md
reports/<timestamp>_r3_factorization_canonical_insert_patch.json
reports/<timestamp>_r3_factorization_canonical_insert_review_checklist.md
```

The insertion patch must include:

```text
status: Advisory Only
source_proposal_v2: reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md
source_manifest: data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
candidate_target_file: data/canonical_bundle/05_R3_CLOSURES.txt or data/canonical_bundle/08_RECONNAISSANCE_OBSERVATIONS.txt
candidate_target_section:
placement_rationale:
exact_insert_text:
required_pre_insert_checks:
rollback_note:
proof_boundary:
```

The exact insert text must preserve these facts:

```text
status_label: Verified Fact, finite-level only
r: 3
level: S-level
models: unit and full
unit dimension: 18
unit factor_degree_pattern: [1,1,2,6]
unit multiplicity_pattern: [1,1,2,2]
full dimension: 27
full factor_degree_pattern: [1,1,3,9]
full multiplicity_pattern: [1,2,2,2]
recorded ring: QQ[t][y]
y-separability ring: QQ(t)[y]
manifest file hash: fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254
manifest payload hash: e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f
```

The exact insert text must explicitly say:

```text
This is a finite-level S-level characteristic-polynomial factorization fact only. It does not prove or imply the Collatz conjecture, global orbit behavior, determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism.
```

It must use the wording:

```text
Sage-displayed irreducibility over QQ[t][y]
y-separability checked over QQ(t)[y]
```

It must not say simply:

```text
irreducible factors are proved irreducible
```

unless a separate proof is produced.

## Part 2 — Additional finite-level factor-structure work

Codex must do more than report formatting. It must run a finite-level factor-structure analysis over the existing audited factor bundle.

Required outputs:

```text
data/generated/r3_factor_structure/<timestamp>/factor_relation_manifest.json
reports/<timestamp>_r3_factor_structure_analysis.md
reports/<timestamp>_r3_factor_structure_analysis.json
reports/<timestamp>_r3_factor_structure_next_targets.md
```

Implement a small helper if useful:

```text
scripts/r3_factor_structure_analysis.py
```

or Sage if exact gcd/divisibility work is attempted:

```text
sage/r3_factor_structure_analysis.sage
```

The analysis must inspect:

```text
data/generated/r3_factorization_audit/20260513T160231Z/unit/factors/*.json
data/generated/r3_factorization_audit/20260513T160231Z/full/factors/*.json
```

Required factor-structure questions:

1. Which factor hashes are shared between unit and full?
2. Which factor is the row-sum/Perron factor for each model?
3. Does the shared non-row-sum factor have the same multiplicity in unit and full?
4. Are full-model higher-degree factors degree-multiples of unit-model factors in a simple way?
5. Are there obvious quotient/residual degree patterns?
6. What exact Sage follow-up tests are justified next?
7. Which structural-mechanism claims remain `Not Established`?

Minimum expected observations to verify from the bundle:

```text
unit factor_01 hash == full factor_01 hash == 02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69
unit row-sum factor index: 0
full row-sum factor index: 0
unit degree pattern: [1,1,2,6]
full degree pattern: [1,1,3,9]
```

If Sage is available, attempt exact pairwise gcds over `QQ(t)[y]` or `QQ[t][y]` for all unit/full factors and record:

```text
unit_factor_i
full_factor_j
gcd_degree_y
gcd_hash_or_expression
claim_label
```

If Sage is unavailable, perform static hash/degree analysis only and label gcd work `Not Established`.

## Part 3 — Proposed next research packet

Create a short next-packet recommendation:

```text
reports/<timestamp>_r3_next_structural_mechanism_packet_recommendation.md
```

It must propose one or two exact next missions, such as:

```text
1. commutant / symmetry / equitable-partition search for the squared factors;
2. exact pairwise gcd/divisibility and quotient-residual relation search over QQ(t)[y];
3. row-sum factor quotient analysis for unit/full residual characteristic polynomials.
```

Do not create the next active packet yet. Only recommend it.

## Validation

Run:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<timestamp>_r3_factorization_canonical_insert_patch.md
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<timestamp>_r3_factor_structure_analysis.md
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/<timestamp>_r3_canonical_insert_structure_claim_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

If any proof-boundary blocker appears, patch the offending report before committing.

## Publication

Obey:

```text
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
```

Commit message:

```text
Prepare r3 canonical insertion and structure analysis
```

After pushing, print:

```text
pushed_commit: <commit hash>
branch: <branch name>
canonical_insert_patch: reports/<timestamp>_r3_factorization_canonical_insert_patch.md
structure_analysis: reports/<timestamp>_r3_factor_structure_analysis.md
factor_relation_manifest: data/generated/r3_factor_structure/<timestamp>/factor_relation_manifest.json
claim_validation: reports/<timestamp>_r3_canonical_insert_structure_claim_validation.json
next_recommendation: reports/<timestamp>_r3_next_structural_mechanism_packet_recommendation.md
```

## Acceptance criteria

Mission complete only if:

1. canonical insertion patch artifact exists but canonical files are untouched;
2. insertion text includes all required hashes, rings, patterns, and proof boundaries;
3. factor-structure analysis exists in Markdown/JSON;
4. shared factor and row-sum factors are identified or explicitly blocked;
5. any exact gcd work is either run and recorded or marked `Not Established` if Sage unavailable;
6. next structural-mechanism recommendation exists;
7. proof-boundary validation runs;
8. witness manifest updates;
9. safe results are committed and pushed;
10. no Collatz-level conclusion is asserted.
