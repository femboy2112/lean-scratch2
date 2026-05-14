# Codex Mission Packet — r=3 Structural Mechanism Grand Campaign

- **plan_id:** `2026-05-14_r3_structural_mechanism_grand_campaign_packet`
- **status:** `Advisory Only`
- **mission_type:** massive multi-phase finite-level research campaign
- **target:** explain, test, and classify the residual/factor structure behind the audited r=3 S-level unit/full characteristic-polynomial factorizations
- **launch:** `$collatz-research-orchestrator go`
- **publication:** obey `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md`
- **hard boundary:** no finite-level matrix, spectral, determinant, factorization, or residual fact proves or implies the Collatz conjecture

## 0. Mission objective

Use the now-validated specialized skill/agent layer to conduct a comprehensive finite-level r=3 research campaign.

The campaign begins from the verified finite-level facts already in the repo:

```text
r=3 unit S-level factorization:
  dimension = 18
  factor_degree_pattern = [1, 1, 2, 6]
  multiplicity_pattern = [1, 1, 2, 2]
  row_sum_factor_index = 0

r=3 full S-level factorization:
  dimension = 27
  factor_degree_pattern = [1, 1, 3, 9]
  multiplicity_pattern = [1, 2, 2, 2]
  row_sum_factor_index = 0

shared non-row-sum factor:
  unit factor_01 == full factor_01
  hash = 02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69

exact unit/full gcd table over QQ(t)[y]:
  only factor_01 vs factor_01 has nonconstant gcd
  all other unit/full factor pairs have gcd 1

residual coprimality:
  U_residual and F_residual have cross-gcd degree 0 over QQ(t)[y]
```

The campaign should move from these facts toward:

```text
mechanism candidates
residual block decompositions
commutant/projector/equitable partition evidence
factor-root/spectral tracking targets
determinant/root-isolation target selection
canonical readiness review
Lean readiness screening
red-team evidence audit
next exact mission packets
```

## 1. Non-negotiable guardrails

### 1.1 Scope

In scope:

```text
finite-level r=3 S-level matrices
unit/full models
QQ[t][y] and QQ(t)[y] factor algebra
row-sum/Perron factors
shared factor C
residual factors and residual characteristic polynomials
commutants, projectors, idempotents, automorphisms, equitable partitions
specialized rational-t exact specializations
bounded numerical spectral sweeps
bounded modular determinant samples
canonical insertion previews only
proof-boundary and red-team audit
Lean-readiness reports only for exact finite-level candidates
```

Out of scope:

```text
Collatz proof
global orbit behavior
B-level descent from S-level facts
all-real-s determinant nonvanishing unless exactly proved for a named polynomial
cross-level invariance unless exact witness is produced
structural mechanism unless exact generic witness is produced
canonical bundle edits without explicit human authorization
Lean proofs of exploratory claims
```

### 1.2 Required claim labels

Every nontrivial statement must use one of:

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

Default labels:

| Claim type | Default label |
|---|---|
| Exact Sage equality over stated ring | `Verified Fact` |
| Exact fixed-rational specialization over QQ | `Verified Fact` for that specialization only |
| Numerical eigenvalue ordering | `Computational Observation` |
| Modular sample | `Computational Observation` |
| Pattern across several specializations | `Computational Observation` |
| Generic structural mechanism | `Not Established` unless exact generic witness exists |
| Determinant positivity/nonvanishing for all real s > 0 | `Not Established` unless complete exact proof exists |
| Canonical insertion preview | `Advisory Only` |
| Tooling cleanup | `Patched` |

## 2. Required reads before action

Codex must read:

```text
AGENTS.md
CODEX.md
CODEX_SKILLS.md
CODEX_TASKS.md
CLAIM_GUARDRAILS.md
REVIEW_RULES.md
plans/ACTIVE_CODEX_PLAN.md
plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md
plans/codex/2026-05-14_codex_specialized_capability_validation_packet.md
reports/20260514T070727Z_codex_capability_matrix.md
reports/20260514T070727Z_specialized_skills_validation.md
reports/20260513T160231Z_r3_factorization_audit.md
reports/20260514T052552Z_r3_factor_structure_gcd.md
reports/20260514T055252Z_r3_deep_program_final.md
reports/20260514T063536Z_r3_deep_program_final.md
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json
data/generated/r3_deep_program/20260514T063536Z/program_manifest.json if present
src/collatz_codex_harness/construct.py
sage/r3_factor_structure_gcd.sage
sage/r3_factor_relation_expansion.sage
```

