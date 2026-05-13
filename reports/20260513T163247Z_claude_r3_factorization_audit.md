# Claude Code Audit — r=3 Factorization Bundle

audit_timestamp: 20260513T163247Z
auditor: Claude (claude-opus-4-7[1m])
target_bundle: data/generated/r3_factorization_audit/20260513T160231Z
prior_codex_artifacts: reports/20260513T160231Z_r3_factorization_audit.{md,json}, reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md
hash_audit_artifact: data/generated/claude_audit/20260513T163247Z/hash_audit.json
command_log: data/generated/claude_audit/20260513T163247Z/command_log.txt
sandbox_failures: data/generated/claude_audit/20260513T163247Z/sandbox_failures.txt

claim_boundary: This is a static-audit assessment of a finite-level S-level characteristic-polynomial factorization artifact bundle inside the lifted-operator framework. It does not prove, imply, nearly imply, or essentially solve the Collatz conjecture. It does not establish determinant nonvanishing for all real `s > 0`, cross-level invariance, structural mechanism, or global orbit behavior.

## Disposition

PASS_WITH_PATCHES

Rationale: Every recorded hash in the audited bundle is reproducible from the on-disk bytes using Python stdlib, the script `sage/r3_factorization_audit.sage` performs a substantive exact reconstruction check (not merely an assertion), and the recorded factor degree/multiplicity sums match the matrix dimensions for unit (18) and full (27). Sage itself is not present in this sandbox, so the algebraic reconstruction could not be re-executed end-to-end in this audit pass — that remains a required external/human verification step. Several wording refinements to the canonical patch proposal are recommended before any canonical-file insertion; they are PATCH-level only.

## Executive Summary

The Codex bundle `data/generated/r3_factorization_audit/20260513T160231Z/` is internally consistent. The 18 (unit) and 27 (full) S-level matrices are reconstructed inside the Sage script directly from `collatz_codex_harness.construct.s_counter_matrix`, the characteristic polynomial is computed over the recorded ring `QQ[t][y]` with `var="y"`, the displayed factorization's product reconstruction is exact-equality checked against `charpoly`, total y-degree is checked against the matrix size, and the row-sum eigenfactor `(y - row_sum(t))` is matched against factor 00 in both models. All artifact SHA-256 hashes recorded in the manifest, in `reports/20260513T160231Z_r3_factorization_audit.json`, and in the canonical patch proposal reproduce exactly from the on-disk files (`hash_audit.json` mismatches_count = 0). The internal `manifest_payload_sha256` is itself reproducible by stripping that field and canonical-JSON-hashing the remaining payload. The "Verified Fact" status label is appropriately scoped to a finite-level exact algebraic identity and is paired with explicit `not_established` items (positivity for all real `s > 0`, structural mechanism, cross-level invariance, Collatz-level implications). Required PATCH-level refinements concern (i) wording precision around what "irreducible" means in this audit (Sage `factor()` output trust, not an independent irreducibility proof), and (ii) noting that exact prior-string match is a convenience, not the authoritative check.

## Checked Commands

| # | Command | Status | Notes |
|---|---|---|---|
| 1 | `git status --short` | PASS | Clean tree on branch `claude-audit/r3-factorization-8PvP2`. |
| 2 | `ls -la data/generated/r3_factorization_audit/20260513T160231Z/` | PASS | unit/, full/, manifest.json present. |
| 3 | `find data/generated/r3_factorization_audit/20260513T160231Z/ -type f` | PASS | All expected files present (manifest, per-model factorization.{txt,json}, row_sum_witness.json, factors/factor_{00..03}.{txt,json}). |
| 4 | `python3 scripts/run_py_checks.py` | PASS | Sanity gates green; `payload_sha256 = 923614c3...`. |
| 5 | `python3 scripts/check_codex_skills.py` | PASS | Skills present. |
| 6 | `which sage` / `sage --version` | BLOCKED | Sage binary not present in sandbox (exit 127). Reconstruction cannot be re-executed here; static audit only. |
| 7 | Python stdlib hash recompute | PASS | All artifact/manifest hashes match; 0 mismatches (see `hash_audit.json`). |

## Findings

