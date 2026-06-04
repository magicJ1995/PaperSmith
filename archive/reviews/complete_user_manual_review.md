# COMPLETE_USER_MANUAL.md 新手视角审阅报告

审阅对象：`E:\ai\papersmith\docs\COMPLETE_USER_MANUAL.md`

审阅视角：第一次使用 PaperSmith 的课题组同学，不假设了解 Codex、Agent、Skill、CoPaper 或 OpenCode。

## 总体结论

这份手册整体可以作为课题组内部正式使用说明。它清楚说明了工具定位、目录结构、输入材料、推荐写作顺序、常用 prompt、核心 skill、高风险 skill 和常见错误。新同学如果愿意从头读完，基本可以照着创建项目、填写 `PROJECT_CONTEXT.md`、完善 `storyline.md`、整理 references、逐节写 `paper.md`、做 review 和 precheck。

主要问题不是内容缺失，而是文档太长、信息密度高。第一次使用者可能在第 5 节之前已经理解工具，但还不知道“我现在马上该复制哪条 prompt”。建议增加一个更短的 `STUDENT_ONE_PAGE_GUIDE.md` 作为入口，把完整手册作为详细参考。

## 逐项检查

### 1. 是否能看懂这个工具是干什么的

通过。

第 1 节已经明确说明：

- 这是科研论文写作的本地工作流包；
- 不是自动写论文机器；
- 不是 copaper.ai webapp；
- 不依赖 copaper-opencode 插件；
- 核心目标是把写作拆成可检查、可审阅、可追踪步骤。

对新手来说，“不是自动写论文机器，而是把论文写作拆成可检查步骤”这句话很有效。

建议改进：可以在开头再加一个“你可以把它理解成：论文项目文件夹 + Codex 使用规则 + 一组可复制 prompt”的一句话解释，降低 Agent/Skill 的陌生感。

### 2. 是否知道第一步该做什么

基本通过。

文档第 5 节说明先创建独立论文项目，第 6 节给了第一次打开 Codex 的 prompt，第 7 节说明先填 `PROJECT_CONTEXT.md`。

潜在问题：新手可能会在“准备材料”和“创建项目”之间犹豫，不知道是否必须先准备齐全部材料才能创建项目。实际应该是：先创建项目，再逐步把已有材料填进去。

建议改进：在开头或第 5 节前增加“如果你什么都不确定，先创建项目，然后填能填的信息；不知道的地方留 TODO”。

### 3. 是否知道需要准备哪些输入材料

通过。

第 4 节按“最低要求”和“推荐材料”列出了研究主题、方法想法、任务、数据集、baseline、指标、相关论文，以及草稿、方法说明、实验结果、数据集说明、baseline 结果、图表、reviewer comments、实验日志等。

这部分足够具体。

建议改进：最低要求里可以补一句“如果还没有实验结果，也可以创建项目，但不能写 Results，只能写计划和缺口”。

### 4. 是否知道每类材料放在哪里

通过。

第 3 节和第 4 节都明确说明了：

- 文献放 `references/`；
- 中间笔记放 `notes/`；
- 审阅结果放 `reviews/`；
- 导出产物放 `outputs/`；
- 实验结果放 `PROJECT_CONTEXT.md` 或 `notes/experiment_results.md`；
- reviewer comments 放 `reviews/reviewer_comments.md`。

建议改进：可以增加一个“材料放置速查表”，例如两列表格“我有什么材料 / 放到哪里”。这对新手比长段说明更快。

### 5. 是否知道 PROJECT_CONTEXT.md、storyline.md、paper.md 的区别

通过。

第 3 节分别解释了：

- `PROJECT_CONTEXT.md` 是论文事实库；
- `storyline.md` 是论文逻辑主线，不是正文；
- `paper.md` 是论文正文草稿。

第 7 节和第 8 节进一步强调先填 `PROJECT_CONTEXT.md`，再完善 `storyline.md`。

建议改进：可以增加一个非常短的对照例子：

