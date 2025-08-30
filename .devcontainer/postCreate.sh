#!/usr/bin/env bash
set -euo pipefail

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ensure uv is on PATH for current session
export PATH="$HOME/.local/bin:$PATH"

# Initialize venv + install deps if project exists
if [ -f "pyproject.toml" ]; then
  uv venv
  . .venv/bin/activate
  uv sync

  # Setup pre-commit hooks
  uv run pre-commit install
fi

echo "Dev container setup complete ✅"
