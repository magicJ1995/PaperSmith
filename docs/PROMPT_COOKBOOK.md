# Prompt Cookbook

## 0. 使用前说明

这些 prompts 应在具体论文项目目录中使用，例如：

```text
E:\ai\papers\my-paper
```

不要在母版目录中写论文：

```text
E:\ai\papersmith
```

每条 prompt 都可以直接复制给 Codex。凡是信息不足，Codex 应标记 `DATA_NEEDED`、`CITATION_NEEDED`、`BASELINE_NEEDED`、`NEEDS_USER_EVIDENCE`，不要编造实验、数据集、baseline、citation、novelty 或 conclusion。

所有 review/checker 输出写入 `reviews/`。所有 notes 输出写入 `notes/`。citation gap、missing evidence、missing experiment 不要写进 `paper.md` 正文，应写入 `reviews/` 或 `notes/`。

## 1. 项目初始化与结构检查

### 检查当前项目结构

```text
请检查当前论文项目结构是否完整。

要求：
1. 读取 AGENTS.md；
2. 确认是否包含 AGENTS.md、PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md、workflow-dataflow.md、.agents/skills/、references/、notes/、reviews/、outputs/；
3. 检查 .agents/skills/ 是否存在；
4. 不修改任何文件；
5. 输出检查结果到 reviews/project_structure_check.md。
```

### 检查所有 skills 是否存在

```text
请检查当前项目中的 .agents/skills/。

要求：
1. 不修改任何文件；
2. 列出所有 skill 目录；
3. 检查每个 skill 是否包含 SKILL.md；
4. 检查是否缺少 name 或 description；
5. 输出到 reviews/skill_metadata_check.md。
```

## 2. PROJECT_CONTEXT.md 填写与检查

### 列出 PROJECT_CONTEXT.md 缺失信息

```text
请读取 AGENTS.md 和 PROJECT_CONTEXT.md。

任务：检查 PROJECT_CONTEXT.md 还缺哪些关键信息。

要求：
1. 不修改文件；
2. 按 Basic Information、Source Materials、Research Claim Boundaries、Problem、Existing Methods and Gap、Insight and Method、Experiments、References 分类；
3. 对缺失项标记 TODO、DATA_NEEDED、CITATION_NEEDED、BASELINE_NEEDED 或 NEEDS_USER_EVIDENCE；
4. 输出到 reviews/project_context_review.md。
```

### 根据用户材料更新 PROJECT_CONTEXT.md

```text
我现在提供论文项目信息。请根据这些信息更新 PROJECT_CONTEXT.md。

要求：
1. 只填写我明确提供的信息；
2. 不确定的地方保留 TODO 或 NEEDS_USER_EVIDENCE；
3. 不要发明实验结果；
4. 不要扩展 contribution；
5. 先给 edit plan；
6. 等我确认后再写入 PROJECT_CONTEXT.md；
7. 不修改 storyline.md、paper.md 或其他文件。

材料如下：
<粘贴材料>
```

### 检查 Research Claim Boundaries 是否过度

```text
请读取 AGENTS.md、PROJECT_CONTEXT.md、storyline.md 和 paper.md。

任务：检查 Research Claim Boundaries 是否过度。

要求：
1. 不修改文件；
2. 列出 supported claims、claims needing more evidence、claims not allowed；
3. 检查是否存在没有实验、citation 或用户证据支持的 novelty/conclusion；
4. 输出到 reviews/claim_boundary_review.md。
```

### 检查 Experiments 是否足够支持 Results

```text
请读取 PROJECT_CONTEXT.md、notes/experiment_results.md（如果存在）和 paper.md。

任务：检查 Experiments 信息是否足够支持写 Results。

要求：
1. 不修改文件；
2. 检查 datasets、baselines、metrics、main results、ablation、efficiency、implementation details；
3. 缺失实验标记 DATA_NEEDED；
4. 缺失 baseline 标记 BASELINE_NEEDED；
5. 输出到 reviews/experiment_readiness_review.md。
```

## 3. storyline.md 检查与完善

