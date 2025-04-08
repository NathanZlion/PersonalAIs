from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Request
from src.api.v1.middlewares.auth_middleware import authenticated_only
from src.core.container import Container
from src.core.exceptions import NotFoundError
from src.dtos.auth_dto import AuthAccessTokenSignedData
from src.dtos.user_dto import UserGetResultDto
from src.services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me", response_model=UserGetResultDto)
@authenticated_only
@inject
async def get_current_user_info(
    request: Request,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    """Get the current user data from the access key."""
    current_user: AuthAccessTokenSignedData = request.state.auth
    user_claims = current_user.user_data

    # Check if the user is in the database
    user = await user_service.get_user_detail(user_id=user_claims.id)

    if not user:
        raise NotFoundError("User not found")

    return user
