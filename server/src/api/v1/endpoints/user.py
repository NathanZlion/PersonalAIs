from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.core.container import Container

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me")
@inject
async def get_me():
    """Get the current user data from the access key."""


@router.patch("/me")
@inject
async def update_user():
    """Update the current user data."""
