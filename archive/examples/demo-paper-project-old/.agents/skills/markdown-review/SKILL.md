---
name: markdown-review
description: Use when the user wants a structured review of paper.md, storyline.md, or a specific section. Writes findings to reviews/. Do not use to directly edit the paper unless followed by review-revise and user approval.
---

# Markdown Review

## Purpose

Produce a durable review report that identifies paper risks before revision.

## Inputs

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `writingrules.md`
- Relevant notes, references, experiment outputs, and prior reviews

## Checker Dimensions

Review the requested scope using these dimensions:

1. Problem clarity and importance.
2. Novelty and differentiation from related work.
3. Technical depth and non-triviality.
4. Logic and claim-evidence consistency.
5. Clarity, definitions, and readability.
6. Evaluation protocol, baselines, metrics, and threats.
7. Data authenticity and reproducibility.

## Report Format

Write the report to `reviews/` with a stable filename. Recommended names:

- `reviews/introduction_review.md`
- `reviews/method_review.md`
- `reviews/experiment_review.md`
- `reviews/discussion_review.md`
- `reviews/related_work_review.md`
- `reviews/full_paper_review.md`

Use this structure:

```markdown
# Review: <scope>

## Summary

## Critical Issues

## Major Issues

## Minor Issues

## Missing Evidence

## Suggested Revision Order
```

Each issue should include:

- location;
- problem;
- why it matters;
- evidence needed;
- suggested repair path.

## Empty or Placeholder Sections

If the requested section contains only headings, `description` comments, `TODO`, or placeholder text:

1. State that there is no real prose or claim to review.
2. Do not invent content to make the review possible.
3. List the missing user inputs required for that section.
4. Write the review report under `reviews/`.
5. Do not modify `paper.md` or `storyline.md`.

## Introduction Review Template

For Introduction reviews, use this additional checklist:

```markdown
# Review: Introduction

## Summary

## Problem and Importance
- Is the concrete problem stated?
- Is importance supported by evidence or citations?

## Existing-Method Limitation
- Are prior method families identified?
- Is the shared limitation explained without exaggeration?

## Insight and Opportunity
- Is the core insight stated?
- Are validity conditions and boundaries clear?

## Approach and Contributions
- Is the method overview connected to the insight?
- Are contributions evidence-backed?

## Missing Evidence

## Suggested Revision Order
```

## Constraints

- Review-only tasks must not edit `paper.md` or `storyline.md`.
- Do not fabricate checker results.
- Do not infer facts not present in project files.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
