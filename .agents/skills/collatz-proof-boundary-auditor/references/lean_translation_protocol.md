# Lean Translation Protocol

Lean is used after a statement is stable.

## Do not formalize first

Do not use Lean to explore. Use Python/Sage first.

## Translation stages

1. State an English finite theorem candidate.
2. Expand every implicit hypothesis.
3. Replace project vocabulary with exact definitions.
4. Create a Lean namespace and theorem stub.
5. Mark hard proof bodies with `by
  sorry` only in skeleton files.
6. Do not treat stubs as proved.

## Naming convention

```text
CollatzSpectral.<Area>.<TheoremName>
```

Examples:

```lean
namespace CollatzSpectral.R3

theorem finite_rank_kernel_candidate
  (level : Nat)
  (hlevel : level = 3) :
  True := by
  trivial

end CollatzSpectral.R3
```
