# Codex Capability Matrix

status: Verified Fact
scope: Codex specialized skill and agent capability validation only; no canonical bundle edits and no mathematical claims changed
method: Python validation scripts, project config inspection, and report-only capability mapping
claim_boundary: This is a finite-level workflow capability validation. It does not prove or imply any Collatz-level theorem.
reproduction_command: python3 scripts/check_codex_skills.py && python3 scripts/run_py_checks.py && python3 scripts/build_specialized_codex_capabilities.py && python3 scripts/check_codex_skills.py
files_touched: see Artifacts and touched files
artifacts_produced: capability matrix JSON/Markdown and specialized skills validation report

## Matrix

| Project need | Skill | Agent role | Backend | Expected artifacts |
|---|---|---|---|---|
| active plan execution | `collatz-campaign-manager` | `campaign_operator` | Python/report orchestration | phase manifests, checkpointing, resume/retry, final manifests |
| exact Sage factor work | `collatz-factor-structure-lab` | `sage_factor_algebraist` | Sage exact algebra | QQ[t][y] and QQ(t)[y] exact factorization work |
| residual/gcd/resultant work | `collatz-factor-structure-lab` | `factor_cartographer` | Sage exact algebra plus report indexes | factor registries, pairwise gcds, resultants, discriminants |
| canonical insert previews | `collatz-canonical-curator` | `canonical_curator` | report-only curation | canonical insertion previews and rollback notes |
| artifact hashes/indexes | `collatz-provenance-reproducibility-lab` | `provenance_librarian` | Python/report provenance | hash verification, artifact indexes, witness manifest hygiene |
| commutants/projectors/symmetry | `collatz-symmetry-mechanism-lab` | `mechanism_hunter` | Python/Sage structural search | commutants, automorphisms, projectors, equitable partitions |
| determinant root isolation | `collatz-spectrum-determinant-lab` | `determinant_root_analyst` | Sage exact algebra | Sturm/sign-chart attempts without positivity overclaim |
| spectral tracking | `collatz-spectrum-determinant-lab` | `spectral_tracker` | Python/SymPy plus exact artifact links | factor-root ownership and subdominant spectral behavior tracking |
| Lean bridge | `collatz-lean-formalization-bridge` | `formalization_engineer` | Lean stubs/report-only proof obligations | finite-level theorem stubs after exact witness audit |
| adversarial review | `collatz-red-team-reviewer` | `red_team_skeptic` | report-only recomputation and consistency checks | source-artifact contradiction and overclaim detection |

## Input Hashes

| Path | SHA-256 | Bytes |
|---|---:|---:|
| `CODEX_SKILLS.md` | `13ebb7fed37911182bc1c3d9962cc7a0479a04691de13a28748486c93f8f24ee` | 3716 |
| `CODEX_TASKS.md` | `3e529e57c8604e8e7b6836ba25a8d7243e092afe5efc8b37841c07ee4f21b12e` | 3021 |
| `.codex/config.toml` | `29d895ec5039c95c6783e66749aeb1575f0238c78061b2e1ebb782707a1efa5b` | 4052 |
| `scripts/check_codex_skills.py` | `4b1940db069e557333410d9deaa70034cd53ce9976f20da7869010fac136ad89` | 8268 |
| `plans/ACTIVE_CODEX_PLAN.md` | `4172cbd65530e4794d6e45458282517fb604a22b833d4ff45f349b4f07bf7856` | 1520 |
| `plans/codex/2026-05-14_codex_specialized_capability_validation_packet.md` | `732689f6e953abebdc875049ab54d4678cabbdb73f26df974ba5eeeaa623dda4` | 2134 |
| `plans/codex/2026-05-13_r3_next_research_cycle_publish_addendum.md` | `611bbebc4755e88f9758d20dc3d512ae3e871ff923782920f1b2c461271c1fdb` | 2999 |
| `CLAIM_GUARDRAILS.md` | `8db84da52d9004b22814a0ab730d20a2165b8c1f98f5d21df0d78b04bfcc73fc` | 1644 |

## Commands

- `bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh`: passed. bootstrap and skill validation completed; final checker findings are empty after capability refresh
- `python3 .agents/skills/collatz-research-orchestrator/scripts/summarize_state.py`: passed. canonical bundle and installed skills summarized
- `python3 scripts/check_codex_skills.py`: passed. initial run passed with warnings before capability refresh
- `python3 scripts/run_py_checks.py`: passed. wrote reports/py_sanity_checks.json
- `python3 scripts/build_specialized_codex_capabilities.py`: passed_after_escalation. created optional support directories for specialized skills after sandbox read-only error
- `python3 scripts/check_codex_skills.py`: passed. final run returned ok true with no findings
- `python3 .agents/skills/collatz-research-orchestrator/scripts/orchestrate.py --target "specialized capability validation" --run-preflight --out-prefix codex_specialized_capability_validation`: passed. wrote orchestration report pair

## Boundary

No mathematical progress is claimed here. This validates workflow capability only.