### 检查 storyline.md 完整性

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：检查 storyline.md 的完整性。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md 和 writingrules.md；
2. 不修改 storyline.md；
3. 不补全空白内容；
4. 列出哪些部分已有内容，哪些部分缺少用户输入；
5. 输出到 reviews/storyline_review.md。
```

### 完善 Problem

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：根据 PROJECT_CONTEXT.md 完善 storyline.md 的 Problem 部分。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 Problem 部分；
4. 不修改其他章节；
5. 不新增 PROJECT_CONTEXT.md 中没有的研究内容。
```

### 完善 Background

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：根据 PROJECT_CONTEXT.md 完善 storyline.md 的 Background 部分。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 Background / Required Concepts / Reader Assumptions；
4. 不修改其他章节；
5. 缺失概念标记 NEEDS_USER_EVIDENCE。
```

### 完善 Existing Methods and Gap

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：完善 storyline.md 的 Existing Methods and Gap 部分。

要求：
1. 读取 PROJECT_CONTEXT.md、references/ 和 storyline.md；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Existing Methods and Gap 部分；
5. 不修改其他章节；
6. 不编造文献；
7. 缺少 citation 的方法族写入 reviews/storyline_citation_gaps.md。
```

### 完善 Insight

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：完善 storyline.md 的 Insight 部分。

要求：
1. 从 PROJECT_CONTEXT.md 中提取 core insight；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Insight 部分；
5. 不修改其他章节；
6. 不夸大 novelty。
```

### 完善 Method

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：完善 storyline.md 的 Method 部分。

要求：
1. 读取 PROJECT_CONTEXT.md 和 notes/method_notes.md（如果存在）；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Method 部分；
5. 不修改其他章节；
6. 不补造公式、算法或模块。
```

### 完善 Evaluation Plan

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：完善 storyline.md 的 Evaluation Plan 部分。

要求：
1. 读取 PROJECT_CONTEXT.md 和 notes/experiment_results.md（如果存在）；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Evaluation Plan 部分；
5. 不修改其他章节；
6. 缺少实验标记 DATA_NEEDED；
7. 缺少 baseline 标记 BASELINE_NEEDED。
```

### 完善 Contribution Boundaries

```text
请使用 storyline-helper。

在声称使用该 skill 前，请先读取 .agents/skills/storyline-helper/SKILL.md。

任务：完善 storyline.md 的 Contribution Boundaries 部分。

要求：
1. 根据 PROJECT_CONTEXT.md 区分 supported claims、claims needing more evidence、claims not allowed；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Contribution Boundaries 部分；
5. 不修改其他章节；
6. 不强化没有证据支持的 contribution。
```

## 4. Introduction 写作

### Introduction evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Introduction 起草前做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md 和 writingrules.md；
2. 不修改 paper.md；
3. 列出 problem、motivation、gap、insight、method overview、contribution、evidence；
4. 缺失项标记 DATA_NEEDED、CITATION_NEEDED 或 NEEDS_USER_EVIDENCE；
5. 输出到 reviews/evidence_inventory_introduction.md。
```

### Introduction paragraph plan

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Introduction 制定 paragraph plan。

要求：
1. 读取 reviews/evidence_inventory_introduction.md、PROJECT_CONTEXT.md、storyline.md 和 paper.md；
2. 不修改 paper.md；
3. 给出每段的主张、证据来源和缺失证据；
4. 输出到 reviews/introduction_paragraph_plan.md。
```

### 写入 Introduction

```text
我确认写入 Introduction。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 paper.md 的 Introduction 部分；
4. 不修改其他章节；
5. 不新增没有证据的 contribution；
6. citation gap、missing evidence 不写进正文，单独写入 reviews/introduction_missing_items.md；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

### 审阅 Introduction

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 Introduction。

要求：
1. 不修改 paper.md；
2. 检查 problem、motivation、gap、contribution、citation；
3. 输出到 reviews/introduction_review.md。
```

### 根据 review 修改 Introduction

```text
请使用 review-revise。

在声称使用该 skill 前，请先读取 .agents/skills/review-revise/SKILL.md。

任务：根据 reviews/introduction_review.md 逐条修改 Introduction。

