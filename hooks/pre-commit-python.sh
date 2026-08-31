#!/usr/bin/env bash
# pre-commit-python — lint + typecheck staged .py files before commit
set -euo pipefail

cd "C:/Users/Alexa/Desktop/SandBox/projects/Python-projects"

echo "[pre-commit-python] Checking staged Python files..."

# Get staged .py files
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$' || true)

if [ -z "$STAGED" ]; then
    echo "[pre-commit-python] No staged Python files. OK."
    exit 0
fi

echo "[pre-commit-python] Staged: $(echo "$STAGED" | wc -l) file(s)"

# Run ruff
echo "[pre-commit-python] Running ruff check..."
echo "$STAGED" | xargs ruff check || {
    echo "[pre-commit-python] ruff failed — fix before committing"
    exit 1
}

# Run ruff format check
echo "[pre-commit-python] Running ruff format --check..."
echo "$STAGED" | xargs ruff format --check || {
    echo "[pre-commit-python] format issues — run 'ruff format .' first"
    exit 1
}

echo "[pre-commit-python] All checks passed."
