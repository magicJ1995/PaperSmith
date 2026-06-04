# Related Work Skills Diagnosis

## Scope

Checked files:

- `E:\ai\papersmith\.agents\skills\relatedwork-finder\SKILL.md`
- `E:\ai\papersmith\.agents\skills\relatedwork-summarizer\SKILL.md`

No skill file was modified.

## 1. relatedwork-finder Responsibilities

`relatedwork-finder` is responsible for building a verifiable related-work base for the paper.

Current responsibilities:

- extract search themes from `PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md`;
- organize existing references, user-provided search results, PDFs, BibTeX, and paper notes;
- store related-work assets under `references/`;
- distinguish metadata-only, abstract-skimmed, full-paper-read, and user-provided-summary states;
- write related-work notes to `references/relatedwork-notes.md`;
- mark missing citations as `CITATION_NEEDED`;
- avoid fabricated titles, authors, venues, years, DOIs, and BibTeX.

## 2. relatedwork-summarizer Responsibilities

`relatedwork-summarizer` is responsible for summarizing verified related-work notes or papers into local Markdown summaries.

Current responsibilities:

- summarize user-provided papers, abstracts, notes, PDFs, or BibTeX entries;
- use `references/`, `PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` as inputs;
- write summaries to `references/relatedwork_summary.md` or `references/papers/*.md`;
- avoid claiming full-paper understanding when only metadata is available;
- preserve Codex-compatible rules: no fabrication, local Markdown outputs, edit plan before source edits.

## 3. Do They Include a Related Work Drafting Workflow?

No.

They do not currently provide a clear workflow for drafting the `Related Work` section of `paper.md`.

They cover:

- finding or organizing references;
- summarizing references;
- marking missing citations.

They do not cover:

- selecting Related Work section goals;
- grouping papers into argument-driven method families;
- drafting comparative paragraphs;
- connecting each group to the paper's problem, gap, and insight;
- proposing edits to `paper.md` Related Work.

## 4. Do They Explain Related Work Subsection Structure?

No, not sufficiently.

Current files do not explain how to organize Related Work subsections, for example:

- by method family;
- by problem formulation;
- by technical limitation;
- by evaluation setting;
- by contrast with the paper's core insight.

They also do not warn against weak structures such as a paper-by-paper list with no synthesis.

## 5. Do They Explain How to Turn References Into Paper Prose?

No.

They do not currently define a prose-conversion workflow such as:

1. extract verified claims from each reference;
2. group references into theme clusters;
3. identify what each cluster solves and does not solve;
4. connect the limitation to the current paper's motivation;
5. draft a paragraph with citations;
6. preserve citation provenance;
7. mark gaps as `CITATION_NEEDED` instead of inventing support.

## 6. Do They Require Edit Plan Before Modifying paper.md?

Partially yes.

`relatedwork-summarizer` explicitly includes the generic Codex-compatible workflow:

- before modifying `paper.md` or `storyline.md`, provide an edit plan;
- wait for explicit user confirmation.

`relatedwork-finder` does not explicitly state this general edit-plan rule, but its current workflow mostly writes to `references/` and only says to mark missing citations in `paper.md` as `CITATION_NEEDED`. It should be strengthened if it remains responsible for any `paper.md` interaction.

## 7. Minimal Modification Recommendation

Recommendation: add a new `relatedwork-writer` skill rather than overloading `relatedwork-summarizer`.

Reason:

- `relatedwork-finder` should remain responsible for locating and organizing reference materials.
- `relatedwork-summarizer` should remain responsible for verified summaries and synthesis notes.
- Drafting the actual `Related Work` section is a distinct writing task with stronger source-edit risk.

Minimal new skill: `relatedwork-writer`

Suggested responsibilities:

- read `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `writingrules.md`, and `references/`;
- inspect existing `paper.md` Related Work section;
- build a related-work structure plan by method family or theme;
- map each subsection to verified references;
- produce `reviews/relatedwork_draft_plan.md`;
- before modifying `paper.md`, provide an edit plan and wait for user confirmation;
- draft only approved Related Work subsection(s);
- never invent citations or claim a paper was read if it was not.

Suggested default outputs:

- planning/review output: `reviews/relatedwork_draft_plan.md`;
- citation gap report: `reviews/relatedwork_citation_gaps.md`;
- approved source edits: `paper.md` only after confirmation.

## 8. Alternative: Strengthen relatedwork-summarizer

This is possible but less clean.

If avoiding a new skill, `relatedwork-summarizer` could be extended with:

- Related Work section structure rules;
- paragraph drafting workflow;
- citation provenance tracking;
- edit-plan-before-`paper.md` rules;
- default `reviews/relatedwork_draft_plan.md` output.

However, that would mix summary generation with paper-section writing. For maintainability, a separate `relatedwork-writer` is preferable.

## Diagnosis Summary

Current state:

- `relatedwork-finder`: good for reference discovery/organization.
- `relatedwork-summarizer`: good for reference summarization.
- Missing: a dedicated Related Work writing workflow.

Recommended minimal fix:

- add `relatedwork-writer`;
- keep finder and summarizer focused on reference base and summaries;
- make `relatedwork-writer` responsible for section structure, prose planning, citation grounding, and approved `paper.md` edits.
