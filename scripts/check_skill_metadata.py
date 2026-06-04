#!/usr/bin/env python3
"""Check that each skill has name and description front matter."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FIELD_RE = re.compile(r"^(name|description):\s*(.+?)\s*$", re.MULTILINE)


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end]
    return {match.group(1): match.group(2) for match in FIELD_RE.finditer(block)}


def check_skills(root: Path) -> list[str]:
    errors: list[str] = []
    skill_files = sorted(root.rglob("SKILL.md"))
    if not skill_files:
        return [f"no SKILL.md files found under {root}"]

    for path in skill_files:
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        for field in ("name", "description"):
            if field not in meta or not meta[field].strip():
                errors.append(f"{path}: missing {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check skill metadata.")
    parser.add_argument("skills_dir", nargs="?", default=".agents/skills", help="Directory containing skills.")
    args = parser.parse_args()

    root = Path(args.skills_dir).resolve()
    errors = check_skills(root)
    if errors:
        print("Skill metadata check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill metadata check passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
