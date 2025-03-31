from beanie import Document, PydanticObjectId
from typing import Optional
from src.models.base_models import CreatedUpdatedAt


class Accounts(Document, CreatedUpdatedAt):
    """Account DB representation."""

    user_id: PydanticObjectId
    provider: str  # OAuth, local

    # only for local accounts
    password: Optional[str] = None

    # only for OAuth
    provider_id: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_expires: Optional[int] = None

    def __repr__(self) -> str:
        return f"<Account {self.id} : user {self.user_id}>"

    def __str__(self) -> str:
        return f"{self.provider} account for user {self.user_id}"

    def __hash__(self) -> int:
        return hash((self.provider_id, self.user_id))
