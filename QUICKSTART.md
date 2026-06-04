# Quickstart

This guide is for lab members who want to start a new paper project. You do not need to know CoPaper or OpenCode.

## Important Rule

Do not write a paper directly inside `E:\ai\papersmith`. That folder is the shared template kit.

Each paper should have its own project folder, for example:

```text
E:\ai\papers\my-paper
```

The recommended order is:

```text
create project -> fill PROJECT_CONTEXT.md -> complete storyline.md -> draft paper.md
```

This kit now includes the full migrated CoPaper-style skill set, not only the first core skills. To choose a skill, read:

```text
E:\ai\papersmith\docs\SKILL_INDEX.md
E:\ai\papersmith\docs\SKILL_COMPATIBILITY_MATRIX.md
```

The current version has completed Codex Compatibility Mode testing for all 32 skills. It is ready for a small trial with 1 to 2 lab members. During trial use, keep a senior reviewer in the loop for high-risk skills.

High-risk skills:

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

By default, high-risk skills may only be used in planning/evidence-gating mode. They should produce plans, missing-evidence lists, review notes, or questions. They should not generate fake data, draft a full paper, polish unsupported content, or modify `paper.md` without an approved edit plan.

## Option A: Initialize With Python

Use this if you can run Python.

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

This copies:

- `templates/paper-project/` into the target project;
- `.agents/skills/` into the target project's `.agents/skills/`;
- required folders such as `reviews/`, `notes/`, `references/`, and `outputs/`.

Then check the project:

```powershell
python E:\ai\papersmith\scripts\check_project_structure.py E:\ai\papers\my-paper
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papers\my-paper\.agents\skills
```

## Option B: Manual Copy Fallback

Use this if Python is unavailable.

1. Create a new folder for the paper, such as:

```text
E:\ai\papers\my-paper
```

2. Copy everything from:

```text
E:\ai\papersmith\templates\paper-project
```

into the new paper folder.

3. Create this folder inside the new paper project:

```text
E:\ai\papers\my-paper\.agents
```

4. Copy the entire skills folder:

```text
E:\ai\papersmith\.agents\skills
```

to:

```text
E:\ai\papers\my-paper\.agents\skills
```

5. Confirm the new project contains:

```text
AGENTS.md
PROJECT_CONTEXT.md
storyline.md
paper.md
writingrules.md
workflow-dataflow.md
.agents/skills/
reviews/
notes/
references/
outputs/
```

If `.agents/skills/` is missing, the project setup is incomplete.

## 1. Fill PROJECT_CONTEXT.md

Before asking an agent to write, review, revise, or choose a high-risk skill, fill `PROJECT_CONTEXT.md` with verified facts:

- project title;
- target venue;
- authors;
- research problem;
- current method;
- available experiments;
- known baselines;
- provided references.

Do not leave critical facts only in chat. Put them in project files.

## 2. Build Storyline

Ask Codex:

```text
Read AGENTS.md and .agents/skills/storyline-helper/SKILL.md. Help me check storyline.md section by section. Do not invent content. Mark missing evidence clearly.
```

If you are not sure which skill is appropriate, ask:

```text
Read AGENTS.md and docs/SKILL_INDEX.md. Recommend the right skill for my task, then read that skill's SKILL.md before proceeding.
```

## 3. Draft the Paper

Ask Codex:

```text
Read AGENTS.md and .agents/skills/paper-section-drafter/SKILL.md. Before drafting the Introduction, make an evidence inventory from PROJECT_CONTEXT.md and storyline.md. Then propose an edit plan using only provided facts.
```

Approve the plan before edits.

## 4. Review and Revise

Ask Codex:

```text
Read .agents/skills/markdown-review/SKILL.md. Review the Introduction section and write the report to reviews/introduction_review.md. This is review-only; do not edit paper.md.
```

Then:

```text
Read .agents/skills/review-revise/SKILL.md. Use reviews/introduction_review.md to create reviews/revise_plan.md. Address one issue at a time and wait for confirmation before editing paper.md.
```

## 5. Check Before Submission

Ask Codex:

```text
Read .agents/skills/submission-precheck/SKILL.md. Check project structure first, then paper readiness. Write the report to reviews/submission_precheck.md.
```
