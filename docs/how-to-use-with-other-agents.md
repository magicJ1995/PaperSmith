# How to Use With Other Agents

This kit can be used by any agent that can read and write local Markdown files.

## Minimum Requirements

The agent must be able to:

- read `AGENTS.md`;
- read and edit Markdown files;
- list local directories;
- write review reports to `reviews/`;
- avoid hidden state or plugin-only state.

## Recommended Prompt

```text
Read AGENTS.md first. Treat PROJECT_CONTEXT.md, storyline.md, and paper.md as source-of-truth files. Before editing paper.md or storyline.md, propose a plan and wait for approval. Put review outputs in reviews/. Do not invent citations, data, experiments, baselines, or novelty.
```

## Skill Portability

The files under `.agents/skills/` are Markdown instructions. If another agent does not auto-discover skills, paste or reference the relevant `SKILL.md` in the prompt.
