# Audit Checklist

## Report audit

- [ ] Does every claim have an allowed label?
- [ ] Are all exact claims scoped to finite level/model/slice?
- [ ] Is every command reproducible?
- [ ] Are input hashes recorded?
- [ ] Are failed probes preserved?
- [ ] Is numerical evidence quarantined?
- [ ] Is modular evidence scoped?
- [ ] Is Collatz-level language absent?

## Script audit

- [ ] Does the script fail loudly on missing dependencies?
- [ ] Does it record outputs?
- [ ] Does it avoid silent fallback from Sage exact to float?
- [ ] Does it preserve prior artifacts?
- [ ] Does it identify exact backend and domain?

## Lean audit

- [ ] Is the theorem finite-level only?
- [ ] Are hypotheses explicit?
- [ ] Are stubs marked as stubs?
- [ ] No global Collatz conclusion appears.
