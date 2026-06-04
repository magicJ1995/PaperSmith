# Codex Compatibility

This kit is designed for Codex and other local-file agents. It deliberately avoids CoPaper/OpenCode plugin features.

## Not Migrated

| CoPaper/OpenCode feature | Status | Codex replacement |
|---|---|---|
| `/copaper` dashboard | Not migrated | Read `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, and `reviews/` directly |
| `/copaper-doctor` | Not migrated | Run `scripts/check_project_structure.py` and `scripts/check_skill_metadata.py` |
| `copaper_*` tools | Not migrated | Use local Markdown files and normal agent file operations |
| `@copaper-*` subagents | Not migrated | Use explicit skills under `.agents/skills/` |
| `task(category=...)` | Not migrated | Use direct prompts and section-by-section work |
| OpenCode plugin state | Not migrated | Store durable state in Markdown files |
| `.agents/state.json` | Not migrated | Use `PROJECT_CONTEXT.md`, `reviews/`, and notes |
| `.agents/events.jsonl` | Not migrated | Use dated review notes or changelog entries in Markdown |
| Automatic dashboard/status updates | Not migrated | Use explicit review reports and project checks |
| `copaper relatedwork` CLI | Not migrated | Store references in `references/` and write literature notes manually or via agent-supported search |

## Codex Operating Model

Codex should:

- read `AGENTS.md` first;
- read `.agents/skills/<skill-name>/SKILL.md` before claiming to use that skill;
- use project files as the source of truth;
- propose a plan before editing `storyline.md` or `paper.md`;
- write review outputs to `reviews/` with stable filenames;
- mark missing evidence explicitly;
- report empty templates and `TODO` sections as missing user input, not as content to complete speculatively;
- treat missing `.agents/skills/` in a generated project as a setup error;
- avoid hidden state.

## Initialization Model

The reusable kit and paper projects are separate:

- `E:\ai\papersmith` is the shared template kit.
- Each paper should live in its own project folder.
- A valid paper project contains both copied template files and copied `.agents/skills/`.

If Python is unavailable, users can manually copy `templates/paper-project/` and `.agents/skills/` into a new project. No CoPaper/OpenCode plugin is needed.

## Why Markdown State

Markdown files are easy to inspect, diff, review, commit, and share across agents. This makes the workflow portable across Codex, Claude Code, Cursor-style agents, and normal manual editing.
