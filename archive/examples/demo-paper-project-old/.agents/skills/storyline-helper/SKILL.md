---
name: storyline-helper
description: Use when the user wants to build, inspect, or refine storyline.md section by section from provided research material. Do not use for inventing a new research idea, adding unsupported novelty, or rewriting paper.md directly.
---

# Storyline Helper

## Purpose

Help the researcher express the paper's research logic in `storyline.md` without inventing content.

## Inputs

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- Optional notes in `notes/`
- Optional references in `references/`

## Workflow

1. Read `AGENTS.md` and `PROJECT_CONTEXT.md`.
2. Inspect the relevant `storyline.md` section.
3. Identify missing evidence, unclear assumptions, and unsupported claims.
4. Present a section-level edit plan before changing `storyline.md`.
5. After approval, edit only the targeted section.
6. Mark unresolved items with `NEEDS_USER_EVIDENCE`, `CITATION_NEEDED`, or `DATA_NEEDED`.

## Empty/TODO Section Checklist

When checking `storyline.md`, inspect each substantive section for:

- empty body text;
- `TODO`;
- placeholder wording;
- missing problem statement;
- missing importance evidence;
- missing background assumptions;
- missing related method families;
- missing shared limitation;
- missing core insight;
- missing validity conditions;
- missing method overview;
- missing technical challenges;
- missing research questions;
- missing baselines, metrics, datasets, or workloads;
- missing contribution boundaries.

If `storyline.md` is still an empty template, do not complete it. Report the missing sections and ask the user for the required research material.

## Review Output

When asked to check rather than edit, write findings to `reviews/storyline_review.md` or another user-specified file under `reviews/`.

Use this structure:

```markdown
# Storyline Review

## Summary

## Empty or TODO Sections

## Missing User Inputs

## Unsupported or Unclear Claims

## Suggested Fill Order
```

## Constraints

- Do not create new research contributions.
- Do not invent problem statements, insights, methods, experiments, citations, or contribution claims.
- Do not strengthen claims beyond project evidence.
- Do not silently rewrite multiple sections.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
