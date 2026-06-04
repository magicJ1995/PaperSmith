---
name: data-checker
description: Use before submitting experiment sections or when checking for unsupported result claims. Not suitable when: Do not invent data or mark data as verified without source artifacts. File changes: no. Default output: reviews/data_review.md.
---

# data-checker

## Purpose

Check whether reported data, tables, figures, and claims are backed by user-provided artifacts.

## When to Use

Use before submitting experiment sections or when checking for unsupported result claims.

## When Not to Use

Do not invent data or mark data as verified without source artifacts.

## Inputs

PROJECT_CONTEXT.md, paper.md, notes/, outputs/

Always read AGENTS.md first. For paper projects, treat PROJECT_CONTEXT.md, storyline.md, paper.md, and writingrules.md as the source-of-truth files.

## Default Outputs

reviews/data_review.md

Review, checker, diagnosis, and readiness outputs must go under reviews/. Intermediate reasoning notes must go under notes/. Related-work materials must go under references/. Final deliverables must go under outputs/.

## Codex-Compatible Workflow

1. Read this SKILL.md before claiming to use the skill.
2. Read the relevant project files listed above.
3. Build an evidence inventory before drafting, revising, or judging claims.
4. If evidence is missing, use NEEDS_USER_EVIDENCE, CITATION_NEEDED, DATA_NEEDED, or BASELINE_NEEDED instead of inventing content.
5. For review-only, check-only, diagnose-only, or planning tasks, write a Markdown report to the default output path and do not modify paper.md or storyline.md.
6. Before modifying paper.md or storyline.md, provide an edit plan with target section, evidence used, proposed change, and risk; wait for explicit user confirmation.
7. After approved edits, recommend a targeted review report under reviews/.

## File Modification Policy

- May modify paper.md: No.
- May modify storyline.md: No by default.
- Requires user confirmation before source edits: Yes.

## Safety Rules

- Do not fabricate experiments, results, datasets, baselines, citations, novelty, conclusions, or reviewer comments.
- Do not use legacy plugin commands, plugin tools, plugin-specific agents, UI status panels, or hidden workflow state.
- Do not write workflow state to JSON logs. Use local Markdown files in reviews/, notes/, references/, and outputs/.
- If the requested task depends on unavailable external files or unverified evidence, stop and ask for the missing material.

## Migration Note

This is a Codex-compatible migration of the CoPaper-style data-checker skill. The original intent is preserved, but execution is local-file-driven and Markdown-based.
