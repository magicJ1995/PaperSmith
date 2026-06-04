# PaperSmith

<p>
  <a href="#english"><img src="https://img.shields.io/badge/US-English%20Default%20Source-111111?style=flat-square&labelColor=343a40" alt="English Default Source"></a>
  <a href="#中文"><img src="https://img.shields.io/badge/CN-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%20%E6%9F%A5%E7%9C%8B-8250df?style=flat-square&labelColor=343a40" alt="简体中文 查看"></a>
</p>

---

## 中文

PaperSmith 是课题组内部 beta 版论文写作工作流包。你可以把它理解成：一个论文项目模板 + Codex 写作规则 + 一组论文写作 skills，用来帮助你按步骤整理、写作、审阅和修改论文。

## 第一次使用

第一次使用请先看：

[学生一页版使用指南](docs/STUDENT_ONE_PAGE_GUIDE.md)

需要完整步骤说明时看：

[完整用户手册](docs/COMPLETE_USER_MANUAL.md)

想复制常用 prompt 时看：

[Prompt Cookbook](docs/PROMPT_COOKBOOK.md)

### 重要规则

不要在母版目录里写论文：

```text
E:\ai\papersmith
```

每篇论文都要创建独立项目，例如：

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

创建项目后，请在 Codex 中打开新论文项目目录：

```text
E:\ai\papers\my-paper
```

不要在写论文时把 Codex 工作目录指向 `E:\ai\papersmith`。

### 这个工具提供什么

- `templates/paper-project/`：每篇论文的项目模板。
- `.agents/skills/`：Codex 可读取的论文写作 skills。
- `scripts/create_paper_project.py`：创建新论文项目。
- `scripts/check_project_structure.py`：检查论文项目结构。
- `scripts/check_skill_metadata.py`：检查 skill metadata。
- `AGENTS.md`：课题组级写作规则。
- `docs/`：学生指南、完整手册、prompt cookbook、skill 索引和兼容性说明。

### 基本流程

1. 创建独立论文项目。
2. 填写 `PROJECT_CONTEXT.md`。
3. 完善 `storyline.md`。
4. 整理 `references/`。
5. 逐节起草 `paper.md`。
6. 将审阅报告写入 `reviews/`。
7. 根据 review 逐条修改。
8. 投稿前运行 precheck。
9. 将最终导出内容放入 `outputs/`。

### Codex 不能做什么

不要让 Codex 编造：

- 实验结果；
- 引用、作者、年份、venue、DOI 或 BibTeX；
- baseline 或 baseline 结果；
- 数据集；
- novelty 或 contribution；
- 没有项目文件支持的 conclusion。

`PROJECT_CONTEXT.md`、`storyline.md` 和 `paper.md` 是论文项目的事实来源。缺实验、缺引用、缺 baseline 时，Codex 应标记 `DATA_NEEDED`、`CITATION_NEEDED`、`BASELINE_NEEDED` 或 `NEEDS_USER_EVIDENCE`，而不是自行补全。

### 高风险 skills

以下 skills 默认不要直接让普通同学使用：

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

它们只能默认用于 planning / evidence-gating mode。不要让它们生成假数据、强化无证据 claim、自动润色成不可追踪的最终稿，或直接写整篇论文。

### 出问题时发给维护者

请把以下文件发给维护者：

```text
PROJECT_CONTEXT.md
storyline.md
paper.md
reviews/
AGENTS.md
.agents/skills/<出问题的skill>/SKILL.md
```

同时附上你复制给 Codex 的 prompt，以及相关终端输出。

### 目录概览

```text
.agents/skills/              可复用论文写作 skills
templates/paper-project/     每篇论文的初始化模板
scripts/                     项目创建和检查脚本
examples/demo-paper-project/ 示例论文项目
docs/                        使用说明和维护文档
archive/                     发布前归档材料
```

### 许可

本工具包用于课题组内部 beta 试用。详见 `LICENSE`。

---

## English

PaperSmith is the lab's internal beta workflow kit for paper writing with Codex. You can think of it as a paper-project template plus Codex writing rules plus a set of paper-writing skills. It helps lab members organize, draft, review, and revise papers step by step.

It is not an automatic paper-writing machine, not the copaper.ai webapp, not the copaper-opencode plugin, and not an OpenCode command package. It does not require `/copaper`, `/copaper-doctor`, `copaper_*` tools, or hidden OpenCode plugin state. All durable state lives in Markdown files inside each paper project.

### First-Time Use

Start here:

```text
docs/STUDENT_ONE_PAGE_GUIDE.md
```

For full step-by-step instructions, read:

```text
docs/COMPLETE_USER_MANUAL.md
```

For copyable prompts, read:

```text
docs/PROMPT_COOKBOOK.md
```

### Important Rule

Do not write papers inside the template kit directory:

```text
E:\ai\papersmith
```

Each paper must have its own project folder. Create one with:

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

After creating the project, open Codex in the new paper project folder:

```text
E:\ai\papers\my-paper
```

Do not open Codex in `E:\ai\papersmith` when writing a paper.

### What This Kit Provides

- `templates/paper-project/`: the template copied for each paper.
- `.agents/skills/`: Codex-readable paper-writing skills.
- `scripts/create_paper_project.py`: create a new paper project.
- `scripts/check_project_structure.py`: check paper project structure.
- `scripts/check_skill_metadata.py`: check skill metadata.
- `AGENTS.md`: lab-level writing rules.
- `docs/`: student guides, complete manual, prompt cookbook, skill index, and compatibility notes.

### Basic Workflow

1. Create an independent paper project.
2. Fill `PROJECT_CONTEXT.md`.
3. Complete `storyline.md`.
4. Organize `references/`.
5. Draft `paper.md` section by section.
6. Write review reports to `reviews/`.
7. Revise issue by issue.
8. Run precheck before submission.
9. Put final exports in `outputs/`.

### What Codex Must Not Do

Do not ask Codex to invent:

- experiment results;
- citations, authors, years, venues, DOIs, or BibTeX;
- baselines or baseline results;
- datasets;
- novelty or contributions;
- conclusions not supported by project files.

`PROJECT_CONTEXT.md`, `storyline.md`, and `paper.md` are the source-of-truth files. When experiments, citations, or baselines are missing, Codex should mark `DATA_NEEDED`, `CITATION_NEEDED`, `BASELINE_NEEDED`, or `NEEDS_USER_EVIDENCE` instead of filling the gap.

### High-Risk Skills

The following skills should not be used directly by regular users by default:

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

They default to planning / evidence-gating mode only. Do not use them to generate fake data, strengthen unsupported claims, polish unsupported text into untraceable final prose, or draft an entire paper.

### If Something Breaks

Send these files to the maintainer:

```text
PROJECT_CONTEXT.md
storyline.md
paper.md
reviews/
AGENTS.md
.agents/skills/<problem-skill>/SKILL.md
```

Also include the prompt you gave Codex and any relevant terminal output.

### Directory Overview

```text
.agents/skills/              Reusable paper-writing skills
templates/paper-project/     Template copied for each paper
scripts/                     Project creation and validation scripts
examples/demo-paper-project/ Example paper project
docs/                        User and maintainer documentation
archive/                     Pre-release archived materials
```

### License

This kit is intended for internal lab beta use. See `LICENSE`.
