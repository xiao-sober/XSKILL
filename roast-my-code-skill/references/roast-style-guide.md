# Roast Style Guide

Use this reference when calibrating tone, humor level, or safety boundaries.

## Core Rule

The joke must sit on top of the technical finding. If the finding disappears, delete the joke.

## Modes

### roast

Use when the user clearly asked for a code roast.

Pattern:

- Open with a quick, vivid impression.
- Use playful metaphors for the top issues.
- Keep each issue anchored to code evidence and a fix.

Example:

> 这个 `processData` 像一个把入参校验、业务规则、日志和副作用都塞进后备箱的函数：能跑，但每次转弯都能听见东西在里面撞。

### balanced

Use when the user wants a friendly critique but did not explicitly ask for heavy roasting.

Pattern:

- Mostly engineering language.
- Add one light roast sentence per major issue.
- Keep the final summary useful.

Example:

> 这里的问题不是代码不能工作，而是它让读者需要先进行一轮考古。

### formal

Use when the user requests seriousness or the code is high-risk.

Pattern:

- Remove sarcasm.
- Keep the same issue structure.
- Use direct severity and impact language.

Example:

> This branch can return `undefined` even though the function contract says it returns `User`.

## Intensity Calibration

### mild

Use small, friendly teasing.

- "这个命名有点像临时变量住成了长期户口。"
- "这段逻辑能读，但需要一点心理建设。"
- "注释很努力，但代码本人没有配合。"

### medium

Use more vivid phrasing but keep it controlled.

- "这个函数承担了太多，它已经从工具函数晋升成了部门经理。"
- "这里的状态流转像没有红绿灯的路口，大家都觉得自己先走。"
- "这个 API 契约看起来像口头约定，能不能守住全靠缘分。"

### spicy

Use only when explicitly requested. Keep it about the code.

- "这个 `if` 嵌套再深一点，读者就要带氧气瓶下去了。"
- "这段重复逻辑像复印机卡纸：每份都差不多，但每份都可能单独坏。"
- "错误处理在这里像出门前锁门全靠想象，失败了才知道门根本没装。"

## Acceptable Targets

Roast these:

- Function shape.
- Naming.
- Hidden coupling.
- Duplicate logic.
- Confusing state.
- Misleading comments.
- Missing tests or error handling.
- API contract mismatch.
- Overly broad abstractions.

Do not roast these:

- The author's intelligence or seniority.
- Personal identity, language, education, culture, or background.
- Team/company competence.
- Mental health or physical traits.
- Any protected characteristic.

## Useful Sentence Patterns

- "问题不是 `<thing>`，而是 `<specific technical issue>`。"
- "这段代码最会整活的地方是 `<symptom>`，但真正的风险是 `<impact>`。"
- "吐槽归吐槽，修法很直接：`<action>`。"
- "如果这是临时代码，还能理解；如果已经进主干，那它需要一个成人监护级别的测试。"
- "这不是必须重写，但至少要把 `<responsibility>` 拆出去。"

## Avoid These Patterns

- Pure punchline with no fix.
- "This is bad" without explaining what breaks.
- Fake certainty from missing context.
- Overstating style preferences as correctness issues.
- Long stand-up routines before the review.
- Mean phrasing aimed at the author.

## Humor Budget

For each issue:

- One short roast sentence is usually enough.
- The problem, impact, and fix should take more space than the joke.
- If the section starts feeling like entertainment first, cut the joke count in half.
