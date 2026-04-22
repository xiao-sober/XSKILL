# XSKILL

XSKILL 是一个用于沉淀个人 Agent skills 的长期合集仓库。

这个项目的目标不是保存一次性的提示词，而是把可复用、可维护、可迁移的工作流整理成结构化 skill。每个 skill 都应包含清晰的触发边界、执行规则、参考文档、必要模板和辅助脚本，让 AI Agent 在未来处理类似任务时能够稳定复用已有经验。

## 项目目的

- 建立个人专属的 Agent skill 知识库。
- 将高频工程任务沉淀为可复用的团队级工作流。
- 让 skill 优先遵循现有项目风格，而不是每次重新设计方案。
- 用工程化方式管理模板、参考资料和辅助脚本。
- 让未来新增 skill 可以被独立维护、版本化和持续改进。

## 本地部署/使用方法

这个仓库本身不是需要启动服务的应用，而是一组可被 Codex/Agent 读取的 skill 文件。部署到本地的核心流程是：拉取仓库，然后把需要使用的 skill 放到 Codex 的 skills 目录，或直接在本地工作区中引用。

### 1. 拉取仓库

```powershell
git clone https://github.com/xiao-sober/XSKILL.git
cd XSKILL
```

如果本地已经有仓库，后续更新使用：

```powershell
git pull origin main
```

### 2. 部署到 Codex skills 目录

推荐把需要长期使用的 skill 复制到 Codex 的 skills 目录。Windows PowerShell 示例：

```powershell
$codexSkills = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $codexSkills | Out-Null

Copy-Item -Recurse -Force ".\project-scaffold-skill" $codexSkills
Copy-Item -Recurse -Force ".\roast-my-code-skill" $codexSkills
Copy-Item -Recurse -Force ".\daily-dev-diary-skill" $codexSkills
```

macOS/Linux 示例：

```bash
CODEX_SKILLS="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS"

cp -R ./project-scaffold-skill "$CODEX_SKILLS/"
cp -R ./roast-my-code-skill "$CODEX_SKILLS/"
cp -R ./daily-dev-diary-skill "$CODEX_SKILLS/"
```

如果希望本地仓库更新后 skill 自动同步，也可以改用符号链接。Windows 需要在支持创建符号链接的终端中执行：

```powershell
New-Item -ItemType SymbolicLink -Path (Join-Path $codexSkills "daily-dev-diary-skill") -Target (Resolve-Path ".\daily-dev-diary-skill")
```

### 3. 验证 skill 可用

部署后可以在 Codex 中用类似请求触发：

- `使用 daily-dev-diary-skill 根据今天的 git log 写开发日记`
- `使用 roast-my-code-skill 帮我吐槽并 review 这段代码`
- `使用 project-scaffold-skill 为当前项目生成一个设置页功能骨架`

如果 skill 没有被自动发现，优先检查目录是否位于 `$CODEX_HOME/skills` 或 `~/.codex/skills` 下，并确认每个 skill 目录内都有 `SKILL.md`。

## 当前内容

### `project-scaffold-skill`

用于 React + TypeScript + FastAPI 项目的全栈功能模块脚手架生成。

它的定位是生成“最小可继续开发骨架”，而不是完整实现复杂业务。适用场景包括新增页面、组件、hooks、API 请求封装、types、FastAPI router、service、schema、CRUD/repository 占位以及前后端联动骨架。

核心原则：

- 先观察当前仓库，再生成文件。
- 优先复用已有目录结构、命名、导入、路由和错误处理风格。
- 只生成最小骨架。
- 对不明确的业务逻辑使用 TODO 占位。
- 尽量减少对现有项目的无关改动。

### `roast-my-code-skill`

用于“毒舌吐槽 + 专业审查”风格的代码点评。

它的定位不是单纯搞笑，而是用轻松、辛辣但有边界的表达方式指出真实代码问题，并给出可执行的改进建议。适用场景包括用户要求吐槽代码、用毒舌但专业的方式 review、让代码点评更有趣，或希望在娱乐化表达中仍然获得可靠工程判断。

核心原则：

- 先专业，后吐槽。
- 只吐槽代码问题，不攻击作者本人。
- 区分真实问题、风格偏好和严重缺陷。
- 每个关键槽点都必须包含问题、影响和改法。
- 支持 `roast`、`balanced`、`formal` 三种模式，能根据场景自动收敛语气。

### `daily-dev-diary-skill`

用于根据当天或某个阶段的开发痕迹生成真实、自然、有结构的开发日记、日报、周报草稿或简洁工作摘要。

它的定位不是罗列 commit message，也不是生成正式 release notes，而是综合用户手动记录、git 提交、diff、改动文件、issue/TODO、错误日志、调试结论和会议备注，整理出“今天做了什么、为什么做、遇到了什么问题、如何处理、当前进展和下一步计划”。适用场景包括写开发日记、根据提交记录生成开发日报、整理零散任务记录、从 bug 修复过程提炼工作总结等。

核心原则：

- 基于事实生成内容，不编造用户没有做过的工作。
- 把零散记录整理成有主线的叙述，而不是 raw commit 列表。
- 支持 `diary`、`report`、`concise` 三种输出模式。
- 支持今日、本周、功能阶段和单次 bug 修复过程等不同时间粒度。
- 对信息不足的部分使用保守表述，明确区分事实和推断。

## 目录规划

每个 skill 建议保持类似结构：

```text
skill-name/
  SKILL.md
  references/
  assets/
  scripts/
  agents/
```

其中：

- `SKILL.md` 描述 skill 的触发边界、目标、流程和约束。
- `references/` 存放按需加载的详细参考文档。
- `assets/` 存放模板、示例或可复用资源。
- `scripts/` 存放真正有助于执行 skill 的辅助脚本。
- `agents/` 存放可选的 UI 元数据。

## 未来方向

XSKILL 会逐步扩展为一个覆盖个人常用开发场景的 skill 集合。未来可能加入：

- 项目初始化与规范检查 skill。
- 前端页面/组件生成 skill。
- 后端 API 与数据库迁移辅助 skill。
- 测试用例生成与补全 skill。
- 代码审查与重构建议 skill。
- 文档生成与项目知识整理 skill。
- 部署、CI/CD、自动化运维相关 skill。

每个新增 skill 都应保持稳健、保守、可验证的工程风格：不擅自引入新架构，不编造业务规则，不进行无关重构，并尽量让输出结果可以直接进入真实项目迭代。

## 使用原则

在真实项目中使用这些 Agent skills 时，应优先把它们当作“工程协作规则”和“可复用脚手架”，而不是一次性生成完整业务的工具。

如果需求不明确，skill 应选择保守实现；如果现有仓库已有清晰模式，skill 应优先模仿；如果业务规则缺失，skill 应留下 TODO，而不是做没有依据的假设。
