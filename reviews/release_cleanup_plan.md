# Release Cleanup Plan

工具包路径：`E:\ai\papersmith`

生成时间：2026-06-04

本报告只做发布前清理分析。未删除、未移动、未修改任何既有文件。

## 1. 当前目录结构概览

当前根目录结构：

```text
E:\ai\papersmith
  .agents/
    skills/                         # 母版 skill 集，当前 33 个 skill
  docs/                             # 使用文档、索引、兼容矩阵
  examples/
    demo-paper-project/             # 示例项目，当前包含一份复制的 .agents/skills
  reviews/                          # 工具包级审阅和诊断报告
  scripts/                          # 初始化和检查脚本
  templates/
    paper-project/                  # 每篇论文项目的初始化模板
  AGENTS.md
  CODEX_COMPATIBILITY.md
  LICENSE
  QUICKSTART.md
  README.md
  WRITING_PRINCIPLES.md
```

关键观察：

- 根目录 `.agents/skills/` 当前有 33 个 skill。
- `examples/demo-paper-project/.agents/skills/` 当前有 32 个 skill，少于母版，疑似旧示例项目未同步新增的 `relatedwork-writer`。
- `templates/paper-project/` 包含项目初始化必需文件和空目录 `.gitkeep`。
- `reviews/` 当前有两份工具包级报告：
  - `reviews/relatedwork_skills_diagnosis.md`
  - `reviews/complete_user_manual_review.md`
- `docs/` 当前有完整使用手册、一页版、新手指南、skill 索引、兼容矩阵、prompt cookbook 等文档。

## 2. 必须保留的文件和目录

### 运行和初始化必须保留

```text
.agents/skills/
templates/paper-project/
scripts/create_paper_project.py
scripts/check_skill_metadata.py
scripts/check_project_structure.py
```

理由：

- `create_paper_project.py` 依赖 `templates/paper-project/` 和 `.agents/skills/`。
- `.agents/skills/` 是所有论文项目复制 skill 的来源。
- `templates/paper-project/` 是每篇论文项目初始化来源。
- `check_skill_metadata.py` 和 `check_project_structure.py` 是发布后排查 setup error 的最小工具。

### 根目录说明文件必须保留

```text
README.md
QUICKSTART.md
AGENTS.md
CODEX_COMPATIBILITY.md
WRITING_PRINCIPLES.md
LICENSE
```

理由：

- `README.md`：项目入口说明。
- `QUICKSTART.md`：短流程说明。
- `AGENTS.md`：母版级 agent 规则。
- `CODEX_COMPATIBILITY.md`：说明未迁移 OpenCode/CoPaper 功能和 Codex 替代方式。
- `WRITING_PRINCIPLES.md`：写作原则。
- `LICENSE`：内部复用和版权边界说明。

### 模板项目必须保留

```text
templates/paper-project/AGENTS.md
templates/paper-project/PROJECT_CONTEXT.md
templates/paper-project/storyline.md
templates/paper-project/paper.md
templates/paper-project/writingrules.md
templates/paper-project/workflow-dataflow.md
templates/paper-project/reviews/.gitkeep
templates/paper-project/notes/.gitkeep
templates/paper-project/references/.gitkeep
templates/paper-project/outputs/.gitkeep
```

理由：

- 这些文件是每篇新论文项目的初始结构。
- `.gitkeep` 用于保留空目录，不能随意删除。
- 删除 `reviews/`、`notes/`、`references/`、`outputs/` 的 `.gitkeep` 不一定破坏脚本运行，因为脚本会创建目录，但会破坏模板目录在版本控制中的完整可见性。

## 3. 可以移动到 archive/ 的文件和目录

建议先创建：

```text
archive/
archive/reviews/
archive/examples/
```

### 可归档：工具包级历史 review 报告

```text
reviews/relatedwork_skills_diagnosis.md
reviews/complete_user_manual_review.md
```

建议移动到：

```text
archive/reviews/relatedwork_skills_diagnosis.md
archive/reviews/complete_user_manual_review.md
```

理由：

- 这两份报告是开发过程记录，不是新同学日常使用入口。
- 对维护者有历史价值，建议保留为版本记录而不是删除。
- 如果 `reviews/` 目录作为“当前待处理检查报告”使用，历史报告放在 `archive/reviews/` 更清楚。

### 可归档或精简：examples/demo-paper-project/

```text
examples/demo-paper-project/
```

