# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary,
schedule, ruff, mypy, uv
**Status:** Active

---

## Similar Projects

| Project | Why Relevant |
|---------|--------------|
| cookiecutter-django-tailwind (workspace) | Shares uv + ruff tooling conventions |
| ecom (workspace) | Shared Python packaging patterns |
| uv (astral.sh) | Reference tooling for the whole collection |

---

## Key Findings

**Package management (uv).** Rust-powered, 8–100× faster than pip (Real Python measured ~8×; HN benchmark 38s pip vs 3s uv). Replaces pip, pip-tools, virtualenv, pyenv, Poetry. `uv add <pkg>` (dep + lock), `uv sync`, `uv run script.py` (auto venv + PEP 723 inline deps), `uvx <tool>`. For standalone scripts, PEP 723 `# /// script` block removes the need for `requirements.txt`.

**Python version guidance (2026, verified).** 3.12 security-only (EOL Oct 2028). **3.13** bugfix (EOL Oct 2029) — JIT (experimental, ~30% CPU-bound) + free-threaded build opt-in. **3.14** (released Oct 7, 2025) bugfix (EOL ~Oct 2030) — **free-threaded now officially supported**, opt-in JIT in Win/macOS binaries, template strings (t-strings), deferred annotations, subinterpreters, `compression.zstd`. 3.15 prerelease (EOL ~2031).
**Rec:** 3.13+ for new scripts; 3.12 floor for ecosystem compat.

**Ruff linter/formatter.** All-in-one (flake8+isort+pyupgrade+Black) single Rust binary. Config in `pyproject.toml`: `E4/7/9`, `F`, `B`, `I`, `UP`, `N`, `ERA`, `LOG`. `ruff check . --fix`, `ruff format .`.

**Testing with pytest.** `tests/test_*.py` + `conftest.py`; fixture scopes function/module/session; `tmp_path` for file tests; `@pytest.mark.parametrize`; plugins `pytest-cov`, `pytest-xdist` (`-n auto`), `pytest-mock`. Start with calculator tests, mock requests for scrapers.

**Security (OpenSSF pyscg, May 2026).** No `shell=True`; no hardcoded secrets; always `requests.get(url, timeout=10)`; pin deps; validate input. Scan: `bandit -r .` + `pip-audit`; use `secrets` not `random`.

---

## Cheatsheets & Quick Reference

| Topic | Resource |
|-------|----------|
| Python 3.14 Docs | https://docs.python.org/3.14 |
| PEP 723 (script deps) | https://peps.python.org/pep-0723 |
| uv | https://docs.astral.sh/uv |
| Ruff | https://docs.astral.sh/ruff |
| pytest | https://docs.pytest.org |
| OpenSSF pyscg | https://best.openssf.org/Secure-Coding-Guide-for-Python/ |

---

## Best Practices
1. Use **uv** for all installs/runs; adopt PEP 723 inline deps for standalone scripts.
2. Target **Python 3.13+**; keep 3.12 as minimum supported.
3. Run **ruff** (lint + format) and **mypy** (`strict`) in CI/pre-commit.
4. Write **pytest** tests for pure-logic scripts; mock network calls.
5. Scan with **bandit + pip-audit**; never commit secrets — use `.env`.

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Mixing tabs/spaces | 4-space consistent indent |
| `is` vs `==` | `==` for values; `is` only for `None` |
| Mutable default args (`def f(x=[])`) | `None` default, instantiate inside |
| Modifying list while iterating | Comprehension for filtered copy |
| Bare `except: pass` | Catch specific exceptions |
| Hardcoded secrets | Env vars + `.env` files |
| Free-threading surprises (3.13/3.14) | Guard shared state; prefer 3.13 stable |

---

## Performance
- **Python 3.14 JIT** experimental ~30% CPU-bound; 3.13 comprehension inlining ~2×
- **List comprehensions** 2–3× faster than `for`+`.append()`; `lxml` parser for BS4 10–20× faster
- **Set membership** O(1) vs list O(n); `lru_cache` for pure functions; generators for memory
- **OpenCV** — prefer NumPy vectorization over pixel loops.
- **uv** installs 8–100× faster (CI: pip 38s vs uv 3s).

---

## Security
1. No `shell=True`; pass arg lists to subprocess.
2. No hardcoded secrets — `secrets` module, `.env` files.
3. `requests.get(url, timeout=10)` to avoid hangs.
4. Pin dependency versions; run `pip-audit` regularly.
5. `bandit -r .` static scan in CI.

---

## Type Hints & Static Analysis
- **mypy** in `pyproject.toml`: `strict = true`, `disallow_untyped_defs = true`
- Python 3.10+ `str | int` union; 3.9+ `list[str]` not `typing.List[str]`
- Pragmatic: type hints on public functions; `@dataclass` for structured data

---

## Related Projects

| Project | Relevance |
|---------|-----------|
| cookiecutter-django-tailwind | Shared uv/ruff tooling |
| ecom | Python packaging conventions |
| selenium_webdriver | Standalone script + dependency mgmt |

---

## Resources

| Resource | URL |
|----------|-----|
| Python 3.14 Docs | https://docs.python.org/3.14 |
| PEP 723 | https://peps.python.org/pep-0723 |
| uv | https://docs.astral.sh/uv |
| Ruff | https://docs.astral.sh/ruff |
| pytest | https://docs.pytest.org |
| OpenSSF pyscg | https://best.openssf.org/Secure-Coding-Guide-for-Python/ |

**Methodology:** 9 web searches (uv, Python 3.14, Ruff, pytest, OpenSSF pyscg) + Astral/Python/OpenSSF doc extraction. Version + tooling facts verified.