要求：
1. 每次只处理一个 issue；
2. 先判断证据是否足够；
3. 证据不足则写入 reviews/revise_plan.md 并标记 NEEDS_USER_EVIDENCE；
4. 证据足够则先给 edit plan；
5. 等我确认后再写入；
6. 只修改 Introduction；
7. 不修改其他章节。
```

## 5. Related Work 写作

### Related Work skills 区别

- `relatedwork-finder`：找和登记文献类型。
- `relatedwork-summarizer`：总结已有文献。
- `relatedwork-writer`：组织并起草 Related Work 章节。

### 检查缺失文献类型

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

### 总结已有文献

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

### Planning / Review mode

Planning / Review mode 只写 `reviews/` 或 `notes/`，不修改 `paper.md`，可以使用 `CITATION_NEEDED`、`NEEDS_USER_EVIDENCE` 和 missing-input report。

```text
请使用 relatedwork-writer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-writer/SKILL.md。

任务：为 paper.md 的 Related Work 章节制定写作计划。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md、references/ 和 notes/；
2. 使用 Planning / Review mode；
3. 不修改 paper.md；
4. 建立 related work taxonomy；
5. 将 taxonomy 写入 notes/relatedwork_taxonomy.md；
6. 将写作计划写入 reviews/relatedwork_draft_plan.md；
7. 将 citation gaps 写入 reviews/relatedwork_citation_gaps.md；
8. 不要编造引用。
```

### Paper-writing mode

Paper-writing mode 写入 `paper.md`。正文必须是正式论文正文，不能出现 `current project context`、`this draft`、`CITATION_NEEDED`、`NEEDS_USER_EVIDENCE`、process notes 或审阅提醒。citation gaps 必须单独写入 `reviews/relatedwork_citation_gaps.md`。

```text
我确认要将 Related Work 写入 paper.md。

请使用 relatedwork-writer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-writer/SKILL.md。

要求：
1. 使用 Paper-writing mode；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 paper.md 的 Related Work 部分；
5. 不修改其他章节；
6. 如果没有 Related Work 章节，请在 edit plan 中说明插入位置；
7. 只使用 PROJECT_CONTEXT.md、references/、notes/ 中已有材料；
8. paper.md 正文必须是正式论文正文；
9. paper.md 正文中不能出现 current project context、this draft、CITATION_NEEDED、NEEDS_USER_EVIDENCE、DATA_NEEDED、BASELINE_NEEDED；
10. citation gaps 必须单独写入 reviews/relatedwork_citation_gaps.md；
11. 写入前后记录 paper.md 的 SHA256 hash。
```

## 6. Method 写作

### Method evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Method 部分做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、notes/method_notes.md（如果存在）、paper.md；
2. 不修改 paper.md；
3. 检查 problem formulation、input/output、overall framework、modules、algorithm、formulas、training objective、inference procedure、implementation details、difference from baselines；
4. 缺失内容标记 METHOD_DETAIL_NEEDED、FORMULA_NEEDED、ALGORITHM_NEEDED 或 NEEDS_USER_EVIDENCE；
5. 输出到 reviews/evidence_inventory_method.md。
```

### Method section plan

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Method 制定 section plan。

要求：
1. 读取 reviews/evidence_inventory_method.md；
2. 不修改 paper.md；
3. 给出 Method 小节结构、每节目的、输入证据、缺失证据；
4. 输出到 reviews/method_section_plan.md。
```

### 写入 Method

```text
我确认写入 Method。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 paper.md 的 Method 部分；
4. 不修改其他章节；
5. 不编造公式、算法、模块或实现细节；
6. missing method detail 写入 reviews/method_missing_items.md；
7. 写入前后记录 paper.md 的 SHA256 hash。
```

### 审阅 Method

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 Method。

要求：
1. 不修改 paper.md；
2. 检查 problem formulation、framework、modules、algorithm、formulas、training objective、inference、implementation details；
3. 输出到 reviews/method_review.md。
```

### 修改 Method

```text
请使用 review-revise。

在声称使用该 skill 前，请先读取 .agents/skills/review-revise/SKILL.md。

任务：根据 reviews/method_review.md 逐条修改 Method。

要求：
1. 每次只处理一个 issue；
2. 先判断证据是否足够；
3. 证据不足写入 reviews/revise_plan.md；
4. 证据足够则先给 edit plan；
5. 等我确认后再写入；
6. 只修改 Method；
7. 不修改其他章节。
```

## 7. Experiments 写作

