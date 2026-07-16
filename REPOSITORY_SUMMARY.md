# Repository Summary — `Python-projects`

> Generated from real local git history on 2026-07-16. All facts are evidence-based
> (commit hashes, dates, file names) and were not invented.

## Overview

`Python-projects` is a **collection of 18 standalone Python scripts** (educational/utility
focus) maintained by **rhixecompany**. It is a sibling of the other four repos under
`SandBox/projects/`, bootstrapped in mid-June 2026. Unlike the web-app repos, this is a
flat, framework-free collection: each script is independently runnable (`python script.py`)
with no shared code or package structure beyond a common `requirements.txt`.

The working tree contains the 18 scripts plus standard community files
(`README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `AGENTS.md`),
a `.ruff_cache/`, and the generated `web-research-python-projects.md` (22 KB) and
`RESEARCH_REPORT.md`.

## Architecture

- **Type:** Script collection (single-file, modular, no framework).
- **Pattern:** Each script is standalone with an `if __name__ == "__main__":` guard;
  module docstrings; PEP 8 + `snake_case`; type hints encouraged.
- **Quality:** `ruff` (lint) and `mypy` (type check) are the declared gates.
- **No shared runtime:** scripts do not import one another.

## Key Components

| Script | Purpose |
|--------|---------|
| `basic_calculator.py` | Arithmetic calculator |
| `qr_code_generator.py` | QR code generation (qrcode) |
| `python_face_detection.py` | OpenCV-based face detection |
| `binary_search_algorithm.py` | Algorithm demo |
| `currency_converter.py` | Currency conversion (requests) |
| `dice_rolling_simulator.py` | Game/random |
| `email_sender.py` | SMTP email send |
| `email_slicer.py` | Email parsing utility |
| `graph_plotter.py` | Matplotlib plot |
| `image_resizer.py` | Pillow resize |
| `interest_payment_calculator.py` | Finance calc |
| `leap_year_checker.py` | Date utility |
| `quiz_program.py` | Interactive quiz |
| `random_password_generator.py` | Password gen |
| `rock_paper_scissors.py` | Game |
| `site_connectivity_checker.py` | HTTP health check |
| `word_dictionary.py` | PyDictionary lookup |
| `word_replacement.py` | Text utility |
| `automate_morning_text.py` | Scheduled task (schedule lib) |
| `requirements.txt` | Shared Python deps |
| `docs/` | Architecture workflow docs |

## Technologies

- **Language:** Python 3.x
- **Libraries:** `requests`, `opencv-python`, `matplotlib`, `pillow`, `qrcode`,
  `beautifulsoup4`, `PyDictionary`, `schedule`
- **Quality:** `ruff` (lint), `mypy` (type check)
- **Tooling:** VS Code (`.vscode/`, `.github/`), `.ruff_cache/`

## Data Flow

Each script is a self-contained pipeline:

```
Input (CLI args / stdin / file) → Script logic → Output (stdout / file / image / QR)
```

No cross-script data flow; no database; no network server. Shared `requirements.txt`
is the only coupling point.

## Team

| Contributor | Commits | Role |
|-------------|---------|------|
| `rhixecompany` <rhixecompany@gmail.com> | 5 / 5 (100%) | Sole author — setup, config, docs, research reports |

**Bus factor:** 1. All 5 commits were authored by a single contributor;
no co-authors, merges, or external PRs.
