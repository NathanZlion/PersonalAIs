from datetime import datetime
from beanie import Document, PydanticObjectId
from typing import Optional
from src.models.base_models import CreatedUpdatedAt


class Session(Document, CreatedUpdatedAt):
    """Sessions DB to store active user session."""

    user_id: PydanticObjectId
    refresh_token: str
    expires_at: datetime  # refresh token expiration time
    ip_address: Optional[str]
    user_agent: Optional[str]

    def __repr__(self) -> str:
        return f"<Account {self.id} : user {self.user_id}>"

    def __str__(self) -> str:
        return f"session <{self.id}> of user <{self.user_id}>"

    def __hash__(self) -> int:
        return hash((self.id, self.user_id))