Codex must use local Sage explicitly:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage <script>
```

Never use bare `sage`.

## 3. Required specialized skills and agents

Use the new skill layer deliberately:

| Workstream | Skill | Agent |
|---|---|---|
| Campaign execution | `collatz-campaign-manager` | `campaign_operator` |
| Provenance and manifests | `collatz-provenance-reproducibility-lab` | `provenance_librarian` |
| Factor/residual algebra | `collatz-factor-structure-lab` | `sage_factor_algebraist`, `factor_cartographer` |
| Mechanism search | `collatz-symmetry-mechanism-lab` | `mechanism_hunter` |
| Spectrum/determinant | `collatz-spectrum-determinant-lab` | `spectral_tracker`, `determinant_root_analyst` |
| Canonical preview | `collatz-canonical-curator` | `canonical_curator` |
| Lean readiness | `collatz-lean-formalization-bridge` | `formalization_engineer` |
| Adversarial review | `collatz-red-team-reviewer` | `red_team_skeptic` |
| Proof boundary | `collatz-proof-boundary-auditor` | `proof_auditor` |

The `go` command counts as permission to use subagents where useful. If subagents are unavailable, proceed single-agent but preserve role-labeled sections in all reports.

## 4. Output root and timestamp

Create one run timestamp:

```text
<TS> = UTC timestamp like 20260514T123456Z
```

Use these roots:

```text
data/generated/r3_mechanism_campaign/<TS>/
reports/<TS>_*.md
reports/<TS>_*.json
```

Every phase must write a phase receipt:

```text
data/generated/r3_mechanism_campaign/<TS>/phase_receipts/<phase_id>.json
```

Every phase receipt must include:

```json
{
  "phase_id": "A",
  "status": "PASS | PARTIAL | BLOCKED_BY_TIMEOUT | BLOCKED_BY_ENVIRONMENT | REJECTED_BY_AUDIT",
  "commands_run": [],
  "artifacts_created": [],
  "claim_labels": [],
  "blocked_items": [],
  "safe_next_phase": "..."
}
```

## 5. Phase map

| Phase | Name | Main purpose |
|---|---|---|
| A | State lock and campaign manifest | Verify environment and create campaign scaffold |
| B | Provenance and factor registry | Consolidate all audited factor data |
| C | Residual algebra verification | Recompute/verify residuals and coprimality |
| D | Exact relation expansion, selected targets | Compute targeted gcd/resultant/discriminant/substitution data |
| E | Commutant specialization search | Fixed-rational commutant dimensions and basis summaries |
| F | Projector/idempotent search | Search for exact finite block/projection evidence |
| G | Equitable partition and quotient search | Try quotient matrices explaining factors |
| H | Automorphism/permutation search | Search finite symmetries at specializations |
| I | Spectral factor-root tracking | Numerical factor-root ownership, with strict labels |
| J | Determinant target taxonomy and one exact attempt | Define determinant objects and select one exact target |
| K | Canonical insertion final preview | Human-review insertion packet, no canonical edits |
| L | Lean readiness screening | Report finite theorem candidates; stubs only if safe |
| M | Red-team review | Source/evidence adversarial audit |
| N | Final synthesis and next packets | Final campaign report and next mission recommendations |

## Phase A — State lock and campaign manifest

### Goal

Verify that the specialized Codex layer is installed and that the campaign can run with local Sage.

### Commands

```bash
git pull --ff-only || true
git status --short
git rev-parse HEAD
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 scripts/build_specialized_codex_capabilities.py
python3 scripts/check_codex_skills.py
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage --version
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/campaign_manifest.json
data/generated/r3_mechanism_campaign/<TS>/state_lock.json
reports/<TS>_r3_mechanism_campaign_state_lock.md
reports/<TS>_r3_mechanism_campaign_state_lock.json
```

### Required checks

- `scripts/check_codex_skills.py` returns `ok: true`.
- all 11 skills are discoverable.
- all 14 configured agents are present.
- local Sage is executable.
- current commit SHA is recorded.

### Stop condition

If Sage is unavailable, stop exact algebra phases and produce `BLOCKED_BY_ENVIRONMENT` final report.

## Phase B — Provenance and factor registry

### Goal

Create a single canonical campaign-local registry of factor artifacts and exact relationships.

### Inputs

```text
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/factor_registry.json
data/generated/r3_mechanism_campaign/<TS>/factor_registry.csv
data/generated/r3_mechanism_campaign/<TS>/factor_graph/factor_graph.json
data/generated/r3_mechanism_campaign/<TS>/factor_graph/factor_graph.dot
reports/<TS>_r3_campaign_factor_registry.md
reports/<TS>_r3_campaign_factor_network.md
```

### Required registry fields

```text
model
factor_index
factor_hash
degree_y
degree_t_max
multiplicity
is_row_sum_factor
is_shared_unit_full_factor
shared_with
gcd_relations
source_json
source_txt
status_label
claim_boundary
```

### Graph nodes

```text
unit factor_00..03
full factor_00..03
Ru, Rf, C
U_no_row, F_no_row
U_residual, F_residual
```

### Graph edges

```text
same_hash
row_sum_factor
nonconstant_gcd
coprime_gcd_1
residual_component
multiplicity_relation
higher_degree_ratio
```

### Labels

- Exact registry facts: `Verified Fact`.
- Graph layout/summary: `Advisory Only`.
- Mechanism inference from graph: `Not Established` unless later proved.

## Phase C — Residual algebra verification

### Goal

Recompute or verify residual characteristic-polynomial objects.

### Definitions

```text
U(y,t) = unit characteristic polynomial
F(y,t) = full characteristic polynomial
Ru = unit row-sum factor
Rf = full row-sum factor
C = shared non-row-sum linear factor
U_no_row = U / Ru
F_no_row = F / Rf
U_residual = U / (Ru * C)
F_residual = F / (Rf * C^2)
```

### Required Sage script

Create or update:

```text
sage/r3_residual_mechanism_analysis.sage
```

### Required exact checks

```text
U == Ru * C * unit_factor_02^2 * unit_factor_03^2
F == Rf * C^2 * full_factor_02^2 * full_factor_03^2
deg_y(U_residual) = 16
deg_y(F_residual) = 24
gcd(U_residual, F_residual) = 1 over QQ(t)[y]
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/residuals/unit_no_row.txt
data/generated/r3_mechanism_campaign/<TS>/residuals/full_no_row.txt
data/generated/r3_mechanism_campaign/<TS>/residuals/unit_residual.txt
data/generated/r3_mechanism_campaign/<TS>/residuals/full_residual.txt
data/generated/r3_mechanism_campaign/<TS>/residuals/residual_manifest.json
reports/<TS>_r3_residual_mechanism_analysis.md
reports/<TS>_r3_residual_mechanism_analysis.json
```

### Labels

Exact equalities and gcd: `Verified Fact`.
Structural explanation: `Not Established` unless a later phase provides exact witness.

## Phase D — Exact relation expansion, selected targets

### Goal

Do not attempt every huge resultant blindly. Select high-value targeted relations that can finish under timeouts.

### Required Sage script

```text
sage/r3_selected_relation_expansion.sage
```

### Required targets

1. `gcd(U_residual, F_residual)` over `QQ(t)[y]`.
2. `gcd(unit_factor_02, full_factor_02)` over `QQ(t)[y]`.
3. `gcd(unit_factor_03, full_factor_03)` over `QQ(t)[y]`.
4. Discriminants in `y` for all displayed factors where feasible.
5. Coefficient-support profiles for all displayed factors.
6. Test whether factors are polynomials in `z = t^2`.
7. Test sign/parity behavior under `t -> -t`.
8. Attempt bounded resultant only for small-degree pairs:
   - unit factor_02 vs full factor_02;
   - unit factor_02 vs full factor_01;
   - shared factor C vs row-sum factors.

### Timeout rule

Use `timeout 1800` for this phase. If a target times out, record:

```text
phase_status: PARTIAL
claim_label: Not Established for that target
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/relations/gcd_table.json
data/generated/r3_mechanism_campaign/<TS>/relations/discriminant_table.json
data/generated/r3_mechanism_campaign/<TS>/relations/resultant_selected_table.json
data/generated/r3_mechanism_campaign/<TS>/relations/coefficient_support.json
data/generated/r3_mechanism_campaign/<TS>/relations/substitution_profiles.json
reports/<TS>_r3_selected_relation_expansion.md
reports/<TS>_r3_selected_relation_expansion.json
```

## Phase E — Commutant specialization search

### Goal

Search for evidence of repeated-factor mechanism via exact commutant dimensions at fixed rational `t` values.

### Values

```text
t = 1/2, 2/3, 3/2, 2, 5/3
```

Avoid values where specialization degenerates or causes denominator failure; record skipped values.

### Required Sage script

```text
sage/r3_commutant_specialization_campaign.sage
```

### For each model and t

Compute over `QQ`:

```text
specialized matrix M_t
commutant solution space for X M_t = M_t X
commutant dimension
basis size
minimal sparse basis summary if feasible
nullity of commutator operator
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/commutant/unit_t_*.json
data/generated/r3_mechanism_campaign/<TS>/commutant/full_t_*.json
reports/<TS>_r3_commutant_specialization_campaign.md
reports/<TS>_r3_commutant_specialization_campaign.json
```

### Labels

- Fixed rational `t` exact result: `Verified Fact` for that specialization.
- Pattern across `t`: `Computational Observation`.
- Generic commutant: `Not Established` unless separately solved.

## Phase F — Projector/idempotent search

### Goal

Search the commutant for evidence of exact block/projector structure.

### Work

For each feasible fixed rational specialization:

```text
search small rational linear combinations of commutant basis elements
try idempotent condition P^2 = P
try low-rank projectors
record exact rank/trace where found
compare projected subspace dimensions to factor degrees/multiplicities
```

This can be heuristic but exact over `QQ` for tested candidates.

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/projectors/projector_candidates.json
reports/<TS>_r3_projector_idempotent_search.md
reports/<TS>_r3_projector_idempotent_search.json
```

