# Examples

These examples are intentionally short. Use them as patterns, not fixed text.

## Example 1: Diary From Git Commits

Input:

```text
Goal: 今天在做设置页。
git log:
9a1b2c3 feat: add settings form shell
7d8e9f0 fix: handle save validation error
2c4d6e8 test: cover settings save failure
diff files:
src/pages/settings.tsx
src/api/settings.ts
src/pages/settings.test.tsx
```

Output:

```markdown
## 今日工作概述

今天的主线是推进设置页，重点放在表单结构、保存流程和异常处理上。

## 主要完成内容

先搭建了设置页的基础表单和页面结构，并接入了设置保存相关的接口逻辑。随后围绕保存时的校验错误做了修复，让接口返回异常时能进入更明确的处理路径。

## 问题与处理过程

过程中主要卡在保存失败场景的校验处理上。从提交记录看，先完成基础能力后，又专门修正了 validation error 的处理，并补充了失败路径测试来确认该场景不会被遗漏。

## 当前结果或阶段性进展

设置页已经具备基础形态，保存失败场景有了对应处理和测试覆盖。是否覆盖全部边界输入还需要结合实际验收继续确认。

## 下一步计划

继续验证设置页在真实接口和边界输入下的表现，并补充必要的提示文案或交互细节。
```

## Example 2: Report From Bug Logs

Input:

```text
Error: TypeError when project.owner is null
Notes: reproduced on archived projects, added null guard, tests pass locally
Files: src/project/card.tsx, src/project/card.test.tsx
```

Output:

```markdown
## 今日完成事项

- 排查并修复了归档项目在负责人为空时触发的 TypeError。
- 在项目卡片渲染逻辑中补充了空值保护。
- 增加了负责人为空场景的测试覆盖，并完成本地验证。

## 当前进度

该问题已有明确复现路径和对应修复，本地测试通过。

## 遇到的问题与处理情况

问题出现在归档项目缺少 owner 数据时，卡片组件仍按必填字段读取。处理方式是在渲染层补充空值分支，并用测试覆盖该异常数据结构。

## 风险或待确认事项

还需要确认线上历史数据中是否存在其他类似缺字段场景。

## 下一步安排

继续检查相邻项目字段的空值处理，并视情况补充回归测试。
```

## Example 3: Concise Summary

Input:

```text
Worked on auth redirect cleanup, removed duplicate callback handling, still need QA on mobile.
```

Output:

```markdown
- 完成事项：整理了登录重定向流程，移除了重复的 callback 处理逻辑。
- 问题处理：针对跳转链路中的重复处理进行了清理，降低后续状态不一致的风险。
- 下一步：在移动端继续做一轮 QA，确认登录后跳转和异常返回路径。
```

## Example 4: Very Thin Evidence

Input:

```text
git log:
abc123 update config
def456 cleanup
files:
vite.config.ts
package.json
```

Output:

```markdown
以下内容基于提交记录和变更文件整理，具体业务意图需要补充确认。

今天主要围绕项目配置和依赖相关文件做了调整。从目前能看到的信息看，工作可能集中在构建或本地开发环境的整理上，同时做了一些清理性质的改动。由于提交信息较简略，暂不能判断这些调整是否对应某个明确功能或问题修复。

下一步建议补充这次配置调整的目标，例如是为了解决构建问题、升级依赖，还是优化开发流程，再据此完善开发记录。
```
