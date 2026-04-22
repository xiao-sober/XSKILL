from .schemas import {{FeatureName}}Create, {{FeatureName}}ListResponse, {{FeatureName}}Read


class {{FeatureName}}Service:
    async def list_{{feature_snake}}(self) -> {{FeatureName}}ListResponse:
        # TODO: connect to repository/CRUD layer when persistence requirements are confirmed.
        return {{FeatureName}}ListResponse(items=[])

    async def create_{{feature_snake}}(self, payload: {{FeatureName}}Create) -> {{FeatureName}}Read:
        # TODO: implement domain validation and persistence.
        raise NotImplementedError("{{FeatureTitle}} creation is not implemented yet.")


def get_{{feature_snake}}_service() -> {{FeatureName}}Service:
    # TODO: follow project dependency injection/container pattern if one exists.
    return {{FeatureName}}Service()
