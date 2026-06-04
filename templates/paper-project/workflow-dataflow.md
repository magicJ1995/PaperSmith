# Workflow Dataflow

This project uses local files as durable state.

```text
PROJECT_CONTEXT.md
        |
        v
storyline.md <-------- reviews/storyline-*.md
        |
        v
references/ -----> paper.md <------ reviews/*.md
        |             |
        v             v
notes/          outputs/
```

## Artifacts

| Artifact | Purpose |
|---|---|
| `PROJECT_CONTEXT.md` | Verified project facts and claim boundaries |
| `storyline.md` | Research logic and narrative |
| `paper.md` | Paper draft |
| `references/` | Papers, BibTeX, citation notes, literature summaries |
| `notes/` | Meeting notes, experiment notes, scratch analysis |
| `reviews/` | Durable review and precheck reports |
| `outputs/` | Final exports and deliverables |

## Review Loop

1. Draft or revise one section.
2. Write a review report to `reviews/`.
3. Convert review findings into a revision plan.
4. Apply approved edits.
5. Re-run review if the claim or evidence changed.
