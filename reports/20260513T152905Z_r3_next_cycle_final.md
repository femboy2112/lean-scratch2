# r=3 Next Cycle Final Report

status: Advisory Only
scope: finite-level lifted-operator r=3 compact-factorization and determinant-nonvanishing triage cycle
method: Python reconnaissance, proof-boundary audit, Sage exact algebra factor search, witness collection
claim_boundary: This is finite-level structural/spectral/determinant work inside the lifted-operator framework. It does not prove or imply the Collatz conjecture, global orbit behavior, cross-level invariance, or determinant nonvanishing for all real `s > 0`.
reproduction_command: see `commands_run`
files_touched: scripts, reports, witness data, theorem-candidate notes
artifacts_produced: Phase A-H reports and witness artifacts listed below

## commands_run

- `bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh`
- `bash scripts/bootstrap_codex.sh`
- `python3 scripts/check_codex_skills.py`
- `python3 scripts/run_py_checks.py`
- `python3 .agents/skills/collatz-research-orchestrator/scripts/summarize_state.py > reports/$(date -u +%Y%m%dT%H%M%SZ)_state_summary.json`
- `python3 .agents/skills/collatz-research-orchestrator/scripts/orchestrate.py --target "r=3 compact factorization and determinant nonvanishing triage" --run-preflight --out-prefix r3_next_research_cycle`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-unit-fast`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-full-fast`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py factor-python`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py cross-level`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py`
- `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/20260513T152235Z_claim_ladder_validation.json`
- `bash scripts/bootstrap_codex.sh --with-sage`
- `timeout 900 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r2`
- `timeout 1800 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r3-unit`
- `timeout 3600 python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py sage-r3-full`
- `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/20260513T152735Z_post_sage_claim_ladder_validation.json`
- `python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py`
- `python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py > reports/20260513T153035Z_final_claim_ladder_validation.json`
- `pytest -q || true`
- `python3 scripts/run_py_checks.py`

## artifacts_created

- `reports/20260513T152017Z_state_summary.json`
- `reports/20260513T152142Z_r3_next_research_cycle_orchestration.md`
- `reports/20260513T152142Z_r3_next_research_cycle_orchestration.json`
- `reports/20260513T152202Z_spectral-fast_analysis.md`
- `reports/20260513T152202Z_spectral-fast_witness.json`
- `reports/20260513T152202Z_spectral-fast.log`
- `reports/20260513T152206Z_modular-unit-fast_analysis.md`
- `reports/20260513T152206Z_modular-unit-fast_witness.json`
- `reports/20260513T152206Z_modular-unit-fast.log`
- `reports/20260513T152209Z_modular-full-fast_analysis.md`
- `reports/20260513T152209Z_modular-full-fast_witness.json`
- `reports/20260513T152209Z_modular-full-fast.log`
- `reports/20260513T152214Z_factor-python_analysis.md`
- `reports/20260513T152214Z_factor-python_witness.json`
- `reports/20260513T152214Z_factor-python.log`
- `reports/20260513T152220Z_cross-level_analysis.md`
- `reports/20260513T152220Z_cross-level_witness.json`
- `reports/20260513T152220Z_cross-level.log`
- `reports/20260513T152235Z_claim_ladder_validation.json`
- `reports/20260513T152358Z_r3_recon_triage.md`
- `reports/20260513T152358Z_r3_recon_triage.json`
- `reports/20260513T152551Z_sage-r2_analysis.md`
- `reports/20260513T152551Z_sage-r2_witness.json`
- `reports/20260513T152551Z_sage-r2.log`
- `reports/20260513T152602Z_sage-r3-unit_analysis.md`
- `reports/20260513T152602Z_sage-r3-unit_witness.json`
- `reports/20260513T152602Z_sage-r3-unit.log`
- `reports/20260513T152643Z_sage-r3-full_analysis.md`
- `reports/20260513T152643Z_sage-r3-full_witness.json`
- `reports/20260513T152643Z_sage-r3-full.log`
- `reports/20260513T152735Z_post_sage_claim_ladder_validation.json`
- `reports/20260513T152815Z_theorem_candidates.md`
- `reports/20260513T152815Z_theorem_candidates.json`
- `reports/20260513T153035Z_final_claim_ladder_validation.json`
- `reports/sage_r2_factorization.sageout`
- `reports/sage_r3_unit_factorization.sageout`
- `reports/sage_r3_full_factorization.sageout`
- `reports/witness_manifest.json`

## claim_labels

- `Verified Fact`: `sage-r2` sanity factorization witness completed successfully.
- `Computational Observation`: Phase C spectral/modular/factor/cross-level reconnaissance; `sage-r3-unit`; `sage-r3-full`; theorem-candidate factorization shapes pending independent audit.
- `Not Established`: all-real-s determinant nonvanishing, cross-level invariance, structural mechanism, subdominant exact spectral structure, and Lean-ready theorem candidates.
- `Advisory Only`: orchestration, triage, final report, witness-manifest status, Sage promotion decisions.
- `Patched`: setup/harness defects patched during execution: direct invocation import path in `scripts/run_py_checks.py`; Sage sandbox dot-directory in `run_exact_target.py`.

## exact_results

- `Verified Fact`: `sage-r2` sanity check produced `reports/sage_r2_factorization.sageout`.
- `Computational Observation`: `sage-r3-unit` factored the generic r=3 unit S-level characteristic polynomial over `QQ[t]` with degree pattern `1 + 1 + 2*2 + 2*6 = 18`; artifact hash `f341ce713b73a759e7a970f23178ea71047eb0821cf1b373ca3401ad38abf07c`.
- `Computational Observation`: `sage-r3-full` factored the generic r=3 full S-level characteristic polynomial over `QQ[t]` with degree pattern `1 + 2*1 + 2*3 + 2*9 = 27`; artifact hash `fe1477297a2a807520390978a2dc3ea259e403698c420e1ecff74df16b68e71a`.

## computational_observations

- `spectral-fast`: positive numerical S-level spectral gaps at `s = 0.50, 0.55, 0.60` for unit and full models; not exact spectral closure.
- `modular-unit-fast` and `modular-full-fast`: `4/4` nonzero finite-field determinant samples each; not all-real-s determinant nonvanishing.
- `factor-python`: no smaller Python exact factor candidate; recommended Sage exact factorization by model.
- `cross-level`: no invariant claimed; exact cross-level work requires a candidate invariant and normalization first.

## not_established_items

- r=3 determinant nonvanishing for all real `s > 0`.
- r=3 structural mechanism explaining the factorization patterns.
- r=3 exact subdominant spectral structure.
- cross-level r=2/r=3 spectral invariance.
- Lean-ready theorem candidates.
- canonical upgrade of the new Sage r=3 factorization artifacts to `Verified Fact`.

## blocked_items

- No proof-boundary blocker remains from the post-Sage validator.
- No proof-boundary blocker remains from the final claim-ladder validator.
- `pytest -q || true` could not find `pytest` on PATH; because the plan made pytest nonblocking with `|| true`, this is recorded as an environment limitation rather than a blocker.
- The first `sage-r2` run was blocked by Sage trying to write `/home/leah/.sage`; patched by setting `DOT_SAGE` under repo `.codex/sage` in the wrapper and rerun successfully.
- Fixed-path outputs under `reports/` are overwritten by underlying Phase C/Sage scripts; timestamped wrapper logs preserve command execution, but fixed-path provenance should be improved in a later harness patch.

## recommended_next_plan

1. `Advisory Only`: independently audit `reports/sage_r3_unit_factorization.sageout` and `reports/sage_r3_full_factorization.sageout`, then package individual factor hashes.
2. `Advisory Only`: identify row-sum/Perron factors in the generic `QQ[t]` factorizations and compare the non-Perron factor lattice between unit and full.
3. `Advisory Only`: search for a finite-level structural mechanism for the observed squared factors: exact projectors, commutants, automorphisms, or equitable partitions over `QQ[t]`.
4. `Advisory Only`: keep determinant nonvanishing for all real `s > 0` as `Not Established` until a determinant-polynomial/root-isolation target is separately specified.
