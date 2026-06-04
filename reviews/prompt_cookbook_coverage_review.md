# Prompt Cookbook Coverage Review

审阅对象：`E:\ai\papersmith\docs\PROMPT_COOKBOOK.md`

审阅目标：检查是否覆盖完整论文写作流程。

## 总体结论

通过。

`PROMPT_COOKBOOK.md` 已覆盖从项目初始化、`PROJECT_CONTEXT.md`、`storyline.md`、章节起草、Related Work、Method、Experiments、Discussion/Limitation/Conclusion、Review、Revise、References、Experiment analysis、Submission precheck、LaTeX export 到高风险 skills 安全用法的完整流程。

文档中的 skill prompt 基本都包含“在声称使用该 skill 前，请先读取 `.agents/skills/<skill-name>/SKILL.md`”的要求；会修改 `paper.md` 或 `storyline.md` 的 prompt 基本都包含 edit plan、等待确认、只修改指定章节、不修改其他章节的约束。

## 覆盖检查表

| 检查项 | 是否覆盖 | 位置 | 评价 |
|---|---|---|---|
| 1. `PROJECT_CONTEXT.md` | Yes | `## 2. PROJECT_CONTEXT.md 填写与检查` | 覆盖缺失信息检查、根据用户材料更新、claim boundaries、experiments readiness。 |
| 2. `storyline.md` | Yes | `## 3. storyline.md 检查与完善` | 覆盖完整性检查和 Problem、Background、Existing Methods and Gap、Insight、Method、Evaluation Plan、Contribution Boundaries。 |
| 3. Introduction | Yes | `## 4. Introduction 写作` | 覆盖 evidence inventory、paragraph plan、写入、审阅、根据 review 修改。 |
| 4. Related Work | Yes | `## 5. Related Work 写作` | 覆盖 finder、summarizer、writer，并区分 Planning / Review mode 和 Paper-writing mode。 |
| 5. Method | Yes | `## 6. Method 写作` | 覆盖 evidence inventory、section plan、写入、审阅、修改；包含 problem formulation、input/output、framework、modules、algorithm、formulas 等检查项。 |
| 6. Experiments | Yes | `## 7. Experiments 写作` | 覆盖 evidence inventory、experiment-analyzer、Datasets、Baselines/Metrics/Implementation/Main Results/Ablation/Efficiency/Case Study、审阅和修改。 |
| 7. Discussion | Yes | `## 8. Discussion / Limitation / Conclusion 写作` | 覆盖 evidence inventory 和写入 Discussion，并要求不要过度解释。 |
| 8. Limitation | Yes | `## 8. Discussion / Limitation / Conclusion 写作` | 覆盖 evidence inventory 和写入 Limitation，并要求不能隐藏缺陷。 |
| 9. Conclusion | Yes | `## 8. Discussion / Limitation / Conclusion 写作` | 覆盖 evidence inventory 和写入 Conclusion，并要求不能新增实验结果或贡献。 |
| 10. Review | Yes | `## 9. Review / Checker prompts` | 覆盖 markdown-review、section review 和多类 checker。 |
| 11. Revise | Yes | `## 10. review-revise prompts` | 覆盖通用逐条修改流程，并给出 Introduction/Related Work/Method/Experiments 替换示例。 |
| 12. Submission precheck | Yes | `## 13. Submission precheck prompts` | 覆盖项目结构、claim-evidence、citation、figures/tables、experiments、contribution boundary、final precheck。 |
| 13. References | Yes | `## 11. References / Citation prompts` | 覆盖 seed references、references readiness、citation gaps、relatedwork_summary。 |
| 14. Experiment analysis | Yes | `## 12. Experiment analysis prompts` | 覆盖主结果表、ablation/efficiency、claims 支撑、baseline 缺失、result/conclusion 对齐。 |
| 15. LaTeX export | Yes | `## 14. LaTeX / Markdown export prompts` | 覆盖 markdown2latex、latex2markdown、template-latex-export、latex-final-writer，并要求输出到 outputs/ 或 notes/。 |
| 16. 高风险 skills 安全用法 | Yes | `## 15. 高风险 skills 的安全 prompts` | 覆盖 bogus-data-helper、humanizer、mad-writer、state-machine-markdown-helper，限制为 planning/evidence-gating。 |

