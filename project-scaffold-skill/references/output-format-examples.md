# Output Format Examples

Use this reference to produce concise, useful final responses after scaffolding.

## Minimal Frontend Scaffold Summary

```text
已生成 `<FeatureName>` 前端骨架：

Created:
- src/features/<feature>/<FeatureName>Page.tsx
- src/features/<feature>/api.ts
- src/features/<feature>/hooks.ts
- src/features/<feature>/types.ts
- src/features/<feature>/index.ts

Modified:
- src/routes.tsx

保留 TODO:
- 确认列表字段和空态文案
- 接入真实筛选条件

Verification:
- `npm run typecheck` passed
```

## Minimal Backend Scaffold Summary

```text
已生成 `<feature>` FastAPI 骨架：

Created:
- app/api/<feature>/router.py
- app/api/<feature>/schemas.py
- app/services/<feature>_service.py

Registration:
- 已在 app/main.py 注册 router

保留 TODO:
- 补充领域校验
- 接入数据库查询

Verification:
- `pytest app/tests/test_<feature>.py` not run; no matching tests exist yet
```

## Full-Stack Scaffold Summary

```text
已生成 `<feature>` 全栈最小骨架。

Frontend:
- src/features/<feature>/<FeatureName>Page.tsx
- src/features/<feature>/api.ts
- src/features/<feature>/types.ts

Backend:
- app/api/<feature>/router.py
- app/api/<feature>/schemas.py
- app/api/<feature>/service.py

Alignment:
- Frontend `GET /api/<feature>` matches backend router prefix.
- TypeScript response type mirrors Pydantic response schema placeholders.

Still TODO:
- 确认业务字段
- 实现 service 查询
- 确认权限和异常策略
```

## When Registration Is Not Edited

```text
我没有修改路由注册文件，因为项目里存在多个注册入口。
建议下一步在 `app/main.py` 或 `app/api/router.py` 中按现有顺序接入 `<feature>` router。
```
