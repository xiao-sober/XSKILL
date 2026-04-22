# Writing Patterns

Use this reference to turn raw development traces into natural but factual diary/report text.

## From Raw Records To Narrative

Do not mirror the commit list. First cluster related records:

- Feature work: routes, pages, components, state, API integration, interaction logic.
- Bug fix: symptom, reproduction clue, investigation, change, validation state.
- Refactor: moved responsibilities, simplified structure, renamed concepts, reduced duplication.
- Tests: added coverage, fixed failing cases, improved mocks or fixtures.
- Tooling/build: config, dependency, CI, scripts, local workflow.
- Documentation: README, comments, examples, usage notes.

Then identify the main thread:

- What goal best explains the largest or most explicit set of changes?
- Which changes are supporting work rather than separate achievements?
- Are there problem-solving steps that should be described as a process?
- What is clearly done, and what remains uncertain?

## Useful Sentence Shapes

High confidence:

- "今天主要推进了设置页的表单状态和保存流程。"
- "在修复过程中，先定位到校验逻辑与接口返回结构不一致，随后调整了解析和错误提示。"
- "补充了相关测试，覆盖了成功保存和接口失败两类路径。"

Medium confidence:

- "从提交记录看，今天的工作主要集中在设置页相关能力上。"
- "围绕登录流程做了一轮调整，重点可能是异常状态处理和提示文案。"
- "当前已经形成了基础实现，但是否达到完整验收标准还需要结合实际测试确认。"

Low confidence:

- "目前只能确认修改集中在配置和构建脚本上，具体业务目的需要进一步补充。"
- "看起来是在为后续功能搭建基础结构，暂不能判断功能是否已经完整可用。"

## Bug-Fix Chain

When logs, errors, or fix commits are available, prefer this chain:

1. Problem observed: symptom, failing test, error message, or user-facing issue.
2. Investigation: what was checked or narrowed down.
3. Cause or likely cause: only state as fact if evidenced.
4. Fix or mitigation: what changed.
5. Validation: tests passed, issue reproduced no longer, or validation still pending.
6. Remaining risk: unclear edge cases, missing environment coverage, or follow-up.

Avoid saying "根因是..." unless the evidence clearly supports it. Use "问题可能来自..." when uncertain.

## Avoid Raw Commit Lists

Instead of:

- "feat: add settings page"
- "fix: validation"
- "test: add settings test"

Write:

"今天的主线是推进设置页。从提交记录看，先完成了页面骨架和表单交互，随后针对保存校验做了修复，并补充了相关测试来覆盖主要路径。当前设置页已经具备基础可用形态，后续还需要确认边界输入和接口异常场景。"

## Conservative Wording Rules

Use conservative wording when evidence is incomplete:

- "初步完成" instead of "完成" when only scaffolding is visible.
- "围绕......进行了调整" when intent is inferred from files.
- "排查并尝试修复" when validation is not evidenced.
- "阶段性推进" when there are commits but no completion signal.
- "可能需要补充确认" when business meaning cannot be determined.

Do not add exact metrics, impact, root cause, stakeholder names, or release claims unless present in the source material.
