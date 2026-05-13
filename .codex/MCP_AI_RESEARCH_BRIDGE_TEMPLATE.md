# MCP / External Math Bridge Template

Do not commit secrets, bearer tokens, tunnel URLs, or live bridge endpoints.

Use this as a planning template if you connect Codex to an external math bridge or local service.

## Desired capabilities

- exact SymPy/Sage job dispatch;
- result polling;
- read-only retrieval of witness artifacts;
- HMAC/token security handled outside the repo;
- logs with tokens redacted.

## Safe prompt for Codex

```text
An external math bridge may be available. Before using it, inspect the local MCP/server configuration and verify that no secrets will be committed. Use the bridge only for allowlisted exact algebra tasks, and copy returned witnesses into `reports/` with hashes and reproduction metadata.
```

## Required report fields

```text
bridge_name:
endpoint_source:
auth_handling:
task_id:
input_hash:
output_hash:
claim_label:
claim_boundary:
```
