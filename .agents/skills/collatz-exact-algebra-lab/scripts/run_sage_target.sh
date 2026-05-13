#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: $0 sage-r2|sage-r3-unit|sage-r3-full" >&2
  exit 2
fi

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

case "$TARGET" in
  sage-r2|sage-r3-unit|sage-r3-full)
    python .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py "$TARGET"
    ;;
  *)
    echo "Unknown Sage target: $TARGET" >&2
    exit 2
    ;;
esac
