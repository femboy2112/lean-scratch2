# .codex Project Configuration

These files are optional project-scoped Codex aids.

Codex loads `.codex/config.toml` only when the project is trusted. If Codex ignores this directory, trust the project in Codex or copy the relevant settings into your user-level `~/.codex/config.toml`.

## Included

- `config.toml` — safe project defaults, subagent role descriptions, and review settings.
- `agents/*.toml` — role-specific configuration layers.
- `prompts/*.md` — copy-paste launch prompts.
- `MCP_AI_RESEARCH_BRIDGE_TEMPLATE.md` — template for connecting an external math bridge without committing secrets.
