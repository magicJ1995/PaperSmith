# Paper Project Agent Rules

Follow the root PaperSmith rules. In this project, `PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` are the source of truth.

## Skill Use

- This project includes the full CoPaper-style skill set migrated for Codex and local Markdown workflows.
- Before claiming to use a skill, first read `.agents/skills/<skill-name>/SKILL.md`.
- If you are unsure which skill to use, consult `docs/SKILL_INDEX.md` in the template kit when available.
- If a skill contains historical workflow terminology, follow the template kit's `CODEX_COMPATIBILITY.md` and `docs/SKILL_COMPATIBILITY_MATRIX.md`; execute through local Markdown files.
- If `.agents/skills/` is missing, report a setup error before doing paper-writing work.
- Do not use CoPaper webapp, copaper-opencode plugin tools, OpenCode slash commands, or hidden plugin state.
- Tasks that formerly depended on plugin-managed state must become Markdown outputs under `reviews/`, `notes/`, `references/`, or `outputs/`.

## Before Editing

- Read `PROJECT_CONTEXT.md`.
- Read the relevant section of `storyline.md` or `paper.md`.
- Present a short edit plan before changing `storyline.md` or `paper.md`.
- Wait for user confirmation before changing `storyline.md` or `paper.md`.
- Use only facts available in project files or explicitly provided by the user.
- Review-only, check-only, and diagnose-only tasks must not modify `storyline.md` or `paper.md`.
- Empty templates, `TODO` sections, and placeholder content must be reported as missing user input, not filled with invented research content.

## Output Locations

- Reviews and checker reports: `reviews/` with stable filenames, such as `storyline_review.md`, `introduction_review.md`, `method_review.md`, `experiment_review.md`, `revise_plan.md`, and `submission_precheck.md`.
- Scratch notes and meeting notes: `notes/`
- Papers, BibTeX, PDFs, and citation notes: `references/`
- Final deliverables: `outputs/`

## Evidence Boundaries

- Any experiment result, dataset, baseline, citation, novelty claim, or conclusion must come from user-provided material or project files.
- Do not strengthen claims beyond available evidence.

## Required Labels

Use these labels instead of inventing missing information:

- `CITATION_NEEDED`
- `DATA_NEEDED`
- `BASELINE_NEEDED`
- `NEEDS_USER_EVIDENCE`
- `UNCLEAR_ASSUMPTION`
