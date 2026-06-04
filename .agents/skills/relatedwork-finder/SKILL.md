---
name: relatedwork-finder
description: Use when the user wants to organize, search for, or summarize related work using storyline.md, paper.md, and references/. Do not use to fabricate citations or claim a paper was read when only metadata is available.
---

# Related Work Finder

## Purpose

Help build a verifiable related-work base for the paper.

## Inputs

- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- Existing files in `references/`
- User-provided search results, PDFs, BibTeX, or paper notes

## Workflow

1. Extract search themes from the problem, existing methods, shared limitation, and insight.
2. Ask the user before performing broad literature expansion if the scope is unclear.
3. Store user-provided papers, BibTeX, and summaries under `references/`.
4. For each paper, distinguish:
   - metadata only;
   - abstract skimmed;
   - full paper read;
   - user-provided summary.
5. Write related-work notes to `references/relatedwork-notes.md` or a user-specified file.
6. Mark missing citations in `paper.md` as `CITATION_NEEDED` unless a verified reference exists.

## Constraints

- Do not invent titles, authors, venues, years, DOIs, or BibTeX entries.
- Do not claim full-paper understanding without reading the full text or user-provided detailed notes.
- Do not use legacy related-work commands, plugin tools, UI status panels, or hidden workflow state.
