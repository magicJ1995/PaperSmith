---
name: relatedwork-writer
description: Use when the project already has references or related-work notes and the user wants to plan, organize, or draft the Related Work section of paper.md. Not suitable for finding papers online, fabricating citations, replacing real literature reading, or editing paper.md without an approved edit plan. Default outputs: reviews/relatedwork_draft_plan.md, reviews/relatedwork_citation_gaps.md, notes/relatedwork_taxonomy.md; paper.md only after explicit user confirmation.
---

# relatedwork-writer

## Purpose

Guide and draft the Related Work section in `paper.md` from verified project materials. This skill turns reference notes and paper summaries into problem-oriented, method-family-oriented, and gap-oriented prose.

This skill is not for finding literature and is not for simple paper summarization. Use `relatedwork-finder` to find/register references and `relatedwork-summarizer` to summarize existing references. Use `relatedwork-writer` to organize and write the actual Related Work section.

## When to Use

Use this skill when:

- `PROJECT_CONTEXT.md` exists and contains the paper's problem, method, and contribution boundaries;
- `storyline.md` exists and gives the problem, existing methods, shared limitations, insight, and method direction;
- `references/` contains at least some verified papers, BibTeX entries, abstracts, summaries, or notes;
- `notes/` contains related-work notes, if available;
- the user needs to convert related work from "paper-by-paper summaries" into a Related Work section organized by problem, method family, and gap.

## When Not to Use

Do not use this skill when:

- there are no references or related-work notes;
- the user asks to invent citations;
- the user asks to write the full paper;
- the user has not confirmed writing into `paper.md`;
- the core problem, contribution boundaries, or method direction are unclear;
- the user expects this skill to replace reading the actual papers.

## Required Inputs

- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `writingrules.md`
- `references/`
- `notes/relatedwork*.md`, if present
- `reviews/relatedwork_plan.md`, if present

## Default Outputs

- `notes/relatedwork_taxonomy.md`
- `reviews/relatedwork_draft_plan.md`
- `reviews/relatedwork_citation_gaps.md`
- `paper.md` only after explicit user confirmation

## Operating Modes

### Planning / Review Mode

Use this mode when the user asks to plan, inspect, diagnose, organize, or review Related Work materials.

Allowed outputs:

- `notes/relatedwork_taxonomy.md`
- `reviews/relatedwork_draft_plan.md`
- `reviews/relatedwork_citation_gaps.md`

Rules:

- Do not modify `paper.md`.
- It is acceptable to use `CITATION_NEEDED`, `NEEDS_USER_EVIDENCE`, and missing-input reports in `reviews/` or `notes/`.
- Keep process notes, evidence warnings, citation gaps, and missing-input reports outside the manuscript body.

### Paper-Writing Mode

Use this mode only when the user explicitly confirms writing the Related Work section into `paper.md`.

Required behavior:

- Write formal paper prose only.
- Modify only the confirmed Related Work section or subsection.
- Do not include process notes, review reminders, setup notes, or missing-input reports in `paper.md`.
- Do not include meta phrases such as "current project context", "this draft", "source material is missing", "should avoid", or "should remain" in `paper.md`.
- Do not include `CITATION_NEEDED`, `NEEDS_USER_EVIDENCE`, `DATA_NEEDED`, or `BASELINE_NEEDED` markers in the Related Work manuscript text.
- Put all citation gaps, evidence warnings, and missing-input reports in `reviews/relatedwork_citation_gaps.md` or `reviews/relatedwork_draft_plan.md`.
- Use only references already present in `PROJECT_CONTEXT.md`, `references/`, or project notes; do not invent papers, authors, years, venues, DOIs, or BibTeX.

## Core Principle

Related Work is not a paper-by-paper list. It should explain the research landscape, group methods by problem or technique, identify shared limitations, and connect those limitations to this paper's motivation and method.

## General Related Work Structure

Use a structure like this unless the project suggests a better one:

1. Problem background methods.
2. Mainstream technical families.
3. Closely related methods.
4. Transfer, adaptation, or robustness methods if relevant.
5. Summary gap and transition to this paper.

