# Frontend Module Template Guide

Use this reference when the requested scaffold touches React + TypeScript frontend code.

## Inspect Before Generating

Check these signals first:

- `package.json` dependencies for React, routing, UI libraries, data-fetching libraries, and test tools.
- Existing feature folders under names such as `src/features`, `src/pages`, `src/routes`, `src/modules`, `src/components`, `app`, or `client/src`.
- Existing API wrappers under names such as `api`, `services`, `http`, `client`, or `lib`.
- Existing type files under names such as `types.ts`, `*.types.ts`, `models.ts`, or colocated schema files.
- Existing route registration files.

## Recommended File Responsibilities

Only create files that match existing conventions. If no convention exists, use this fallback shape:

```text
src/features/<feature-slug>/
  <FeatureName>Page.tsx
  components/<FeatureName>Panel.tsx
  hooks.ts
  api.ts
  types.ts
  index.ts
```

Responsibilities:

- Page: Compose the feature UI, call hooks, and render loading/error/empty placeholders.
- Components: Hold small presentational sections with minimal props.
- Hooks: Encapsulate local loading/error/data state or call existing query hooks.
- API: Wrap HTTP calls with the project's existing client; fall back to `fetch` only if no wrapper exists.
- Types: Define request/response shapes that match backend schemas.
- Index: Export public module entry points only if the repo already uses barrel exports.

## Naming Rules

- Use nearby casing conventions: `FeaturePage.tsx`, `feature-page.tsx`, or route-file naming as the repo requires.
- Use existing component style: named exports vs default exports, `React.FC` vs plain functions, props interface naming.
- Prefer `FeatureName`, `FeatureNamePage`, `useFeatureName`, `FeatureNameItem`, and `FeatureNameListResponse` only as fallback names.

## State Placeholders

Include basic states when they are natural for the project:

- Loading: simple placeholder or existing spinner component.
- Error: existing alert/toast/error component or a minimal accessible message.
- Empty: neutral empty state with TODO for product copy.

Do not implement complex client workflows, optimistic updates, caching policies, or permission handling unless the repo already has an exact local pattern.

## Route Integration

If route registration is obvious and low-risk, add the route using the existing route pattern. If not, leave a concise integration note in the final response, including the likely file to edit.

## Fallback Templates

Use `assets/templates/frontend/*.tpl` only after adapting names, imports, HTTP client usage, and style to the current repository.
