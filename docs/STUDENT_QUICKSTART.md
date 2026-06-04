# Student Quickstart

This guide is for lab members using PaperSmith for the first time.

## 1. Create Your Own Paper Project

Do not write your paper inside:

```text
E:\ai\papersmith
```

That folder is the shared template kit. Each paper needs its own project folder.

If you can run Python:

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

If you cannot run Python:

1. Create a new paper folder, for example `E:\ai\papers\my-paper`.
2. Copy everything from `E:\ai\papersmith\templates\paper-project` into it.
3. Copy `E:\ai\papersmith\.agents\skills` into `E:\ai\papers\my-paper\.agents\skills`.

Your project should contain:

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

## 2. Files You Must Fill First

Start with `PROJECT_CONTEXT.md`. Fill as much as you know:

- paper title or working title;
- target venue if known;
- research problem;
- method idea;
- available experiments or planned experiments;
- datasets, baselines, and metrics if known;
- references already provided by you or your advisor;
- claims that are not yet supported.

Then work on `storyline.md`. Do not start drafting `paper.md` until the problem, insight, method, and evaluation plan are at least roughly filled.

Use `paper.md` only after Codex has enough project context.

## 3. Five Common Codex Prompts

### Fill project context

```text
Read AGENTS.md and PROJECT_CONTEXT.md. Ask me what verified information is missing. Do not invent anything.
```

### Check storyline

```text
Read AGENTS.md and .agents/skills/storyline-helper/SKILL.md. Check storyline.md section by section and write missing items to reviews/storyline_review.md. Do not modify storyline.md.
```

### Draft one section

```text
Read AGENTS.md and .agents/skills/paper-section-drafter/SKILL.md. Make an evidence inventory for Section 1.1 from PROJECT_CONTEXT.md and storyline.md. Then propose an edit plan before changing paper.md.
```

### Review a section

```text
Read .agents/skills/markdown-review/SKILL.md. Review the Introduction section of paper.md and write the report to reviews/introduction_review.md. This is review-only; do not edit paper.md.
```

### Plan Related Work

```text
Read .agents/skills/relatedwork-writer/SKILL.md. Use references/ and notes/ to build notes/relatedwork_taxonomy.md and reviews/relatedwork_draft_plan.md. Do not edit paper.md yet and do not invent citations.
```

### Revise from review

```text
Read .agents/skills/review-revise/SKILL.md. Use reviews/introduction_review.md to create reviews/revise_plan.md. Handle one issue at a time and wait for my confirmation before editing paper.md.
```

## 4. What Codex Must Not Do

Do not ask Codex to:

- invent experiments, numbers, figures, tables, datasets, baselines, citations, novelty, or conclusions;
- write a full paper in one pass;
- modify `paper.md` or `storyline.md` without an edit plan and your confirmation;
- treat `TODO` sections as content it can freely fill;
- use high-risk skills as automatic writing tools.

High-risk skills are:

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

Use them only for planning, evidence checks, missing-input reports, or supervised local suggestions.

For Related Work:

- `relatedwork-finder` finds and registers literature.
- `relatedwork-summarizer` summarizes existing literature.
- `relatedwork-writer` organizes and drafts the Related Work section after references exist.

## 5. What to Send Maintainers When Something Breaks

Send these files or screenshots:

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- the relevant `.agents/skills/<skill-name>/SKILL.md`
- the review file in `reviews/` that shows the issue
- any terminal output from:

```powershell
python E:\ai\papersmith\scripts\check_project_structure.py <your-project-path>
python E:\ai\papersmith\scripts\check_skill_metadata.py <your-project-path>\.agents\skills
```

Do not send private data, unpublished experiment logs, or confidential references unless your advisor says it is OK.
