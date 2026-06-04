---
name: experiment-analyzer
description: Use when the user wants to analyze provided experiment code, logs, tables, figures, or protocols and map them to paper claims. Do not use to generate fake numbers, baselines, or conclusions.
---

# Experiment Analyzer

## Purpose

Connect experiment artifacts to the claims in `storyline.md` and `paper.md`.

## Inputs

- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- Experiment notes in `notes/`
- Result files, tables, figures, logs, or scripts provided by the user

## Workflow

1. Identify the research questions and claims that need evidence.
2. Inventory available experiment artifacts.
3. Map each result to:
   - research question;
   - dataset/workload;
   - baseline;
   - metric;
   - figure/table;
   - claim supported;
   - limitations.
4. Write analysis to `reviews/experiment-analysis.md` unless the user specifies another file.
5. Flag gaps with `DATA_NEEDED`, `BASELINE_NEEDED`, or `NEEDS_USER_EVIDENCE`.

## Constraints

- Do not fabricate numbers or trends.
- Do not infer statistical significance without analysis.
- Do not add experimental conclusions to `paper.md` before proposing a revision plan.
- Do not use legacy plugin commands, plugin tools, UI status panels, or hidden workflow state.
