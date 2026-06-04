---
name: paper-section-drafter
description: Use when the user wants to draft or polish one section of paper.md from PROJECT_CONTEXT.md, storyline.md, notes, references, and verified experiment material. Do not use for full-paper one-shot writing or unsupported claims.
---

# Paper Section Drafter

## Purpose

Draft or polish `paper.md` one section at a time while preserving the research logic in `storyline.md`.

## Inputs

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `writingrules.md`
- Relevant files from `notes/`, `references/`, or `outputs/`

## Workflow

1. Read the project rules and the target section.
2. Create an evidence inventory before drafting.
3. State the section goal and evidence to be used.
4. Present a modification plan before editing `paper.md`.
5. Draft only the approved section or subsection.
6. Use labels for missing support:
   - `CITATION_NEEDED`
   - `DATA_NEEDED`
   - `BASELINE_NEEDED`
   - `NEEDS_USER_EVIDENCE`
7. After editing, recommend a `markdown-review` pass for the changed section.

## Evidence Inventory

Before drafting, list what is known and what is missing:

- known research problem;
- known method;
- known datasets or workloads;
- known experiment results;
- known baselines;
- known limitations;
- known citations;
- known contribution boundaries.

If an item is missing, mark it explicitly with:

- `DATA_NEEDED` for missing data, result values, tables, figures, or experimental evidence;
- `CITATION_NEEDED` for unsupported literature or background claims;
- `BASELINE_NEEDED` for missing comparison methods;
- `NEEDS_USER_EVIDENCE` for any claim that cannot be verified from project files.

If the evidence inventory is too sparse to draft responsibly, stop and ask for user input instead of writing speculative content.

## Style Rules

- Keep claims specific and evidence-backed.
- Avoid promotional language.
- Do not claim "first", "state-of-the-art", or "significant improvement" unless verified.
- Preserve uncertainty when evidence is incomplete.

## Constraints

- Do not write the whole paper in one pass.
- Do not invent citations, baselines, experiments, datasets, or numbers.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
