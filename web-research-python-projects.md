# Web Research: Python-projects

**Date:** 2026-07-16
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy, uv

---

## Table of Contents

1. [Python Project Structure & Layout](#1-python-project-structure--layout)
2. [Package Management (uv)](#2-package-management-uv)
3. [Common Pitfalls & Beginner Mistakes](#3-common-pitfalls--beginner-mistakes)
4. [Security Best Practices](#4-security-best-practices)
5. [Performance Optimization](#5-performance-optimization)
6. [Type Hints & Static Analysis](#6-type-hints--static-analysis)
7. [Ruff Linter & Formatter Configuration](#7-ruff-linter--formatter-configuration)
8. [Testing with pytest](#8-testing-with-pytest)
9. [Python Version Guidance (2026)](#9-python-version-guidance-2026)
10. [Cheatsheets & Quick Reference](#10-cheatsheets--quick-reference)
11. [Resources & Further Reading](#11-resources--further-reading)

---

## 1. Python Project Structure & Layout

**Source:** [Real Python — project layout](https://realpython.com/ref/best-practices/project-layout/)

### Two Main Layout Types

**`src/` layout** — Source code lives inside `src/`. Best for library code and larger projects; prevents accidental imports from working directory, avoids import errors in tests.

```
project_name/
├── bin/                    # Optional — executable scripts
├── docs/                   # Optional — documentation
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── __main__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── LICENSE
├── README.md
└── pyproject.toml
```

**Flat layout** — Source package lives at root level. Works for quick scripts but prone to import confusion as project grows.

```
project_name/
├── project_name/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
├── README.md
├── pyproject.toml
└── LICENSE
```

### Standard Components

| File/Dir | Purpose |
|----------|---------|
| `src/` or `project_name/` | Source code package |
| `tests/` | Unit tests |
| `README.md` | Overview, install, usage |
| `LICENSE` | Legal terms |
| `pyproject.toml` | Centralized config (metadata, deps, build system, tool settings) |
| `docs/` | Documentation (optional) |
| `bin/` or `scripts/` | Executable scripts calling package functions (optional) |

### What to Avoid

- ❌ Everything in root (flat soup with tests, source, config all mixed)
- ❌ `utils.py` grab bags that accumulate unrelated functions
- ❌ No virtual environment / no dependency isolation
- ❌ Hardcoded paths — use `pathlib.Path` + `os.environ` instead

---

## 2. Package Management (uv)

**Sources:** [DataCamp — uv guide](https://www.datacamp.com/tutorial/python-uv), [Tech Insider — uv vs pip 2026](https://tech-insider.org/uv-vs-pip-2026), [Astral — uv GitHub](https://github.com/astral-sh/uv)

### Why uv?

- **Rust-powered** — 8–100x faster than `pip` (8x on Real Python benchmarks, 10x+ cold install on Hacker News tests)
- **Single tool replaces:** pip, pip-tools, pipx, virtualenv, pyenv, Poetry
- **85,000+ GitHub stars** as of 2026
- **~28M downloads/month**, ~13.3% of all PyPI downloads

### Key Commands

```bash
uv init project-name       # Initialize new project
uv add package-name        # Add dependency + create venv + generate uv.lock
uv sync                    # Sync environment from lockfile
uv run script.py           # Run script with PEP 723 inline metadata support
uv python install 3.13     # Manage Python versions
uvx tool-name              # Run CLI tools (pipx-style)
uv pip install -r requirements.txt  # Drop-in pip compatibility
```

### uv vs pip Comparison

| Capability | uv | pip + ecosystem |
|---|---|---|
| Implementation | Rust | Python |
| Install packages | Yes (`uv pip install` / `uv add`) | Yes |
| Create venvs | Built-in (`uv venv`) | Needs `venv`/`virtualenv` |
| Manage Python versions | Built-in (`uv python install`) | Needs `pyenv` |
| Universal lockfile | Yes (`uv.lock`, cross-platform) | Needs `pip-tools`/`Poetry` |
| Run CLI tools (pipx-style) | Yes (`uvx` / `uv tool`) | Needs `pipx` |
| Run PEP 723 scripts | Yes (`uv run script.py`) | No native support |
| Global cache + hardlinks | Yes (avoids disk duplication) | Wheel cache only |
| Speed | 8–100x faster | Baseline |

### Verdict for Python-projects

For a collection of standalone scripts, **uv** is ideal for:
- `uv run script.py` — auto-creates ephemeral env from inline deps
- `uv sync` — fast reproducible installs from `pyproject.toml`
- No manual virtualenv activation needed

---

## 3. Common Pitfalls & Beginner Mistakes

**Source:** [Medium — 15 Common Python Mistakes 2026](https://medium.com/@codepractice1922/stop-breaking-your-own-code-15-common-python-mistakes-beginners-must-avoid-in-2026-ee7968763b2b)

### Top 15 Mistakes to Avoid

| # | Mistake | Fix |
|---|---------|-----|
| 1 | **Mixing tabs & spaces** (IndentationError) | Configure IDE for 4-space indents consistently |
| 2 | **`is` vs `==` confusion** | Use `==` for value equality; `is` only for `None` checks |
| 3 | **Mutable default arguments** (`def f(x=[])`) | Use `None` as default, instantiate inside function |
| 4 | **Shadowing built-in names** (`list`, `str`, `dict`) | Never name variables after built-in functions |
| 5 | **Modifying list while iterating** | Use list comprehension to create filtered copy |
| 6 | **Scope misunderstanding** (NameError) | Understand local vs global; use `return` to pass values |
| 7 | **Bare excepts** (`except: pass`) | Always catch specific exceptions (`ValueError`, `KeyError`, etc.) |
| 8 | **Not writing Pythonic code** (C++/Java style loops) | `for item in my_list:` instead of `for i in range(len(my_list))` |
| 9 | **Not using `with open()`** | Always use `with open(...) as f:` for automatic cleanup |
| 10 | **NameError vs TypeError confusion** | NameError = undefined name; TypeError = unsupported operation |
| 11 | **Overcomplicating simple logic** | Use stdlib (`math`, `itertools`, `collections`) instead of reinventing |
| 12 | **Infinite loops** (`while True` without break) | Always ensure loop variable reaches exit condition |
| 13 | **Neglecting PEP 8** | Use Ruff formatter to auto-enforce style |
| 14 | **Hardcoding secrets** | Use environment variables + `.env` files |
| 15 | **Manual search when built-in exists** | Know stdlib — `str.find()`, `list.index()`, `sorted()` exist |

### Key Pythonic Patterns

```python
# ❌ Bad
for i in range(len(items)):
    print(items[i])

# ✅ Good
for item in items:
    print(item)

# ❌ Bad (mutable default)
def add_user(name, users=[]):
    users.append(name)
    return users

# ✅ Good
def add_user(name, users=None):
    if users is None:
        users = []
    users.append(name)
    return users
```

---

## 4. Security Best Practices

**Source:** [OpenSSF Secure Coding Guide for Python (pyscg)](https://openssf.org/blog/2026/05/12/secure-coding-guide-for-python-pyscg-first-release/)

### OpenSSF pyscg — First Comprehensive Python Security Guide (May 2026)

The OpenSSF released the **Secure Coding Guide for Python** (pyscg) with **50+ rules across 9 sections**, each with working compliant/noncompliant code examples. Covers CPython ≥ 3.9 + stdlib.

### Security Rule Categories

| Section | Topics | Key Rules |
|---------|--------|-----------|
| **01 Introduction** | Trust boundaries, credentials, operator precedence | No hardcoded creds, check access control server-side |
| **02 Encoding & Strings** | Locale, input canonicalization | Consistent encoding (UTF-8 everywhere) |
| **03 Numbers** | Float precision, integer wraparound, type conversion | Use `Decimal` for money; check bounds |
| **04 Neutralization** | Format strings, OS injection, SQL injection, deserialization, path traversal | **Never `shell=True`** in subprocess; use parameterized SQL; avoid `pickle` on untrusted data; sanitize filenames |
| **05 Exception Handling** | Specific exceptions, error propagation, cleanup | Catch specific types; use `finally` for cleanup |
| **06 Logging** | Sensitive data, security events, log neutralization | Never log passwords/tokens; sanitize log output |
| **07 Concurrency** | Resource consumption, deadlocks, race conditions | Use locks properly; avoid shared mutable state |
| **08 Coding Standards** | Mutable iteration, built-in redefinition, assertions | Don't modify iterated collection; don't shadow builtins |
| **09 Cryptography** | Random values | Use `secrets` module, not `random`, for security |

### Critical Security Rules for Python-projects

1. **No OS command injection** — Never pass user input to `subprocess` with `shell=True`
   ```python
   # ❌ Vulnerable
   subprocess.run(f"echo {user_input}", shell=True)
   # ✅ Safe
   subprocess.run(["echo", user_input])
   ```

2. **No hardcoded secrets** — Use `os.environ.get()` or `python-dotenv`

3. **Set `requests` timeout** — Always set `timeout=` to prevent hanging
   ```python
   requests.get(url, timeout=10)
   ```

4. **Pin dependency versions** — Prevent supply chain attacks via unpinned ranges

5. **Validate inputs** — Especially for web scraping and QR code data

6. **Use Bandit for automated scanning**
   ```bash
   pip install bandit
   bandit -r .
   ```

7. **Use `pip-audit`** for dependency vulnerability scanning
   ```bash
   pip install pip-audit
   pip-audit
   ```

### Bandit + pip-audit for CI

```bash
# In CI pipeline
bandit -r src/ -f json -o bandit-report.json
pip-audit --desc on --strict
```

---

## 5. Performance Optimization

**Sources:** Multiple web results compiled 2026-07

### Python Version Performance

| Version | Key Performance Feature | Impact |
|---------|------------------------|--------|
| **Python 3.12** | PEP 709 comprehension inlining | ~2× faster comprehensions |
| **Python 3.13** | JIT compiler (experimental) | ~30% improvement for CPU-bound |
| **Python 3.14** (Apr 2026) | JIT stable, f-string debug, tail-call opt | Production-ready JIT |

### Script-Level Optimization

| Technique | Details |
|-----------|---------|
| **List comprehensions** | 2–3× faster than manual `for` loops with `.append()` |
| **Built-in functions** | `map()`, `filter()`, `sum()`, `sorted()` run in C — much faster |
| **`lxml` parser for BeautifulSoup** | 10–20× faster than `html.parser` |
| **Set membership tests** | `x in set` is O(1) vs `x in list` is O(n) |
| **`functools.lru_cache`** | Memoize expensive pure functions |
| **Use `pathlib`** | Faster and more portable than `os.path` string manipulation |
| **Generator expressions** | Memory-efficient for large iterables — `(x for x in range(1_000_000))` |
| **`__slots__` in classes** | Reduces memory overhead for many instances |
| **OpenCV GPU acceleration** | CUDA backend if available for vision tasks |

### uv Speed Advantage

- uv installs dependencies **8–100× faster** than pip
- Global cache via hardlinks avoids re-downloading across projects
- Cold CI runner: pip = 38s, uv = 3s (Hacker News benchmark)
- For Python-projects with many dependencies (opencv-python, matplotlib, etc.), `uv sync` saves minutes

### Quick Wins for Python-projects Scripts

```python
# ❌ Slow
result = []
for i in range(len(data)):
    result.append(transform(data[i]))

# ✅ Fast (list comprehension)
result = [transform(x) for x in data]

# ❌ Slow (BeautifulSoup with html.parser)
soup = BeautifulSoup(html, "html.parser")

# ✅ Fast (lxml parser)
soup = BeautifulSoup(html, "lxml")
```

---

## 6. Type Hints & Static Analysis

**Sources:** [Real Python — type checking](https://realpython.com/ref/best-practices/type-checking), [OneUptime — Type Hints Guide](https://oneuptime.com/blog/post/2026-01-22-type-hints-python/view)

### Why Type Hints?

- **Catch bugs at analysis time** — before running code
- **Better IDE support** — autocomplete, refactoring, inline docs
- **Self-documenting code** — function signatures express contracts
- **Industry standard** — expected for professional Python in 2026

### Basic Type Hint Patterns

```python
def add(a: int, b: int) -> int:
    return a + b

def process_names(names: list[str]) -> dict[str, int]:
    """Count occurrences of each name."""
    return {name: names.count(name) for name in set(names)}

# Python 3.10+ union syntax
def process_id(id: int | str) -> str:
    return str(id)

# Optional (str | None)
def find_user(user_id: int | None = None) -> str | None:
    ...
```

### mypy Configuration

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.13"
strict = true
ignore_missing_imports = true  # For scripts without stubs
disallow_untyped_defs = true   # Require type annotations on all functions
```

### Type Hint Best Practices

| Rule | Reason |
|------|--------|
| Add types to **all public functions** | Documents contract for consumers |
| Use `list[str]` not `typing.List[str]` (Python 3.9+) | Simpler syntax |
| Use `|` for unions (Python 3.10+) | `str \| int` vs `Union[str, int]` |
| Use `Any` sparingly | Opt-out of type checking |
| **Don't overdo** — small scripts don't need full typing | Pragmatic balance |
| Use `@dataclass` for structured data | Automatic `__init__`, `__repr__`, type-safe |

---

## 7. Ruff Linter & Formatter Configuration

**Source:** [Astral — Ruff Configuration Docs](https://docs.astral.sh/ruff/configuration/)

### Why Ruff?

- **Supersedes** flake8 + isort + pycodestyle + pyupgrade + Black
- **Written in Rust** — 10–100× faster than traditional linters
- **Single `pyproject.toml` config** for all linting + formatting
- **Auto-fix** support for many rules
- **85K+ GitHub stars**, maintained by Astral (same team as uv)

### Recommended Configuration for Python-projects

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
target-version = "py313"

[tool.ruff.lint]
select = [
    "E4", "E7", "E9", "F",   # Default (pyflakes + pycodestyle)
    "B",                      # flake8-bugbear
    "I",                      # isort
    "N",                      # naming conventions
    "UP",                     # pyupgrade
    "RUF",                    # Ruff-specific
    "W",                      # pycodestyle warnings
    "ERA",                    # eradicate (commented-out code)
    "LOG",                    # flake8-logging
    "ARG",                    # unused arguments
]
ignore = ["E501"]  # Let formatter handle line length

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "auto"
docstring-code-format = true
```

### Common Commands

```bash
ruff check .                  # Lint all files
ruff check . --fix            # Auto-fix what's possible
ruff format .                 # Format all files
ruff check --watch .          # Watch mode for dev
```

### Rules to Enable for Beginners

| Code | Rule Set | What It Catches |
|------|----------|-----------------|
| `F` | Pyflakes | Undefined names, unused imports |
| `E`/`W` | pycodestyle | PEP 8 violations |
| `B` | flake8-bugbear | Mutable defaults, `is` with literals |
| `I` | isort | Import ordering |
| `UP` | pyupgrade | Modernize syntax (e.g., f-strings) |
| `N` | Naming | PEP 8 naming conventions |
| `ERA` | eradicate | Leftover commented-out code |

---

## 8. Testing with pytest

**Source:** [QASkills — Pytest Best Practices 2026](https://qaskills.sh/blog/pytest-best-practices-2026)

### Recommended Layout

```
my_project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── conftest.py
│   ├── test_calculator.py
│   └── integration/
│       └── test_api.py
├── pyproject.toml
└── README.md
```

### pytest Configuration (pyproject.toml)

```toml
[tool.pytest.ini_options]
minversion = "8.0"
testpaths = ["tests"]
addopts = [
    "-ra",                  # Show summary of non-passing tests
    "--strict-markers",     # Error on unregistered markers
    "--strict-config",      # Error on unknown config keys
    "--import-mode=importlib",
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests requiring external services",
    "smoke: critical-path smoke tests",
]
```

### Fixture Best Practices

```python
# tests/conftest.py
import pytest
from my_package.calculator import Calculator

@pytest.fixture
def calculator():
    """A fresh Calculator instance for each test."""
    return Calculator()

@pytest.fixture(scope="session")
def app_config():
    """Expensive config loaded once per test session."""
    return {"env": "test", "timeout": 5}
```

### Fixture Scopes

| Scope | Runs | Use Case |
|-------|------|----------|
| `function` (default) | Once per test | Cheap, mutable, isolated objects |
| `class` | Once per class | Shared state across class methods |
| `module` | Once per file | Module-level resources |
| `session` | Once per run | Expensive read-only (DB engine, config) |

### Parametrize Tests

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
    ids=["positives", "mixed-signs", "zeros"],
)
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
```

### Essential Plugins

```bash
pip install pytest-cov pytest-xdist pytest-mock
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = "--cov=src/ --cov-report=term-missing -n auto"
```

### Arrange-Act-Assert Pattern

```python
def test_apply_discount():
    # Arrange
    cart = Cart(items=[Item(price=100), Item(price=50)])
    coupon = Coupon(percent=10)

    # Act
    total = cart.apply_coupon(coupon).total()

    # Assert
    assert total == 135
```

### Applying to Python-projects

Even for standalone scripts, pytest is valuable:
- Test calculators, QR generation, web scraping output
- Use `pytest-mock` to mock `requests` for web scraper tests
- Use `tmp_path` fixture for file-based script tests
- Start with `tests/test_*.py` and grow gradually

---

## 9. Python Version Guidance (2026)

**Source:** Python.org, PEP changelogs, community benchmarks

| Version | Release | EOL | Highlights |
|---------|---------|-----|------------|
| **3.12** | Oct 2023 | Oct 2028 | PEP 709 (comprehension inlining), f-strings unleashed, security-only now |
| **3.13** | Oct 2024 | Oct 2029 | **JIT compiler** (experimental), free-threaded Python (no-GIL), improved error messages |
| **3.14** | Apr 2026 | ~2031 | **Production JIT**, f-string debug `f"{x=}"`, tail-call optimization |
| **3.15** | Jun 2026 (beta) | ~2031 | Next annual release |

### Recommendation for Python-projects

- **Primary target:** Python 3.13 — JIT performance boost, modern syntax
- **Compatibility floor:** Python 3.12 — ensures wide compat with library ecosystem
- **Use `uv python pin`** to lock project Python version
- **Test on 3.13** for JIT speedups on CPU-bound scripts

---

## 10. Cheatsheets & Quick Reference

### Essential Python Commands

```bash
# uv (preferred package manager)
uv init                    # Initialize project
uv add requests            # Add dependency
uv sync                    # Sync from lockfile
uv run script.py           # Run with auto venv
uv python list             # List managed Python versions

# Ruff (linter + formatter)
ruff check .               # Lint all files
ruff check . --fix         # Auto-fix
ruff format .              # Format all files

# mypy (type checking)
mypy .                     # Type check all files
mypy --strict .            # Strict mode

# Testing
pytest                     # Run all tests
pytest -v                  # Verbose
pytest -k "test_name"      # Filter by name
pytest -m "not slow"       # Skip slow tests
pytest --cov=src/          # Coverage report

# Security
bandit -r .                # Static security scan
pip-audit                  # Dependency vulnerability scan
```

### Quick Links

| Topic | URL |
|-------|-----|
| Python 3.13 docs | <https://docs.python.org/3.13/> |
| uv documentation | <https://docs.astral.sh/uv/> |
| Ruff documentation | <https://docs.astral.sh/ruff/> |
| pytest docs | <https://docs.pytest.org/> |
| mypy docs | <https://mypy-lang.org/> |
| OpenSSF Secure Coding Guide for Python | <https://best.openssf.org/Secure-Coding-Guide-for-Python/> |
| PEP 723 (inline script metadata) | <https://peps.python.org/pep-0723/> |
| Real Python | <https://realpython.com/> |
| Bandit security linter | <https://bandit.readthedocs.io/> |

---

## 11. Resources & Further Reading

### Best Practices
- [Real Python — Python Best Practices](https://realpython.com/tutorials/best-practices/)
- [Real Python — Project Layout](https://realpython.com/ref/best-practices/project-layout/)
- [Real Python — Type Checking](https://realpython.com/ref/best-practices/type-checking/)

### Performance
- [Python 3.13 What's New (JIT)](https://docs.python.org/3.13/whatsnew/3.13.html)
- [PEP 709 — Comprehension Inlining](https://peps.python.org/pep-0709/)
- [Real Python — uv vs pip benchmarks](https://realpython.com/uv-vs-pip/)

### Security
- [OpenSSF Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [Bandit — Python Security Linter](https://bandit.readthedocs.io/)

### Testing
- [QASkills — Pytest Best Practices 2026](https://qaskills.sh/blog/pytest-best-practices-2026)
- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)

### Tooling
- [uv GitHub](https://github.com/astral-sh/uv)
- [Ruff GitHub](https://github.com/astral-sh/ruff)
- [mypy documentation](https://mypy.readthedocs.io/)

---

## Research Methodology

- **Web search:** 7 targeted searches covering best practices, pitfalls, security, performance, uv/package management, Ruff configuration, pytest, and type hints
- **Content extraction:** Full-text extraction from Real Python, OpenSSF blog (pyscg release), Datacamp (uv guide), Tech Insider (uv vs pip benchmarks), QASkills (pytest guide), Astral docs (Ruff config), and Medium (common mistakes)
- **Tooling tested:** uv, Ruff, mypy, pytest, Bandit — all verified as current 2026 production-ready tools
- **Cross-reference:** Findings supplemented existing RESEARCH_REPORT.md with deeper dives and updated benchmarks
- **Last verified:** 2026-07-16
