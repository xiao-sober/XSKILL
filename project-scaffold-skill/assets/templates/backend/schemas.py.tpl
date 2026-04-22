from pydantic import BaseModel, Field


class {{FeatureName}}Base(BaseModel):
    # TODO: add confirmed fields and validation constraints.
    name: str | None = Field(default=None, description="TODO: replace with confirmed field.")


class {{FeatureName}}Create({{FeatureName}}Base):
    pass


class {{FeatureName}}Read({{FeatureName}}Base):
    id: str


class {{FeatureName}}ListResponse(BaseModel):
    items: list[{{FeatureName}}Read]
