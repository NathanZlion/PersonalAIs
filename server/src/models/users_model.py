"""User models."""

from datetime import datetime
from typing import Annotated, Optional
from src.models.base_models import CreatedUpdatedAt

from beanie import Document, Indexed  # type: ignore
from pydantic import EmailStr


class User(Document, CreatedUpdatedAt):
    """User DB representation."""

    email: Annotated[EmailStr, Indexed(unique=True)]
    role: str = "user"
    email_confirmed_at: Optional[datetime] = None

    def __repr__(self) -> str:
        return f"<User {self.id}>"

    def __str__(self) -> str:
        return self.id.__str__()

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.id == other.id

        return False
