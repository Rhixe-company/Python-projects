#!/usr/bin/env python3
"""Run all Python-projects quality checks: ruff, mypy, and per-script smoke tests.

Usage:
    python scripts/quality_check.py [--fix] [--verbose]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = sorted(ROOT.glob("*.py"))


def run(cmd: list[str], label: str) -> tuple[int, str]:
    print(f"\n{'=' * 60}")
    print(f"[CHECK] {label}")
    print(f"{'=' * 60}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.stdout:
        print(result.stdout[:2000])
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr[:1000], file=sys.stderr)
        print(f"[FAIL] {label} (exit {result.returncode})")
    else:
        print(f"[PASS] {label}")
    return result.returncode, result.stdout + result.stderr


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fix", action="store_true", help="Apply auto-fixes")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    failures = []

    # 1. ruff check
    cmd = ["ruff", "check", "."]
    if args.fix:
        cmd.append("--fix")
    rc, _ = run(cmd, "ruff check")
    if rc != 0:
        failures.append("ruff check")

    # 2. ruff format
    cmd = ["ruff", "format", "--check", "."]
    if args.fix:
        cmd[2] = "--write"
    rc, _ = run(cmd, "ruff format")
    if rc != 0:
        failures.append("ruff format")

    # 3. mypy
    rc, _ = run(["mypy", "--ignore-missing-imports", "."], "mypy")
    if rc != 0:
        failures.append("mypy")

    # 4. per-script syntax check
    print(f"\n{'=' * 60}")
    print("[CHECK] Per-script syntax validation")
    print(f"{'=' * 60}")
    syntax_failures = []
    for script in SCRIPTS:
        if script.name == "quality_check.py":
            continue
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec")
            if args.verbose:
                print(f"  [OK] {script.name}")
        except SyntaxError as e:
            print(f"  [FAIL] {script.name}: {e}")
            syntax_failures.append(script.name)
    if syntax_failures:
        failures.append(f"syntax ({len(syntax_failures)} scripts)")
    else:
        print(f"  All {len(SCRIPTS)} scripts pass syntax check.")

    # Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    if failures:
        print(f"FAILURES ({len(failures)}):")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print("All checks passed ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