- `PROJECT_CONTEXT.md` 写“我们使用 HDFS/BGL/Thunderbird，指标是 F1”；
- `storyline.md` 写“为什么跨域泛化是核心问题”；
- `paper.md` 写正式论文段落。

### 6. 是否知道论文生成顺序

通过。

第 17 节给出了 19 步推荐顺序，并解释了为什么不建议按 Abstract -> Introduction -> Related Work 的阅读顺序写。

这部分对新手很有价值。

建议改进：第 22 节有 10 步最小流程，可以在文档开头提前引用：“如果你只想快速开始，先看第 22 节”。

### 7. 是否每个论文部分都有可复制 prompt

基本通过。

文档为以下部分给出了可复制 prompt：

- 项目结构检查；
- 第一次诊断；
- 填 `PROJECT_CONTEXT.md`；
- 检查和完善 `storyline.md`；
- Related Work planning 和 writing；
- Introduction evidence inventory 和 writing；
- Method evidence inventory 和 writing；
- Experiments evidence inventory 和 writing；
- Discussion、Limitation、Conclusion；
- review；
- revise；
- submission precheck；
- log anomaly detection 示例流程。

轻微缺口：Discussion、Limitation 的 prompt 主要是 evidence inventory，Conclusion 有写入 prompt；Discussion/Limitation 没有完整“确认写入 paper.md”的 prompt。对新手来说，可能会不知道如何从 inventory 进入正式正文写入。

建议改进：给 Discussion 和 Limitation 各补一条“我确认写入 paper.md，只修改 Discussion/Limitation 部分”的 prompt。

### 8. 是否知道如何调用 skill

通过。

文档反复使用格式：

```text
请使用 <skill-name>。
在声称使用该 skill 前，请先读取 .agents/skills/<skill-name>/SKILL.md。
```

这对 Codex 使用是清楚的。

潜在问题：新手可能不知道“当前项目目录”是什么意思，尤其在 Codex 中需要打开哪个 folder。建议在第 5 或第 6 节增加一句：“打开 Codex 时，请让工作目录指向你的论文项目，例如 `E:\ai\papers\my-paper`，不要指向母版目录。”

### 9. 是否知道哪些 skill 是高风险

通过。

第 19 节明确列出：

- `bogus-data-helper`
- `humanizer`
- `mad-writer`
- `state-machine-markdown-helper`

并说明了为什么高风险、默认怎么用、不能做什么。

建议改进：可以在核心 skill 表里也用中文标注风险等级，当前表里风险等级是 `low/medium`，第 19 节是中文解释。为了新手一致性，可以写成 `low（低）`、`medium（中）`、`high（高）`。

### 10. 是否存在术语过多、跳步、过于抽象的问题

存在少量问题，但不影响作为详细手册使用。

术语较多的地方：

- `Codex-compatible Agent Skill`
- `evidence inventory`
- `edit plan`
- `Planning / Review mode`
- `Paper-writing mode`
- `claim-evidence gap`
- `taxonomy`

这些术语在上下文里能推断，但第一次使用者可能需要一个小词典。

建议改进：在第 1 节或附录增加“常见术语解释”：

- skill：一份本地说明书，告诉 Codex 某类任务怎么做；
- evidence inventory：写正文前先列出已有证据和缺失证据；
- edit plan：修改前的计划；
- review-only：只审阅，不改正文；
- citation gap：需要引用但当前没有引用的地方。

跳步问题：

- 第 5 节创建项目后，没有明确要求“切换到新项目目录再和 Codex 对话”。虽然后文有提到，但可以更醒目。
- 第 9 节 Related Work 写入 prompt 里说“只使用 references/ 和 PROJECT_CONTEXT.md 中已有引用名称”，但如果 `references/` 为空，只靠 `PROJECT_CONTEXT.md` 中的引用名称能否写，容易让新手误解。建议补一句：“这种情况下只能写保守正文，引用缺口必须进入 reviews/。”

过于抽象的问题不严重。整体是 SOP 风格，不是官方概念文档。

### 11. 是否适合直接发给 1 到 2 个同学试用