### Labels

- Exact `P^2=P` at fixed `t`: `Verified Fact` for that specialization and candidate.
- Candidate search failure: `Not Established`.
- Mechanism from projector: `Computational Observation` unless generic witness exists.

## Phase G — Equitable partition and quotient search

### Goal

Search exact quotient structures that could explain row-sum/shared/residual factors.

### Required script

```text
scripts/r3_equitable_partition_campaign.py
```

If Sage is needed for exact quotient charpolys, use local Sage.

### Work

Try partitions derived from:

```text
factor degrees
row/column support signatures
exponent-pattern signatures in construct.py counters
unit/full live-class structure
known U/O construction groups if exposed in canonical bundle
```

For each candidate partition:

```text
check equitable row-block sums
construct quotient matrix
compute quotient charpoly if feasible
compare quotient charpoly to row-sum/shared factors
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/partitions/partition_candidates.json
reports/<TS>_r3_equitable_partition_campaign.md
reports/<TS>_r3_equitable_partition_campaign.json
```

### Labels

Exact equitable partition check: `Verified Fact` for the stated finite matrix/specialization.
Mechanism claim: `Not Established` unless generic relation to factors is proved.

## Phase H — Automorphism/permutation search

### Goal

Search for exact permutation symmetries that might explain repeated factors.

