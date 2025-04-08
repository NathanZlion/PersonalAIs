"""User models."""

from typing import Annotated, List, Optional
from src.dtos.user_dto import SpotifyImage
from src.models.base_models import CreatedUpdatedAt

from beanie import Document, Indexed
from pydantic import EmailStr


class User(Document, CreatedUpdatedAt):
    """User DB representation."""

    email: Annotated[EmailStr, Indexed(unique=True)]
    spotify_id: Annotated[str, Indexed(unique=True)]
    display_name: Optional[str] = None
    country: str
    images: List[SpotifyImage]  # could be empty

    def __repr__(self) -> str:
        return f"<User: {self.id}>"

    def __str__(self) -> str:
        return self.id.__str__()

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.id == other.id

        return False
