---
name: daily-dev-diary-skill
description: "Generate factual, natural daily dev diaries, developer work logs, daily or weekly reports, and concise status summaries from one or more sources such as user notes, git log, git diff, changed files, issues, TODOs, bug logs, debugging notes, and meeting notes. Use when the user asks to write today's development diary, generate a development daily or weekly report from commits or diffs, organize scattered dev work into a readable record, summarize git log/diff/issues into a work summary, or draft programmer diary/report text. Do not use for formal release notes, README or technical documentation, commit messages, raw git log display, or requests to invent work not supported by evidence."
---

# Daily Dev Diary Skill

## Goal

Turn real development traces into a readable development record. Use the available evidence to explain what was done, why it mattered, what blocked progress, how problems were handled, what the current state is, and what should happen next.

Do not produce a raw commit list. Synthesize scattered inputs into a coherent work narrative while preserving uncertainty when the evidence is thin.

## When To Use

Use this skill when the user asks for any of the following:

- "帮我写今天的开发日记"
- "根据今天提交记录生成开发日报"
- "把今天做的事情整理成开发记录"
- "根据 git log / diff / issue 生成工作总结"
- "帮我写成程序员开发日记、日报、周报草稿"
- "把这些零散任务记录整理成顺畅的叙述"
- A daily, weekly, feature-stage, or bug-fix process summary based on development traces.

## When Not To Use

Do not use this skill when the user only wants:

- Formal release notes or a changelog for external users.
- Technical documentation, README content, API docs, or design docs.
- A commit message.
- The raw git log or raw diff without narrative synthesis.
- A fabricated report about work not evidenced by notes, commits, diffs, issues, logs, or context.
- Very specific claims from very little input. In that case, produce a conservative summary and ask for missing details if needed.

## Acceptable Inputs

Accept one or more of these sources:

- User-provided goals, task notes, meeting notes, standup notes, or manual work records.
- Git commits, branch names, tags, and commit messages.
- Git diff, changed file lists, diff stats, or uncommitted work.
- Issues, TODOs, task lists, tickets, acceptance criteria, or checklist items.
- Error logs, stack traces, failed test output, bug reproduction notes, fix notes, and debugging conclusions.
- Existing conversation context or previous diary entries, when relevant.

If helpful and available, use `scripts/collect_dev_context.py` to collect git and TODO context before drafting. Read `references/input-sources.md` for source handling details.

## Input Priority

Use this default priority order:

1. User's direct notes, stated goals, task descriptions, and clarifications.
2. Git commit records for the requested period.
3. Git diff, changed files, diff stats, and uncommitted changes.
4. Issues, TODOs, task lists, and checklist progress.
5. Logs, errors, failed tests, fix records, and debugging notes.
6. Historical context from the current conversation or nearby project files.

When sources conflict, prefer the most explicit, recent, and user-provided information. When logs or bug-fix traces are present, prioritize the "problem -> investigation -> fix/mitigation -> result" chain.

## Core Workflow

1. Identify the requested time range and output mode.
2. Gather facts from the available sources without over-reading unrelated project history.
3. Group evidence into logical work items instead of preserving every commit boundary.
4. Infer the main development thread only when supported by filenames, commit messages, notes, or logs.
5. Draft in the selected mode: `diary`, `report`, or `concise`.
6. Add conservative uncertainty language where intent or completion state is not fully supported.
7. Final-check that every concrete claim is grounded in evidence.

## Output Modes

### diary

Use for personal development diary or self-archive requests. Prefer this when the user says "开发日记", "今天做了什么", "整理一下今天的工作", or does not specify a formal audience.

Required structure:

1. 今日工作概述
2. 主要完成内容
3. 问题与处理过程
4. 当前结果或阶段性进展
5. 下一步计划

Style: natural, readable, first-person or neutral according to the user's tone. It should feel like a real developer record, not a status template.

### report

Use for daily reports, weekly reports, team sync, manager-facing updates, or messages intended for a group, lead, coworker, or project tracker.