### Required script

```text
scripts/r3_automorphism_campaign.py
```

### Work

At fixed rational `t` values, search permutations preserving:

```text
matrix entries exactly
support graph
exponent counter signatures
row/column signature clusters
```

Do not brute force all 18! or 27! permutations. Use signature partitions first.

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/automorphisms/automorphism_candidates.json
reports/<TS>_r3_automorphism_campaign.md
reports/<TS>_r3_automorphism_campaign.json
```

### Labels

- Exact verified permutation symmetry: `Verified Fact` for that finite specialization or generic support graph.
- No found symmetry: `Not Established` for mechanism.

## Phase I — Spectral factor-root tracking

### Goal

Track which exact factor block owns numerically dominant/subdominant roots at selected rational `t` values.

### Values

Use:

```text
t = 1/5, 1/4, 1/3, 1/2, 2/3, 3/4, 4/5, 1, 5/4, 4/3, 3/2, 2, 3
```

### Work

For each model and t:

```text
specialize each factor
compute numerical roots with high precision
rank roots by absolute value
assign root ownership by factor index
track row-sum root
track shared factor root
track largest residual root
```

### Outputs

```text
data/generated/r3_mechanism_campaign/<TS>/spectral_tracking/factor_root_tracking.json
reports/<TS>_r3_factor_root_tracking.md
reports/<TS>_r3_factor_root_tracking.json
```

### Labels

Numerical root ownership/order: `Computational Observation`.
Exact dominance for all t: `Not Established`.

## Phase J — Determinant target taxonomy and one exact target

### Goal

Move determinant work from vague to precise.

### Work

Create determinant taxonomy:

```text
det(S)
det(I - S)
charpoly at y=0
charpoly at y=1
row-sum factor roots
residual discriminants
candidate compact determinant if identifiable from prior constraints
```

Then choose **one** exact determinant/root target that is small enough to attempt.

Candidate target priority:

1. shared factor C roots/sign structure;
2. row-sum factor at y=1 or y=0;
3. discriminant of a linear or quadratic factor;
4. determinant of residual quotient if already compact.

### Required outputs

```text
data/generated/r3_mechanism_campaign/<TS>/determinant_targets/taxonomy.json
data/generated/r3_mechanism_campaign/<TS>/determinant_targets/selected_target.json
reports/<TS>_r3_determinant_target_campaign.md
reports/<TS>_r3_selected_root_isolation_attempt.md
```

### Claim labels

- Taxonomy: `Advisory Only`.
- Exact root isolation for named polynomial: `Verified Fact` for that polynomial/domain only.
- All-real-s determinant nonvanishing: `Not Established` unless complete proof.

## Phase K — Canonical insertion final preview

### Goal

Prepare a final human-review canonical insertion packet using all now-current factor/gcd/residual facts, but do not edit canonical files.

### Required outputs

```text
reports/<TS>_r3_canonical_insert_final_review_packet.md
reports/<TS>_r3_canonical_insert_final_review_packet.json
reports/<TS>_r3_canonical_insert_diff_preview.patch
reports/<TS>_canonical_insert_human_checklist.md
```

### Must include

```text
factorization verified facts
exact gcd table summary
residual coprimality
manifest hashes
ring/domain statements
Sage-displayed irreducibility wording
proof boundary
human rerun checklist
rollback note
```

### Must not include

```text
structural mechanism claim
determinant nonvanishing claim
cross-level invariance claim
Collatz-level conclusion
```

## Phase L — Lean readiness screening

### Goal

Do not prove in Lean. Prepare readiness report and stubs only for safe candidates.

### Candidate classes

```text
r=3 finite S-level factorization
exact unit/full gcd table
residual coprimality
fixed-specialization commutant dimensions if generated
```

### Outputs

```text
reports/<TS>_r3_lean_readiness.md
reports/<TS>_r3_proof_obligations.md
lean/generated/ if and only if safe finite stubs are generated
```

### Rule

If a theorem candidate is under-specified, write `not Lean-ready` and do not create a stub.

## Phase M — Red-team review

### Goal

Have Codex adversarially inspect its own campaign outputs.

### Work

Use `collatz-red-team-reviewer` / `red_team_skeptic` behavior:

```text
recompute selected hashes
compare final claims against manifests
scan for Collatz-level language
scan for determinant overclaims
scan for structural-mechanism overclaims
scan for generic claims from specialization evidence
```

### Outputs

```text
reports/<TS>_r3_campaign_red_team_review.md
reports/<TS>_r3_campaign_red_team_review.json
data/generated/red_team/<TS>/hash_audit.json
```

### Disposition choices

```text
PASS
PASS_WITH_PATCHES
REJECT
BLOCKED
```

If `REJECT`, patch final reports before publication.

## Phase N — Final synthesis and next mission packets

### Goal

Summarize what was proved, observed, blocked, and what exact next packets should be built.

### Outputs

```text
reports/<TS>_r3_mechanism_campaign_final.md
reports/<TS>_r3_mechanism_campaign_final.json
reports/<TS>_r3_next_exact_mechanism_packet_recommendation.md
reports/<TS>_r3_next_determinant_packet_recommendation.md
reports/<TS>_r3_next_formalization_packet_recommendation.md
data/generated/r3_mechanism_campaign/<TS>/program_manifest.json
```

### Final report sections

```text
status
scope
commands_run
artifacts_created
verified_facts
computational_observations
not_established_items
blocked_items
candidate_mechanisms
canonical_readiness
lean_readiness
next_exact_targets
proof_boundary
red_team_disposition
```

### Final classification table

| Area | Required classification |
|---|---|
| factorization facts | Verified / unchanged |
| residual algebra | Verified / partial / blocked |
| commutant evidence | Verified fixed-specialization / computational observation / not established |
| projector evidence | Verified fixed-specialization / computational observation / not established |
| equitable partitions | Verified / not established |
| automorphisms | Verified / not established |
| determinant target | exact target selected / blocked / not established |
| spectral tracking | computational observation / not established |
| structural mechanism | verified / candidate only / not established |
| canonical readiness | ready for human review / needs patch / not ready |
| Lean readiness | ready / partial / not ready |

## 6. Required validation and publication

After all phases:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<TS>_r3_mechanism_campaign_final.md
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py --since <TS> --exclude-audits --output reports/<TS>_r3_mechanism_campaign_claim_validation.json || python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/<TS>_r3_mechanism_campaign_claim_validation.json
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

Then obey the publication addendum.

Commit message:

```text
Run r3 structural mechanism grand campaign
```

After pushing, print:

```text
pushed_commit: <commit hash>
branch: <branch name>
final_report: reports/<TS>_r3_mechanism_campaign_final.md
red_team_review: reports/<TS>_r3_campaign_red_team_review.md
program_manifest: data/generated/r3_mechanism_campaign/<TS>/program_manifest.json
claim_validation: reports/<TS>_r3_mechanism_campaign_claim_validation.json
next_mechanism_packet: reports/<TS>_r3_next_exact_mechanism_packet_recommendation.md
```

## 7. Acceptance criteria

Mission is complete only if:

1. specialized skills and agents validate;
2. phase receipts exist;
3. campaign manifest exists;
4. factor registry and graph exist;
5. residual algebra pass exists;
6. selected exact relation expansion is attempted and classified;
7. commutant specialization search is attempted or explicitly blocked;
8. projector/idempotent search is attempted or explicitly blocked;
9. equitable partition search is attempted or explicitly blocked;
10. automorphism search is attempted or explicitly blocked;
11. spectral tracking exists;
12. determinant taxonomy exists and one exact target is attempted or explicitly blocked;
13. canonical insertion preview exists and canonical files are untouched;
14. Lean readiness report exists;
15. red-team review exists;
16. final synthesis exists;
17. witness manifest updates;
18. proof-boundary validation passes or required patches are applied;
19. safe artifacts are committed and pushed;
20. no Collatz-level conclusion is asserted.

## 8. Stop and degrade rules

Stop immediately if:

```text
canonical files are modified unexpectedly
Sage exact factorization contradicts locked source manifests
proof-boundary audit rejects final report
red-team review finds unpatched blocker
```

Degrade and continue if:

```text
specific generic computation times out
projector search finds no candidates
resultants/discriminants are too large
Lean readiness fails for some candidates
```

Use labels:

```text
BLOCKED_BY_TIMEOUT
Not Established
Computational Observation
```

as appropriate.

## 9. Final launch command

After this packet is active:

```text
$collatz-research-orchestrator go
```

Expanded equivalent:

```text
$collatz-research-orchestrator go. Execute the active r=3 structural mechanism grand campaign using the specialized skills and agents. Use local Sage at ./.sage-conda/bin/sage with DOT_SAGE=$PWD/.codex/sage. Produce phase receipts, exact algebra artifacts, mechanism-search reports, determinant and spectral target reports, canonical preview, Lean readiness, red-team review, final synthesis, and next-packet recommendations. Do not edit canonical files unless explicitly authorized. Commit and push safe results. Do not claim or imply a Collatz proof.
```