## Log Anomaly Detection Recommended Structure

For log anomaly detection papers, prefer this structure when supported by the references:

1. Log parsing and log representation.
2. Traditional and deep log anomaly detection.
3. Robust or semi-supervised log anomaly detection.
4. Cross-domain transfer and adaptation for log analysis.
5. LLM-based log analysis, if relevant.
6. Summary gap.

## Writing Procedure

### Step 1: Evidence Inventory

Before drafting, list:

- available references;
- each reference's reading status: metadata only, abstract skimmed, full paper read, or user-provided summary;
- each reference's method family;
- what claim each reference can support;
- missing support as `CITATION_NEEDED`.

Do not claim a reference supports a point unless the project files actually show that support.

### Step 2: Taxonomy Construction

Build `notes/relatedwork_taxonomy.md`:

- subsection structure;
- purpose of each subsection;
- references mapped to each subsection;
- unsupported subsection claims marked as `CITATION_NEEDED`.

### Step 3: Gap Alignment

Connect each method family to limitations:

- what the method family solves;
- what it does not solve;
- how the limitation connects to `PROJECT_CONTEXT.md`;
- how the final gap aligns with `storyline.md`;
- whether the gap is too broad for the available evidence.

### Step 4: Draft Plan

Write `reviews/relatedwork_draft_plan.md`.

The plan must include:

- target `paper.md` section or subsection;
- subsection structure;
- evidence and citations to use;
- claims to avoid;
- citation gaps;
- risks of overstating prior work;
- exact edit scope.

Do not modify `paper.md` at this step.

### Step 5: User Confirmation

Wait for explicit user confirmation before editing `paper.md`.

Confirmation must name:

- the target section;
- which subsection(s) may be drafted;
- whether citation placeholders are acceptable.

### Step 6: Draft Related Work

Draft only confirmed subsection(s).

Rules:

- use only available references;
- if writing into `paper.md`, write formal manuscript prose and move missing-citation details to `reviews/relatedwork_citation_gaps.md`;
- avoid paper-by-paper listing;
- connect each subsection to the paper's problem, method, or gap;
- do not broaden the gap beyond what `PROJECT_CONTEXT.md` and `storyline.md` support.

## Safety Rules

- Do not invent papers, authors, venues, years, DOIs, or BibTeX.
- Do not claim a paper has been fully read if only metadata or abstract is available.
- Do not use vague phrases such as "many studies" unless supported by citations.
- Do not overstate the weakness of prior work.
- Do not make the gap broader than what `PROJECT_CONTEXT.md` supports.
- Do not edit `paper.md` without an edit plan and user confirmation.
- When output goes to `paper.md`, do not include process notes, review reminders, "current project context", "this draft", `CITATION_NEEDED`, `NEEDS_USER_EVIDENCE`, `DATA_NEEDED`, or `BASELINE_NEEDED`.
- When citation support is missing during paper-writing mode, record the gap in `reviews/relatedwork_citation_gaps.md` instead of placing markers in the manuscript.
- Do not use plugin commands, plugin tools, UI status panels, hidden workflow state, or JSON workflow logs.

## Output Template: notes/relatedwork_taxonomy.md

```markdown
# Related Work Taxonomy

## Source Inventory

| Reference | Reading Status | Method Family | Supported Claim | Citation Gap |
|---|---|---|---|---|

## Proposed Subsections

### <Subsection Name>

- Purpose:
- Included references:
- Main supported claims:
- Missing support:

## Summary Gap

- Supported gap:
- Unsupported or overbroad gap:
- Required user evidence:
```

## Output Template: reviews/relatedwork_draft_plan.md

```markdown
# Related Work Draft Plan

## Target Section

## Proposed Structure

## Evidence to Use

## Citation Gaps

## Claims to Avoid

## Proposed Edit Scope

## User Confirmation Needed
```

## Output Template: reviews/relatedwork_citation_gaps.md

```markdown
# Related Work Citation Gaps

| Claim Needing Support | Current Location | Needed Reference Type | Status |
|---|---|---|---|

## High Priority Gaps

## Lower Priority Gaps

## Notes
```
