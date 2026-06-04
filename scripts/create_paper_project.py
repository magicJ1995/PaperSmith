#!/usr/bin/env python3
"""Create a paper project from the PaperSmith template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PROTECTED_FILES = {"paper.md", "storyline.md", "PROJECT_CONTEXT.md"}
REQUIRED_DIRS = ["reviews", "notes", "references", "outputs", ".agents", ".agents/skills"]


def kit_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_tree_contents(src: Path, dst: Path, *, force: bool) -> None:
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue

        if target.exists() and rel.name in PROTECTED_FILES and not force:
            print(f"skip protected existing file: {target}")
            continue

        if target.exists() and not force:
            print(f"skip existing file: {target}")
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)


def create_project(name: str, target: Path, *, force: bool) -> None:
    root = kit_root()
    template = root / "templates" / "paper-project"
    skills = root / ".agents" / "skills"

    if not template.exists():
        raise FileNotFoundError(f"template not found: {template}")
    if not skills.exists():
        raise FileNotFoundError(f"skills not found: {skills}")

    context_existed = (target / "PROJECT_CONTEXT.md").exists()

    target.mkdir(parents=True, exist_ok=True)
    copy_tree_contents(template, target, force=force)

    target_skills = target / ".agents" / "skills"
    copy_tree_contents(skills, target_skills, force=force)

    for rel in REQUIRED_DIRS:
        (target / rel).mkdir(parents=True, exist_ok=True)

    context = target / "PROJECT_CONTEXT.md"
    if context.exists() and (force or not context_existed):
        text = context.read_text(encoding="utf-8")
        text = text.replace("- Project name: TODO", f"- Project name: {name}")
        context.write_text(text, encoding="utf-8", newline="\n")

    print(f"created paper project: {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a paper project from PaperSmith.")
    parser.add_argument("--name", required=True, help="Project name written into PROJECT_CONTEXT.md when possible.")
    parser.add_argument("--target", required=True, help="Target project directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files, including protected files.")
    args = parser.parse_args()

    create_project(args.name, Path(args.target).resolve(), force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