建议可以发给 1 到 2 个同学试用，但最好同时提供一个更短的一页版入口。

完整手册适合做正式说明和查阅文档，但新同学第一次打开时可能被 45KB 的内容吓到。更好的试用方式是：

1. 先发 `STUDENT_ONE_PAGE_GUIDE.md`；
2. 让同学按一页版创建项目和填 `PROJECT_CONTEXT.md`；
3. 遇到具体步骤再查 `COMPLETE_USER_MANUAL.md` 对应章节；
4. 让维护者收集第一次使用时卡住的位置。

## 需要修改的地方

建议优先修改：

1. 在开头增加“快速开始路径”：第一次使用只看第 5、6、7、22 节。
2. 在第 5 节明确说明：创建项目后，要在 Codex 中打开新论文项目目录，不要打开母版目录。
3. 增加“材料放置速查表”，用表格说明不同材料放到哪个文件。
4. 增加“常见术语解释”，解释 skill、evidence inventory、edit plan、review-only、citation gap、taxonomy。
5. 给 Discussion 和 Limitation 增加确认写入 `paper.md` 的 prompt。
6. 在 Related Work 写入部分强调：如果只有引用名称、没有 BibTeX 或 notes，正文要保守，引用缺口必须单独写到 `reviews/relatedwork_citation_gaps.md`。
7. 在核心 skill 表中将风险等级改成更适合中文新手的形式，例如 `low（低）`、`medium（中）`、`high（高）`。

可选修改：

1. 在第 1 节增加一句非常通俗的定义：“它就是一个论文项目文件夹模板，加上一组告诉 Codex 如何安全写论文的规则。”
2. 在第 22 节补充“如果你只想开始，请先复制这里的最小流程 prompt”。
3. 给 `PROJECT_CONTEXT.md`、`storyline.md`、`paper.md` 增加一个三行对比例子。

## 是否建议生成 STUDENT_ONE_PAGE_GUIDE.md

建议生成。

理由：

- 完整手册适合查阅，但不适合作为第一次上手的唯一入口。
- 一页版可以只保留“创建项目 -> 填 PROJECT_CONTEXT.md -> 检查 storyline -> 放 references -> evidence inventory -> 起草一节 -> review -> revise -> precheck”的最小路径。
- 一页版应只包含 5 到 8 条最常用 prompt，不介绍全部 skill。
- 一页版能降低试用门槛，适合发给 1 到 2 个同学先跑通流程。

建议文件名：

```text
E:\ai\papersmith\docs\STUDENT_ONE_PAGE_GUIDE.md
```

## 是否建议配一个 demo 项目截图或目录示例

建议配一个目录示例，截图可选。

更推荐先配“文本目录示例”，因为它可以直接放进 Markdown，不依赖图片：

```text
E:\ai\papers\my-paper
  AGENTS.md
  PROJECT_CONTEXT.md
  storyline.md
  paper.md
  writingrules.md
  .agents\skills\
  references\
    references.bib
    relatedwork-notes.md
  notes\
    method_notes.md
    experiment_results.md
  reviews\
    storyline_review.md
    introduction_review.md
  outputs\
```

如果要给完全不熟悉文件夹结构的同学试用，可以再配一张 Windows Explorer 截图。但第一版试用不强制需要截图，文本目录示例已经足够。

## 试用建议

可以进入 1 到 2 名同学的小范围试用阶段，但建议试用任务不要从“写完整论文”开始，而是从以下任务开始：

1. 创建一个新论文项目。
2. 填 `PROJECT_CONTEXT.md` 的 Basic Information、Problem、Method、Experiments。
3. 让 Codex 检查 `storyline.md` 并输出 `reviews/storyline_review.md`。
4. 放 3 到 5 篇 references，测试 `relatedwork-writer` 的 Planning / Review mode。
5. 对 Introduction 做 evidence inventory。
6. 起草一个小节并 review。

这样可以验证新手是否真正理解“先证据、后正文；先 review、后 revise；缺证据不编造”的使用原则。
