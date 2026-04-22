---
name: react-ts-fastapi-feature-scaffold
description: "Generate minimal repository-style scaffolds for new React + TypeScript + FastAPI feature modules. Use when the user asks in English or Chinese to add a new feature module, page, component, API client, hook, types, FastAPI router, service, schema, model, CRUD/repository, route registration hint, or aligned frontend/backend skeleton. Do not use for complete business implementation, large refactors, architecture replacement, or introducing unrelated UI/state/backend frameworks."
---

# React TS FastAPI Feature Scaffold

## Goal

Use this skill to create the smallest useful development skeleton for a new full-stack feature in an existing repository that uses React + TypeScript on the frontend and FastAPI + Python on the backend.

The generated result must help the next developer continue implementation quickly without pretending that uncertain business logic is already known.

## Core Principles

- Observe the repository before generating files.
- Prefer existing directory layout, naming, imports, test style, formatting, API clients, error handling, and route registration patterns.
- Generate only the minimum skeleton needed for continued development.
- Keep existing files untouched unless a small registration change is clearly required and consistent with the repo.
- Use TODO comments for unclear business rules, fields, permissions, validation, persistence, side effects, and integration details.
- Do not introduce new UI frameworks, state libraries, API clients, ORMs, routers, dependency systems, or architectural layers unless the project already uses them.
- Do not implement complex business behavior from guesses.

## Suitable Requests

Use this skill when the user asks to add or scaffold:

- A frontend feature module, page, component group, hook, API client wrapper, type file, or index export.
- A FastAPI router, service, schema, model, CRUD/repository layer, or route registration hint.
- A full-stack feature skeleton where frontend API calls and backend routes should align.
- A module directory structure for future development.

## Unsuitable Requests

Do not use this skill as the main approach for:

- Completing a full business feature with detailed domain rules.
- Replacing the existing architecture or state management.
- Large refactors, migrations, or framework changes.
- Designing a database schema without repo evidence or user-provided requirements.
- Adding authentication, permissions, billing, workflows, background jobs, or external integrations beyond placeholders.

## Resource Navigation

Load only the reference files needed for the current request:

- `references/frontend-module-template.md`: React + TypeScript module shape and fallback file responsibilities.
- `references/backend-module-template.md`: FastAPI module shape and fallback file responsibilities.
- `references/style-matching-guide.md`: How to inspect and imitate existing code style.
- `references/user-request-examples.md`: Request patterns and how to classify scope.
- `references/output-format-examples.md`: Expected final summaries and generated skeleton examples.

Use assets as fallback templates only after repository inspection:

- `assets/templates/frontend/`
- `assets/templates/backend/`

Optionally run `scripts/detect_project_patterns.py --root <repo> --feature <feature-name>` to quickly identify likely frontend/backend roots, common layer directories, and similar modules.

## Execution Flow

1. Clarify scope only if the request is impossible to interpret. Otherwise make conservative assumptions.
2. Inspect repository structure with fast searches such as `rg --files`, `Get-ChildItem`, and targeted file reads.
3. Identify the closest existing module that resembles the requested feature.
4. Determine whether the request is frontend-only, backend-only, or full-stack.
5. Select the smallest file set that matches existing patterns.
6. Create new files by copying local conventions, not by forcing these templates.
7. Modify existing registration files only when the repo has an obvious pattern and the user asked for an integrated skeleton.
8. Add TODO placeholders for missing business logic.
9. Run available formatters, linters, type checks, or tests only when they are already configured and cheap enough for the change.
10. Report what was generated, what was intentionally left as TODO, and any manual registration still needed.

## Frontend Scaffold Rules

For React + TypeScript modules, first look for existing conventions for:

- Page directories and route files.
- Component naming and export style.
- Hook naming and async data handling.
- API client location and HTTP utility usage.
- Type location and naming.
- Index barrel exports.
- Loading, empty, and error states.
- CSS, CSS modules, utility classes, or component library usage.

Prefer generating only the files that the project would naturally contain, such as:

- `Page` or route component.
- Small child component placeholders.
- `hooks` for data loading or local UI state.
- API request wrapper using the existing HTTP client.
- `types` for request and response shapes.
- `index` exports when the repo uses barrel files.
- Route registration hint or minimal registration edit if the route system is clear.

Frontend constraints:

- Do not introduce a UI framework that is not already present.
- Do not add Redux, Zustand, TanStack Query, SWR, Apollo, or another state/data library unless the repo already uses it.
- Keep props, type aliases/interfaces, component names, and file casing consistent with nearby code.
- Include basic loading, empty, and error placeholders when the surrounding UI pattern supports them.
- Do not fake complex interactions, permission checks, optimistic updates, or workflow logic.

## Backend Scaffold Rules

For FastAPI + Python modules, first look for existing conventions for:

- Router location, prefix style, tags, dependencies, and registration.
- Service layer structure and dependency injection style.
- Pydantic schema version and naming.
- ORM model layer, if one exists.
- CRUD/repository layer, if one exists.
- Exception handling and status code patterns.
- Test layout and fixtures.

Prefer generating only the files that the project would naturally contain, such as:

- `router.py` or equivalent route module.
- `service.py` for business boundary placeholders.
- `schemas.py` for request/response models.
- `models.py` only when the project already has an ORM layer and the requested feature needs persistence.
- `crud.py` or `repository.py` only when that layer already exists.
- Router registration hint or minimal registration edit if app registration is obvious.

Backend constraints:

- Follow existing directory layering before choosing a new module layout.
- Do not invent database columns, relationships, permissions, background tasks, or domain workflows.
- Keep input and output structures explicit, with TODOs where fields are unknown.
- Put unclear logic behind service methods with TODO placeholders.
- Use the existing exception style; otherwise leave a clear placeholder rather than inventing a policy.

## Full-Stack Alignment Rules

When scaffolding a full-stack feature:

- Keep frontend and backend feature names, route names, and field names aligned.
- Make frontend API paths match backend router prefixes and endpoint paths.
- Make request body and response types correspond to backend Pydantic schemas.
- Keep placeholder fields minimal and documented as TODO.
- State clearly which pieces are generated and which business logic still needs manual implementation.

## Missing Information Strategy

If requirements are missing:

- Choose the least invasive skeleton.
- Prefer optional or TODO fields over invented domain detail.
- Generate route/API shapes only when the requested feature name implies enough structure.
- Use neutral names such as `Item`, `ListParams`, `CreateRequest`, or repo-specific equivalents.
- Avoid persistence files unless the repository has a clear pattern and the request implies stored data.
- Add comments like `# TODO: apply domain validation once requirements are confirmed`.

## Output Requirements

When completing a scaffold task:

- List created files and modified existing files separately.
- Mention registration changes or registration hints.
- Mention TODOs that need business decisions.
- Mention verification commands run and their result.
- If validation was not run, state why.

## Risk Controls

- Never overwrite existing feature files without reading them first.
- Avoid broad edits to shared routers, app bootstrap, global state, build config, and database setup.
- Do not remove or rename user code.
- Do not normalize unrelated formatting.
- Avoid adding dependencies unless the user explicitly requests them.
- Treat generated templates as starting points, not authoritative architecture.

## Success Criteria

A successful result:

- Matches the repository's existing style closely enough that the skeleton looks native.
- Contains the minimum frontend and/or backend files needed to continue development.
- Has aligned frontend API calls and backend route/schema placeholders for full-stack work.
- Leaves uncertain business logic as TODOs.
- Requires little or no unrelated change to existing project files.
- Can be type-checked, imported, or wired with predictable next steps.
