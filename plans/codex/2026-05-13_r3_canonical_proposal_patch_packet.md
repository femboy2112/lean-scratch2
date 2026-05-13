# Codex Mission Packet — Patch r=3 Factorization Canonical Proposal

- **plan_id:** `2026-05-13_r3_canonical_proposal_patch_packet`
- **status:** `Advisory Only`
- **target:** patch the r=3 factorization canonical patch proposal using Claude audit findings
- **scope:** report/proposal refinement only; no canonical bundle modification
- **publication:** obey `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md`
- **guardrail:** no Collatz-level theorem, no determinant nonvanishing claim, no structural-mechanism claim, no canonical-file edit

## Go command

This mission must be launchable with:

```text
$collatz-research-orchestrator go
```

When invoked with `go`, Codex must:

1. read `plans/ACTIVE_CODEX_PLAN.md`;
2. read this packet;
3. read the publication addendum;
4. patch only the proposal/report artifacts named below;
5. validate proof boundary;
6. commit and push safe results.

## Required inputs

Read:

```text
AGENTS.md
CLAIM_GUARDRAILS.md
reports/20260513T160231Z_r3_factorization_audit.md
reports/20260513T160231Z_r3_factorization_audit.json
reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
```

If available locally, also read Claude’s audit branch or files. If not available, use the findings embedded in this packet.

## Claude audit findings to implement

Claude’s disposition was `PASS_WITH_PATCHES`. No blockers. Implement these patch-level refinements in a new revised proposal:

1. Add per-model degree pattern, multiplicity pattern, and dimension:
   - unit: dimension `18`, factor_degree_pattern `[1, 1, 2, 6]`, multiplicity_pattern `[1, 1, 2, 2]`.
   - full: dimension `27`, factor_degree_pattern `[1, 1, 3, 9]`, multiplicity_pattern `[1, 2, 2, 2]`.
2. Add `manifest_payload_sha256`:
   - `e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f`.
3. Keep the manifest file hash:
   - `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254`.
4. Add recorded ring:
   - `QQ[t][y]`, represented by Sage as `Univariate Polynomial Ring in y over Univariate Polynomial Ring in t over Rational Field`.
5. Add y-separability ring:
   - `QQ(t)[y]`, represented by a polynomial ring over `FractionField(QQ[t])`.
6. Reword irreducibility as:
   - `Sage-displayed irreducibility over QQ[t][y]`.
   Do not state or imply a separate human proof of irreducibility.
7. Add reproduction caveat:
   - a human-side rerun of `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage` is required before canonical-file insertion.
8. Keep canonical proposal status `Advisory Only`.
9. Keep canonical bundle files untouched.

## Required output files

Create a new revised proposal; do not overwrite the original proposal:

```text
reports/<timestamp>_r3_factorization_canonical_patch_proposal_v2.md
reports/<timestamp>_r3_factorization_canonical_patch_proposal_v2.json
```

Also create a short patch summary:

```text
reports/<timestamp>_r3_canonical_proposal_patch_summary.md
```

## Required content for v2 proposal

The v2 proposal must include:

```text
status: Advisory Only
source_audit_report: reports/20260513T160231Z_r3_factorization_audit.md
source_manifest: data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
original_proposal: reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md
factorization_manifest_file_sha256:
manifest_payload_sha256:
recorded_ring:
y_separability_ring:
irreducibility_wording:
reproduction_caveat:
proof_boundary:
required_external_review:
```

It must include this table:

```text
model | dimension | factor_degree_pattern | multiplicity_pattern | reconstruction_check | row_sum_factor_index | status_label
unit  | 18        | [1,1,2,6]             | [1,1,2,2]            | True                 | 0                    | Verified Fact, finite-level only
full  | 27        | [1,1,3,9]             | [1,2,2,2]            | True                 | 0                    | Verified Fact, finite-level only
```

It must preserve these hashes exactly:

```text
unit factor hashes:
- factor_00: fb4cc15db6c76dea45ece185f3a2808bc519f4183864a7124646a32588376aec
- factor_01: 02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69
- factor_02: 3860a125d1de0df7c0cf81fb47a2164c29760a73f7c70eef58ce54b5099fb3e7
- factor_03: a6d3d2b27ed7a8d34fc651677ffa1a58b8e70744c0bf1fc576c0118d1555fc1d

full factor hashes:
- factor_00: a44fcd571bbd816ac64489d88a87cd35f967e14d04e2ee88a1b0af98454c1b14
- factor_01: 02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69
- factor_02: d201683ad25dacc610b24120a0f1ddd4e051442771b803bdeda1ab7d532fd42a
- factor_03: 498455175f2d2defadc095649900160284cec3b6c69f63bc639d187b0271c9a5
```

## Proof-boundary requirements

The v2 proposal must explicitly say:

```text
This proposal supports only a finite-level exact S-level characteristic-polynomial factorization claim for the r=3 unit/full matrices reconstructed in this repo. It does not prove or imply the Collatz conjecture, global orbit behavior, all-real-s determinant nonvanishing, cross-level invariance, or a structural mechanism.
```

It must list `Not Established` items:

```text
- determinant nonvanishing for all real s > 0
- structural mechanism explaining factorization
- exact subdominant spectral structure
- cross-level invariance
- Collatz-level implications
- independent human proof of irreducibility beyond Sage-displayed factorization
```

## Validation commands

Run:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<timestamp>_r3_factorization_canonical_patch_proposal_v2.md
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/<timestamp>_r3_canonical_proposal_patch_claim_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

If the proof-boundary auditor reports a blocker, patch the v2 proposal before committing.

## Publication

Obey:

```text
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
```

Commit message:

```text
Patch r3 factorization canonical proposal
```

After pushing, print:

```text
pushed_commit: <commit hash>
branch: <branch name>
v2_proposal: reports/<timestamp>_r3_factorization_canonical_patch_proposal_v2.md
v2_json: reports/<timestamp>_r3_factorization_canonical_patch_proposal_v2.json
patch_summary: reports/<timestamp>_r3_canonical_proposal_patch_summary.md
claim_validation: reports/<timestamp>_r3_canonical_proposal_patch_claim_validation.json
```

## Acceptance criteria

Mission complete only if:

1. original proposal is preserved;
2. v2 proposal exists in Markdown and JSON;
3. v2 includes degree/multiplicity/dimension table;
4. v2 includes both manifest file hash and manifest payload hash;
5. v2 states recorded ring and y-separability ring;
6. v2 uses `Sage-displayed irreducibility` wording;
7. v2 contains reproduction caveat;
8. v2 does not edit canonical files;
9. proof-boundary validation runs;
10. safe results are committed and pushed.
