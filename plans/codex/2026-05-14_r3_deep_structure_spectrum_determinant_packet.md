# Codex Mission Packet — r=3 Deep Structure, Spectrum, Determinant Program

- **plan_id:** `2026-05-14_r3_deep_structure_spectrum_determinant_program`
- **status:** `Advisory Only`
- **target:** large multi-phase finite-level r=3 S-level research program
- **scope:** finite-level r=3 unit/full S-level matrices, factorization artifacts, residual algebra, finite experimental data, determinant targets, spectral tracking, and theorem-candidate triage
- **publication:** obey `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md`
- **launch:** `$collatz-research-orchestrator go`
- **hard guardrail:** no finite-level matrix fact proves or implies the Collatz conjecture

## 0. Mission objective

Run a staged research program around the verified finite-level r=3 S-level characteristic-polynomial factorization facts.

Move from:

```text
Verified factorization artifact
```

to:

```text
factor relation map
→ residual quotient structure
→ symmetry / commutant / projector search
→ determinant and spectral target generation
→ canonical insertion readiness
→ exact theorem-candidate triage
→ next mission packet recommendation
```

No canonical files may be edited in this mission.

## 1. Global guardrails

### In scope

```text
r = 3
S-level matrices
unit and full models
finite-dimensional characteristic-polynomial factorization
factor relations over QQ[t][y] and QQ(t)[y]
row-sum/Perron factor structure
residual characteristic-polynomial structure
commutant / symmetry / projector / equitable-partition searches
determinant-polynomial target discovery
rational, modular, and slice specialization sweeps
proof-boundary report generation
canonical insertion preview and human-review checklist
finite theorem-candidate triage
```

### Out of scope

Codex must not attempt or assert:

```text
Collatz proof
global orbit behavior
descent-to-Q from S-level facts
determinant nonvanishing for all real s > 0 unless separately proved
cross-level invariance unless exact witness exists
structural mechanism unless exact algebraic evidence exists
canonical-file edits without explicit human authorization
Lean formalization of exploratory claims
```

### Claim labels

Use exactly one label per claim:

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

Default classification:

| Claim type | Default label |
|---|---|
| Exact reconstructed factorization with hashes | Verified Fact |
| Sage exact pairwise gcd table | Verified Fact |
| Numerical spectra | Computational Observation |
| Modular samples | Computational Observation |
| Symmetry hints without proof | Computational Observation |
| Determinant positivity | Not Established |
| Structural mechanism | Not Established until exact witness |
| Cross-level invariance | Not Established |
| Canonical patch proposal | Advisory Only |

## 2. Current base state

Codex should treat the following as finite-level verified starting facts from existing artifacts:

```text
r=3 unit factorization:
dimension = 18
factor_degree_pattern = [1, 1, 2, 6]
multiplicity_pattern = [1, 1, 2, 2]
row_sum_factor_index = 0

r=3 full factorization:
dimension = 27
factor_degree_pattern = [1, 1, 3, 9]
multiplicity_pattern = [1, 2, 2, 2]
row_sum_factor_index = 0

shared unit/full factor:
unit factor_01 == full factor_01
hash = 02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69

exact gcd table:
only nonconstant unit/full gcd is factor_01 vs factor_01
all other unit/full pairwise gcds over QQ(t)[y] are 1
```

These are finite-level facts only.

## 3. Required reads

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
reports/20260514T050426Z_r3_factor_structure_analysis.md
reports/20260514T052552Z_r3_factor_structure_gcd.md
reports/20260514T050426Z_r3_factorization_canonical_insert_patch.md
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json
sage/r3_factorization_audit.sage
sage/r3_factor_structure_gcd.sage
src/collatz_codex_harness/construct.py
scripts/run_py_checks.py
```

Codex must use local Sage explicitly:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage <script>
```

Never depend on bare `sage` being on PATH.

## 4. Super-phase map

