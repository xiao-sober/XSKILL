# Style Matching Guide

Use this reference to keep generated scaffolds native to the current repository.

## Repository Observation Checklist

Before writing files, inspect:

- File tree: `rg --files` or a shallow directory listing.
- Similar feature modules and naming.
- Import aliases and relative import depth.
- Existing frontend route and backend router registration.
- Existing formatting: semicolons, quotes, async style, dependency injection, docstrings, and comment density.
- Existing tests for similar modules.

## Frontend Signals

Look for:

- Component exports: named export, default export, or mixed.
- Props style: `type Props =`, `interface Props`, inline props, `React.FC`.
- API style: `fetch`, `axios`, generated client, custom `request`, `http`, or `apiClient`.
- Data style: plain hooks, TanStack Query, SWR, Redux, Zustand, context, or route loaders.
- Styling: CSS modules, Tailwind, Sass, styled-components, vanilla CSS, or UI library components.

Mirror the strongest local pattern. If multiple patterns exist, use the one closest to the target feature directory.

## Backend Signals

Look for:

- Router object naming: `router`, `api_router`, or feature-specific names.
- Route prefixes and tags.
- Dependency injection with `Depends`.
- Service construction style: class, functions, container, or request-scoped dependency.
- Pydantic v1/v2 conventions.
- ORM and transaction/session handling.
- Error helpers and response envelope patterns.

Mirror the closest feature. If uncertain, generate a thin router + schema + service skeleton and leave persistence as TODO.

## File Modification Rules

- Create new files first.
- Modify existing registration files only after reading them.
- Keep registration edits minimal and ordered like surrounding imports/routes.
- Do not reformat unrelated lines.
- If a registration target is ambiguous, do not edit it; provide a precise hint instead.

## Template Adaptation Rules

The assets in this skill are fallback templates. Before using them:

- Replace placeholders with repo-specific names.
- Replace generic HTTP calls with the repo's client.
- Replace generic errors with local error handling.
- Replace placeholder schemas with user-confirmed fields.
- Remove optional files that do not match the repo's architecture.