Required structure:

1. 今日/本周完成事项
2. 当前进度
3. 遇到的问题与处理情况
4. 风险或待确认事项
5. 下一步安排

Style: formal, restrained, clear, and suitable for team communication.

### concise

Use when the user asks for a short summary, quick archive, task-system note, chat message, or compact status.

Required structure:

- 完成事项
- 问题处理
- 下一步

Style: brief, specific, and easy to paste.

Mode selection rules:

- "日报" or "周报" -> prefer `report`.
- "开发日记" or personal archive -> prefer `diary`.
- "整理一下今天做了什么" with no audience -> default to `diary` with a balanced tone.
- "发群里", "发给领导", "同步给同事" -> prefer `report`.
- "复制到任务系统", "简短一点", "一句话/三条" -> prefer `concise`.

Use `assets/output-templates.md` when a stable skeleton is useful.

## Time Granularity

Support these scopes:

- Today or a specific date.
- This week or a specific date range.
- A feature stage, milestone, sprint segment, or implementation phase.
- A single bug investigation and fix process.

For weekly or stage summaries, group work by theme instead of day-by-day unless the user asks for a chronological log. For bug-fix records, emphasize reproduction, investigation, root cause evidence, fix, validation, and remaining risk.

## Writing Principles

- Base the output on facts. Do not invent tasks, results, decisions, root causes, or completion states.
- Convert records into narrative. Explain the main thread, intent, process, and outcome instead of listing raw commits.
- Merge related small changes into logical work items.
- Preserve process feeling: why the work was done, where it got stuck, what decision moved it forward, and what changed afterward.
- Accurately classify work such as feature development, bug fix, refactor, tests, documentation, scaffolding, config, build, or cleanup.
- If the user gives a main goal such as "今天在做设置页", organize the diary around that goal instead of evenly listing every minor file change.
- Avoid empty praise, vague productivity claims, and generic filler.

Read `references/writing-patterns.md` for transformation patterns, conservative wording, and examples of turning git traces into narrative.

## Missing Information Strategy

When evidence is incomplete, write conservatively:

- "初步完成......相关骨架搭建"
- "围绕......进行了调整"
- "针对......问题进行了排查与修复"
- "从提交记录看，主要集中在......"
- "目前能确认的是......，具体业务意图可能还需要补充"

If only filenames or commit messages are available, do not state detailed intent as fact. If work appears in progress, do not say "已完成" unless completion is evidenced. If a fix is attempted but validation is unclear, say "进行了修复尝试/调整，后续仍需验证".

Optionally include a short evidence note such as: "以下内容基于提交记录和变更文件整理，部分意图为保守推断。"

## Risk Controls

- Never fabricate work the user did not do.
- Never claim something is solved when the evidence only shows investigation or an attempted fix.
- Never turn an uncertain commit intention into a definitive business conclusion.
- Never expose sensitive logs, secrets, tokens, customer data, or private issue content in the final diary. Summarize sensitive details safely.
- Separate facts from inference when uncertainty matters.
- Ask for clarification only when a reasonable, conservative summary would be misleading.

## Bundled Resources

- `references/input-sources.md`: How to collect and prioritize notes, git records, diffs, TODOs, issues, and logs.
- `references/writing-patterns.md`: How to synthesize raw records into readable development diary text.
- `references/examples.md`: Short examples for diary, report, concise, and git-to-narrative conversion.
- `assets/output-templates.md`: Reusable output skeletons.
- `scripts/collect_dev_context.py`: Optional helper for collecting git commits, changed files, uncommitted changes, and TODO-style markers.

## Success Criteria

A successful output:

- Is grounded in the provided or discovered evidence.
- Clearly answers what was done, why, what happened during the process, current progress, and next steps.
- Reads like a real development record rather than a commit log.
- Uses the correct mode and audience tone.
- Handles missing information without exaggeration.
- Is directly reusable in a diary, report, weekly summary, issue update, or task system.