建议方案 A：移动整个示例项目到：

```text
archive/examples/demo-paper-project/
```

理由：

- 当前示例项目内复制了一整套 `.agents/skills/`，且 skill 数量为 32，少于母版 33，已经和母版不同步。
- 示例项目体积和维护成本较高。
- `create_paper_project.py` 不依赖 `examples/`，移动不会破坏初始化流程。

建议方案 B：保留示例项目，但删除或重建其中 `.agents/skills/`。

理由：

- 示例项目可以帮助新同学理解目录结构。
- 但示例项目内复制完整 skills 容易过期，也会造成“到底用母版 skills 还是示例 skills”的困惑。
- 如果保留，建议只保留一个轻量示例结构，不保留重复 skills，或重新用当前母版脚本生成一份同步示例。

需用户确认后再执行。

## 4. 可以删除的文件和目录

当前不建议直接删除任何文件。

原因：

- 当前工具包整体比较干净，没有明显临时文件、缓存文件、日志文件、压缩包或自动生成垃圾文件。
- `reviews/` 中两份报告有版本记录价值，建议归档而不是删除。
- `examples/demo-paper-project/` 虽可能过期，但仍可能有示例价值，建议先归档或重建，不建议直接删除。

如果必须压缩 beta 包体积，唯一可考虑删除的是：

```text
examples/demo-paper-project/.agents/skills/
```

但需要先确认是否还希望 `examples/demo-paper-project` 能作为完整可运行项目。如果希望示例项目可直接运行，就不应删除；应改为重新同步到 33 个 skills。

## 5. 不确定是否能删除、需要确认的文件

### examples/demo-paper-project/

不确定点：

- 是否需要向新同学提供一个可打开的示例项目？
- 是否要求示例项目自带完整 `.agents/skills/`？
- 是否接受示例项目只展示目录和少量文本，不保证可直接运行？

当前风险：

- 示例项目内 skills 数量为 32，母版为 33，说明示例项目已经不同步。
- 如果新同学复制示例项目使用，可能缺少 `relatedwork-writer`。

建议：

- 若 beta 发布包需要简洁：移动到 `archive/examples/`。
- 若 beta 发布包需要 demo：用当前 `scripts/create_paper_project.py` 重建一个干净 demo，并确认包含 33 个 skills。

### docs/BEGINNER_USAGE_GUIDE.md

不确定点：

- 它和 `docs/STUDENT_QUICKSTART.md`、`docs/STUDENT_ONE_PAGE_GUIDE.md` 内容有重叠。

建议：

- beta 阶段先保留。
- 等 1 到 2 名同学试用后，根据反馈决定是否合并到 `STUDENT_ONE_PAGE_GUIDE.md` 或删除。

### docs/STUDENT_QUICKSTART.md

不确定点：

- 它和 `STUDENT_ONE_PAGE_GUIDE.md`、`QUICKSTART.md` 有部分重叠。

建议：

- beta 阶段保留。
- 如果要精简文档入口，可以把 `STUDENT_ONE_PAGE_GUIDE.md` 作为学生入口，把 `STUDENT_QUICKSTART.md` 归档或合并。

### docs/skill-design-notes.md

不确定点：

- 面向维护者，不是普通学生必读。

建议：

- beta 阶段保留，方便后续新增/修改 skill。
- 如果发布包只给学生，可以移动到 `archive/docs-maintainer/`，但内部 beta 不建议删。

## 6. 每个建议删除或移动项的理由

| 项目 | 建议 | 理由 | 风险 |
|---|---|---|---|
| `reviews/relatedwork_skills_diagnosis.md` | 移动到 `archive/reviews/` | 历史诊断报告，不是学生入口；有版本记录价值 | 低 |
| `reviews/complete_user_manual_review.md` | 移动到 `archive/reviews/` | 手册审阅报告，已被修订吸收；有维护记录价值 | 低 |
| `examples/demo-paper-project/` | 移动到 `archive/examples/` 或重建 | 当前示例 skills 与母版不同步，容易误导 | 中 |
| `examples/demo-paper-project/.agents/skills/` | 若保留示例，可删除后改为说明“请用脚本创建项目” | 避免重复维护 skills | 中，可能导致示例不可直接运行 |
| `docs/BEGINNER_USAGE_GUIDE.md` | 暂不删除；后续可合并 | 与学生指南重叠，但仍有简短说明价值 | 低 |
| `docs/STUDENT_QUICKSTART.md` | 暂不删除；后续可合并 | 与一页版和完整手册重叠，但可作为中等长度入口 | 低 |
| `docs/skill-design-notes.md` | 暂不删除；维护者文档 | 对普通学生不重要，但对维护有用 | 低 |