### Experiments evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Experiments 部分做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、notes/experiment_results.md（如果存在）、paper.md；
2. 不修改 paper.md；
3. 列出 datasets、baselines、metrics、implementation details、main results、ablation、efficiency、case study；
4. 不要编造数值；
5. 不要编造 baseline；
6. 不要补不存在的实验；
7. 缺失实验写入 reviews/experiment_missing_items.md；
8. 输出到 reviews/evidence_inventory_experiments.md。
```

### 使用 experiment-analyzer 分析实验材料

```text
请使用 experiment-analyzer。

在声称使用该 skill 前，请先读取 .agents/skills/experiment-analyzer/SKILL.md。

任务：分析当前已有实验材料是否能支持 Experiments 写作。

要求：
1. 读取 PROJECT_CONTEXT.md、notes/experiment_results.md、outputs/ 和 paper.md；
2. 不修改 paper.md；
3. 检查 datasets、baselines、metrics、main results、ablation、efficiency、case study；
4. 缺失实验写入 reviews/experiment_missing_items.md；
5. 输出到 reviews/experiment-analysis.md。
```

### 写入 Datasets

```text
我确认写入 Experiments 的 Datasets 小节。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 Experiments 的 Datasets 小节；
4. 不修改其他章节或小节；
5. 只使用 PROJECT_CONTEXT.md 和 notes/datasets.md 中已有信息；
6. 缺失 dataset 信息写入 reviews/experiment_missing_items.md。
```

### 写入 Baselines / Metrics / Implementation Details / Main Results / Ablation / Efficiency / Case Study

```text
我确认写入 Experiments 的 <小节名> 小节。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. <小节名> 可以是 Baselines、Metrics、Implementation Details、Main Results、Ablation Study、Efficiency Analysis 或 Case Study；
2. 先给 edit plan；
3. 等我确认后再写入；
4. 只修改 Experiments 的 <小节名> 小节；
5. 不修改其他章节或小节；
6. 不编造数值、baseline、实验或 conclusion；
7. 缺失内容写入 reviews/experiment_missing_items.md；
8. 写入前后记录 paper.md 的 SHA256 hash。
```

### 审阅 Experiments

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 Experiments。

要求：
1. 不修改 paper.md；
2. 检查 datasets、baselines、metrics、implementation details、main results、ablation、efficiency、case study；
3. 检查 result 和 conclusion 是否对齐；
4. 输出到 reviews/experiments_review.md。
```

### 修改 Experiments

```text
请使用 review-revise。

在声称使用该 skill 前，请先读取 .agents/skills/review-revise/SKILL.md。

任务：根据 reviews/experiments_review.md 逐条修改 Experiments。

要求：
1. 每次只处理一个 issue；
2. 先判断证据是否足够；
3. 证据不足写入 reviews/revise_plan.md；
4. 证据足够则先给 edit plan；
5. 等我确认后再写入；
6. 只修改 Experiments；
7. 不修改其他章节。
```

## 8. Discussion / Limitation / Conclusion 写作

### Discussion evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Discussion 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md 和 reviews/experiments_review.md（如果存在）；
2. 不修改 paper.md；
3. 列出可以讨论的 verified findings、practical implications、failure cases、open questions；
4. Discussion 不要过度解释；
5. 输出到 reviews/evidence_inventory_discussion.md。
```

### 写入 Discussion

```text
我确认写入 Discussion。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 paper.md 的 Discussion 部分；
4. 不修改其他章节；
5. 不新增实验结果；
6. 不过度解释没有证据支持的现象。
```

### Limitation evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Limitation 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md 的 Research Claim Boundaries、storyline.md 的 Contribution Boundaries 和 paper.md；
2. 不修改 paper.md；
3. 列出必须承认的限制；
4. Limitation 不能隐藏缺陷；
5. 输出到 reviews/evidence_inventory_limitation.md。
```

### 写入 Limitation

```text
我确认写入 Limitation。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 paper.md 的 Limitation 部分；如果没有该部分，请在 edit plan 中说明插入位置；
4. 不修改其他章节；
5. 不隐藏缺陷；
6. 不把 limitation 写成夸大式 future work。
```

### Conclusion evidence inventory

