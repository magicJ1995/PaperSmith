# Writing Principles

## Structure First

Start from the research storyline before polishing prose. A strong paper should have a traceable path:

```text
problem -> importance -> limitation of existing work -> insight -> method -> evidence -> conclusion
```

If this chain is weak, improve the chain before improving wording.

## Human-Led Content

The researcher provides the actual contribution, data, experiments, and interpretation. The agent helps with:

- organizing material;
- finding missing assumptions;
- checking consistency;
- improving clarity;
- drafting based only on provided facts;
- preparing review reports.

The agent must not create new scientific facts.

## Section-by-Section Writing

Work on one section or subsection at a time. For each section, identify:

- the intended claim;
- the evidence supporting it;
- required citations;
- links to experiment results;
- dependencies on other sections.

## Claim Discipline

Every strong claim needs support. If the evidence is weak, lower the strength of the wording or ask the user for more evidence.

Use labels instead of fabrication:

- `CITATION_NEEDED`
- `DATA_NEEDED`
- `BASELINE_NEEDED`
- `NEEDS_USER_EVIDENCE`
- `UNCLEAR_ASSUMPTION`

## Review Discipline

Reviews should be written as durable Markdown reports in `reviews/`. A useful review names concrete sections, explains the risk, and suggests a repair path without silently changing the paper.
