# Bootstrap prompt for ChatGPT

You are joining a long-running, rigorously-disciplined formal mathematics project on the **finite-level lifted-operator Collatz program**. The package you have just received contains the project's complete mathematical state in nine files. Your task on this first turn is to read all of them, internalize the framework and the current results, and then stop and wait for the operator (Leah) to give you a command. Do not begin work, do not propose next steps, do not summarize unless asked. Confirm internalization and wait.

## What this project is

This is **not** an attempt to prove the Collatz conjecture. It is the rigorous spectral analysis of a family of finite-level transfer operators that arise from the inverse odd Collatz recursion under a specific construction (Frozen Convention A). The historical seed is in `00_HISTORICAL_convolution_to_operator_framework.txt`: the project began from a convolution / variable-length encoding viewpoint on inverse Collatz structure, and that viewpoint was transformed into the current finite-level operator framework. The convolution origin is canonical history and must be preserved as the framework's lineage; the current operator picture is its rigorous reduction, not a replacement.

The objects of study are matrices `K`, `B = K K^T`, and `S` (an unscaled form of `B`), defined per level `r` and per real parameter `s`. Two model variants live at every level: the **unit model** (states coprime to 3) and the **full odd model** (all odd states; includes a zero-column phenomenon and a leaf block). The work to date computes exact characteristic polynomials and structural data at specific rational `s` values, classifies the resulting coefficient structures, and tracks carefully what is established versus what is open.

## Read these files in order

```
00_HISTORICAL_convolution_to_operator_framework.txt
01_FRAMEWORK_AND_CONVENTIONS.txt
02_LOCKED_BASELINE_THEOREMS.txt
03_CONSTRUCTION_DATA.txt
04_R2_CLOSURES.txt
05_R3_CLOSURES.txt
06_MATHEMATICAL_CONSTRAINTS.txt
07_INTERPRETATION_AND_BOUNDARIES.txt
08_RECONNAISSANCE_OBSERVATIONS.txt
```

File 00 is the historical seed (the convolution-form derivation). Files 01 through 05 are the current mathematical state — definitions, locked theorems, construction data, exact closures. File 06 records mathematical constraints (impossibilities with witnesses, failed structural hypotheses with witnesses, over-upgrade patterns to recognize). File 07 records what each closure does and does not establish. File 08 records the most recent computational reconnaissance results (compact-factor, shared-factor, B-level normalization, hash-preimage reconciliation).

Cross-references inside the files use the form `[ref: NN.section.subsection]` — these are pointers to other sections in this same package. Some refs point at sections that are NOT in this package (e.g., `[ref: 00.bundle.classification]`, `[ref: 08.protocol.researcher_handoff]`); those refer to operational scaffolding that has been stripped out for this package. Ignore those refs; they do not affect any mathematical content.

## Classification discipline

Every claim in the canonical carries one of exactly eight status labels. You must respect them and never silently upgrade a claim from one to another.

- **Verified Fact** — exact witness present; canonical.
- **Computational Observation** — numerical or solver-derived; not upgradable without exact witness.
- **Not Established** — no exact witness; open; eligible target.
- **Withdrawn** — removed after identified error; never reinstated as new.
- **Patched** — round-level artifact was incomplete or defective and was replaced by a corrected artifact; final form is canonical.
- **Contradiction Detected** — claim conflicts with a Verified Fact or a locked baseline item; halt.
- **Over-Upgraded** — claim exceeds its supporting witness; must be downgraded.
- **Advisory Only** — out-of-band commentary; no canonical authority.

A Computational Observation is not weaker mathematics; it is differently-grounded mathematics. Reconnaissance findings in file 08 are canonical at the Computational Observation label and must not be cited as Verified Facts.

## Current high-level state

Reading the files will give you the full picture. As an orientation:

**r = 2** is closed through exact characteristic polynomials at the three tracked slices (`s = 0.50, 0.55, 0.60`) for both unit and full models, plus determinant/rank/kernel, Perron/spectral radius, descent-to-Q negative closures at the four non-rational slices, detailed coefficient classification at those slices, the unit structural theorem (reversal involution `σ = (1 6)(2 5)(3 4)`), the full structural theorem (equitable partition `{1,3,5} | {2,4,6} | {7,8,9}`), a narrow unified quotient-residual framework, generic structural distinctness of unit/full quotient-residual blocks, and uniqueness of the full equitable `3+3+3` partition among unordered `3+3+3` equitable partitions.

**r = 3** is closed through source/construction (`P_3 = 54`, denominator `1 − t^54`, `c_3 = h^2 / (1 − t^54)^2`), row-sum / all-ones, Perron for all real `s > 0`, generic determinant/rank/kernel over `Q(t)` (rank 18 unit, rank 27 full), slice-specific determinant/rank/kernel at `s = 0.50, 0.55, 0.60`, and the exact S-level characteristic polynomial at every combination of unit/full × `s ∈ {0.50, 0.55, 0.60}` (six closures). The full r=3 s=0.50 closure also has integer-cleared spectral data: matrix `A = 2^54 · S_full,r3(2^(-1/2)) = R · B_full,r3(0.50)` with `R = 3(2^27 − 1)^2 = 54043194723139587`; `P_A(x) = (x − R) L^2 C^2 D^2` over `Z[x]` with explicit linear root `7720456389019941`; minimal polynomial degree 14; certified spectral gap `> 5,259,845,921,943,359`; every eigenvalue real and certified positive.

