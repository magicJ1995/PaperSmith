#!/usr/bin/env python3
"""Check that a paper project has the required PaperSmith structure."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
    "PROJECT_CONTEXT.md",
    "storyline.md",
    "paper.md",
    "writingrules.md",
]

REQUIRED_DIRS = [
    ".agents/skills",
    "reviews",
    "notes",
    "references",
    "outputs",
]


def check_project(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.is_file():
            errors.append(f"missing file: {rel}")
    for rel in REQUIRED_DIRS:
        path = root / rel
        if not path.is_dir():
            errors.append(f"missing directory: {rel}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check paper project structure.")
    parser.add_argument("project_dir", help="Paper project directory to check.")
    args = parser.parse_args()

    root = Path(args.project_dir).resolve()
    errors = check_project(root)
    if errors:
        print(f"Project structure check failed: {root}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Project structure check passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
