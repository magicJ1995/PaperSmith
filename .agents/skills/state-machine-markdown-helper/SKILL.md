---
name: state-machine-markdown-helper
description: Use for high-risk sections where context isolation and careful progression matter. Not suitable when: Do not rely on hidden state or automatic paper-structure tools. File changes: conditional. Default output: reviews/state_machine_draft_plan.md or approved edits to paper.md.
---

# state-machine-markdown-helper

## Purpose

Run strict step-by-step section drafting with explicit evidence checks and confirmation gates.

## When to Use

Use for high-risk sections where context isolation and careful progression matter.

## When Not to Use

Do not rely on hidden state or automatic paper-structure tools.

## Inputs

PROJECT_CONTEXT.md, storyline.md, paper.md, writingrules.md, notes/, references/, outputs/

Always read AGENTS.md first. For paper projects, treat PROJECT_CONTEXT.md, storyline.md, paper.md, and writingrules.md as the source-of-truth files.

## Default Outputs

reviews/state_machine_draft_plan.md or approved edits to paper.md

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

- May modify paper.md: Only after an edit plan and explicit user confirmation.
- May modify storyline.md: No by default.
- Requires user confirmation before source edits: Yes.

## Safety Rules

- Do not fabricate experiments, results, datasets, baselines, citations, novelty, conclusions, or reviewer comments.
- Do not use legacy plugin commands, plugin tools, plugin-specific agents, UI status panels, or hidden workflow state.
- Do not write workflow state to JSON logs. Use local Markdown files in reviews/, notes/, references/, and outputs/.
- If the requested task depends on unavailable external files or unverified evidence, stop and ask for the missing material.

## Migration Note

This is a Codex-compatible migration of the CoPaper-style state-machine-markdown-helper skill. The original intent is preserved, but execution is local-file-driven and Markdown-based.
