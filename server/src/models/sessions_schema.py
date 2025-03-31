from beanie import Document, PydanticObjectId
from typing import Optional
from src.models.base_models import CreatedUpdatedAt
from pydantic.networks import IPvAnyAddressType


class Sessions(Document, CreatedUpdatedAt):
    """Sessions DB to store active user session."""

    user_id: PydanticObjectId
    refresh_token: str
    ip_address: Optional[IPvAnyAddressType]
    userAgent: Optional[str]

    def __repr__(self) -> str:
        return f"<Account {self.id} : user {self.user_id}>"

    def __str__(self) -> str:
        return f"{self.provider} account for user {self.user_id}"

    def __hash__(self) -> int:
        return hash((self.provider_id, self.user_id))
