# PaperSmith

<p>
  <a href="README.md"><img src="https://img.shields.io/badge/US-English%20Default%20Source-111111?style=flat-square&labelColor=343a40" alt="English Default Source"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/CN-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%20%E6%9F%A5%E7%9C%8B-8250df?style=flat-square&labelColor=343a40" alt="简体中文 查看"></a>
</p>

PaperSmith 是课题组内部 beta 版论文写作工作流包。你可以把它理解成：一个论文项目模板 + Codex 写作规则 + 一组论文写作 skills，用来帮助你按步骤整理、写作、审阅和修改论文。

它不是自动写论文机器，不是 copaper.ai webapp，不依赖 copaper-opencode 插件，也不需要 `/copaper`、`/copaper-doctor`、`copaper_*` 工具或 OpenCode 的隐藏状态。所有重要信息都保存在每个论文项目里的 Markdown 文件中。

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
