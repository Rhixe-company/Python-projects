# REPOSITORY_SUMMARY.md

# Python-projects — 18 Beginner Scripts Collection

**Generated:** 2026-07-25  
**Status:** Archive Candidate  
**Path:** `projects/Python-projects/`

---

## Architecture

| Property | Value |
|----------|-------|
| **Type** | Collection of standalone Python scripts |
| **Pattern** | Single-file modular scripts, no framework |
| **Reference** | [Workflow Analysis](../docs/Project_Architecture/Workflow_Analysis.md) |

Python 3.x scripts: calculator, games, face detection, QR code generator, web scraper, and more. Each script is standalone with no shared dependencies.

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.x |
| **Key Libraries** | `requests`, `opencv-python`, `matplotlib`, `pillow`, `qrcode`, `beautifulsoup4`, `PyDictionary`, `schedule` |
| **Quality** | `ruff` (lint), `mypy` (type check) |
| **Testing** | Manual / ad-hoc |

---

## Project Structure

```
Python-projects/
├── basic_calculator.py
├── qr_code_generator.py
├── face_detection.py
├── web_scraper.py
├── game_*.py
├── requirements.txt
└── README.md
```

---

## Commands

```bash
pip install -r requirements.txt
python basic_calculator.py
python qr_code_generator.py
ruff check .
mypy *.py
```

---

## Issues

| Issue | Severity |
|-------|----------|
| No framework | INFO (by design) |
| No formal tests | MEDIUM |
| `opencv-python` system deps | MEDIUM |
| Archive candidate | HIGH |

---

## CI/CD

**Workflow:** `.github/workflows/python-projects-ci.yml`  
**Jobs:** Install → Ruff → MyPy → Smoke tests
