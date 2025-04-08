from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends

from src.api.v1.middlewares.auth_middleware import UnauthorizedUserBlockMiddleware


router = APIRouter(
    prefix="/session",
    tags=["session"],
    # Session related endpoints are only for authenticated users
    dependencies=[Depends(UnauthorizedUserBlockMiddleware)],
)


@router.get("/refresh")
@inject
async def get_active_sessions():
    """Get the active sessions for the current user."""

    return {"message": "Not implemented yet."}


@router.get("/{session_id}")
@inject
async def get_detail_session_data(session_id: str):
    """Get a detailed view of a specific session."""

    return {"message": f"Not implemented yet. ${session_id}"}


@router.delete("/{session_id}")
@inject
async def terminate_session(session_id: str):
    """Terminate a specific session."""

    return {"message": f"Not implemented yet. ${session_id}"}


@router.delete("/all-other")
@inject
async def terminate_all_other_sessions():
    """Terminate all sessions except the current one."""

    return {"message": "Not implemented yet."}
