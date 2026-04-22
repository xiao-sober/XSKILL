from .schemas import {{FeatureName}}Create, {{FeatureName}}Read


class {{FeatureName}}Repository:
    async def list(self) -> list[{{FeatureName}}Read]:
        # TODO: implement using the project's database/session pattern.
        return []

    async def create(self, payload: {{FeatureName}}Create) -> {{FeatureName}}Read:
        # TODO: persist confirmed fields and return the stored entity.
        raise NotImplementedError("{{FeatureTitle}} persistence is not implemented yet.")
