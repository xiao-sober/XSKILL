from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import {{FeatureName}}Create, {{FeatureName}}ListResponse, {{FeatureName}}Read
from .service import {{FeatureName}}Service, get_{{feature_snake}}_service

router = APIRouter(prefix="{{api_path}}", tags=["{{feature_label}}"])


@router.get("", response_model={{FeatureName}}ListResponse)
async def list_{{feature_snake}}(
    service: {{FeatureName}}Service = Depends(get_{{feature_snake}}_service),
) -> {{FeatureName}}ListResponse:
    return await service.list_{{feature_snake}}()


@router.post("", response_model={{FeatureName}}Read, status_code=status.HTTP_201_CREATED)
async def create_{{feature_snake}}(
    payload: {{FeatureName}}Create,
    service: {{FeatureName}}Service = Depends(get_{{feature_snake}}_service),
) -> {{FeatureName}}Read:
    try:
        return await service.create_{{feature_snake}}(payload)
    except NotImplementedError as exc:
        # TODO: replace with project-specific exception handling.
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=str(exc)) from exc