```text
请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

任务：为 Conclusion 做 evidence inventory。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md 和 paper.md；
2. 不修改 paper.md；
3. 只列出正文已有的 problem、method、results、contribution boundaries；
4. Conclusion 不能新增实验结果或新贡献；
5. 输出到 reviews/evidence_inventory_conclusion.md。
```

### 写入 Conclusion

```text
我确认写入 Conclusion。

请使用 paper-section-drafter。

在声称使用该 skill 前，请先读取 .agents/skills/paper-section-drafter/SKILL.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只修改 paper.md 的 Conclusion 部分；
4. 不修改其他章节；
5. 不新增实验结果；
6. 不新增 contribution 或 conclusion。
```

## 9. Review / Checker prompts

### Section review

```text
请使用 markdown-review。

在声称使用该 skill 前，请先读取 .agents/skills/markdown-review/SKILL.md。

任务：审阅 paper.md 的 <章节名>。

要求：
1. <章节名> 可以是 Introduction、Related Work、Method、Experiments 或 Full Paper；
2. 不修改 paper.md；
3. 检查结构、逻辑、证据、citation、claim 是否匹配；
4. 输出到 reviews/<section>_review.md。
```

### problem-checker

```text
请使用 problem-checker。

在声称使用该 skill 前，请先读取 .agents/skills/problem-checker/SKILL.md。

任务：检查问题定义是否清楚、重要、具体。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md；
2. 不修改文件；
3. 输出到 reviews/problem_review.md。
```

### novelty-checker

```text
请使用 novelty-checker。

在声称使用该 skill 前，请先读取 .agents/skills/novelty-checker/SKILL.md。

任务：检查 novelty 和 contribution 是否过度。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md、references/；
2. 不修改文件；
3. 输出到 reviews/novelty_review.md。
```

### logic-checker

```text
请使用 logic-checker。

在声称使用该 skill 前，请先读取 .agents/skills/logic-checker/SKILL.md。

任务：检查论文逻辑链和 claim-evidence gap。

要求：
1. 读取 PROJECT_CONTEXT.md、storyline.md、paper.md；
2. 不修改文件；
3. 输出到 reviews/logic_review.md。
```

### clarity / technical-depth / data / evaluation-protocol checkers

```text
请依次使用 clarity-checker、technical-depth-checker、data-checker 和 evaluation-protocol-checker。

在声称使用任一 skill 前，请先读取对应的 .agents/skills/<skill-name>/SKILL.md。

任务：对当前 paper.md 做综合 checker 审阅。

要求：
1. 不修改 paper.md；
2. 不修改 storyline.md；
3. clarity-checker 输出到 reviews/clarity_review.md；
4. technical-depth-checker 输出到 reviews/technical_depth_review.md；
5. data-checker 输出到 reviews/data_review.md；
6. evaluation-protocol-checker 输出到 reviews/evaluation_protocol_review.md；
7. 对证据不足内容只报告缺失项，不补写内容。
```

## 10. review-revise prompts

### 通用逐条修改

```text
请使用 review-revise。

在声称使用该 skill 前，请先读取 .agents/skills/review-revise/SKILL.md。

任务：根据 reviews/<review-file>.md 逐条修改 <章节名>。

要求：
1. 每次只处理一个 issue；
2. 修改前先判断证据是否足够；
3. 证据不足则写入 reviews/revise_plan.md 并标记 NEEDS_USER_EVIDENCE；
4. 证据足够则先给 edit plan；
5. 等我确认后再写入 paper.md；
6. 只修改 <章节名>；
7. 不修改其他章节。
```

可替换示例：

- `reviews/introduction_review.md` -> Introduction
- `reviews/relatedwork_review.md` -> Related Work
- `reviews/method_review.md` -> Method
- `reviews/experiments_review.md` -> Experiments

## 11. References / Citation prompts

### 创建 references/seed_references.md

```text
请根据我提供的文献信息创建或更新 references/seed_references.md。

要求：
1. 先给 edit plan；
2. 等我确认后再写入；
3. 只写我提供的论文信息；
4. 不编造 BibTeX、DOI、venue、year；
5. 不修改 paper.md。

文献信息如下：
<粘贴文献信息>
```

### 检查 references 是否足够支持 Related Work

```text
请使用 relatedwork-finder。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-finder/SKILL.md。

任务：检查 references/ 是否足够支持 Related Work。

要求：
1. 不联网；
2. 不编造论文；
3. 输出缺口到 reviews/relatedwork_missing_references.md；
4. 不修改 paper.md。
```

