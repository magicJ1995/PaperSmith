# PaperSmith 完整使用手册

本文档面向第一次使用 PaperSmith 的课题组同学。你不需要了解 Codex、Agent、Skill、CoPaper 或 OpenCode 的内部概念，只需要按照下面的步骤准备材料、创建项目、向 Codex 提问、检查输出、确认修改。

请记住最重要的一句话：这个工具不是自动写论文机器，而是一个把论文写作拆成可检查、可审阅、可追踪步骤的本地工作流包。

## 快速开始路径

如果你是第一次使用，不需要先读完整份手册。建议先只看这四节：

1. 第 5 节：如何创建一个新论文项目。
2. 第 6 节：第一次打开 Codex 应该说什么。
3. 第 7 节：第一步如何填写 `PROJECT_CONTEXT.md`。
4. 第 22 节：给课题组同学的最小使用版本。

你可以先创建项目，再逐步把已有材料填进去。不需要等所有实验、引用和图表都准备齐全才开始；不知道的信息保留 `TODO`、`DATA_NEEDED`、`CITATION_NEEDED` 或 `NEEDS_USER_EVIDENCE`，不要让 Codex 猜。

## 1. 这个工具是什么

PaperSmith 是一个面向科研论文写作的 Codex-compatible Agent Skill 工具包。简单说，它是一套本地文件模板和写作规则，用来让 Codex 在写论文时先读项目材料，再按步骤做诊断、计划、起草、审阅和修改。

你也可以把它理解成：一个论文项目文件夹模板，加上一组告诉 Codex 如何安全写论文的规则，以及一批可以直接复制使用的 prompt。

它不是 copaper.ai webapp，不依赖 copaper-opencode 插件，也不需要 `/copaper`、`/copaper-doctor`、`copaper_*` 工具或 OpenCode 的隐藏状态。所有重要信息都放在你能看到、能修改、能发给别人检查的 Markdown 文件里。

它的核心作用不是替你“创造研究”，而是帮助你把已有研究材料组织成论文：

- 整理论文项目信息；
- 设计和检查 storyline；
- 按章节起草 `paper.md`；
- 审阅结构、逻辑、实验和 citation；
- 根据 review 逐条修改；
- 整理 Related Work；
- 分析已有实验结果；
- 投稿前做结构和证据检查。

这个工具通过以下文件约束 Codex：

- `PROJECT_CONTEXT.md`：论文事实库，存研究问题、方法、数据、baseline、实验结果、贡献边界。
- `storyline.md`：论文逻辑主线，说明问题、gap、insight、方法和实验如何连起来。
- `paper.md`：论文正文草稿。
- `references/`：参考文献、BibTeX、文献笔记。
- `notes/`：中间分析结果，例如实验分析、related work taxonomy。
- `reviews/`：所有审阅报告、修改计划、投稿前检查。
- `outputs/`：最终导出结果，例如 LaTeX、投稿版本、最终检查产物。

推荐流程如下：

```text
准备材料
-> 创建论文项目
-> 填 PROJECT_CONTEXT.md
-> 完善 storyline.md
-> 整理 references/
-> 起草 paper.md
-> 审阅 reviews/
-> 逐条修改
-> 投稿前检查
-> 导出 outputs/
```

## 常见术语解释

第一次使用时，你只需要理解下面几个词：

| 术语 | 通俗解释 | 你需要怎么做 |
|---|---|---|
| skill | 一份本地说明书，告诉 Codex 某类任务应该怎么做 | 使用某个 skill 前，让 Codex 先读 `.agents/skills/<skill-name>/SKILL.md` |
| evidence inventory | 写正文前的证据清单 | 让 Codex 先列出已有证据和缺失证据，再决定能不能写正文 |
| edit plan | 修改前计划 | 修改 `paper.md` 或 `storyline.md` 前，要求 Codex 先说明改哪里、为什么改、依据是什么 |
| review-only | 只审阅，不改正文 | 这类任务只能输出到 `reviews/`，不能修改 `paper.md` 或 `storyline.md` |
| citation gap | 需要引用但当前没有引用的地方 | 写到 `reviews/relatedwork_citation_gaps.md`，不要编造 citation |
| taxonomy | 分类结构 | Related Work 中常用于把文献按方法族、问题或技术路线分组 |

## 2. 这个工具适合做什么，不适合做什么

### 适合做的事情

PaperSmith 适合用于“把已有研究材料变成可审阅论文”的过程。

- 整理论文项目信息：把标题、任务、方法、数据集、baseline、实验结果、引用和贡献边界放进 `PROJECT_CONTEXT.md`。
- 梳理研究问题和 motivation：检查问题是否具体，重要性是否清楚，实际场景是否明确。
- 构建 storyline：把“问题 -> 现有方法不足 -> insight -> 方法 -> 实验证据 -> 贡献边界”连成一条逻辑链。
- 根据已有证据起草 Introduction：先做 evidence inventory，再写 problem、motivation、gap、method overview、contribution。
- 根据已有方法细节起草 Method：把模块、算法、训练策略、输入输出和设计理由组织成正文。
- 根据已有实验结果起草 Experiments：把 datasets、baselines、metrics、main results、ablation、efficiency 和 limitation 写清楚。
- 整理 Related Work：先整理 references，再总结文献，再组织成按方法族展开的 Related Work。
- 审阅已有正文：检查结构、逻辑、clarity、citation、data、novelty 和 technical depth。
- 根据 review 逐条修改：每次只处理一个 issue，先判断证据是否足够，再给 edit plan。
- 检查实验设计是否完整：确认数据集、baseline、metric、协议、消融和威胁是否齐全。
- 检查 contribution 是否过度：防止把“已有证据支持的结果”写成“更大的 novelty”。
- 检查是否缺 citation：把缺口写进 `reviews/`，不要现场编造文献。
- 投稿前结构检查：检查项目结构、正文完整性、引用、图表、实验、限制和 claims。

### 不适合做的事情

以下事情不要让 Codex 做：

- 不能替研究者发明研究问题。
- 不能编造实验结果、数字、表格、图。
- 不能编造 baseline 或 baseline 结果。
- 不能编造数据集、数据规模、采样方式。
- 不能编造 citation、作者、年份、venue、DOI、BibTeX。
- 不能自动保证论文录用。
- 不能在没有证据的情况下强化 novelty。
- 不能直接一口气生成完整投稿稿。
- 不能把空白模板当作“可以自由发挥”的空间。
- 不能在没有 edit plan 和用户确认的情况下修改 `paper.md` 或 `storyline.md`。

