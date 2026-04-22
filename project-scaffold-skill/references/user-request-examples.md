# User Request Examples

Use this reference to classify scaffold scope quickly.

## Frontend-Only Triggers

Examples:

- "新增一个订单列表页面骨架"
- "帮我加一个 UserProfile 组件目录"
- "给这个模块补 hooks、api 和 types"
- "Create a React page skeleton for reports"

Expected action:

- Inspect frontend layout.
- Generate page/component/hook/api/type files as needed.
- Add route registration only if clearly requested or obvious.
- Leave business interactions as TODO.

## Backend-Only Triggers

Examples:

- "新增一个 FastAPI router 和 service 骨架"
- "给 notification 模块加 schemas 和 repository 占位"
- "Create an API endpoint skeleton for invoices"

Expected action:

- Inspect backend layout.
- Generate router/service/schema files and optional persistence layer only if local pattern supports it.
- Add or suggest router registration.
- Leave domain validation and database behavior as TODO.

## Full-Stack Triggers

Examples:

- "新增一个库存管理功能的前后端骨架"
- "Create a minimal tasks module with React page and FastAPI endpoints"
- "帮我生成页面、API 调用、后端 router/service/schema"

Expected action:

- Align frontend API client with backend route prefix.
- Align TypeScript types with Pydantic schemas.
- Generate only the endpoints needed by the request.
- Report generated pieces and remaining business TODOs.

## Requests That Should Stay Conservative

Examples:

- "做一个完整权限系统"
- "把项目改成 Redux"
- "设计订单、支付、发票全流程"
- "重构整个后端架构"

Expected action:

- Do not treat this skill as a full implementation engine.
- Either scaffold a minimal slice if the user asks for one, or explain that the request needs design decisions before implementation.