## 7. 哪些脚本依赖 templates/

### scripts/create_paper_project.py

直接依赖：

```text
templates/paper-project/
.agents/skills/
```

关键代码行为：

- 从 `templates/paper-project/` 复制项目模板到目标目录。
- 从 `.agents/skills/` 复制 skills 到目标项目的 `.agents/skills/`。
- 确保目标项目包含：

```text
reviews/
notes/
references/
outputs/
.agents/
.agents/skills/
```

不要删除：

```text
templates/paper-project/
.agents/skills/
```

### scripts/check_project_structure.py

不直接依赖 `templates/`，但检查生成项目是否包含模板要求的文件和目录：

```text
AGENTS.md
PROJECT_CONTEXT.md
storyline.md
paper.md
writingrules.md
.agents/skills/
reviews/
notes/
references/
outputs/
```

注意：脚本当前没有检查 `workflow-dataflow.md`，但模板中有该文件。若要更严格，可后续考虑更新脚本，但本次清理不建议修改。

### scripts/check_skill_metadata.py

不依赖 `templates/`。它检查 `.agents/skills/` 下每个 `SKILL.md` 是否包含 `name` 和 `description`。

## 8. 哪些文档是上线必须保留的

面向学生必须保留：

```text
README.md
QUICKSTART.md
docs/STUDENT_ONE_PAGE_GUIDE.md
docs/COMPLETE_USER_MANUAL.md
docs/PROMPT_COOKBOOK.md
```

理由：

- `README.md`：仓库入口。
- `QUICKSTART.md`：快速开始。
- `STUDENT_ONE_PAGE_GUIDE.md`：第一次使用入口。
- `COMPLETE_USER_MANUAL.md`：完整 SOP。
- `PROMPT_COOKBOOK.md`：常用 prompt 查找。

面向 Codex/兼容性必须保留：

```text
AGENTS.md
CODEX_COMPATIBILITY.md
docs/SKILL_INDEX.md
docs/SKILL_COMPATIBILITY_MATRIX.md
docs/how-to-use-with-codex.md
docs/how-to-use-with-other-agents.md
```

理由：

- `AGENTS.md`：全局规则。
- `CODEX_COMPATIBILITY.md`：解释不依赖旧插件。
- `SKILL_INDEX.md`：查 skill 用途。
- `SKILL_COMPATIBILITY_MATRIX.md`：查风险和兼容性。
- `how-to-use-with-codex.md`：Codex 使用说明。
- `how-to-use-with-other-agents.md`：其他 agent 使用说明。

面向维护者建议保留：

```text
docs/skill-design-notes.md
docs/workflow.md
docs/BEGINNER_USAGE_GUIDE.md
docs/STUDENT_QUICKSTART.md
WRITING_PRINCIPLES.md
```

理由：

- 对 beta 维护、文档迭代和试用反馈处理有帮助。
- 可等 beta 试用后再决定合并或归档。

## 9. 哪些 review/test report 建议保留作为版本记录

建议保留但归档：

```text
reviews/relatedwork_skills_diagnosis.md
reviews/complete_user_manual_review.md
```

理由：

- `relatedwork_skills_diagnosis.md` 记录了新增 `relatedwork-writer` 的原因。
- `complete_user_manual_review.md` 记录了完整手册从学生视角的审阅结果。
- 这两份文件是 beta 发布前决策记录，建议保留到 `archive/reviews/`。

建议本报告保留在当前 `reviews/`：

```text
reviews/release_cleanup_plan.md
```

理由：

- 这是当前清理决策入口。
- 后续执行清理时可以按此报告操作。

## 10. 如果执行清理，建议的具体命令

以下命令仅为建议，当前未执行。

### 方案 A：保守清理，仅归档历史 review

```powershell
New-Item -ItemType Directory -Force E:\ai\papersmith\archive\reviews | Out-Null
Move-Item -LiteralPath E:\ai\papersmith\reviews\relatedwork_skills_diagnosis.md -Destination E:\ai\papersmith\archive\reviews\
Move-Item -LiteralPath E:\ai\papersmith\reviews\complete_user_manual_review.md -Destination E:\ai\papersmith\archive\reviews\
```