## 3. 目录结构总览

每篇论文都应该是一个独立项目。创建后，目录大致如下：

```text
paper-project/
  AGENTS.md
  PROJECT_CONTEXT.md
  storyline.md
  paper.md
  writingrules.md
  workflow-dataflow.md
  .agents/
    skills/
  references/
  notes/
  reviews/
  outputs/
```

### AGENTS.md

`AGENTS.md` 是 Codex 的项目规则。每次让 Codex 做论文相关任务时，都应该让它先读取这个文件。

它规定：

- 不能编造实验、结果、引用、baseline、novelty；
- 使用某个 skill 前必须先读取对应的 `SKILL.md`；
- 修改 `paper.md` 或 `storyline.md` 前必须先给 edit plan；
- review-only、check-only、diagnose-only 任务不能修改正文；
- review 和 checker 输出必须写入 `reviews/`。

### PROJECT_CONTEXT.md

`PROJECT_CONTEXT.md` 是论文事实库。它决定 Codex 能写什么、不能写什么。

这里应该放：

- 论文标题、目标会议、作者；
- 研究问题；
- 方法概述；
- 数据集；
- baseline；
- 实验结果；
- metrics；
- contribution boundaries；
- 不能声称的内容；
- 已有引用和材料来源。

写论文前必须先填它。如果这里没有某个实验结果，Codex 就不能把那个结果写进论文。

### storyline.md

`storyline.md` 是论文逻辑主线，不是正文。

它回答：

- 为什么这个问题重要？
- 现有方法哪里不够？
- 本文的 insight 是什么？
- 方法为什么能解决这个 gap？
- 实验如何验证贡献？
- 哪些 claim 可以说，哪些不能说？

`storyline.md` 用来检查 Introduction、Related Work、Method 和 Experiments 是否互相对齐。

### paper.md

`paper.md` 是论文正文草稿。后续 Introduction、Related Work、Method、Experiments、Discussion、Conclusion 都写在这里。

不要一开始就让 Codex 直接写完整 `paper.md`。推荐一节一节来，每节先做 evidence inventory，再起草，再 review，再 revise。

### 三个核心文件的区别例子

同一项信息在三个文件里的写法不同：

```text
PROJECT_CONTEXT.md 写事实：
我们使用 HDFS、BGL 和 Thunderbird 数据集，评价指标包括 Precision、Recall 和 F1。

storyline.md 写逻辑：
跨域 log anomaly detection 的困难在于不同系统日志表面形式不同，但异常语义可能共享。

paper.md 写正文：
In cross-domain log anomaly detection, models must adapt to heterogeneous log formats while preserving semantic signals that may transfer across systems.
```

### references/

`references/` 放参考文献材料，例如：

```text
references/references.bib
references/relatedwork-notes.md
references/seed_references.md
references/papers/deeplog.md
references/papers/logrobust.md
```

没有 references，就不能让 Codex 编造 Related Work。缺 citation 时应写入 `reviews/relatedwork_citation_gaps.md`，而不是在正文中假装已经有引用。

### notes/

`notes/` 放中间分析结果，例如：

```text
notes/method_notes.md
notes/experiment_results.md
notes/datasets.md
notes/figures.md
notes/relatedwork_taxonomy.md
notes/socratic_discussion.md
```

这些文件不是最终论文正文，但它们是 Codex 起草正文的重要依据。

### reviews/

`reviews/` 放所有审阅报告和检查结果，例如：

```text
reviews/storyline_review.md
reviews/introduction_review.md
reviews/method_review.md
reviews/experiment_review.md
reviews/relatedwork_draft_plan.md
reviews/relatedwork_citation_gaps.md
reviews/revise_plan.md
reviews/submission_precheck.md
```

不要把 review 内容只留在聊天记录里。重要审阅结果要保存成文件，后续修改才能追踪。

### outputs/

`outputs/` 放最终导出文件，例如：

```text
outputs/latex_plan.md
outputs/tex/
outputs/final-paper.md
outputs/submission_package/
outputs/figures/
```

## 4. 使用前需要准备哪些输入材料

### 最低要求

至少准备以下信息：

- 一个研究主题；
- 初步方法想法；
- 目标任务；
- 数据集名称；
- 计划对比的 baseline；
- 预期实验指标；
- 已读过的部分相关论文。

如果连这些都没有，Codex 可以帮你提问和整理空缺，但不能替你发明研究内容。

如果还没有实验结果，也可以先创建项目并填写已知信息；此时只能做实验计划、证据缺口检查和章节结构规划，不能写 Results 或声称方法有效。

### 推荐材料

### 材料放置速查表

| 你手里有什么材料 | 推荐放到哪里 |
|---|---|
| 论文标题、目标会议、作者、研究方向 | `PROJECT_CONTEXT.md` 的 Basic Information |
| 研究问题、motivation、应用场景 | `PROJECT_CONTEXT.md` 的 Problem |
| 方法想法、模块、训练策略 | `PROJECT_CONTEXT.md` 的 Insight and Method；或 `notes/method_notes.md` |
| 数据集名称、数据规模、划分方式 | `PROJECT_CONTEXT.md` 的 Experiments；或 `notes/datasets.md` |
| baseline 名称和设置 | `PROJECT_CONTEXT.md` 的 Experiments；或 `notes/baseline_results.md` |
| 实验结果、表格数字、消融结果 | `PROJECT_CONTEXT.md` 的 Experiments；或 `notes/experiment_results.md` |
| BibTeX | `references/references.bib` |
| 相关论文列表 | `references/seed_references.md` 或 `references/relatedwork-notes.md` |
| 单篇论文阅读笔记 | `references/papers/<paper-name>.md` |
| 图表说明 | `notes/figures.md`；最终图放 `outputs/figures/` |
| reviewer comments | `reviews/reviewer_comments.md` |
| 实验日志、代码路径、运行记录 | `notes/experiment_logs.md` |
| Codex 审阅报告 | `reviews/<section>_review.md` |
| 最终导出版本或 LaTeX | `outputs/` |

1. 已有论文草稿

   放到：

   ```text
   paper.md
   notes/draft.md
   ```

2. 方法说明

   放到：

   ```text
   PROJECT_CONTEXT.md 的 Insight and Method
   notes/method_notes.md
   ```

