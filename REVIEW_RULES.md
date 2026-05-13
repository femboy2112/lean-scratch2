# Codex Review Rules

Use this file when running `/review` or asking a proof-auditor subagent to inspect a diff.

## Highest priority checks

1. No finite-level result is presented as a Collatz proof.
2. Every new mathematical claim has one approved status label.
3. Every new experiment records exact reproduction commands.
4. Any exact-algebra claim names the backend and domain/ring.
5. Any determinant/rank/charpoly claim states r, model, slice, level, and variable conventions.
6. Numerical observations are not upgraded to theorem status.
7. Scripts do not silently skip missing dependencies.
8. Reports include enough information for a second run to reproduce the result.

## Patch disposition labels

Use these review dispositions:

- `ACCEPT`
- `ACCEPT_WITH_PATCHES`
- `BLOCKED`
- `REJECT`
- `NEEDS_MORE_EVIDENCE`

## Reject immediately if

- The diff claims or implies a proof of the Collatz conjecture.
- A script deletes prior report artifacts without archiving.
- A report uses floating-point eigenvalues as proof.
- A theorem candidate omits hypotheses needed to identify the finite model.
- The code guesses a construction detail absent from the canonical bundle.
