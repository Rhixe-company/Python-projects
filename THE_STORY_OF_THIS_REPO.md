# The Story of Python-projects

*The archive that taught us to script*

---

## Prologue: The Learning Repository

2023. A folder named `Python-projects`. No framework. No architecture. Just scripts.

Each file a tutorial completed. Each import a library learned.

```
basic_calculator.py          # Functions, loops, input validation
guess_the_number.py          # Random, while loops, conditionals
qr_code_generator.py         # pillow, qrcode, CLI args
face_detection.py            # opencv-python, haar cascades
web_scraper.py               # requests, beautifulsoup4, ethics
```

---

## Chapter 1: The Standalone Principle

**Rule:** No shared code between scripts.

`web_scraper.py` imports `requests` and `bs4`. `face_detection.py` imports `cv2`. They don't share a `utils.py`. They don't share a `config.py`.

**Why?** Each script is a complete lesson. Copy-paste into a new project, it runs. No dependency graph to untangle.

---

## Chapter 2: The Dependency Reality

`requirements.txt` grew:

```
requests==2.32.3
beautifulsoup4==4.12.3
opencv-python==4.11.0.86
matplotlib==3.10.1
pillow==11.1.0
qrcode==8.2
PyDictionary==2.0.1
schedule==1.2.2
```

`opencv-python` needs system libraries (`libglib2.0`, `libsm6`, `libxext6`). On Windows, it usually works. On Linux CI, it fails without `apt-get install`.

**Lesson:** Document system dependencies. Or use `opencv-python-headless`.

---

## Chapter 3: Quality Without Tests

No `pytest`. No `unittest`. The "test" is running the script and seeing output.

```bash
python qr_code_generator.py "https://github.com" output.png
# → output.png exists, scans correctly
```

`ruff check .` catches style. `mypy *.py` catches types (where annotated).

**Lesson:** For scripts, linting > testing. The script *is* the test.

---

## Chapter 4: The Archive Decision

July 2025. The workspace chronicler reviews 17 projects.

| Project | Status |
|---------|--------|
| `comicwise` | Active (Next.js) |
| `rhixe_scans` | Active (Next.js) |
| `university-libary-jsm` | Active (Next.js) |
| `Python-projects` | **Archive** |

**Why archive?**
- No active development in 12 months
- Served its purpose (learning)
- Clutters workspace inventory
- `opencv-python` drags down dependency audits

**How to archive:**
1. Move to `archive/Python-projects/`
2. Remove from `pr-ci.yml` matrix
3. Keep `README.md` at root referencing it
4. `git tag archive/python-projects-2025`

---

## Chapter 5: What Remains

The scripts still run. The lessons still apply.

A new hire wants to learn web scraping? `web_scraper.py` — 50 lines, commented, ethical.

A designer needs QR codes? `qr_code_generator.py` — CLI, batch mode, logo embedding.

The folder is frozen. But not dead.

---

## Epilogue: The Next Beginner

Someone will clone this repo. They'll run `python basic_calculator.py`. They'll break it. They'll fix it. They'll learn.

That's the only metric that matters.

---

*Written by the workspace chronicler, July 25, 2025.  
Filed at `projects/Python-projects/THE_STORY_OF_THIS_REPO.md`.*