优点：

- 不影响初始化流程。
- 不影响 skills。
- 不影响 docs。
- 保留历史记录。

### 方案 B：归档过期 demo 项目

```powershell
New-Item -ItemType Directory -Force E:\ai\papersmith\archive\examples | Out-Null
Move-Item -LiteralPath E:\ai\papersmith\examples\demo-paper-project -Destination E:\ai\papersmith\archive\examples\
```

优点：

- 移除一个疑似过期示例项目。
- 避免示例项目内旧 skills 误导学生。

风险：

- `examples/` 目录会变空或缺少 demo。
- 如果 README 或文档提到 `examples/demo-paper-project/`，需要后续同步更新文档。

### 方案 C：重建 demo 项目，而不是归档

```powershell
Remove-Item -Recurse -Force E:\ai\papersmith\examples\demo-paper-project
python E:\ai\papersmith\scripts\create_paper_project.py --name demo-paper-project --target E:\ai\papersmith\examples\demo-paper-project --force
python E:\ai\papersmith\scripts\check_project_structure.py E:\ai\papersmith\examples\demo-paper-project
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith\examples\demo-paper-project\.agents\skills
```

注意：

- 这是破坏性命令，会删除旧 demo 项目。
- 只有在用户明确确认后才能执行。
- 如果 demo 项目包含人工示例内容，不应直接执行。

### 方案 D：只删除示例项目中的重复 skills

```powershell
Remove-Item -Recurse -Force E:\ai\papersmith\examples\demo-paper-project\.agents\skills
```

注意：

- 不建议 beta 前执行，除非同时更新示例说明。
- 删除后示例项目不再是完整可运行论文项目。

## 11. 清理后需要运行哪些测试

执行任何清理后，建议至少运行：

```powershell
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith\.agents\skills
```

创建一个干净测试项目：

```powershell
python E:\ai\papersmith\scripts\create_paper_project.py --name release-smoke-test --target E:\ai\papersmith-release-smoke-test --force
```

检查项目结构：

```powershell
python E:\ai\papersmith\scripts\check_project_structure.py E:\ai\papersmith-release-smoke-test
```

检查生成项目 skills：

```powershell
python E:\ai\papersmith\scripts\check_skill_metadata.py E:\ai\papersmith-release-smoke-test\.agents\skills
```

手动检查生成项目是否包含：

```text
AGENTS.md
PROJECT_CONTEXT.md
storyline.md
paper.md
writingrules.md
workflow-dataflow.md
.agents/skills/
reviews/
notes/
references/
outputs/
```

建议再做一个最小 Codex 流程测试：

1. 读取生成项目的 `AGENTS.md`。
2. 读取 `.agents/skills/storyline-helper/SKILL.md`。
3. 检查空模板 `storyline.md`，输出 `reviews/storyline_review.md`。
4. 读取 `.agents/skills/paper-section-drafter/SKILL.md`。
5. 对 Introduction 做 evidence inventory，输出 `reviews/evidence_inventory_introduction.md`。
6. 确认没有修改 `paper.md` 或 `storyline.md`。

## 12. 推荐 beta 发布前清理策略

建议采用“两步保守策略”：

1. 先不删除任何内容，只执行一次 release smoke test。
2. 用户确认后，将历史 review 报告移动到 `archive/reviews/`。
3. 对 `examples/demo-paper-project/` 做明确决策：
   - 若 beta 包强调简洁：归档到 `archive/examples/`。
   - 若 beta 包需要示例：用当前脚本重建，确保包含 33 个 skills。

发布前不建议删除：

```text
.agents/
templates/
scripts/
docs/
README.md
QUICKSTART.md
AGENTS.md
CODEX_COMPATIBILITY.md
WRITING_PRINCIPLES.md
LICENSE
```

## 13. 当前最重要的待确认问题

1. 是否保留 `examples/demo-paper-project/` 作为 beta 示例项目？
2. 如果保留，是否允许我后续重建它，使其同步当前 33 个 skills？
3. 是否要创建 `archive/` 目录并归档历史 review 报告？
4. 是否希望学生只看 `STUDENT_ONE_PAGE_GUIDE.md` 和 `COMPLETE_USER_MANUAL.md`，把 `BEGINNER_USAGE_GUIDE.md`、`STUDENT_QUICKSTART.md` 作为维护者备用文档？