### 检查 citation gaps

```text
请使用 relatedwork-writer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-writer/SKILL.md。

任务：检查 paper.md 中 Related Work 的 citation gaps。

要求：
1. 使用 Planning / Review mode；
2. 不修改 paper.md；
3. 不编造 citation；
4. 输出到 reviews/relatedwork_citation_gaps.md。
```

### 根据 BibTeX 或文献笔记生成 relatedwork_summary

```text
请使用 relatedwork-summarizer。

在声称使用该 skill 前，请先读取 .agents/skills/relatedwork-summarizer/SKILL.md。

任务：根据 references/ 中的 BibTeX 或文献笔记生成 relatedwork_summary。

要求：
1. 不声称读过未提供全文的论文；
2. 不编造 BibTeX、DOI、venue、year；
3. 输出到 references/relatedwork_summary.md；
4. 不修改 paper.md。
```

## 12. Experiment analysis prompts

### 分析主结果表

```text
请使用 experiment-analyzer。

在声称使用该 skill 前，请先读取 .agents/skills/experiment-analyzer/SKILL.md。

任务：分析 notes/experiment_results.md 中的主结果表。

要求：
1. 不修改 paper.md；
2. 不编造数值；
3. 检查 result 是否支持 PROJECT_CONTEXT.md 中的 claims；
4. 输出到 reviews/main_results_analysis.md。
```

### 分析 ablation / efficiency

```text
请使用 experiment-analyzer。

在声称使用该 skill 前，请先读取 .agents/skills/experiment-analyzer/SKILL.md。

任务：分析 ablation 和 efficiency 结果。

要求：
1. 读取 PROJECT_CONTEXT.md、notes/experiment_results.md 和 outputs/；
2. 不修改 paper.md；
3. 不补不存在的实验；
4. 缺失结果写入 reviews/experiment_missing_items.md；
5. 输出到 reviews/ablation_efficiency_analysis.md。
```

### 检查实验设计是否支持 claims

```text
请使用 experiment-analyzer。

在声称使用该 skill 前，请先读取 .agents/skills/experiment-analyzer/SKILL.md。

任务：检查实验设计是否支持 paper.md 和 PROJECT_CONTEXT.md 中的 claims。

要求：
1. 不修改文件；
2. 检查缺失 baseline；
3. 检查 result 和 conclusion 是否对齐；
4. 输出到 reviews/experiment_claim_alignment.md。
```

## 13. Submission precheck prompts

```text
请使用 submission-precheck。

在声称使用该 skill 前，请先读取 .agents/skills/submission-precheck/SKILL.md。

任务：对当前论文项目做 final precheck。

要求：
1. 先检查项目结构；
2. 检查 claim-evidence consistency；
3. 检查 citation completeness；
4. 检查 figures/tables completeness；
5. 检查 experiments completeness；
6. 检查 contribution boundary；
7. 不修改 paper.md；
8. 输出到 reviews/submission_precheck.md。
```

## 14. LaTeX / Markdown export prompts

### markdown2latex

```text
请使用 markdown2latex。

在声称使用该 skill 前，请先读取 .agents/skills/markdown2latex/SKILL.md。

任务：规划从 paper.md 到 LaTeX 的转换。

要求：
1. 不覆盖 paper.md；
2. 不声称生成最终投稿稿；
3. 缺模板文件时标记 TEMPLATE_NEEDED；
4. 输出到 outputs/markdown2latex_plan.md。
```

### latex2markdown

```text
请使用 latex2markdown。

在声称使用该 skill 前，请先读取 .agents/skills/latex2markdown/SKILL.md。

任务：规划从已有 LaTeX 草稿导入到 paper.md 的转换。

要求：
1. 不覆盖 paper.md；
2. 先输出导入映射；
3. 缺 LaTeX 源文件时标记 TEMPLATE_NEEDED；
4. 输出到 notes/latex_import_map.md。
```

### template-latex-export

