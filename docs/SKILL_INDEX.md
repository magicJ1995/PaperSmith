# Skill Index

This index covers the full CoPaper-style skill set migrated into PaperSmith. Before using any skill, read its `.agents/skills/<skill-name>/SKILL.md`.

| Skill | Category | Purpose | Trigger Scenario | Inputs | Outputs | May Edit paper.md | May Edit storyline.md | Confirmation | Frequency |
|---|---|---|---|---|---|---|---|---|---|
| auto-init | utility | Initialize or inspect paper project setup | start new project; verify setup | AGENTS.md; PROJECT_CONTEXT.md; template files | reviews/setup_check.md; notes/setup_notes.md | No | No | Yes before setup edits | 偶尔 |
| bogus-data-helper | experiment | Plan result table structure without fake data | plan tables before real results exist | PROJECT_CONTEXT.md; storyline.md; notes/; outputs/ | notes/result_table_plan.md; reviews/data_gap_report.md | No | No | Yes | 谨慎使用 |
| clarity-checker | review | Check clarity, terms, and readability | review unclear prose | paper.md; storyline.md; writingrules.md | reviews/clarity_review.md | No | No | No for review | 常用 |
| copaper-manage | legacy utility | Map legacy management requests to local Markdown checks | project status; setup; readiness | PROJECT_CONTEXT.md; storyline.md; paper.md; reviews/ | reviews/project_status.md | No | No | No for status | 谨慎使用 |
| data-checker | review | Check result claims against artifacts | data authenticity review | paper.md; notes/; outputs/ | reviews/data_review.md | No | No | No for review | 常用 |
| evaluation-protocol-checker | review | Review RQs, baselines, metrics, validity | evaluation design review | PROJECT_CONTEXT.md; storyline.md; paper.md; notes/ | reviews/evaluation_protocol_review.md | No | No | No for review | 常用 |
| experiment-analyzer | experiment | Analyze provided experiment artifacts and map to claims | experiment code/result analysis | PROJECT_CONTEXT.md; storyline.md; paper.md; notes/; outputs/ | reviews/experiment-analysis.md | No by default | No | Yes before edits | 常用 |
| human-comment-helper | review | Structure real human feedback | advisor or reviewer comments | reviews/; notes/; paper.md | reviews/human_comments.md | No | No | No for organizing | 偶尔 |
| humanizer | writing | Polish prose naturally without changing claims | final prose polish | paper.md; writingrules.md | outputs/polished_text.md or edit plan | Only with confirmation | No | Yes | 谨慎使用 |
| latex-final-writer | latex | Plan final LaTeX manuscript drafting | after stable paper.md and template | paper.md; references/; template files | outputs/latex_plan.md; outputs/tex/ | Only with confirmation | No | Yes | 高级 |
| latex2markdown | latex | Map LaTeX draft into paper.md | import existing .tex draft | user .tex; paper.md; writingrules.md | notes/latex_import_map.md | Only with confirmation | No | Yes | 高级 |
| logic-checker | review | Check contradictions and claim-evidence gaps | logic review | PROJECT_CONTEXT.md; storyline.md; paper.md | reviews/logic_review.md | No | No | No for review | 常用 |
| mad-writer | writing | Controlled fast-drafting plan for low-risk sections | explicit fast drafting request | PROJECT_CONTEXT.md; storyline.md; paper.md; evidence files | reviews/mad_writer_plan.md or approved edit | Only with confirmation | No | Yes | 谨慎使用 |
| markdown-helper | writing | Draft or polish Markdown sections | section drafting | PROJECT_CONTEXT.md; storyline.md; paper.md; writingrules.md | reviews/section_draft_plan.md or approved edit | Only with confirmation | No | Yes | 常用 |
| markdown-review | review | Structured review of paper or section | paper/section review | PROJECT_CONTEXT.md; storyline.md; paper.md; writingrules.md | reviews/*_review.md | No | No | No for review | 常用 |
| markdown2latex | latex | Plan Markdown to LaTeX conversion | LaTeX export planning | paper.md; references/; template files | outputs/markdown2latex_plan.md | No | No | No | 高级 |
| novelty-checker | review | Check novelty claims against related work | novelty review | PROJECT_CONTEXT.md; storyline.md; paper.md; references/ | reviews/novelty_review.md | No | No | No for review | 常用 |
| paper-section-drafter | writing | Draft one paper section after evidence inventory | section-by-section drafting | PROJECT_CONTEXT.md; storyline.md; paper.md; evidence files | approved paper.md edit; reviews/section plan | Only with confirmation | No | Yes | 常用 |
| pdf2paper | utility | Map user PDF draft into paper structure | PDF draft migration | user PDF/extracted text; paper.md | notes/pdf_import_map.md | Only with confirmation | No | Yes | 高级 |
| phase-navigation | legacy utility | Suggest next local workflow step | what should we do next | PROJECT_CONTEXT.md; storyline.md; paper.md; reviews/ | notes/next_steps.md | No | No | No | 偶尔 |
| ppt2storyline | utility | Map slide content into storyline | PPT to storyline bootstrapping | user slides/extracted text; storyline.md | notes/ppt_storyline_map.md | No | Only with confirmation | Yes | 高级 |
| problem-checker | review | Review problem clarity and importance | problem review | PROJECT_CONTEXT.md; storyline.md; paper.md; references/ | reviews/problem_review.md | No | No | No for review | 常用 |
| relatedwork-finder | related-work | Organize and verify related work | find or organize related work | storyline.md; paper.md; references/ | references/relatedwork-notes.md | No | No | No | 常用 |
| relatedwork-summarizer | related-work | Summarize verified related-work materials | summarize papers/notes | references/; storyline.md; paper.md | references/relatedwork_summary.md | No | No | No | 常用 |
| relatedwork-writer | related-work | Plan, organize, and draft the Related Work section from verified references | write Related Work from existing references and notes | PROJECT_CONTEXT.md; storyline.md; paper.md; writingrules.md; references/; notes/relatedwork*.md | reviews/relatedwork_draft_plan.md; reviews/relatedwork_citation_gaps.md; notes/relatedwork_taxonomy.md; approved paper.md edit | Only with confirmation | No | Yes | 常用 |
| review-revise | review | Turn reviews into confirmed edits | revise from reviews | reviews/; PROJECT_CONTEXT.md; storyline.md; paper.md | reviews/revise_plan.md or approved edit | Only with confirmation | Only with confirmation | Yes | 常用 |
| socratic-discussion | core | Stress-test claims through structured questions | research discussion | PROJECT_CONTEXT.md; storyline.md; paper.md; reviews/ | notes/socratic_discussion.md | No | No | No | 偶尔 |
| state-machine-markdown-helper | writing | Strict staged drafting workflow | high-risk drafting | PROJECT_CONTEXT.md; storyline.md; paper.md; evidence files | reviews/state_machine_draft_plan.md or approved edit | Only with confirmation | No | Yes | 高级 |
| storyline-helper | core | Build or inspect storyline from provided material | storyline work | PROJECT_CONTEXT.md; storyline.md; notes/; references/ | reviews/storyline_review.md or approved storyline edit | No | Only with confirmation | Yes | 常用 |
| submission-precheck | submission | Check project setup and submission readiness | before submission/export | all project files and dirs | reviews/submission_precheck.md | No | No | No for check | 常用 |
| technical-depth-checker | review | Check method/design technical depth | method depth review | PROJECT_CONTEXT.md; storyline.md; paper.md; notes/ | reviews/technical_depth_review.md | No | No | No for review | 常用 |
| template-latex-export | latex | Plan export into user LaTeX template | template export planning | paper.md; references/; template files | outputs/template_latex_export_plan.md | No | No | No | 高级 |
| writing-orchestrator | writing | Coordinate writing order and review gates | decide next writing step | PROJECT_CONTEXT.md; storyline.md; paper.md; reviews/ | reviews/writing_plan.md | No | No | No | 常用 |