| Severity | File | Issue | Evidence | Required action |
|---|---|---|---|---|
| NOTE | `sage/r3_factorization_audit.sage` (line 172) | "irreducible_over_recorded_ring" is computed by re-running Sage `.factor()` on each factor and checking the result is a single multiplicity-1 entry. This is a smoke check that Sage agrees with itself, not an independent irreducibility proof. | `refactor = list(factor.factor()); irreducible = ... len(refactor)==1 and parent(refactor[0][0]) == factor and int(refactor[0][1]) == 1` (sage/r3_factorization_audit.sage:171-172). | Acceptable as recorded; in the canonical patch proposal, label the field as "Sage-displayed irreducibility over QQ[t][y]" rather than "irreducible over recorded ring" to avoid suggesting a separate algebraic proof. |
| NOTE | `sage/r3_factorization_audit.sage` (lines 168-170) | y-separability is computed in QQ(t)[y] via `gcd(factor, ∂/∂y factor) == 1` — correct ring choice. | `fraction_parent = PolynomialRing(FractionField(ring), "y"); factor_fraction.gcd(derivative)` (sage/r3_factorization_audit.sage:124, 168-170). | None; the `gcd_parent` field already records the precise ring. |
| NOTE | `sage/r3_factorization_audit.sage` (lines 222-231) | `matches_prior_exact_string` depends on factor ordering and exact formatting of Sage's `str(factorization)`. Reconstruction is the authoritative check; the script's `prior_comparison.explanation` field already says so on the False branch. | Source code lines 222-231 and manifest field `"explanation": "exact string match"`. | None as recorded. Possible WARNING for future readers: a False match would not invalidate the algebraic result — reconstruction_check is authoritative. |
| NOTE | `data/generated/.../manifest.json` (row_sum_witness) | `matching_factor_indices: [0]` for both models is correct: factor_00 has text `y - <row-sum t-polynomial>` (recomputed by Claude). The check uses `.monic()` on each side; both sides are already monic in y. | factor_00.txt content matches the `row_sum_factor` field literally. | None. |
| PATCH | `reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md` | Proposal lists factor hashes but does not include the factor-degree/multiplicity patterns ([1,1,2,6]/[1,1,2,2] for unit, [1,1,3,9]/[1,2,2,2] for full) or the manifest_payload_sha256 (only the file-level manifest hash). For a canonical-section insertion these are the most decision-relevant invariants. | Proposal markdown contains only `factorization_manifest_hash` + per-factor hashes. | Before canonical-section insertion, extend the proposal to also list the degree pattern, multiplicity pattern, dimension, and `manifest_payload_sha256` so reviewers can verify decision-relevant invariants without opening the bundle. |
| PATCH | `reports/20260513T160231Z_r3_factorization_canonical_patch_proposal.md` | Proposal does not name the recorded ring (`Univariate Polynomial Ring in y over Univariate Polynomial Ring in t over Rational Field`) at which irreducibility and separability are recorded. | Proposal markdown body. | Add an explicit `recorded_ring:` line so canonical readers do not have to infer the ring. |
| NOTE | `reports/20260513T160231Z_r3_factorization_audit.md` (line 13) | Uses "Verified Fact" status. Scope statement is appropriate; explicit Not-Established items are listed. | Lines 11-13, 65-77. | None — wording is correctly bounded. |
| NOTE | `reports/20260513T160231Z_r3_factorization_audit.md` (line 21) | Method paragraph says "identifies the exact all-ones row-sum factor". This is precise: it is the t-polynomial row-sum of S, not a constant. | Line 21 wording. | None. |

No BLOCKER findings.

## Hash Audit

All recomputed hashes match the recorded values. Detail:

- `manifest.json` file SHA-256: `fe5d15030c998d9c9ac2ea9b0acf6675edfb4f48dd6636c02c0c4e770aa83254` (matches `reports/20260513T160231Z_r3_factorization_audit.json` `manifest_sha256`).
- `manifest_payload_sha256` (`e13ce695b92ffa08d382f5da14889f1ac8bf59b16a8510c2a305ea4e144dbe7f`) reproduces by stripping that field and canonical-JSON-hashing the remaining payload via `json.dumps(..., sort_keys=True, separators=(",",":"))`.
- For each model in `{unit, full}` and each kind in `{factorization_txt, factorization_json, row_sum_witness_json}`: claimed `artifact_sha256` matches recomputed file SHA-256.
- For each model and each factor_index in `{00, 01, 02, 03}`: `record["factor_sha256"]` matches `sha256(factor_text_without_trailing_newline)`; the on-disk `factor_<idx>.txt` is the factor text followed by `\n`.
- All 8 patch-proposal factor hashes (4 unit + 4 full) match the corresponding `factor_sha256` fields in the per-factor JSON records.
- `reports/20260513T160231Z_r3_factorization_audit.md` SHA-256 = `23837acb97da5c45a46c4dfc81918a296aa4a0188036f03778f76e1d4c4062f4` matches `report_markdown_sha256` in the audit JSON.
- Prior Sage outputs exist with the recorded hashes:
  - `reports/sage_r3_unit_factorization.sageout` SHA-256 = `f341ce713b73a759e7a970f23178ea71047eb0821cf1b373ca3401ad38abf07c`.
  - `reports/sage_r3_full_factorization.sageout` SHA-256 = `fe1477297a2a807520390978a2dc3ea259e403698c420e1ecff74df16b68e71a`.

