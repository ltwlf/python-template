# Python Template 🐍

Modern Python project template with UV, Ruff, Black, Mypy, and Pytest.

## 🚀 Use This Template

1. **Create your project**:

    ```bash
    # Use this template to create a new repository
    # Or download and rename the folder
    ```

2. **Setup**:

    ```bash
    uv sync                    # Install dependencies
    uv run pre-commit install  # Setup quality checks
    ```

3. **Customize**:
    - Update `pyproject.toml` with your project name and details
    - Rename `src/mypackage/` to your package name
    - Replace example code with your implementation
    - Update this README

## 📁 Structure

```
src/mypackage/           # Your package code
├── __init__.py          # Package exports
├── __main__.py          # CLI entry point
└── core.py              # Main functions

tests/                   # Your tests
└── test_sample.py

pyproject.toml          # All configuration
```

## 🛠️ Development

```bash
# Run your package
PYTHONPATH=src uv run python -m mypackage

# Quality checks (or use VS Code tasks)
uv run ruff check      # Linting
uv run ruff format     # Formatting
uv run mypy src/       # Type checking
uv run pytest          # Tests

# All at once
uv run ruff check  && uv run ruff format  && uv run mypy src/ && uv run pytest
```

## 📦 Updating Dependencies

```bash
# Update all packages
uv sync --upgrade

# Update specific package
uv add ruff@latest

# After updates, test everything still works
uv run ruff check . && uv run black . && uv run mypy src/ && uv run pytest
```

## ✨ Features

-   **UV**: Fast package management
-   **Ruff**: Modern linting and formatting
-   **Mypy**: Strict type checking
-   **Pytest**: Testing framework
-   **Pre-commit**: Automated quality gates
-   **VS Code**: Ready-to-use tasks and settings
-   **Dev Container**: Consistent environment

---

Start coding! 🎉
