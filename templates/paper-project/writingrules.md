# Writing Rules

## Source of Truth

- `PROJECT_CONTEXT.md` contains verified project facts.
- `storyline.md` contains the research logic.
- `paper.md` contains the paper draft.
- `reviews/` contains review reports and precheck reports.

## Heading Rules

- Use Markdown headings for structure.
- Do not add body text under a heading before checking its `description` comment.
- Keep edits section-by-section.
- Rename section headings only when the user approves the structural change.

## Evidence Rules

- Use `CITATION_NEEDED` when a citation is required but absent.
- Use `DATA_NEEDED` when a claim needs experimental evidence.
- Use `BASELINE_NEEDED` when a comparison lacks a baseline.
- Use `NEEDS_USER_EVIDENCE` when the project files do not support a statement.

## Paragraph Rules

- Each paragraph should have one main claim.
- Prefer concrete nouns and measured claims.
- Avoid overstating novelty.
- Avoid unsupported adjectives such as "significant", "robust", "efficient", or "state-of-the-art" unless supported by data.

## Revision Rules

- Propose a plan before editing `paper.md` or `storyline.md`.
- Explain which evidence supports the revision.
- Keep rejected or unresolved issues in `reviews/` rather than silently dropping them.
