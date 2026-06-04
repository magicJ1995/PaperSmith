# PaperSmith Rules

These rules apply to every paper project created from this kit.

## Core Principles

- `PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` are the paper project's source-of-truth files.
- Do not fabricate experiments, results, references, baselines, claims, or novelty.
- Any citation, dataset, experiment result, design conclusion, or reviewer response must come from user-provided material or a verifiable source explicitly supplied in the project.
- Any experiment result, dataset, baseline, citation, novelty claim, or conclusion must be traceable to user-provided material or project files.
- Do not treat the model as a generator of substantive research contributions. Use it for structure checks, expression polishing, logic diagnosis, organization, and consistency review.
- Keep `storyline.md`, `paper.md`, experiment notes, and references mutually consistent.
- Prefer section-by-section work. Do not rewrite the whole paper unless the user explicitly requests a full rewrite.

## Skill Use Rules

- This kit keeps the full CoPaper-style skill set, migrated for Codex and local Markdown workflows.
- Before claiming to use a skill, first read `.agents/skills/<skill-name>/SKILL.md`.
- If you are unsure which skill to use, read `docs/SKILL_INDEX.md` first.
- If a skill contains historical workflow terminology, follow `CODEX_COMPATIBILITY.md` and `docs/SKILL_COMPATIBILITY_MATRIX.md`; execute the task through local Markdown files instead of legacy tooling.
- If `.agents/skills/` is missing in a generated paper project, report it as a setup error before doing paper-writing work.
- Skills are local Markdown instructions. Do not replace them with CoPaper webapp, copaper-opencode plugin tools, OpenCode slash commands, or hidden plugin state.
- Tasks that formerly depended on plugin-managed state must be converted into Markdown outputs under `reviews/`, `notes/`, `references/`, or `outputs/`.

## Modification Rules

- Before modifying `paper.md` or `storyline.md`, first present a concrete modification plan.
- For major changes, include the target section, evidence used, expected effect, and risk of changing the claim.
- Apply changes only after the user explicitly approves the plan.
- Review-only, check-only, and diagnose-only tasks must not modify `paper.md` or `storyline.md`.
- Preserve user-provided technical facts unless the user confirms they are wrong.
- Never strengthen claims beyond the available evidence.

## Evidence Rules

- Put raw user-provided material in `notes/`, `references/`, or `PROJECT_CONTEXT.md`.
- Put review and checker outputs in `reviews/` with stable filenames, for example `reviews/introduction_review.md`, `reviews/storyline_review.md`, or `reviews/submission_precheck.md`.
- Put generated deliverables in `outputs/`.
- When a fact cannot be verified from project files, mark it as `NEEDS_USER_EVIDENCE`.
- When a citation is missing, write `CITATION_NEEDED` instead of inventing one.
- Empty templates, `TODO` sections, and placeholder content must be reported as missing user input. Do not fill them with invented research content.

## Writing Workflow

1. Confirm project context in `PROJECT_CONTEXT.md`.
2. Build or check `storyline.md`.
3. Draft `paper.md` by section.
4. Run `markdown-review` after meaningful section updates.
5. Use `review-revise` to address review findings one issue at a time.
6. Run `submission-precheck` before submission or export.

## Agent Scope

Agents may read and edit local Markdown files in the active paper project. They must not rely on CoPaper webapp, copaper-opencode plugin tools, OpenCode slash commands, or hidden plugin state.