```text
请使用 template-latex-export。

在声称使用该 skill 前，请先读取 .agents/skills/template-latex-export/SKILL.md。

任务：规划将 paper.md 导出到指定 LaTeX 模板。

要求：
1. 不覆盖 paper.md；
2. 不声称生成最终投稿稿；
3. 缺模板文件时标记 TEMPLATE_NEEDED；
4. 输出到 outputs/template_latex_export_plan.md。
```

### latex-final-writer

```text
请使用 latex-final-writer。

在声称使用该 skill 前，请先读取 .agents/skills/latex-final-writer/SKILL.md。

任务：规划最终 LaTeX 写作和导出。

要求：
1. 不覆盖 paper.md；
2. 不声称生成最终投稿稿；
3. 只基于稳定的 paper.md、references/ 和模板文件；
4. 缺模板文件时标记 TEMPLATE_NEEDED；
5. 输出到 outputs/latex_plan.md。
```

## 15. 高风险 skills 的安全 prompts

### bogus-data-helper

```text
请使用 bogus-data-helper。

在声称使用该 skill 前，请先读取 .agents/skills/bogus-data-helper/SKILL.md。

任务：只做 result table planning / evidence-gating。

要求：
1. 不允许生成假数据；
2. 不允许编造实验结果；
3. 不修改 paper.md；
4. 输出到 reviews/data_gap_report.md 和 notes/result_table_plan.md。
```

### humanizer

```text
请使用 humanizer。

在声称使用该 skill 前，请先读取 .agents/skills/humanizer/SKILL.md。

任务：只做 evidence-gated prose polishing plan。

要求：
1. 不允许把文本美化到来源不可追踪；
2. 不强化没有证据的 novelty；
3. 不修改 paper.md；
4. 输出建议到 reviews/humanizer_plan.md。
```

### mad-writer

```text
请使用 mad-writer。

在声称使用该 skill 前，请先读取 .agents/skills/mad-writer/SKILL.md。

任务：只做 fast drafting plan，不直接写正文。

要求：
1. 不允许自动写整篇论文；
2. 不允许跳过 evidence inventory；
3. 不修改 paper.md；
4. 输出到 reviews/mad_writer_plan.md。
```

### state-machine-markdown-helper

```text
请使用 state-machine-markdown-helper。

在声称使用该 skill 前，请先读取 .agents/skills/state-machine-markdown-helper/SKILL.md。

任务：只做 staged drafting workflow planning。

要求：
1. 只允许 planning/evidence-gating mode；
2. 不自动推进到写入正文；
3. 不强化没有证据的 novelty；
4. 不修改 paper.md；
5. 输出到 reviews/state_machine_draft_plan.md。
```

## 16. Debug / 维护 prompts

### 检查某个 skill 的 SKILL.md

```text
请读取 .agents/skills/<skill-name>/SKILL.md。

任务：检查这个 skill 的用途、输入、输出、是否会修改 paper.md、是否需要用户确认。

要求：
1. 不修改任何文件；
2. 输出诊断到 reviews/skill_diagnosis_<skill-name>.md。
```

### 检查 skill metadata

```text
请检查 .agents/skills/ 下所有 skill metadata。

要求：
1. 检查每个 SKILL.md 是否包含 name 和 description；
2. 不修改任何文件；
3. 输出到 reviews/skill_metadata_check.md。
```

### 检查项目结构

```text
请检查当前项目结构。

要求：
1. 确认 AGENTS.md、PROJECT_CONTEXT.md、storyline.md、paper.md、writingrules.md、workflow-dataflow.md、.agents/skills/、references/、notes/、reviews/、outputs/ 是否存在；
2. 不修改任何文件；
3. 输出到 reviews/project_structure_check.md。
```

### 检查为什么 Codex 没有按 skill 执行

```text
请诊断为什么上一轮 Codex 没有按指定 skill 执行。

要求：
1. 读取 AGENTS.md；
2. 读取对应 .agents/skills/<skill-name>/SKILL.md；
3. 对照上一轮 prompt 和输出；
4. 不修改任何文件；
5. 输出问题和改进后的 prompt 到 reviews/skill_execution_debug.md。
```

### 生成问题报告给维护者

```text
请生成问题报告给维护者。

要求：
1. 汇总当前任务、使用的 prompt、相关文件、出错现象；
2. 列出需要维护者查看的文件；
3. 不修改 paper.md；
4. 输出到 reviews/maintainer_issue_report.md。
```