3. 实验结果

   放到：

   ```text
   PROJECT_CONTEXT.md 的 Experiments
   notes/experiment_results.md
   references/tables/
   ```

4. 数据集说明

   放到：

   ```text
   PROJECT_CONTEXT.md
   notes/datasets.md
   ```

5. baseline 结果

   放到：

   ```text
   PROJECT_CONTEXT.md
   notes/baseline_results.md
   ```

6. 相关论文

   放到：

   ```text
   references/references.bib
   references/relatedwork-notes.md
   references/papers/<paper-name>.md
   ```

7. 图表

   放到：

   ```text
   notes/figures.md
   outputs/figures/
   ```

8. reviewer comments

   放到：

   ```text
   reviews/reviewer_comments.md
   ```

9. 实验日志或代码路径

   放到：

   ```text
   notes/experiment_logs.md
   ```

材料缺失时，Codex 应使用以下标记，而不是编造：

- `DATA_NEEDED`：需要实验数据或结果。
- `CITATION_NEEDED`：需要引用。
- `BASELINE_NEEDED`：需要 baseline 或 baseline 结果。
- `NEEDS_USER_EVIDENCE`：需要用户提供证据。
- `UNCLEAR_ASSUMPTION`：当前假设不清楚。

## 5. 如何创建一个新论文项目

不要在母版目录里写论文：

```text
E:\ai\papersmith
```

每篇论文都应该有自己的独立目录，例如：

```text
E:\ai\papers\log-anomaly-detection
```

标准创建命令：

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name log-anomaly-detection --target E:\ai\papers\log-anomaly-detection
```

创建后，所有 Codex 操作都应该在该论文项目目录中进行，而不是在 `papersmith` 母版目录中进行。

也就是说，打开 Codex 时，请把工作目录指向你的新论文项目，例如：

```text
E:\ai\papers\log-anomaly-detection
```

不要把 Codex 工作目录指向母版目录：

```text
E:\ai\papersmith
```

母版目录只用于复制模板和维护工具包，不用于写具体论文。

创建后检查 prompt：

```text
请检查当前论文项目结构是否完整。

要求：
1. 读取 AGENTS.md；
2. 确认是否包含 PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md、workflow-dataflow.md、.agents/skills/、references/、notes/、reviews/、outputs/；
3. 如果 .agents/skills/ 缺失，请报告 setup error；
4. 不要修改文件，只输出检查结果。
```

如果 Python 不能用，可以手动复制：

1. 新建论文项目目录。
2. 把 `E:\ai\papersmith\templates\paper-project` 里的全部内容复制进去。
3. 在项目里创建 `.agents/`。
4. 把 `E:\ai\papersmith\.agents\skills` 复制到项目的 `.agents\skills`。

## 6. 第一次打开 Codex 应该说什么

第一次打开一个论文项目时，不要让 Codex 直接写论文。先让它诊断项目状态。

第一条 prompt：

```text
请读取当前项目中的 AGENTS.md、PROJECT_CONTEXT.md、storyline.md、paper.md 和 writingrules.md。

现在不要修改任何文件。请先告诉我：

1. 当前项目是否是一个完整的论文项目；
2. PROJECT_CONTEXT.md 还缺哪些关键信息；
3. storyline.md 是否已经可以支持写作；
4. paper.md 当前有哪些章节；
5. 下一步最应该补充什么。

要求：不要编造研究内容，不要写论文正文，只做诊断。
```

## 7. 第一步：填写 PROJECT_CONTEXT.md

为什么先填 `PROJECT_CONTEXT.md`：

- 它决定 Codex 能写什么，不能写什么；
- 没有它，Codex 容易泛泛而谈；
- 所有实验结果、baseline、contribution 都应该先进入这里；
- 后续 storyline、draft、review、revise 都要以它为事实来源。

让 Codex 先提问的 prompt：

```text
请帮我填写 PROJECT_CONTEXT.md，但不要编造内容。

请先读取 AGENTS.md 和 PROJECT_CONTEXT.md，然后按以下类别向我提问：

1. Basic Information；
2. Source Materials；
3. Research Claim Boundaries；
4. Problem；
5. Existing Methods and Gap；
6. Insight and Method；
7. Experiments；
8. References。

要求：

* 每次最多问 10 个问题；
* 对我没有提供的信息标记 TODO；
* 不要写 paper.md；
* 不要修改 storyline.md。
```

根据你提供材料填入的 prompt：

```text
我现在提供论文项目信息。请根据这些信息更新 PROJECT_CONTEXT.md。

要求：

1. 只填写我明确提供的信息；
2. 不确定的地方保留 TODO 或 NEEDS_USER_EVIDENCE；
3. 不要发明实验结果；
4. 不要扩展贡献；
5. 修改前给出 edit plan，等我确认后再写入文件。

材料如下：
<在这里粘贴你的项目信息>
```

检查 `PROJECT_CONTEXT.md` 是否足够的 prompt：

```text
请读取 AGENTS.md 和 PROJECT_CONTEXT.md。

任务：检查 PROJECT_CONTEXT.md 是否足以支持论文写作。

要求：
1. 不修改文件；
2. 列出已经明确的信息；
3. 列出仍缺失的信息；
4. 标出 DATA_NEEDED、CITATION_NEEDED、BASELINE_NEEDED、NEEDS_USER_EVIDENCE；
5. 输出到 reviews/project_context_review.md。
```

## 8. 第二步：完善 storyline.md

`storyline.md` 不是正文，而是论文论证链。它帮助判断 Introduction、Related Work、Method 和 Experiments 是否对齐。

### 检查 storyline 完整性

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：检查 storyline.md 的完整性。

要求：

1. 读取 PROJECT_CONTEXT.md、storyline.md 和 writingrules.md；
2. 不要修改 storyline.md；
3. 不要补全空白内容；
4. 列出哪些部分已经有内容，哪些部分缺少用户输入；
5. 输出到 reviews/storyline_review.md。
```

### 完善 Problem 部分

```text
请使用 storyline-helper。

任务：根据 PROJECT_CONTEXT.md 完善 storyline.md 的 Problem 部分。

要求：

1. 先给 edit plan；
2. 只处理 Problem 部分；
3. 不要修改其他部分；
4. 不要新增 PROJECT_CONTEXT.md 中没有的研究内容；
5. 等我确认后再写入 storyline.md。
```

