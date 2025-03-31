from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.core.container import Container

router = APIRouter(prefix="/auth/session", tags=["session"])

@router.get("/me")
@inject
async def get_active_sessions():
    """Get the active sessions for the current user."""
    return {"message": "Not implemented yet."}


@router.delete("/sessions/all-other")
@inject
async def terminate_all_other_sessions():
    """Terminate all sessions except the current one."""
    return {"message": "Not implemented yet."}


@router.delete("/session/{session_id}")
@inject
async def terminate_session(session_id: str):
    """Terminate a specific session."""
