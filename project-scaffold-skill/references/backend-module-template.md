# Backend Module Template Guide

Use this reference when the requested scaffold touches FastAPI + Python backend code.

## Inspect Before Generating

Check these signals first:

- FastAPI app entry points such as `main.py`, `app/main.py`, `api.py`, or `server.py`.
- Router directories such as `routers`, `routes`, `api`, `endpoints`, or `controllers`.
- Service directories such as `services`, `domain`, or feature-local service files.
- Schema directories or files using Pydantic, often named `schemas.py`, `dto.py`, or `models.py`.
- ORM layers such as SQLAlchemy, SQLModel, Tortoise, or Prisma-style generated clients.
- CRUD/repository layers named `crud`, `repositories`, `repo`, or `dao`.
- Existing error handling, dependency injection, auth dependencies, and test fixtures.

## Recommended File Responsibilities

Only create layers that already exist or are clearly requested. If no convention exists, use this fallback shape:

```text
app/<feature_slug>/
  router.py
  service.py
  schemas.py
```

Optional only when the repo has matching layers:

```text
app/<feature_slug>/
  models.py
  crud.py
  repository.py
```

Responsibilities:

- Router: Define FastAPI endpoints, response models, dependency wiring, and HTTP status boundaries.
- Service: Hold business workflow placeholders and keep router functions thin.
- Schemas: Define explicit request and response models with TODO fields for unknown business data.
- Model: Define ORM persistence only when the project already has a model layer and requirements justify persistence.
- CRUD/repository: Encapsulate persistence calls only when the project already uses this layer.

## Endpoint Shape

For a minimal module, prefer:

- `GET /<feature>` list endpoint.
- `GET /<feature>/{id}` detail endpoint only if detail is requested.
- `POST /<feature>` create endpoint only if creation is requested.
- `PATCH` or `DELETE` only if explicitly requested.

Do not generate a full CRUD set by default.

## Validation and Exceptions

- Use existing Pydantic version style, including `BaseModel`, `ConfigDict`, `model_config`, or `orm_mode`.
- Put basic field constraints only when known from the user or existing similar modules.
- Use existing exception helpers if present.
- Otherwise add TODO placeholders for domain errors and validation rules.

## Router Registration

If router registration is obvious, add the import and `include_router` line following local order. If not, provide a registration hint with the likely app file and router object.

## Fallback Templates

Use `assets/templates/backend/*.tpl` only after adapting imports, dependencies, schema style, and package paths to the repository.
