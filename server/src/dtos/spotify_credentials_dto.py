from pydantic import BaseModel


class SpotifyCredentialsBase(BaseModel):
    """Spotify credentials DTO."""


class SpotifyCredentialsCreateInputDto(SpotifyCredentialsBase):
    """Spotify credentials creation DTO."""

    spotify_id: str
    access_token: str
    refresh_token: str
    token_type: str
    scope: str
    expires_at: float


class SpotifyCredentialsOutputDto(
    SpotifyCredentialsCreateInputDto,
    SpotifyCredentialsBase,
):
    """Spotify credentials output DTO. This is what the response will look like."""
