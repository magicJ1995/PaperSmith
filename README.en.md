<p align="center">
  <img src="PaperSmith.png" alt="PaperSmith logo" width="180">
</p>

<h1 align="center">PaperSmith</h1>

<p>
  <a href="README.md"><img src="https://img.shields.io/badge/CN-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%20%E9%BB%98%E8%AE%A4%E6%BA%90-8250df?style=flat-square&labelColor=343a40" alt="简体中文 默认源"></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/US-English%20View-111111?style=flat-square&labelColor=343a40" alt="English View"></a>
</p>

PaperSmith is the lab's internal beta workflow kit for paper writing with Codex. You can think of it as a paper-project template plus Codex writing rules plus a set of paper-writing skills. It helps lab members organize, draft, review, and revise papers step by step.

### First-Time Use

Start here:

```text
docs/STUDENT_ONE_PAGE_GUIDE.md
```

For full step-by-step instructions, read:

```text
docs/COMPLETE_USER_MANUAL.md
```

For copyable prompts, read:

```text
docs/PROMPT_COOKBOOK.md
```

### Important Rule

Do not write papers inside the template kit directory:

```text
E:\ai\papersmith
```

Each paper must have its own project folder. Create one with:

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

After creating the project, open Codex in the new paper project folder:

```text
E:\ai\papers\my-paper
```

Do not open Codex in `E:\ai\papersmith` when writing a paper.

### What This Kit Provides

- `templates/paper-project/`: the template copied for each paper.
- `.agents/skills/`: Codex-readable paper-writing skills.
- `scripts/create_paper_project.py`: create a new paper project.
- `scripts/check_project_structure.py`: check paper project structure.
- `scripts/check_skill_metadata.py`: check skill metadata.
- `AGENTS.md`: lab-level writing rules.
- `docs/`: student guides, complete manual, prompt cookbook, skill index, and compatibility notes.

### Basic Workflow

1. Create an independent paper project.
2. Fill `PROJECT_CONTEXT.md`.
3. Complete `storyline.md`.
4. Organize `references/`.
5. Draft `paper.md` section by section.
6. Write review reports to `reviews/`.
7. Revise issue by issue.
8. Run precheck before submission.
9. Put final exports in `outputs/`.

### What Codex Must Not Do

Do not ask Codex to invent:

- experiment results;
- citations, authors, years, venues, DOIs, or BibTeX;
- baselines or baseline results;
- datasets;
- novelty or contributions;
- conclusions not supported by project files.

`PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` are the source-of-truth files. When experiments, citations, or baselines are missing, Codex should mark `DATA_NEEDED`, `CITATION_NEEDED`, `BASELINE_NEEDED`, or `NEEDS_USER_EVIDENCE` instead of filling the gap.

### High-Risk Skills

The following skills should not be used directly by regular users by default:

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

They default to planning / evidence-gating mode only. Do not use them to generate fake data, strengthen unsupported claims, polish unsupported text into untraceable final prose, or draft an entire paper.

### If Something Breaks

Send these files to the maintainer:

```text
PROJECT_CONTEXT.md
storyline.md
paper.md
reviews/
AGENTS.md
.agents/skills/<problem-skill>/SKILL.md
```

Also include the prompt you gave Codex and any relevant terminal output.

### Directory Overview

```text
.agents/skills/              Reusable paper-writing skills
templates/paper-project/     Template copied for each paper
scripts/                     Project creation and validation scripts
examples/demo-paper-project/ Example paper project
docs/                        User and maintainer documentation
archive/                     Pre-release archived materials
```

### License

This kit is intended for internal lab beta use. See `LICENSE`.