### 完善 Background 部分

```text
请使用 storyline-helper。

任务：根据 PROJECT_CONTEXT.md 完善 storyline.md 的 Background 部分。

要求：
1. 先读取 .agents/skills/storyline-helper/SKILL.md；
2. 只处理 Background / Required Concepts / Reader Assumptions；
3. 只使用 PROJECT_CONTEXT.md 中已有信息；
4. 缺失概念标记 TODO 或 NEEDS_USER_EVIDENCE；
5. 先给 edit plan，等我确认后再写入 storyline.md。
```

### 完善 Existing Methods 部分

```text
请使用 storyline-helper。

任务：完善 storyline.md 的 Existing Methods 部分。

要求：
1. 读取 PROJECT_CONTEXT.md、references/ 和 storyline.md；
2. 按方法族组织已有方法；
3. 不编造文献；
4. 缺少 citation 的方法族标记 CITATION_NEEDED；
5. 先给 edit plan，等我确认后只修改 Existing Methods 部分。
```

### 完善 Insight 部分

```text
请使用 storyline-helper。

任务：完善 storyline.md 的 Insight 部分。

要求：
1. 从 PROJECT_CONTEXT.md 中提取 core insight；
2. 说明 insight 依赖哪些条件；
3. 说明哪些情况下 insight 可能不成立；
4. 不夸大 novelty；
5. 先给 edit plan，确认后只修改 Insight 部分。
```

### 完善 Method 部分

```text
请使用 storyline-helper。

任务：完善 storyline.md 的 Method 部分。

要求：
1. 读取 PROJECT_CONTEXT.md 和 notes/method_notes.md，如果存在；
2. 列出 method overview、key components、technical challenges；
3. 不补造公式、算法或模块；
4. 缺失方法细节标记 NEEDS_USER_EVIDENCE；
5. 先给 edit plan，确认后只修改 Method 部分。
```

### 完善 Evaluation Plan 部分

```text
请使用 storyline-helper。

任务：完善 storyline.md 的 Evaluation Plan 部分。

要求：
1. 读取 PROJECT_CONTEXT.md 和 notes/experiment_results.md，如果存在；
2. 列出 RQ、datasets、baselines、metrics、expected evidence；
3. 缺少实验结果标记 DATA_NEEDED；
4. 缺少 baseline 标记 BASELINE_NEEDED；
5. 先给 edit plan，确认后只修改 Evaluation Plan 部分。
```

### 完善 Contribution Boundaries 部分

```text
请使用 storyline-helper。

任务：完善 storyline.md 的 Contribution Boundaries 部分。

要求：
1. 根据 PROJECT_CONTEXT.md 区分 supported claims、claims needing more evidence、claims not allowed；
2. 不强化 contribution；
3. 不新增没有实验支持的 conclusion；
4. 先给 edit plan，确认后只修改 Contribution Boundaries 部分。
```

## 9. 第三步：整理 references/ 和 Related Work 材料

Related Work 不应该从空白开始写。推荐顺序：

1. `relatedwork-finder`：找和登记文献类型、检查缺什么文献。
2. `relatedwork-summarizer`：总结已有文献材料。
3. `relatedwork-writer`：组织并起草 Related Work 章节。

没有 `references/` 或文献 notes，就不能写严肃的 Related Work。

### relatedwork-finder

```text
请使用 relatedwork-finder。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-finder/SKILL.md。

任务：根据 PROJECT_CONTEXT.md 和 storyline.md 检查当前 Related Work 还缺哪些文献类型。

要求：

1. 不联网；
2. 不编造论文；
3. 只基于当前 references/ 和项目文件；
4. 缺失文献标记 CITATION_NEEDED；
5. 输出到 reviews/relatedwork_missing_references.md。
```

### relatedwork-summarizer

```text
请使用 relatedwork-summarizer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-summarizer/SKILL.md。

任务：总结 references/ 中已有文献材料。

要求：

1. 不声称读过未提供全文的论文；
2. 区分 metadata、abstract、full-paper-read、user-provided-summary；
3. 输出到 references/relatedwork_summary.md；
4. 不修改 paper.md。
```

### relatedwork-writer：规划 Related Work

```text
请使用 relatedwork-writer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-writer/SKILL.md。

任务：为 paper.md 的 Related Work 章节制定写作计划。

要求：

1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md、references/ 和 notes/；
2. 使用 Planning / Review mode；
3. 不修改 paper.md；
4. 先建立 related work taxonomy；
5. 将 taxonomy 写入 notes/relatedwork_taxonomy.md；
6. 将写作计划写入 reviews/relatedwork_draft_plan.md；
7. 将 citation 缺口写入 reviews/relatedwork_citation_gaps.md；
8. 不要编造引用。
```

### relatedwork-writer：确认写入 Related Work

正式写入 `paper.md` 时，Related Work 必须是论文正文，不要把 review notes 放进正文。

如果当前只有 `PROJECT_CONTEXT.md` 里的引用名称，而没有 BibTeX、论文摘要或 related-work notes，Related Work 正文必须保守，只能使用项目中已有的 reference 名称做高层次方法族描述。所有引用缺口必须单独写入 `reviews/relatedwork_citation_gaps.md`，不要在正文里放 `CITATION_NEEDED` 或 `NEEDS_USER_EVIDENCE`，也不要编造 citation。

```text
我确认要将 Related Work 草稿写入 paper.md。

请使用 relatedwork-writer。

要求：

1. 在声称使用该 skill 前，先读取 .agents/skills/relatedwork-writer/SKILL.md；
2. 使用 Paper-writing mode；
3. 只修改 paper.md 的 Related Work 部分；
4. 如果没有 Related Work 章节，请插入到 Introduction 之后、Method 之前；
5. 不修改其他章节；
6. 只使用 references/ 和 PROJECT_CONTEXT.md 中已有引用名称；
7. Related Work 必须是正式论文正文；
8. 正文中不要出现 process notes、审阅提醒、current project context、this draft、CITATION_NEEDED、NEEDS_USER_EVIDENCE；
9. citation 缺口单独写入 reviews/relatedwork_citation_gaps.md；
10. 写入前后记录 paper.md 的 SHA256 hash；
11. 写入后输出修改摘要。
```

## 10. 第四步：起草 Introduction

不要一开始就让 Codex 写 Introduction。Introduction 需要 `PROJECT_CONTEXT.md` 和 `storyline.md` 支撑，还需要先做 evidence inventory。

