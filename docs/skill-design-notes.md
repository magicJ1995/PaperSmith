# Skill Design Notes

## Migration Strategy

The original CoPaper workflow contains useful writing and review ideas, but many instructions assume OpenCode plugin tools or a CoPaper CLI state machine. This kit keeps the paper-writing ideas and removes the plugin assumptions.

## Design Choices

- Each skill is narrow and manually triggerable.
- Each `SKILL.md` has `name` and `description` front matter.
- Review outputs go to `reviews/`.
- Project state is represented by Markdown files.
- Skills use explicit missing-evidence labels instead of inventing content.

## First-Version Skill Set

- `storyline-helper`
- `paper-section-drafter`
- `markdown-review`
- `review-revise`
- `relatedwork-finder`
- `experiment-analyzer`
- `submission-precheck`

## Deferred Skills

LaTeX conversion, PDF/PPT import, automatic related-work downloading, and dashboard-style status are intentionally deferred. They require stronger tool assumptions and are less important than the core writing discipline.
