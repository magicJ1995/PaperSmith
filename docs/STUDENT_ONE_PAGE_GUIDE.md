# Student One-Page Guide

这份指南给第一次使用 Codex 和 PaperSmith 的课题组同学。先按这里跑通最小流程，遇到具体问题再查 `docs/COMPLETE_USER_MANUAL.md`。

## 1. 这个工具一句话是什么

PaperSmith 是一个论文项目模板 + Codex 写作规则 + 一组论文写作 skills，用来帮助你按步骤整理、写作、审阅和修改论文。

不要在母版目录里写论文：

```text
E:\ai\papersmith
```

每篇论文都要创建自己的项目目录，例如：

```text
E:\ai\papers\my-paper
```

打开 Codex 时，也要让工作目录指向你自己的论文项目目录，而不是母版目录。

## 2. 第一次使用只做这 6 步

1. 创建自己的论文项目。
2. 打开 Codex，并让工作目录指向自己的论文项目。
3. 填 `PROJECT_CONTEXT.md`。
4. 检查 `storyline.md`。
5. 对一个章节做 evidence inventory。
6. 起草一个小节，然后 review 和 revise。

## 3. 创建项目命令

在 PowerShell 或终端中运行：

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name my-paper --target E:\ai\papers\my-paper
```

创建后确认你打开的是：

```text
E:\ai\papers\my-paper
```

不要打开：

```text
E:\ai\papersmith
```

## 4. 第一次打开 Codex 复制这条

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

## 5. 填 PROJECT_CONTEXT.md 复制这条

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

1. 每次最多问 10 个问题；
2. 对我没有提供的信息标记 TODO；
3. 不要写 paper.md；
4. 不要修改 storyline.md。
```

如果你已经有材料，可以这样说：

```text
我现在提供论文项目信息。请根据这些信息更新 PROJECT_CONTEXT.md。

要求：
1. 只填写我明确提供的信息；
2. 不确定的地方保留 TODO 或 NEEDS_USER_EVIDENCE；
3. 不要发明实验结果；
4. 不要扩展贡献；
5. 修改前给出 edit plan，等我确认后再写入文件。

材料如下：
<粘贴你的材料>
```

## 6. 检查 storyline.md 复制这条

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

## 7. 起草 Introduction 前复制这条

先做 evidence inventory，不要直接让 Codex 写 Introduction。

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

确认要写入 Introduction 时再复制：

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

## 8. 审阅 Introduction 复制这条

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

## 9. 根据审阅修改复制这条

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

## 10. 你不能让 Codex 做什么

不要让 Codex 做这些事：

- 不能编造实验结果、数字、图表或结论。
- 不能编造引用、作者、年份、venue、DOI 或 BibTeX。
- 不能编造 baseline、数据集或 baseline 结果。
- 不能一口气写整篇论文。
- 不能没有 edit plan 就改 `paper.md` 或 `storyline.md`。
- 不能把 `reviews/` 里的审阅内容、process notes、`CITATION_NEEDED`、`NEEDS_USER_EVIDENCE` 混进 `paper.md` 正文。
- 缺实验时标记 `DATA_NEEDED`。
- 缺引用时标记 `CITATION_NEEDED`。
- 缺 baseline 时标记 `BASELINE_NEEDED`。
- 证据不足时标记 `NEEDS_USER_EVIDENCE`。

## 11. 出问题时发给维护者哪些文件

把这些文件发给维护者，方便定位问题：

- `PROJECT_CONTEXT.md`
- `storyline.md`
- `paper.md`
- `reviews/*.md`
- `AGENTS.md`
- `.agents/skills/<出问题的skill>/SKILL.md`

如果是项目创建失败，也附上终端输出，以及以下检查命令的结果：

```powershell
python E:\ai\papersmith\scripts\check_project_structure.py E:\ai\papers\my-paper
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papers\my-paper\.agents\skills
```