### Introduction evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Introduction 起草前做 evidence inventory。

要求：

1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md 和 writingrules.md；
2. 不修改 paper.md；
3. 列出 Introduction 可使用的 problem、motivation、gap、insight、method overview、contribution、evidence；
4. 缺失项标记 DATA_NEEDED、CITATION_NEEDED 或 NEEDS_USER_EVIDENCE；
5. 输出到 reviews/evidence_inventory_introduction.md。
```

### 确认写入 Introduction

```text
我确认根据 evidence inventory 起草 Introduction。

请使用 paper-section-drafter。

要求：

1. 在声称使用该 skill 前，先读取 .agents/skills/paper-section-drafter/SKILL.md；
2. 只起草 Introduction；
3. 先给段落结构计划；
4. 等我确认后写入 paper.md；
5. 不要修改其他章节；
6. 不要新增没有证据的 contribution；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

## 11. 第五步：起草 Method

Method 需要的输入：

- 方法总体框架；
- 模块说明；
- 公式或算法；
- 训练策略；
- 输入输出；
- 与 baseline 的差别；
- 图示说明。

### Method evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Method 部分做 evidence inventory。

要求：

1. 读取 PROJECT_CONTEXT.md、storyline.md、notes/method_notes.md、paper.md 和 writingrules.md；
2. 不修改 paper.md；
3. 列出 method overview、components、inputs、outputs、training strategy、algorithm、formula、implementation details、difference from baselines；
4. 缺失项标记 NEEDS_USER_EVIDENCE；
5. 如果方法 claim 需要实验支持，标记 DATA_NEEDED；
6. 输出到 reviews/evidence_inventory_method.md。
```

### 确认写入 Method

```text
我确认根据 evidence inventory 起草 Method。

请使用 paper-section-drafter。

要求：

1. 只起草 Method；
2. 先给 Method 小节结构和每节证据来源；
3. 等我确认后写入 paper.md；
4. 不修改 Introduction、Related Work、Experiments 或 Conclusion；
5. 不编造公式、算法、模块或实现细节；
6. 对缺失细节保留 TODO 或 NEEDS_USER_EVIDENCE；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

## 12. 第六步：起草 Experiments

Experiments 需要的输入：

- datasets；
- preprocessing；
- baselines；
- metrics；
- implementation details；
- main results；
- ablation；
- efficiency；
- case study；
- statistical analysis，如果有。

### Experiments evidence inventory

```text
请使用 paper-section-drafter。

任务：为 Experiments 部分做 evidence inventory。

要求：

1. 在声称使用该 skill 前，先读取 .agents/skills/paper-section-drafter/SKILL.md；
2. 读取 PROJECT_CONTEXT.md、notes/experiment_results.md、paper.md；
3. 不修改 paper.md；
4. 列出 datasets、baselines、metrics、main results、ablation、efficiency、implementation details；
5. 缺失项标记 DATA_NEEDED 或 BASELINE_NEEDED；
6. 输出到 reviews/evidence_inventory_experiments.md。
```

### 确认写入 Experiments

```text
我确认根据 evidence inventory 起草 Experiments。

请使用 paper-section-drafter。

要求：

1. 只起草 Experiments；
2. 先给小节结构计划；
3. 只使用 PROJECT_CONTEXT.md 和 notes/experiment_results.md 中已有结果；
4. 不编造数字、表格、baseline 或 statistical test；
5. 结果不完整处保留 DATA_NEEDED 或 BASELINE_NEEDED；
6. 等我确认后写入 paper.md；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

## 13. 第七步：起草 Discussion / Limitation / Conclusion

### Discussion

Discussion 用来解释结果含义、适用条件和实际启示。不要把 Discussion 写成新的实验结果，也不要过度解释未验证现象。

```text
请使用 paper-section-drafter。

任务：为 Discussion 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、reviews/experiment_review.md；
2. 不修改 paper.md；
3. 列出可以讨论的 verified findings、practical implications、failure cases、open questions；
4. 不新增实验结论；
5. 输出到 reviews/evidence_inventory_discussion.md。
```

### Limitation

Limitation 不能隐藏缺陷。它应该清楚说明当前证据不能支持什么。

```text
请使用 paper-section-drafter。

任务：起草 Limitation 前做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md 的 Research Claim Boundaries；
2. 读取 storyline.md 的 Contribution Boundaries；
3. 列出必须承认的限制；
4. 不把限制写成未来工作广告；
5. 输出到 reviews/evidence_inventory_limitation.md。
```

### Conclusion

Conclusion 不要新增结果，不要新增 contribution。它只总结已经在正文和实验中出现过的内容。

```text
请使用 paper-section-drafter。

任务：起草 Conclusion。

要求：
1. 先读取 PROJECT_CONTEXT.md、storyline.md、paper.md；
2. 只总结正文已有内容；
3. 不新增实验结果；
4. 不新增 novelty；
5. 先给 edit plan，等我确认后只修改 Conclusion 部分。
```

### 确认写入 Discussion

```text
我确认根据 evidence inventory 起草 Discussion。

请使用 paper-section-drafter。

要求：
1. 在声称使用该 skill 前，先读取 .agents/skills/paper-section-drafter/SKILL.md；
2. 只修改 paper.md 的 Discussion 部分；
3. 只讨论正文和实验中已经出现的发现、适用条件和局限；
4. 不新增实验结果；
5. 不过度解释没有证据支持的现象；
6. 写入前先给 edit plan，等我确认后再修改 paper.md；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

### 确认写入 Limitation

```text
我确认根据 evidence inventory 起草 Limitation。

请使用 paper-section-drafter。

要求：
1. 在声称使用该 skill 前，先读取 .agents/skills/paper-section-drafter/SKILL.md；
2. 只修改 paper.md 的 Limitation 部分；如果 paper.md 没有 Limitation，请先给出插入位置计划；
3. 只写 PROJECT_CONTEXT.md 和 storyline.md 已经支持的限制；
4. 不隐藏缺陷；
5. 不把 limitation 写成夸大式 future work；
6. 写入前先给 edit plan，等我确认后再修改 paper.md；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

## 14. 第八步：审阅已有正文

核心 review skills：

- `markdown-review`：审阅某个章节的结构、表达和完整性。
- `problem-checker`：检查问题是否清楚、重要、具体。
- `novelty-checker`：检查 novelty 是否过度或缺 citation。
- `logic-checker`：检查逻辑链、矛盾和 claim-evidence gap。
- `clarity-checker`：检查可读性、术语和表达清晰度。
- `technical-depth-checker`：检查方法技术深度是否足够。
- `data-checker`：检查结果和数据 claim 是否有证据。
- `evaluation-protocol-checker`：检查实验协议、baseline、metric、validity。

### Introduction review

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 Introduction。

要求：

1. 不修改 paper.md；
2. 检查 problem 是否清楚；
3. 检查 motivation 是否充分；
4. 检查 gap 是否具体；
5. 检查 contribution 是否过度；
6. 检查是否缺 citation；
7. 输出到 reviews/introduction_review.md。
```