Total mismatches: 0. Full detail: `data/generated/claude_audit/20260513T163247Z/hash_audit.json`.

## Reconstruction Audit

Sound, conditional on Sage being correct.

`sage/r3_factorization_audit.sage:79-82` rebuilds `S` directly from `s_counter_matrix(r, model)` (the canonical construction in `src/collatz_codex_harness/construct.py`), entry-wise lifting each exponent Counter to a `QQ[t]` element. The characteristic polynomial is computed over `QQ[t]` with `var="y"` and cast into the recorded ring `parent = PolynomialRing(ring, "y")` = `QQ[t][y]` (line 126). The script then computes:

- `factorization = charpoly.factor()` (line 127)
- `product = prod(parent(factor) ** ZZ(multiplicity))` over the displayed factors (lines 129-131)
- `reconstruction_check = bool(product == charpoly)` (line 132)
- `total_degree_y = sum(int(parent(factor).degree()) * int(multiplicity) for factor, multiplicity in factors)` (line 133)
- `total_degree_check = bool(total_degree_y == matrix.nrows())` (line 135)

These are real comparisons (not assertions), so `reconstruction_check=True` and `total_degree_check=True` in the manifest are supported by script logic, not merely declared. The recorded degree patterns sum correctly:

- unit: `[1,1,2,6] · [1,1,2,2] = 1 + 1 + 4 + 12 = 18` (= matrix dimension).
- full: `[1,1,3,9] · [1,2,2,2] = 1 + 2 + 6 + 18 = 27` (= matrix dimension).

`degree_y` for each factor is computed as `factor.degree()` in `parent = QQ[t][y]`, so it is the degree in y (not t). `degree_t_max` is computed by scanning `poly.list()` (coefficients in `QQ[t]`) and taking the max ZZ-degree, which is a reasonable t-degree summary.

Caveat: re-execution requires Sage, which is unavailable in this sandbox. The static audit verifies (i) the script does what it claims, (ii) the recorded patterns are arithmetically consistent, and (iii) all hashes are reproducible from the on-disk bytes. An independent end-to-end re-run is the human/external verification step that this audit recommends before canonical-file insertion.

## Row-Sum Factor Audit

Sound for the stated finite-level scope.

`sage/r3_factorization_audit.sage:137-145`:

- `row_sums = [sum(matrix[i, j] for j in range(matrix.ncols())) for i in range(matrix.nrows())]`
- `row_sums_equal = bool(all(value == row_sums[0] for value in row_sums[1:]))` — checks all row sums equal as elements of `QQ[t]`.
- `row_sum = ring(row_sums[0])`; `row_sum_factor = parent(y - row_sum)` — exactly the eigenfactor for the all-ones eigenvector.
- `row_sum_charpoly_zero = bool(charpoly(row_sum) == 0)` — evaluates the characteristic polynomial in y at y = row_sum(t) and checks it is the zero element of `QQ[t]`.
- `matching_row_sum_indices = [idx for idx, (factor, _m) in enumerate(factors) if parent(factor).monic() == row_sum_factor.monic()]`.

`matching_factor_indices = [0]` is justified: factor_00 in each model has on-disk text `y - <row_sum_polynomial>` literally matching the `row_sum_factor` field in `row_sum_witness.json`. Cross-check: `record.factor_sha256` for factor_00 (unit/full) equals the `row_sum_factor_sha256` for the same model (Claude recomputed both as SHA-256 of the text without trailing newline).

This is a finite-level row-sum / Perron-style eigenfactor identification. It does not claim or imply anything about subdominant spectrum, all-real-s positivity, or Collatz behavior.

## Irreducibility / Separability Audit

Conditionally justified; wording recommended to be tightened.

- "irreducibility_all_true" is computed by re-factoring each displayed factor with `factor.factor()` and requiring the result to be a single multiplicity-1 entry equal to the input. This trusts Sage's `factor()` over `QQ[t][y]`; it is not an independent algebraic irreducibility proof.
- "separability_all_true" is computed over `QQ(t)[y]` via `gcd(factor, ∂factor/∂y) == 1` in the fraction-field polynomial ring. This is the correct ring for testing y-separability and is recorded as `gcd_parent` in each factor record.
- The recorded ring `QQ[t][y]` is precise; since the charpoly is monic in y (primitive), Gauss's lemma matches `QQ[t][y]` and `QQ(t)[y]` factorizations.
- Repeated factors in the displayed factorization (multiplicity ≥ 2) are about characteristic-polynomial multiplicity, not internal inseparability — the script tests separability per displayed factor, so the two are not confused.