## 关键规则覆盖情况

### 不在母版目录写论文

已覆盖。

位置：`## 0. 使用前说明`

说明：明确要求 prompts 应在具体论文项目目录中使用，并不要在 `E:\ai\papersmith` 母版目录写论文。

### 信息不足不得编造

已覆盖。

位置：`## 0. 使用前说明`，并在 Introduction、Related Work、Method、Experiments、高风险 skills 等章节中重复强调。

覆盖的缺失标记包括：

- `DATA_NEEDED`
- `CITATION_NEEDED`
- `BASELINE_NEEDED`
- `NEEDS_USER_EVIDENCE`
- `METHOD_DETAIL_NEEDED`
- `FORMULA_NEEDED`
- `ALGORITHM_NEEDED`
- `TEMPLATE_NEEDED`

### Review/checker 输出进入 reviews/

已覆盖。

所有 review/checker 类 prompt 均要求输出到 `reviews/`，例如：

- `reviews/project_structure_check.md`
- `reviews/project_context_review.md`
- `reviews/storyline_review.md`
- `reviews/introduction_review.md`
- `reviews/method_review.md`
- `reviews/experiments_review.md`
- `reviews/submission_precheck.md`

### Notes 输出进入 notes/

基本覆盖。

Related Work taxonomy 输出到 `notes/relatedwork_taxonomy.md`；LaTeX import map 输出到 `notes/latex_import_map.md`；高风险 result table plan 输出到 `notes/result_table_plan.md`。

### 修改正文前 edit plan + 用户确认

已覆盖。

涉及 `paper.md` 或 `storyline.md` 修改的 prompts 均包含：

- 先给 edit plan；
- 等用户确认后再写入；
- 只修改指定章节；
- 不修改其他章节。

### Related Work 正文不放元信息

已覆盖。

`Paper-writing mode` 明确禁止正文出现：

- `current project context`
- `this draft`
- `CITATION_NEEDED`
- `NEEDS_USER_EVIDENCE`
- `DATA_NEEDED`
- `BASELINE_NEEDED`
- process notes
- 审阅提醒

并要求 citation gaps 单独写入 `reviews/relatedwork_citation_gaps.md`。

## 可改进点

当前覆盖已经足够用于 beta。后续可考虑的小改进：

1. `Review / Checker prompts` 中的 generic output `reviews/<section>_review.md` 对新手可读性稍弱，可以增加具体文件名示例，如 `reviews/relatedwork_review.md`、`reviews/full_paper_review.md`。
2. `Experiments` 的 “写入 Baselines / Metrics / Implementation Details / Main Results / Ablation / Efficiency / Case Study” 是通用模板，足够灵活，但新手可能更喜欢每个小节各有一条独立 prompt。
3. `References / Citation prompts` 中创建 `references/seed_references.md` 会修改 references 文件，已要求 edit plan 和确认；如果后续希望更严格，可以要求先输出到 `reviews/reference_update_plan.md`。
4. `LaTeX / Markdown export prompts` 中 `latex2markdown` 输出到 `notes/latex_import_map.md`，符合 notes 输出规则；但如果实际会导入 `paper.md`，后续需要单独增加“确认导入 paper.md”的 prompt。

## 结论

`PROMPT_COOKBOOK.md` 已经覆盖完整论文写作流程，可作为 beta 版本的 prompt 入口文档。

建议后续在 `README.md` 和 `COMPLETE_USER_MANUAL.md` 中保持一句说明：`PROMPT_COOKBOOK.md` 已覆盖完整流程，不只是 Related Work。
