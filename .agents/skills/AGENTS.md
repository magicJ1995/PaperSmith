# AGENTS.md for Skills

## Overview

`.agents/skills/` is the reusable skill library for PaperSmith.

Each skill is a local workflow for a specific research-paper writing task, such as storyline checking, section drafting, related work planning, experiment analysis, review, revision, or export planning.

Before Codex claims to use a skill, it must first read the corresponding file:

```text
.agents/skills/<skill-name>/SKILL.md
```

Skills do not invent research content. They operate on local project files and user-provided evidence to plan, review, draft, revise, and check paper-writing work.

## Directory Structure

Each skill directory may contain:

- `SKILL.md`: required. Contains `name`, `description`, and concrete execution rules.
- `README.md`: optional. User-facing explanation for the skill.
- `scripts/`: optional. Helper scripts used by the skill.
- `template.md`: optional. Prompt, output, or report template.

## Required Metadata

Every `SKILL.md` must contain:

- `name`
- `description`

The `description` must explain:

- when to use the skill;
- when not to use the skill;
- default input files;
- default output locations;
- whether the skill may modify `paper.md` or `storyline.md`;
- whether user confirmation is required before edits.

## Codex Compatibility Rules

Skills in this directory must be Codex-compatible and local Markdown driven.

Rules:

- Do not use the OpenCode plugin.
- Do not use `/copaper` commands.
- Do not call `copaper_*` tools.
- Do not depend on `.agents/state.json` or `.agents/events.jsonl`.
- Base all work on local Markdown files.
- Treat `PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` as primary source-of-truth files.
- Treat `writingrules.md` as the writing-rule source.
- Store literature materials in `references/`.
- Store intermediate analysis in `notes/`.
- Store reviews, checks, plans, and gap reports in `reviews/`.
- Store final or export outputs in `outputs/`.

Historical CoPaper/OpenCode terminology may appear only as context. It must be translated into local Markdown operations before execution.

## Safety Rules

Skills must not fabricate:

- experiment results;
- datasets;
- baselines;
- citations;
- novelty;
- conclusions;
- claims beyond what `PROJECT_CONTEXT.md` supports.

When information is missing, use explicit markers instead of guessing:

- `DATA_NEEDED`
- `CITATION_NEEDED`
- `BASELINE_NEEDED`
- `NEEDS_USER_EVIDENCE`
- `UNCLEAR_ASSUMPTION`

## Source Editing Rules

Review-only, check-only, and diagnose-only tasks must not modify `paper.md` or `storyline.md`.

Before modifying `paper.md` or `storyline.md`, Codex must:

1. Provide an edit plan.
2. Identify the target section.
3. Identify the evidence to use.
4. State any risk of changing the claim.
5. Wait for explicit user confirmation.

When editing is approved:

- modify only the specified section;
- do not modify unrelated sections;
- preserve user-provided technical facts unless the user confirms they are wrong;
- output a concise change summary after editing.

## Output Location Rules

Use stable local files for outputs:

- review/checker reports: `reviews/`
- evidence inventory: `reviews/`
- related work taxonomy: `notes/`
- citation gaps: `reviews/`
- experiment analysis: `reviews/` or `notes/`
- final/export outputs: `outputs/`

Do not write process notes, missing-evidence labels, review reminders, or setup diagnostics into formal `paper.md` prose.

For paper-writing mode, manuscript text should be formal paper prose. Put citation gaps, missing evidence, and unresolved assumptions into `reviews/` or `notes/`.

## Skill Categories

Current skill count: 33.

### Core Workflow

- `auto-init`
- `storyline-helper`
- `paper-section-drafter`
- `review-revise`
- `submission-precheck`
- `writing-orchestrator`
- `socratic-discussion`

### Writing

- `markdown-helper`
- `markdown-review`
- `human-comment-helper`

### Related Work

- `relatedwork-finder`
- `relatedwork-summarizer`
- `relatedwork-writer`

### Review / Checker

- `problem-checker`
- `novelty-checker`
- `logic-checker`
- `clarity-checker`
- `technical-depth-checker`
- `data-checker`
- `evaluation-protocol-checker`

### Experiment

- `experiment-analyzer`

### LaTeX / Markdown Conversion

- `latex2markdown`
- `markdown2latex`
- `latex-final-writer`
- `template-latex-export`

### Utility / Legacy

- `copaper-manage`
- `phase-navigation`
- `pdf2paper`
- `ppt2storyline`

These skills may preserve legacy workflow vocabulary, but execution must remain local-file based and Codex-compatible.

### High-Risk Skills

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

High-risk skills default to planning / evidence-gating mode only.

They must not:

- generate fake data;
- strengthen unsupported novelty;
- make prose untraceable to evidence;
- draft a full paper automatically;
- modify `paper.md` without an approved edit plan.

## Maintenance Rules

When adding or modifying skills:

- update `docs/SKILL_INDEX.md`;
- update `docs/SKILL_COMPATIBILITY_MATRIX.md`;
- run `scripts/check_skill_metadata.py`;
- if usage changes, update `docs/PROMPT_COOKBOOK.md`;
- if user-facing workflow changes, update `docs/COMPLETE_USER_MANUAL.md`;
- run a release smoke test before beta release or internal rollout.

Recommended checks:

```powershell
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith\.agents\skills
python E:\ai\papersmith\scripts\create_paper_project.py --name release-smoke-test --target E:\ai\papersmith-release-smoke-test --force
python E:\ai\papersmith\scripts\check_project_structure.py E:\ai\papersmith-release-smoke-test
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith-release-smoke-test\.agents\skills
```
