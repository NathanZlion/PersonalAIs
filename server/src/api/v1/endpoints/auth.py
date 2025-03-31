from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.core.container import Container
from src.dtos.user_dto import UserRegisterInputDto, UserCreateOutDto
from src.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserCreateOutDto)
@inject
async def register(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Register a new user."""
    return await auth_service.register(user_data)


@router.post("/login", response_model=UserCreateOutDto)
@inject
async def login(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Login with email and password"""
    return await auth_service.register(user_data)


@router.post("/logout", response_model=UserCreateOutDto)
@inject
async def logout(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Logout, end a user session."""
    return await auth_service.register(user_data)


@router.post("/login", response_model=UserCreateOutDto)
@inject
async def refresh(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Refresh access token with refresh token"""
    return await auth_service.register(user_data)


@router.post("/password-reset/request", response_model=UserCreateOutDto)
@inject
async def passwordResetRequest(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Request a password reset"""
    return await auth_service.register(user_data)


@router.post("/password-reset/confirm", response_model=UserCreateOutDto)
@inject
async def passwordResetConfirm(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Sign up a new user."""
    return await auth_service.register(user_data)


@router.post("/email/verify/request", response_model=UserCreateOutDto)
@inject
async def emailVerifyRequest(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Sign up a new user."""
    return await auth_service.register(user_data)


@router.post("/email/verify/confirm", response_model=UserCreateOutDto)
@inject
async def emailVerifyConfirm(
    user_data: UserRegisterInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> UserCreateOutDto:
    """Sign up a new user."""
    return await auth_service.register(user_data)