### Method review

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 Method。

要求：
1. 不修改 paper.md；
2. 检查 method overview 是否清楚；
3. 检查模块之间关系是否明确；
4. 检查输入输出、算法、训练策略是否完整；
5. 检查是否有 unsupported technical claim；
6. 输出到 reviews/method_review.md。
```

### Experiments review

```text
请使用 markdown-review。

任务：审阅 paper.md 的 Experiments。

要求：
1. 在声称使用该 skill 前，先读取 .agents/skills/markdown-review/SKILL.md；
2. 不修改 paper.md；
3. 检查 datasets、baselines、metrics、setup、main results、ablation、efficiency、limitations；
4. 缺失实验信息标记 DATA_NEEDED；
5. 缺失 baseline 标记 BASELINE_NEEDED；
6. 输出到 reviews/experiment_review.md。
```

### Related Work review

```text
请使用 markdown-review。

任务：审阅 paper.md 的 Related Work。

要求：
1. 在声称使用该 skill 前，先读取 .agents/skills/markdown-review/SKILL.md；
2. 不修改 paper.md；
3. 检查是否按方法族组织；
4. 检查是否逐篇流水账；
5. 检查是否过度批评已有工作；
6. 检查是否缺 citation；
7. 输出到 reviews/relatedwork_review.md。
```

### Checker suite

```text
请依次使用 problem-checker、novelty-checker、logic-checker、clarity-checker、technical-depth-checker、data-checker 和 evaluation-protocol-checker。

要求：
1. 每个 skill 使用前先读取对应 SKILL.md；
2. 不修改 paper.md；
3. 不修改 storyline.md；
4. 所有结果写入 reviews/checker_suite_report.md；
5. 对空白或证据不足内容，只报告缺失项，不补写内容。
```

## 15. 第九步：根据 review 逐条修改

`review-revise` 不是自动重写工具。它的正确用法是逐条处理 review issue。

每条 issue 都要：

1. 读取 review；
2. 提取一个 issue；
3. 判断证据是否足够；
4. 证据不足则标记 `NEEDS_USER_EVIDENCE`；
5. 证据足够则给 edit plan；
6. 等用户确认后再修改 `paper.md`；
7. 不修改无关章节。

Prompt：

```text
请使用 review-revise。

在声称使用该 skill 前，请先读取 .agents/skills/review-revise/SKILL.md。

任务：根据 reviews/introduction_review.md 逐条修改 Introduction。

要求：

1. 每次只处理一个 issue；
2. 先判断是否有足够证据；
3. 证据不足则标记 NEEDS_USER_EVIDENCE；
4. 证据足够则给 edit plan；
5. 等我确认后再修改 paper.md；
6. 不修改其他章节。
```

如果你还没有准备好让 Codex 改正文，可以先让它生成修改计划：

```text
请使用 review-revise。

任务：根据 reviews/introduction_review.md 生成 revise plan。

要求：
1. 读取 .agents/skills/review-revise/SKILL.md；
2. 不修改 paper.md；
3. 将每个 issue 拆成可执行步骤；
4. 标出每个 issue 需要的证据；
5. 输出到 reviews/revise_plan.md。
```

## 16. 第十步：投稿前检查

`submission-precheck` 用于投稿前检查。它不会保证录用，只能帮你找结构、证据、引用、实验和 claim 风险。

Prompt：

```text
请使用 submission-precheck。

在声称使用该 skill 前，请先读取 .agents/skills/submission-precheck/SKILL.md。

任务：对当前论文项目做投稿前检查。

要求：

