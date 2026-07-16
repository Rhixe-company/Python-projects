# AUDIT — Python-projects

Read-only repo-management audit (Phases 0, 2, 3). Destructive phases HELD.

## Overview
Collection of standalone Python learning scripts (calculator, dice sim, QR generator, face detection, quiz, etc.). Has AGENTS.md, README.md, LICENSE, CODE_OF_CONDUCT.md, CONTRIBUTING.md, `.github/`, `docs/`, `.ruff_cache/`.

## Disk Usage
245K (excluding .git/caches). Small, source-only.

## Entrypoint
No single entrypoint — each `*.py` is independently runnable (e.g. `python basic_calculator.py`). No `__main__`/CLI aggregator.

## Gitignore Audit
`.gitignore` present (Python + VSCode + Windows template).
Covered: .env, *.pyc, __pycache__/, dist/, build/, venv/, .DS_* (via `.DS_Store` not explicit but Windows/Thumbs covered; NOTE: `.DS_Store` itself not listed), .ruff_cache/.
MISSING:
- `node_modules/` — not listed (N/A, pure-Python project, low priority).
- `.next/` — not listed (N/A).
- `.DS_Store` — not explicitly listed (macOS artifact; low priority on Windows).

## Dependency Audit
- `requirements.txt` present, **fully pinned** (`==`): beautifulsoup4 4.13.3, numpy 2.2.4, matplotlib 3.10.1, opencv-python 4.11.0.86, pillow 11.1.0, plus dev tools (pytest 8.3.5, mypy 1.15.0, ruff 0.11.2, black 25.1.0, coverage, pre-commit). Also includes odd/legacy pins: `bs4==0.0.2`, `futures==3.0.5` (Py2 backport, unnecessary on Py3), `environ==1.0` + `credentials==1.1` (likely wrong packages vs django-environ). Flag for review.
- `pip` available. `pip-audit` NOT installed — vulnerability scan not run (read-only; no install).

## Branch State
`git branch`: `* development`, `production`. No `master`/`main`/stray branches. Current = development.

## Destructive Phases HELD
- Phase 1 (branch deletion / push): NOT run.
- Phase 4 (CI creation): NOT run.
- Deferred: review suspicious deps (`futures`, `bs4`, `environ`, `credentials`).
