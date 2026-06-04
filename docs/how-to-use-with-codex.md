# How to Use With Codex

The toolkit contains the full migrated CoPaper-style skill set. Skills are Markdown instructions, not plugin commands. Before using any skill, Codex should read `.agents/skills/<skill-name>/SKILL.md`.

All 32 skills have completed Codex Compatibility Mode internal testing. The toolkit is suitable for a limited 1 to 2 person lab trial. Every paper project must fill `PROJECT_CONTEXT.md` before drafting, review, revision, or high-risk skill use.

High-risk skills are `bogus-data-helper`, `humanizer`, `mad-writer`, and `state-machine-markdown-helper`. Use them only in planning/evidence-gating mode by default: they may produce plans, missing-evidence reports, questions, or review notes, but they must not generate fake data, draft a full paper, polish unsupported content, or modify `paper.md` without a confirmed edit plan.

When the right skill is unclear, ask Codex to read:

```text
docs/SKILL_INDEX.md
docs/SKILL_COMPATIBILITY_MATRIX.md
```

## Initialize a Paper Project

```text
Create a separate project folder for this paper. Do not write the paper inside E:\ai\papersmith. Run scripts/create_paper_project.py with --name "My Paper" and --target <target path>. Then check the new project structure.
```

If Python is unavailable:

```text
Manually copy templates/paper-project/ into a new paper folder, then copy .agents/skills/ into the new folder as .agents/skills/. Confirm that AGENTS.md, PROJECT_CONTEXT.md, storyline.md, paper.md, writingrules.md, workflow-dataflow.md, .agents/skills/, reviews/, notes/, references/, and outputs/ all exist.
```

## Fill PROJECT_CONTEXT.md

```text
Read AGENTS.md and PROJECT_CONTEXT.md. Ask me for missing verified facts needed to complete PROJECT_CONTEXT.md. Do not invent anything.
```

Use this as the first step for every paper project. If `PROJECT_CONTEXT.md` is still empty, Codex should report missing inputs before using writing, review, or high-risk skills.

## Choose a Skill

```text
Read AGENTS.md and docs/SKILL_INDEX.md. Recommend the best skill for this task. Then read the chosen .agents/skills/<skill-name>/SKILL.md before doing the work.
```

## Check storyline.md

```text
Read .agents/skills/storyline-helper/SKILL.md, then use the storyline-helper workflow. Review storyline.md against PROJECT_CONTEXT.md and write findings to reviews/storyline_review.md. Do not edit storyline.md yet. Empty TODO sections should be reported as missing user input.
```

## Draft paper.md Section by Section

```text
Read .agents/skills/paper-section-drafter/SKILL.md, then use paper-section-drafter. First make an evidence inventory for Section 1.1 from PROJECT_CONTEXT.md, storyline.md, notes/, references/, and outputs/. Propose a plan before editing paper.md. Use only provided facts and mark missing evidence.
```

## Review Introduction

```text
Read .agents/skills/markdown-review/SKILL.md, then use markdown-review. Review Section 1 of paper.md for problem clarity, motivation, novelty boundary, and claim-evidence consistency. Write the report to reviews/introduction_review.md. This is review-only; do not edit paper.md.
```

## Review Method

```text
Read .agents/skills/markdown-review/SKILL.md, then review Section 3 of paper.md for technical depth, design rationale, assumptions, and consistency with storyline.md. Write the report to reviews/method_review.md. Do not edit paper.md during review.
```

## Review Experiment

```text
Read .agents/skills/experiment-analyzer/SKILL.md and .agents/skills/markdown-review/SKILL.md. Map Section 4 claims to provided result files, baselines, metrics, and scripts. Write findings to reviews/experiment_review.md. Do not invent results.
```

## Revise From Reviewer Comments

```text
Read .agents/skills/review-revise/SKILL.md, then use review-revise. Read reviews/reviewer_comments.md and paper.md. Group comments by severity, create or update reviews/revise_plan.md, propose edits one issue at a time, and wait for approval before editing.
```

## Submission Precheck

```text
Read .agents/skills/submission-precheck/SKILL.md, then use submission-precheck. Check project structure first, including .agents/skills/. Then check paper.md, storyline.md, PROJECT_CONTEXT.md, references/, notes/, and reviews/. Write the report to reviews/submission_precheck.md.
```