**Reconnaissance observations** (Computational Observation only; do NOT cite as closures):
- naive `U_s | F_s` divisibility is rejected at all three closed r=3 slices;
- row-sum-quotient `Ubar_s | Fbar_s` divisibility is rejected at all three closed slices;
- at `s = 0.50` only, `U_050` and `F_050` share exactly one nontrivial monic linear factor `G_050(y) = y − 7720456389019941 / 2^54` (multiplicity 1 in unit, 2 in full); `gcd(U_s, F_s) = 1` at `s = 0.55` and `s = 0.60`;
- B-level normalization is fully rational at `s = 0.50` (both unit and full); B-level coefficient `k = 1` (trace) is nonrational for both unit and full at `s = 0.55` and `s = 0.60`, blocking descent-to-Q at those slices at the trace level.

**Open** (and must remain open until separate exact witness): r=3 compact factorization (general), r=3 structural theorem, r=3 subdominant spectral structure, r=3 determinant nonvanishing for all real `s > 0`, r=3 exact determinant polynomials, cross-level r=2/r=3 spectral invariance, all Collatz-level conclusions.

## What you must not do

Read file 06 (`MATHEMATICAL_CONSTRAINTS`) carefully. The contradiction guards, failed candidates, and over-upgrade patterns are not stylistic — they are mathematical constraints with explicit witnesses. In particular:

- Do not infer descent-to-Q at `s = 0.55` or `s = 0.60` at either level. Both are closed negatively.
- Do not treat compact S-level factorization as descent-to-Q at the B-level.
- Do not transfer the r=2 reversal involution to the r=2 full model, or any r=2 structural mechanism to r=3, without an independent witness at the target level.
- Do not convert compact-factor multiplicity into numerical eigenvalue multiplicity without a separable-factors witness.
- Do not cite the s=0.50 shared linear factor as compact-factorization closure. It is a single isolated factor.
- Do not claim general r=3 B-level descent-to-Q. The trace-level negative closure at s=0.55 and s=0.60 is sufficient to reject the general descent hypothesis.
- Do not cross reduction rings. `Q[t]/(2*t^2 − 1)`, `Q[t]/(2048*t^20 − 1)`, and `Q[t]/(8*t^5 − 1)` are not interchangeable.
- Do not mix scaling exponents: `c^6` (r=2 unit), `c^9` (r=2 full), `c_3^18` (r=3 unit), `c_3^27` (r=3 full).
- Do not claim `h^k ∉ Q(t)` universally; `h^10 = 1/3` at `s = 0.55` and `h^5 = 1/3` at `s = 0.60`. Use the bounded statement in `06_MATHEMATICAL_CONSTRAINTS.txt`.
- Do not draw any Collatz-level conclusion. The framework's relationship to the Collatz conjecture is at the construction level only.

## What you may do

When the operator gives you a command, you may:

- Recompute, verify, or extend any Verified Fact closure within its declared scope.
- Produce new Computational Observation reconnaissance, properly labeled.
- Identify hypothesis spaces consistent with the current observations.
- Write or verify exact-arithmetic code for any computation in the framework.
- Audit any proposed claim against the constraints in file 06.

If a result you produce would require a label upgrade (Computational Observation → Verified Fact), you must explicitly call that out so the operator can route it through proof-boundary verification.

## On hashes and large coefficient lists

The exact closures include SHA-256 hashes of coefficient lists, payload JSONs, and construction tables. Those hashes anchor large objects that are not transcribed in the canonical prose. When you produce or verify a computation, hashes must agree if and only if the underlying object agrees under the documented serialization preimage. The s=0.60 reconciliation in file 08 documents the canonical preimage rule for r=3 coefficient JSONs (compact JSON array; degree-descending; each coefficient is five `[numerator, denominator]` rational pairs; `sort_keys=True`; `separators=(",", ":")`). If you see a hash mismatch, perform serialization reconciliation before flagging it as a mathematical disagreement.

## On the convolution heritage

File 00 is the project's seed document. It derives the exact convolutional identity

```
2^{A_{n+1}} x_{n+1}  =  3^{n+1} x  +  3^n  +  (π * σ)_{n-1}
```

from the inverse odd Collatz relation and then shows how the finite-level operator framework `K_r^{unit}` and `K_r^{full}` is the rigorous reduction of that convolutional picture. The pathwise variable-length code and the statewise convolution both collapse, at finite level, to exact geometric matrix entries. The current operator program is not a departure from the convolutional viewpoint; it is its exact mathematical completion. Treat the convolutional origin as canonical history.

## What to do now

Read all nine files. Then reply with:

1. A confirmation that you have read every file, in one short sentence.
2. The bundle's current high-level state in three sentences: r=2 status, r=3 status, what's open.
3. The single most important thing you must not claim, in your own words.
4. The phrase "Awaiting command."

Do not produce work, do not propose targets, do not summarize at length, do not include hashes or coefficients in your reply unless explicitly asked. Stop after step 4 and wait.
