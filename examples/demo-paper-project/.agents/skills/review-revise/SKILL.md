---
name: review-revise
description: Use when the user wants to revise paper.md or storyline.md based on review reports, reviewer comments, or precheck findings. Do not use for freeform rewriting without an issue list and user-approved plan.
---

# Review Revise

## Purpose

Turn review findings into controlled, auditable revisions.

## Inputs

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- Relevant files in `reviews/`
- Relevant notes, references, and experiment outputs

## Workflow

1. Read the target review report.
2. Extract one concrete issue.
3. Judge whether enough evidence exists in `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `notes/`, `references/`, or `outputs/`.
4. If evidence is missing, write the blocker to `reviews/revise_plan.md` and do not edit.
5. If evidence exists, provide an edit plan that states:
   - target file and section;
   - current problem;
   - evidence to use;
   - proposed edit;
   - risk of changing the claim.
6. Wait for user approval before editing.
7. Apply only the approved edit.
8. Record unresolved issues in the review file or a follow-up report under `reviews/`.

## No Real Content, No Edit

If the target section is empty, template-only, `TODO`-only, or unsupported by project evidence:

- do not rewrite `paper.md` or `storyline.md`;
- create or update `reviews/revise_plan.md`;
- list the missing user inputs;
- explain why editing now would fabricate research content;
- stop until the user provides evidence and approves a concrete edit plan.

## Standard Revise Plan

Use `reviews/revise_plan.md` unless the user specifies another file.

```markdown
# Revise Plan

## Source Review

## Issue Queue

## Current Issue

## Evidence Check

## Proposed Edit Plan

## User Confirmation Needed

## Deferred or Blocked Issues
```

## Constraints

- Do not auto-apply all review comments.
- Do not change claims without checking `storyline.md` and `PROJECT_CONTEXT.md`.
- Do not invent missing evidence.
- Do not remove `CITATION_NEEDED`, `DATA_NEEDED`, or `BASELINE_NEEDED` unless evidence is provided.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