1. 先检查项目结构；
2. 再检查 PROJECT_CONTEXT.md、storyline.md、paper.md 是否一致；
3. 检查 citation、figures、tables、experiments、limitations、claims；
4. 不修改 paper.md；
5. 输出到 reviews/submission_precheck.md。
```

## 17. 推荐论文生成顺序

推荐顺序：

1. 创建项目。
2. 填 `PROJECT_CONTEXT.md`。
3. 检查 `PROJECT_CONTEXT.md`。
4. 填 `storyline.md`。
5. 检查 `storyline.md`。
6. 整理 `references/`。
7. 建立 relatedwork taxonomy。
8. Introduction evidence inventory。
9. Introduction draft。
10. Related Work draft。
11. Method evidence inventory。
12. Method draft。
13. Experiments evidence inventory。
14. Experiments draft。
15. Discussion / Limitation / Conclusion。
16. 全文 review。
17. review-revise。
18. submission-precheck。
19. 导出 `outputs/`。

不建议直接按 Abstract -> Introduction -> Related Work 的传统阅读顺序写。原因是：

- Abstract 应该最后写，因为它需要总结最终稳定的 problem、method、results 和 conclusion。
- Introduction 需要 storyline 和 evidence inventory 支撑，否则容易写成泛泛的 motivation。
- Related Work 需要 references 支撑，否则容易编造 citation 或只写方法名。
- Experiments 必须基于真实结果，不能先写 conclusion 再补数据。

## 18. 核心 skills 使用表

| Skill | 作用 | 什么时候用 | 输入文件 | 输出文件 | 是否会修改 paper.md | 是否需要用户确认 | 风险等级 |
|---|---|---|---|---|---|---|---|
| `storyline-helper` | 检查或完善 storyline | 填写/检查论文逻辑主线 | `PROJECT_CONTEXT.md`, `storyline.md`, `notes/`, `references/` | `reviews/storyline_review.md` 或确认后的 `storyline.md` 修改 | 否 | 修改 storyline 时需要 | low（低） |
| `paper-section-drafter` | 按章节起草正文 | Introduction/Method/Experiments 等起草前后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, evidence files | `reviews/section_plan.md` 或确认后的 `paper.md` 修改 | 只有确认后 | 是 | low（低） |
| `relatedwork-finder` | 检查和登记相关文献需求 | Related Work 前期 | `storyline.md`, `paper.md`, `references/` | `references/relatedwork-notes.md` 或 `reviews/relatedwork_missing_references.md` | 否 | 通常不需要 | low（低） |
| `relatedwork-summarizer` | 总结已有文献 | 已有 BibTeX、abstract、paper notes | `references/`, `storyline.md`, `paper.md` | `references/relatedwork_summary.md` | 否 | 通常不需要 | low（低） |
| `relatedwork-writer` | 规划/起草 Related Work | references 已整理后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `writingrules.md`, `references/`, `notes/` | `notes/relatedwork_taxonomy.md`, `reviews/relatedwork_draft_plan.md`, `reviews/relatedwork_citation_gaps.md`, 确认后的 `paper.md` 修改 | 只有确认后 | 是 | medium（中） |
| `markdown-review` | 审阅章节结构和表达 | 每写完一个章节后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `writingrules.md` | `reviews/*_review.md` | 否 | 不需要 | low（低） |
| `review-revise` | 根据 review 逐条修改 | 有 review 文件后 | `reviews/`, `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md` | `reviews/revise_plan.md` 或确认后的修改 | 只有确认后 | 是 | low（低） |
| `experiment-analyzer` | 分析已有实验材料 | 有实验结果或日志后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `notes/`, `outputs/` | `reviews/experiment-analysis.md` | 默认否 | 修改正文时需要 | low（低） |
| `submission-precheck` | 投稿前检查 | 初稿稳定后 | 全部项目文件 | `reviews/submission_precheck.md` | 否 | 不需要 | low（低） |
| `problem-checker` | 检查问题定义 | 写完 Introduction 或 storyline 后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `references/` | `reviews/problem_review.md` | 否 | 不需要 | low（低） |
| `novelty-checker` | 检查 novelty 是否过度 | 写 contribution 后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `references/` | `reviews/novelty_review.md` | 否 | 不需要 | low（低） |
| `logic-checker` | 检查逻辑矛盾和 claim-evidence gap | 章节成形后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md` | `reviews/logic_review.md` | 否 | 不需要 | low（低） |
| `clarity-checker` | 检查清晰度和术语 | 章节审阅或润色前 | `paper.md`, `storyline.md`, `writingrules.md` | `reviews/clarity_review.md` | 否 | 不需要 | low（低） |
| `data-checker` | 检查数据和结果 claim | 写 Results/Experiments 后 | `paper.md`, `notes/`, `outputs/` | `reviews/data_review.md` | 否 | 不需要 | low（低） |
| `evaluation-protocol-checker` | 检查实验协议 | 实验设计或实验章节完成后 | `PROJECT_CONTEXT.md`, `storyline.md`, `paper.md`, `notes/` | `reviews/evaluation_protocol_review.md` | 否 | 不需要 | low（低） |

## 19. 高风险 skills 说明

以下 skills 普通同学默认不要直接用作自动写作工具：

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

### bogus-data-helper

风险：名字容易误导。它不能生成假数据，只能帮助规划结果表结构、检查数据缺口。

正确用法：

- planning mode；
- 输出 `notes/result_table_plan.md`；
- 输出 `reviews/data_gap_report.md`；
- 不写实验数字。

### humanizer

风险：可能把未经证据支持的文字润色得更像最终稿，导致来源不可追踪。

正确用法：

- 只能在事实已经稳定后做局部表达建议；
- 不改变 claim；
- 不新增结果或 citation；
- 修改前要 edit plan。

### mad-writer

风险：快速起草容易跳过 evidence inventory，写出看似完整但缺证据的段落。

正确用法：

- 只用于低风险片段的快速草案计划；
- 默认输出 `reviews/mad_writer_plan.md`；
- 不允许直接生成整篇论文。

### state-machine-markdown-helper

风险：流程较复杂，容易让新手误以为可以自动推进所有阶段。

正确用法：

- 只用于严格 staged drafting；
- 每一步都要检查 evidence gate；
- 不能跳过用户确认。

## 20. 常见错误和正确做法

### 1. 没填 PROJECT_CONTEXT.md 就让 Codex 写 Introduction

错误示例：

```text
直接帮我写 Introduction。
```

正确做法：

```text
请先读取 PROJECT_CONTEXT.md 和 storyline.md，为 Introduction 做 evidence inventory。不要修改 paper.md。
```

### 2. 没 references 就写 Related Work

错误示例：

```text
帮我写 Related Work，引用你自己找。
```

正确做法：

```text
请检查 references/ 中已有文献，并把缺失文献类型写入 reviews/relatedwork_missing_references.md。不要编造 citation。
```

### 3. 没实验结果就写 Results

错误示例：

```text
帮我写实验结果，结果应该比 baseline 好。
```

正确做法：

```text
请读取 PROJECT_CONTEXT.md 和 notes/experiment_results.md，列出已有结果和 DATA_NEEDED，不要编造数字。
```

### 4. 没有 edit plan 就让 Codex 直接改 paper.md

错误示例：

```text
直接把 paper.md 改好。
```

正确做法：

```text
请先给出 edit plan，说明修改哪个章节、使用哪些证据、风险是什么。等我确认后再改 paper.md。
```

### 5. 让 Codex 一次性重写整篇论文

错误示例：

```text
把整篇论文重写成顶会水平。
```

正确做法：

```text
请先审阅 Introduction，并输出 reviews/introduction_review.md。不要修改 paper.md。
```

### 6. review 文件没有保存到 reviews/

错误示例：

```text
你在聊天里告诉我问题就行。
```

正确做法：

```text
请把审阅结果写入 reviews/introduction_review.md，使用稳定文件名。
```

### 7. 把 papersmith 母版当作论文项目来写

错误示例：

```text
我在 E:\ai\papersmith\paper.md 里写论文。
```

正确做法：

```text
先创建独立项目：E:\ai\papers\<paper-name>，所有论文内容放在该项目里。
```

### 8. 忘记复制 .agents/skills/

错误示例：

```text
项目里只有 paper.md，没有 .agents/skills/。
```

正确做法：

```text
请检查项目结构。如果 .agents/skills/ 缺失，报告 setup error，不要继续写论文。
```

### 9. citation 不足但没有标记 CITATION_NEEDED

错误示例：

```text
直接写“已有大量研究表明……”，但没有引用。
```

正确做法：

```text
请把缺 citation 的 claim 写入 reviews/relatedwork_citation_gaps.md，正文不要编造引用。
```

### 10. 把 Codex 生成的文字当成最终稿不审查

错误示例：

```text
Codex 写完了，我直接提交。
```

正确做法：

```text
请使用 markdown-review、logic-checker、data-checker 和 submission-precheck 审阅全文，并把结果写入 reviews/。
```

## 21. 一篇 log anomaly detection 论文的示例流程

假设你要写一篇 log anomaly detection 论文，项目名为 `log-anomaly-detection`。

### 创建项目

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name log-anomaly-detection --target E:\ai\papers\log-anomaly-detection
```

### 填 PROJECT_CONTEXT.md

```text
请读取 AGENTS.md 和 PROJECT_CONTEXT.md。

我正在写一篇 log anomaly detection 论文。请按 Basic Information、Problem、Existing Methods and Gap、Insight and Method、Experiments、References 向我提问。

要求：
1. 每次最多问 10 个问题；
2. 不编造内容；
3. 不修改 paper.md。
```

### 检查 storyline

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：检查 storyline.md 是否能支持 log anomaly detection 论文写作。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、writingrules.md；
2. 不修改 storyline.md；
3. 输出到 reviews/storyline_review.md。
```

### 整理 related work

```text
请使用 relatedwork-finder。

任务：根据 PROJECT_CONTEXT.md 和 storyline.md 检查 log anomaly detection 的 Related Work 缺哪些文献类型。

要求：
1. 不联网；
2. 不编造论文；
3. 输出到 reviews/relatedwork_missing_references.md。
```

### 写 Introduction

```text
请使用 paper-section-drafter。

任务：为 Introduction 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md；
2. 列出 problem、motivation、gap、insight、method overview、contribution；
3. 缺失项标记 DATA_NEEDED、CITATION_NEEDED、NEEDS_USER_EVIDENCE；
4. 输出到 reviews/evidence_inventory_introduction.md；
5. 不修改 paper.md。
```

### 写 Related Work

```text
请使用 relatedwork-writer。

任务：为 log anomaly detection 论文规划 Related Work。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、references/ 和 notes/；
2. 建立 taxonomy，包括 log parsing、deep log anomaly detection、robust/semi-supervised methods、transfer/adaptation、LLM-based log analysis；
3. 输出 notes/relatedwork_taxonomy.md；
4. 输出 reviews/relatedwork_draft_plan.md；
5. 输出 reviews/relatedwork_citation_gaps.md；
6. 不修改 paper.md。
```

确认写入：

```text
我确认要写入 Related Work。

请使用 relatedwork-writer 的 Paper-writing mode。

要求：
1. 只修改 paper.md 的 Related Work 部分；
2. 正文必须是正式论文正文；
3. 不出现 process notes、CITATION_NEEDED、NEEDS_USER_EVIDENCE；
4. citation 缺口写入 reviews/relatedwork_citation_gaps.md；
5. 写入前后记录 hash。
```

### 写 Method

```text
请使用 paper-section-drafter。

任务：为 Method 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、notes/method_notes.md；
2. 列出 model overview、log representation、main modules、training strategy、adaptation strategy；
3. 缺失细节标记 NEEDS_USER_EVIDENCE；
4. 输出到 reviews/evidence_inventory_method.md。
```

### 写 Experiments

```text
请使用 paper-section-drafter。

任务：为 Experiments 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、notes/experiment_results.md；
2. 列出 datasets、baselines、metrics、main results、ablation、efficiency；
3. 缺失结果标记 DATA_NEEDED；
4. 缺失 baseline 标记 BASELINE_NEEDED；
5. 输出到 reviews/evidence_inventory_experiments.md。
```

### 审阅

```text
请使用 markdown-review。

任务：审阅 paper.md 当前所有已有正文。

要求：
1. 不修改 paper.md；
2. 按章节输出问题；
3. 检查 problem、gap、method、experiments、related work、claims；
4. 输出到 reviews/full_draft_review.md。
```

### 修改

```text
请使用 review-revise。

任务：根据 reviews/full_draft_review.md 逐条修改。

要求：
1. 每次只处理一个 issue；
2. 先判断证据是否足够；
3. 先给 edit plan；
4. 等我确认后再修改 paper.md。
```

### Precheck

```text
请使用 submission-precheck。

任务：对 log anomaly detection 论文项目做投稿前检查。

要求：
1. 先检查项目结构；
2. 再检查 PROJECT_CONTEXT.md、storyline.md、paper.md 一致性；
3. 检查 citation、figures、tables、experiments、limitations、claims；
4. 输出到 reviews/submission_precheck.md；
5. 不修改 paper.md。
```

## 22. 给课题组同学的最小使用版本

如果你只想先跑通最小流程，按下面 10 步来：

1. 创建项目。
2. 填 `PROJECT_CONTEXT.md`。
3. 填 `storyline.md`。
4. 放 references 到 `references/`。
5. 让 Codex 做 evidence inventory。
6. 让 Codex 起草一个 section。
7. 让 Codex review。
8. 让 Codex revise。
9. 运行 `submission-precheck`。
10. 发给导师或高年级同学检查。

最小流程 prompt：

```text
请读取 AGENTS.md，并检查 PROJECT_CONTEXT.md、storyline.md、paper.md、references/ 是否足够支持起草一个章节。

要求：
1. 不修改文件；
2. 列出最适合先写的一个章节；
3. 列出该章节缺少哪些证据；
4. 推荐下一步 prompt。
```

## 23. 维护者说明

维护者更新工具包时，应遵守以下规则：

- 新增 skill 后，必须更新 `docs/SKILL_INDEX.md`。
- 更新 `docs/SKILL_COMPATIBILITY_MATRIX.md`，说明兼容性和风险等级。
- 如果新增或修改 prompt 模式，更新 `docs/PROMPT_COOKBOOK.md`、`docs/STUDENT_QUICKSTART.md` 和本手册。
- 做内部测试，至少创建一个干净测试项目。
- 检查所有 skill 是否有 `name` 和 `description`：

```powershell
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith\.agents\skills
```

- 检查模板项目结构：

```powershell
python E:\ai\papersmith\scripts\check_project_structure.py <test-project-path>
```
