---
name: submission-precheck
description: Use when the user wants a final readiness check before submission, internal review, or export. Writes a precheck report to reviews/. Do not use to silently fix the paper or bypass missing evidence.
---

# Submission Precheck

## Purpose

Run a final paper-readiness check and produce a durable report.

## Inputs

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `writingrules.md`
- `references/`
- `notes/`
- prior reports in `reviews/`
- deliverables in `outputs/`

## Checks

First check project structure. Only proceed to content maturity checks if setup is valid.

### Project Structure Checklist

Required files:

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `writingrules.md`
- `workflow-dataflow.md`

Required directories:

- `.agents/skills/`
- `reviews/`
- `notes/`
- `references/`
- `outputs/`

If `.agents/skills/` is missing, report a setup error and stop before content-readiness review.

### Content Maturity Checklist

1. Project context is complete enough for submission.
2. Storyline and paper claims are consistent.
3. Citations are present for all literature claims.
4. Figures and tables are referenced and supported.
5. Baselines, datasets, workloads, and metrics are defined.
6. Results in the paper match provided experiment artifacts.
7. Limitations and threats are stated honestly.
8. No unresolved `CITATION_NEEDED`, `DATA_NEEDED`, `BASELINE_NEEDED`, or `NEEDS_USER_EVIDENCE` remains without explanation.
9. Reviewer comments and prior review findings are addressed or explicitly deferred.

## Output

Write the report to `reviews/submission_precheck.md` unless the user specifies another path.

## Constraints

- Do not modify `paper.md` during precheck.
- Do not mark the paper ready if evidence is missing.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