| Phase | Purpose | Main outputs |
|---|---|---|
| A | Environment and state lock | state manifest |
| B | Factor artifact consolidation | factor registry |
| C | Canonical insertion prep | final insert preview |
| D | Residual factor algebra | residual manifests |
| E | Exact relation expansion | gcd/resultant/discriminant/substitution tables |
| F | Symmetry / commutant / projector search | candidate mechanism reports |
| G | Specialization sweeps | exact/numerical data grid |
| H | Determinant target generation | determinant/root-isolation plan |
| I | Subdominant spectral tracking | exact target candidates |
| J | Cross-level comparison | guarded r=2/r=3 comparison |
| K | Report hygiene / tooling | reduced audit spam |
| L | Finite theorem-candidate triage | theorem candidate packet |
| M | Extra useful work: factor graph and artifact explorer | graph/index artifacts |
| N | Extra useful work: reproducibility harness | rerun scripts and checksums |
| O | Final synthesis | final report + next mission recommendation |

## Phase A — Environment and state lock

Run:

```bash
git pull --ff-only || true
git status --short
git rev-parse HEAD
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
./.sage-conda/bin/sage --version
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage --version
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

Outputs:

```text
reports/<timestamp>_deep_program_state_lock.md
reports/<timestamp>_deep_program_state_lock.json
data/generated/r3_deep_program/<timestamp>/state_manifest.json
```

State manifest must include:

```json
{
  "repo_commit": "...",
  "sage_path": "./.sage-conda/bin/sage",
  "sage_version": "...",
  "python_version": "...",
  "canonical_bundle_hashes": {},
  "prior_artifacts": {},
  "claim_boundary": "finite-level only; no Collatz-level conclusion"
}
```

If Sage is not executable, label `BLOCKED_BY_ENVIRONMENT` and do not continue exact algebra phases.

## Phase B — Factor artifact consolidation

Create a normalized factor registry from:

```text
data/generated/r3_factorization_audit/20260513T160231Z/manifest.json
data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/factor_registry.json
data/generated/r3_deep_program/<timestamp>/factor_registry.csv
reports/<timestamp>_factor_registry_summary.md
```

Registry fields:

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

Verify:

```text
unit factor_01 hash == full factor_01 hash
row-sum factors are distinct between unit/full
row-sum factor index = 0 in both models
unit factor-degree contribution = 18
full factor-degree contribution = 27
```

## Phase C — Canonical insertion prep

Produce a final insertion patch artifact, not applied.

Inputs:

```text
reports/20260514T023536Z_r3_factorization_canonical_patch_proposal_v2.md
reports/20260514T050426Z_r3_factorization_canonical_insert_patch.md
```

Outputs:

```text
reports/<timestamp>_r3_canonical_insert_final_review_packet.md
reports/<timestamp>_r3_canonical_insert_final_review_packet.json
reports/<timestamp>_r3_canonical_insert_diff_preview.patch
reports/<timestamp>_canonical_insert_human_checklist.md
```

Target file for preview only:

```text
data/canonical_bundle/05_R3_CLOSURES.txt
```

Preferred placement:

```text
before <<APPEND-POINT::05.charpoly>>
```

The insert preview must include:

```text
status_label: Verified Fact, finite-level only
r: 3
level: S-level
models: unit and full
recorded_ring: QQ[t][y]
y-separability ring: QQ(t)[y]
Sage-displayed irreducibility over QQ[t][y]
row-sum/Perron factor index 0 for both models
shared non-row-sum factor hash
exact gcd table summary
manifest file hash
manifest payload hash
proof boundary
```

Checklist must include:

```text
[ ] Verify Sage rerun
[ ] Verify manifest file hash
[ ] Verify manifest payload hash
[ ] Verify exact gcd manifest
[ ] Verify no determinant positivity claim
[ ] Verify no Collatz-level language
[ ] Verify canonical section placement
[ ] Verify rollback procedure
```

## Phase D — Residual factor algebra

Let:

```text
U(y,t) = unit characteristic polynomial
F(y,t) = full characteristic polynomial
Ru = unit row-sum factor
Rf = full row-sum factor
C = shared non-row-sum linear factor
```

Compute:

```text
U_no_row = U / Ru
F_no_row = F / Rf
U_residual = U / (Ru * C)
F_residual = F / (Rf * C^2)
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/residuals/unit_no_row.txt
data/generated/r3_deep_program/<timestamp>/residuals/full_no_row.txt
data/generated/r3_deep_program/<timestamp>/residuals/unit_residual.txt
data/generated/r3_deep_program/<timestamp>/residuals/full_residual.txt
data/generated/r3_deep_program/<timestamp>/residuals/residual_manifest.json
reports/<timestamp>_r3_residual_factor_analysis.md
reports/<timestamp>_r3_residual_factor_analysis.json
```

Exact Sage checks:

```text
U == Ru * C * unit_factor_02^2 * unit_factor_03^2
F == Rf * C^2 * full_factor_02^2 * full_factor_03^2
deg_y(U_residual) = 16
deg_y(F_residual) = 24
gcd(U_residual, F_residual) over QQ(t)[y]
resultant(U_residual, F_residual, y), if feasible
```

If resultants are too large, record timeout and label `Not Established`.

## Phase E — Exact relation expansion

Create:

```text
sage/r3_factor_relation_expansion.sage
```

For every factor and residual pair, compute if feasible:

```text
gcd over QQ(t)[y]
resultant in y
discriminant in y
content in QQ[t]
primitive part
reciprocity / palindromicity in t
degree_t profile
coefficient support profile
sign symmetry under t -> -t
possible substitution simplifications: z = t^2
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/factor_relations/gcd_table.json
data/generated/r3_deep_program/<timestamp>/factor_relations/resultant_table.json
data/generated/r3_deep_program/<timestamp>/factor_relations/discriminant_table.json
data/generated/r3_deep_program/<timestamp>/factor_relations/coefficient_support.json
data/generated/r3_deep_program/<timestamp>/factor_relations/substitution_profiles.json
reports/<timestamp>_r3_factor_relation_expansion.md
reports/<timestamp>_r3_factor_relation_expansion.json
```

Hypotheses:

```text
H1: only C is shared between unit/full non-row factors.
H2: U_residual and F_residual are coprime over QQ(t)[y].
H3: full residual factors may relate to unit residual factors by substitution/scaling.
H4: degree-ratio pattern 2,6 vs 3,9 has an exact explanation.
```

Labels must be exact: `Verified Fact` only for exact equalities; otherwise `Computational Observation` or `Not Established`.

## Phase F — Symmetry / commutant / projector search

Search for exact structural hints behind squared factors.

### F1 — Specialization commutants

For:

```text
t = 1/2, 2, 3/2, 5/3
```

For each model:

```text
solve X M = M X over QQ
compute dim commutant
compute basis matrices
search sparse/idempotent/projector elements where feasible
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/commutant/unit_t_1_2.json
data/generated/r3_deep_program/<timestamp>/commutant/full_t_1_2.json
reports/<timestamp>_r3_commutant_specialization_analysis.md
```

### F2 — Generic commutant

Attempt only with timeout:

```text
Solve X M(t) = M(t) X over QQ(t)
```

If too expensive, label `Not Established` with blocker.

### F3 — Equitable partitions

Search row/column partitions that make exact quotient matrices. Compare quotient charpolys to row-sum/shared factors.

Outputs:

```text
reports/<timestamp>_r3_equitable_partition_search.md
data/generated/r3_deep_program/<timestamp>/partitions/*.json
```

### F4 — Automorphism search

Search permutations P such that:

```text
P M P^-1 = M
```

at exact specializations, and generically only if feasible.

Outputs:

```text
reports/<timestamp>_r3_automorphism_search.md
data/generated/r3_deep_program/<timestamp>/automorphisms/*.json
```

## Phase G — Specialization sweeps

Generate structured data over rational, modular, and slice grids.

### G1 rational t sweep

Use:

```text
t = 1/5, 1/4, 1/3, 1/2, 2/3, 3/4, 4/5, 1, 5/4, 4/3, 3/2, 2, 3
```

For each model:

```text
specialized factor degrees
multiplicities
row-sum value
shared factor value
approx eigenvalues
approx dominant/subdominant values
factor block owning each root where feasible
```

### G2 finite-field modular sweep

Use primes:

```text
1000003, 1000033, 1000037, 1000039, 1000081
```

For sampled t values:

```text
factor-degree pattern mod p
determinant nonzero samples
shared factor persistence
```

### G3 slice sweep

If repo supports s-slices:

```text
s = 0.45, 0.50, 0.55, 0.60, 0.65, 0.70
```

Outputs:

```text
reports/<timestamp>_r3_specialization_sweep.csv
reports/<timestamp>_r3_specialization_sweep.json
reports/<timestamp>_r3_specialization_sweep.md
```

## Phase H — Determinant target generation

Clarify determinant objects before doing positivity work.

Taxonomy must distinguish:

```text
charpoly evaluated at target y
det(S)
det(I - S)
determinant of residual factor
compact determinant from prior constraints, if any
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/determinant_targets/
reports/<timestamp>_r3_determinant_target_taxonomy.md
reports/<timestamp>_r3_determinant_root_isolation_attempt.md
```

If exact root isolation is feasible, use:

```text
real_roots()
sturm_sequence()
interval checks
sign charts
```

No all-real-s determinant claim unless exact root-isolation proof is complete.

## Phase I — Subdominant spectral tracking

Use factorization to identify which factor block contributes numerical roots at rational t values.

Outputs:

```text
reports/<timestamp>_r3_subdominant_factor_tracking.md
data/generated/r3_deep_program/<timestamp>/spectral_tracking/*.json
```

Guardrail:

```text
Numerical root ordering is Computational Observation only.
Exact dominance for all t > 0 is Not Established unless separately proved.
```

## Phase J — Cross-level comparison

Compare r=2 and r=3 finite-level factor structures without transfer claims.

Outputs:

```text
reports/<timestamp>_r2_r3_factor_structure_comparison.md
reports/<timestamp>_r2_r3_factor_structure_comparison.json
```

Required wording:

```text
This comparison does not establish cross-level invariance.
r=2 mechanisms do not transfer to r=3 without independent r=3 witness.
```

## Phase K — Report hygiene and tooling patch

Prior validation generated audit spam. Patch tooling without weakening guardrails.

Add or update:

```text
scripts/validate_current_reports.py
```

or update:

```text
.agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
```

Support:

```bash
--since <timestamp>
--exclude-audits
--output reports/<timestamp>_claim_validation.json
```

Do not recursively audit unless explicitly requested:

```text
*_audit.md
*_audit.json
*_claim_validation.json
witness_manifest.json
```

Outputs:

```text
reports/<timestamp>_audit_tooling_patch.md
reports/<timestamp>_audit_tooling_patch.json
```

## Phase L — Finite theorem-candidate triage

Create:

```text
reports/<timestamp>_r3_deep_program_theorem_candidates.md
reports/<timestamp>_r3_deep_program_theorem_candidates.json
```

Candidate classes:

```text
1. r=3 generic S-level factorization: Verified Fact, finite-level only.
2. residual coprimality: Verified Fact if proved.
3. shared factor uniqueness: Verified Fact if exact relations confirm.
4. structural mechanism: Not Established unless exact witness.
5. determinant nonvanishing: Not Established unless root isolation succeeds.
```

Schema:

```json
{
  "name": "",
  "status_label": "",
  "r": 3,
  "level": "S-level",
  "model": "unit/full/both",
  "ring": "QQ[t][y] or QQ(t)[y]",
  "statement": "",
  "evidence_artifacts": [],
  "exact_checks": [],
  "missing_proof_steps": [],
  "why_this_does_not_imply_Collatz": ""
}
```

## Phase M — Extra useful work: factor-network graph

Build graph artifacts from factors and relations.

Nodes:

```text
unit factor_00..03
full factor_00..03
row-sum factors
shared factor C
residuals U_residual/F_residual
```

Edges:

```text
same_hash
nonconstant_gcd
coprime_gcd_1
row_sum_factor
residual_component
multiplicity_relation
same_degree_or_ratio
```

Outputs:

```text
data/generated/r3_deep_program/<timestamp>/factor_graph/factor_graph.json
data/generated/r3_deep_program/<timestamp>/factor_graph/factor_graph.dot
reports/<timestamp>_r3_factor_network_analysis.md
```

No image rendering required.

## Phase N — Extra useful work: reproducibility harness

Create a rerun helper that reproduces only high-value artifacts, not the whole massive program.

Add:

```text
scripts/r3_deep_program_reproduce.sh
```

It should run:

```bash
python3 scripts/run_py_checks.py
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_structure_gcd.sage
# plus any newly created exact Sage scripts with safe timeout
```

Also create:

```text
data/generated/r3_deep_program/<timestamp>/reproduction_commands.txt
reports/<timestamp>_r3_reproducibility_notes.md
```

## Phase O — Extra useful work: artifact index and query map

Generate a top-level machine-readable index for humans and future agents:

```text
data/generated/r3_deep_program/<timestamp>/artifact_index.json
reports/<timestamp>_r3_artifact_index.md
```

Index every generated artifact with:

```text
path
kind
status_label
sha256
producer_phase
claim_boundary
summary
```

## Phase P — Final synthesis

Create:

```text
reports/<timestamp>_r3_deep_program_final.md
reports/<timestamp>_r3_deep_program_final.json
reports/<timestamp>_r3_next_mission_recommendation.md
data/generated/r3_deep_program/<timestamp>/program_manifest.json
```

Required final sections:

```text
status
scope
commands_run
artifacts_created
verified_facts
computational_observations
not_established_items
blocked_items
new_exact_targets
recommended_next_mission
proof_boundary
canonical_readiness
```

Classify:

| Area | Status options |
|---|---|
| Factorization canonical insert | Ready / needs human review / not ready |
| Residual algebra | Verified / partial / blocked |
| Structural mechanism | Verified / computational observation / not established |
| Determinant nonvanishing | Verified / partial / not established |
| Subdominant spectrum | Verified / computational observation / not established |
| Cross-level comparison | Verified finite facts only / not established |
| Lean readiness | ready / not ready |

## Subagent deployment

Use subagents if available.

### algebra_explorer

Run exact algebra around residual factors, gcds, resultants, commutants, projectors, quotient/residual decomposition, and structural mechanism candidates.

Return:

```text
exact identities
failed hypotheses
candidate mechanisms
ring/domain used
artifact paths
claim labels
```

### experiment_runner

Run Sage/Python experiments, timestamp outputs, preserve logs, update manifests.

### proof_auditor

Audit final reports and theorem candidates for overreach.

### implementation_engineer

Patch tooling, avoid audit spam, make scripts reproducible, keep local Sage path explicit.

## Required command skeleton

Start:

```bash
git pull --ff-only || true
git status --short
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage --version
```

Then run created scripts with timeouts where needed:

```bash
timeout 1800 env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage
timeout 1800 env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_residual_analysis.sage
timeout 3600 env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_commutant_analysis.sage
python3 scripts/r3_report_consolidator.py || true
```

Validation:

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<timestamp>_r3_deep_program_final.md
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

Publication:

```bash
git status --short
git add reports data/generated scripts sage .agents plans
git commit -m "Run r3 deep structure research program"
git push
```

## Stop conditions

Stop and report if:

```text
Sage unavailable
exact reconstruction fails
gcd table contradicts prior verified fact
canonical files are accidentally modified
proof-boundary audit rejects a report
a generated result suggests contradiction with locked canonical facts
runtime exceeds timeout on exact generic computation
```

Long generic computations should degrade to:

```text
specialization-based Computational Observation
```

not force proof claims.

## Major expected deliverables

```text
data/generated/r3_deep_program/<timestamp>/state_manifest.json
data/generated/r3_deep_program/<timestamp>/factor_registry.json
data/generated/r3_deep_program/<timestamp>/factor_registry.csv
data/generated/r3_deep_program/<timestamp>/residuals/residual_manifest.json
data/generated/r3_deep_program/<timestamp>/factor_relations/gcd_table.json
data/generated/r3_deep_program/<timestamp>/factor_relations/resultant_table.json
data/generated/r3_deep_program/<timestamp>/factor_relations/discriminant_table.json
data/generated/r3_deep_program/<timestamp>/commutant/*.json
data/generated/r3_deep_program/<timestamp>/spectral_tracking/*.json
data/generated/r3_deep_program/<timestamp>/factor_graph/factor_graph.json
data/generated/r3_deep_program/<timestamp>/artifact_index.json
data/generated/r3_deep_program/<timestamp>/program_manifest.json
reports/<timestamp>_r3_canonical_insert_final_review_packet.md
reports/<timestamp>_canonical_insert_human_checklist.md
reports/<timestamp>_r3_residual_factor_analysis.md
reports/<timestamp>_r3_factor_relation_expansion.md
reports/<timestamp>_r3_commutant_specialization_analysis.md
reports/<timestamp>_r3_equitable_partition_search.md
reports/<timestamp>_r3_specialization_sweep.md
reports/<timestamp>_r3_determinant_target_taxonomy.md
reports/<timestamp>_r3_subdominant_factor_tracking.md
reports/<timestamp>_r2_r3_factor_structure_comparison.md
reports/<timestamp>_audit_tooling_patch.md
reports/<timestamp>_r3_deep_program_theorem_candidates.md
reports/<timestamp>_r3_factor_network_analysis.md
reports/<timestamp>_r3_reproducibility_notes.md
reports/<timestamp>_r3_artifact_index.md
reports/<timestamp>_r3_deep_program_final.md
reports/<timestamp>_r3_next_mission_recommendation.md
```

## Acceptance criteria

Mission complete only when:

1. Environment checks pass.
2. Local Sage path is used explicitly.
3. Factor registry is generated.
4. Canonical insertion preview exists and canonical files are untouched.
5. Residual factor artifacts exist.
6. Exact gcd/resultant/discriminant work is attempted and classified.
7. Symmetry/commutant/equitable-partition searches are attempted or explicitly blocked.
8. Specialization sweep data exists.
9. Determinant target taxonomy exists.
10. Subdominant spectral tracking report exists.
11. Cross-level comparison report exists with no invariance overclaim.
12. Audit/report tooling bloat is addressed or documented.
13. Factor-network graph artifacts exist.
14. Reproducibility helper exists.
15. Artifact index exists.
16. Theorem-candidate packet exists.
17. Final report exists.
18. Witness manifest is updated.
19. Proof-boundary validation passes for final reports.
20. Safe artifacts are committed and pushed.
21. No Collatz-level claim is asserted.

## Final launch prompt after merge

```text
$collatz-research-orchestrator go
```

Expanded equivalent:

```text
$collatz-research-orchestrator go. Execute the active r=3 deep structure, spectrum, determinant, and canonical-insertion-prep program. Use local Sage at ./.sage-conda/bin/sage with DOT_SAGE=$PWD/.codex/sage. Use subagents where useful. Generate exact algebra artifacts, experimental data, analysis reports, theorem-candidate notes, factor-network artifacts, reproducibility helpers, and a final synthesis. Do not edit canonical files unless the active packet explicitly allows it. Commit and push safe results. Do not claim or imply a Collatz proof.
```