Recommended wording in the canonical patch proposal: explicitly write "Sage-displayed irreducibility over `QQ[t][y]`" and "y-separability over `QQ(t)[y]`" so readers do not interpret the entries as a standalone irreducibility theorem.

## Prior-Output Comparison

The audit cross-checks against `reports/sage_r3_unit_factorization.sageout` and `reports/sage_r3_full_factorization.sageout` by splitting on `"\n\n"` and comparing the body string to `str(factorization)`. Both `matches_prior_exact_string` flags in the manifest are `True`. Claude verified both prior `.sageout` files exist with the recorded SHA-256 hashes and that their bodies begin with the same factor_00 text as the new factorization output.

Caveats:
- Exact string match depends on Sage's factor ordering and formatting; a future Sage version could produce a False match without invalidating the algebraic content.
- The script's `explanation` field already documents this on the False branch, but on the True branch it says only `"exact string match"`. Readers should not interpret prior-string match as a proof of correctness; reconstruction_check is the authoritative algebraic check.

False-positive risk (current run): negligible — the prior files were generated from the same source and same Sage build chain. False-negative risk (future runs): possible from factor reordering. This is acceptable because reconstruction is authoritative.

## Canonical Patch Proposal Readiness

READY_WITH_PATCHES

Strengths:
- Status is correctly labeled `Advisory Only`.
- Recommends `Verified Fact` only for the finite-level audit artifacts.
- Records `factorization_manifest_hash` and per-factor hashes that match the bundle.
- Explicitly defers canonical-file edits to a human reviewer.

Required PATCH refinements before insertion (none are blockers; all are wording/coverage):

1. Extend the proposal markdown to include the per-model degree pattern, multiplicity pattern, dimension, and `manifest_payload_sha256`, so reviewers can verify the decision-relevant invariants without opening the bundle.
2. Add a `recorded_ring:` line naming `Univariate Polynomial Ring in y over Univariate Polynomial Ring in t over Rational Field` (= `QQ[t][y]`) and explicitly name the y-separability ring as `Frac(QQ[t])[y]` (= `QQ(t)[y]`).
3. Rename the irreducibility metadata field semantics to "Sage-displayed irreducibility over the recorded ring" so that the proposal does not silently overclaim a standalone algebraic irreducibility theorem.
4. Add a one-line reproduction caveat: re-running `env DOT_SAGE=$PWD/.codex/sage sage sage/r3_factorization_audit.sage` is the required human-side verification step before any canonical-file insertion.

Do not apply this patch. This is a human-canonical decision per the bundle's own `required_external_review`.

## Safe Claim Statement

> Verified Fact, finite-level only: for r=3, the S-level unit (18×18) and full (27×27) matrices reconstructed from `src/collatz_codex_harness.construct.s_counter_matrix` have characteristic polynomials in y over `QQ[t]` that, in the Sage factorization recorded at `data/generated/r3_factorization_audit/20260513T160231Z/`, decompose into four displayed factors with degree pattern `[1, 1, 2, 6]` (unit) and `[1, 1, 3, 9]` (full) and multiplicity pattern `[1, 1, 2, 2]` (unit) and `[1, 2, 2, 2]` (full). The displayed product reconstructs the characteristic polynomial exactly, the total y-degree equals the matrix dimension, every artifact SHA-256 hash recorded in the bundle and reports is reproducible from the on-disk bytes (mismatches_count = 0), and the linear factor `(y - row_sum(t))` corresponding to the all-equal row sum of S coincides with displayed factor 00 in both models.

## Unsafe Claims to Avoid

- This proves Collatz. (Forbidden.)
- This essentially proves Collatz. (Forbidden.)
- This rules out divergent Collatz orbits. (Forbidden.)
- The factorization implies determinant nonvanishing for all real `s > 0`. (Not established.)
- The factorization implies cross-level invariance between r=2 and r=3. (Not established.)
- The factorization exposes a structural mechanism / Collatz dynamic. (Not established.)
- The row-sum factor controls the spectral radius for all `s > 0`. (Not established.)
- "Irreducible" entries in the bundle constitute an independent algebraic irreducibility proof. (Over-Upgraded: they are Sage-displayed irreducibility checks.)
- Exact string match against prior `.sageout` files is the authoritative correctness check. (It is a convenience; reconstruction is authoritative.)
- r=2 mechanisms transfer to r=3 because the factorization patterns rhyme. (Known over-upgrade trap per `CLAIM_GUARDRAILS.md`.)
