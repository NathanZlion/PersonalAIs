"""
Spotify credentials is where we store the credentials for the Spotify API.
It should be accessed safely to avoid exposing sensitive information.
It will be encrypted and stored in the database.
"""

from typing import Annotated
from beanie import Document, Indexed

from src.models.base_models import CreatedUpdatedAt


class SpotifyCredential(Document, CreatedUpdatedAt):
    """Spotify credentials DB representation. (model)"""

    spotify_id: Annotated[str, Indexed(unique=True)]
    access_token: str
    refresh_token: str
    token_type: str
    scope: str
    expires_at: float
