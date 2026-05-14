---
name: collatz-campaign-manager
description: Multi-phase campaign execution skill for long Collatz research missions. Use for phase manifests, checkpointing, timeouts, resume/retry behavior, partial completion reports, skip-completed logic, and final program manifests.
---

# Collatz Campaign Manager

Use this skill for long multi-phase research campaigns that may partially complete, timeout, or need resume/retry handling.

## Mission

Manage:

- phase receipts;
- resume/retry behavior;
- skip-completed logic;
- timeouts;
- resource gating;
- checkpoint summaries;
- final program manifests.

## Standard outputs

```text
data/generated/<program>/<timestamp>/campaign_manifest.json
data/generated/<program>/<timestamp>/phase_receipts/*.json
reports/<timestamp>_campaign_status.md
reports/<timestamp>_campaign_final.md
```

## Timeout rule

Do not fail the whole mission because one expensive phase times out. Instead write:

```text
phase_status: BLOCKED_BY_TIMEOUT
claim_label: Not Established
```

Then continue safe independent phases.

## Required phase receipt fields

```text
phase_id
phase_name
status
commands_run
return_codes
artifacts_created
claim_labels
blocked_items
next_safe_phase
```

## Completion criteria

A campaign pass is complete only when every phase has a receipt or an explicit skipped/blocked explanation, and the final report identifies safe continuation points.
