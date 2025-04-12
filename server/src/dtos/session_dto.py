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


class SessionResultDTO(SessionBase, CreatedUpdatedAt):
    """Session get by id result schema."""

    id: PydanticObjectId


SessionBase.model_rebuild()
