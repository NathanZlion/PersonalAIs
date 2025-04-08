from datetime import datetime
from typing import Optional
from beanie import PydanticObjectId
from pydantic import BaseModel

from src.models.base_models import CreatedUpdatedAt


class SessionBase(BaseModel):
    """Session base schema."""

    user_id: PydanticObjectId
    refresh_token: str
    expires_at: datetime  # refresh token expiration time
    ip_address: Optional[str]
    user_agent: Optional[str]


class SessionCreateInputDto(SessionBase):
    """Session create input schema."""


class SessionCreateResultDto(SessionBase, CreatedUpdatedAt):
    """Session create output schema."""

    session_id: PydanticObjectId


class SessionGetByIdInputDto(BaseModel):
    """Session get by id schema."""

    session_id: PydanticObjectId


class SessionGetByIdResultDto(SessionBase, CreatedUpdatedAt):
    """Session get by id result schema."""

    session_id: PydanticObjectId


class SessionGetByUserIdDto(BaseModel):
    """Session get by user id schema."""

    user_id: PydanticObjectId


class SessionDeleteByUserIdDto(BaseModel):
    """Session delete by user id schema."""

    user_id: PydanticObjectId


class SessionDeleteBySessionIdDto(BaseModel):
    """Session delete by session id schema."""

    session_id: PydanticObjectId


SessionBase.model_rebuild()
