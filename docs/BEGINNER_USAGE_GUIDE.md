# Beginner Usage Guide

This guide explains the basic paper-writing workflow for new lab members.

## Start With Project Context

Every paper project must fill `PROJECT_CONTEXT.md` first. Codex should not draft, revise, or claim novelty before the project context is available.

## Use Skills by Reading SKILL.md First

Before using any skill, ask Codex to read:

```text
.agents/skills/<skill-name>/SKILL.md
```

## Related Work Workflow

There are three related-work skills:

- `relatedwork-finder`: find and register literature materials.
- `relatedwork-summarizer`: summarize existing references and notes.
- `relatedwork-writer`: organize and draft the Related Work section from verified references.

Recommended order:

1. Use `relatedwork-finder` to organize available references.
2. Use `relatedwork-summarizer` to summarize verified references.
3. Use `relatedwork-writer` to plan the Related Work section structure.
4. Only after confirmation, let `relatedwork-writer` draft approved subsection(s) in `paper.md`.

## Safety Rule

Do not let Codex invent papers, citations, baselines, datasets, experiment results, novelty, or conclusions. Missing support should be marked as `CITATION_NEEDED`, `DATA_NEEDED`, `BASELINE_NEEDED`, or `NEEDS_USER_EVIDENCE`.
