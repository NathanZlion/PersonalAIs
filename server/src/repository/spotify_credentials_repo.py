from typing import Optional
from src.utils.logger import logg
from src.dtos.spotify_credentials_dto import (
    SpotifyCredentialsCreateInputDto,
    SpotifyCredentialsOutputDto,
)
from src.models.spotify_credentials_model import SpotifyCredential
from src.repository.base_repo import BaseRepo


class SpotifyCredentialsRepo(BaseRepo):

    async def create(
        self,
        credentials: SpotifyCredentialsCreateInputDto,
    ) -> SpotifyCredentialsOutputDto:
        _new_credentials = await SpotifyCredential(**credentials.model_dump()).insert()

        return SpotifyCredentialsOutputDto(**_new_credentials.model_dump())

    async def get_by_spotify_id(
        self,
        spotify_id: str,
    ) -> Optional[SpotifyCredentialsOutputDto]:
        """Get Spotify credentials by Spotify ID."""
        try:
            logg.debug(f"Spotify credentials repo: get_by_spotify_id: {spotify_id}")
            _credentials = await SpotifyCredential.find_one(
                SpotifyCredential.spotify_id == spotify_id
            )
        except Exception as e:
            logg.exception(f"Exception during find_one: {e}, spotify_id: {spotify_id}")
            raise e

        if not _credentials:
            logg.debug(
                f"Spotify credentials repo: No credentials found for {spotify_id}"
            )
            return None

        result = SpotifyCredentialsOutputDto(**_credentials.model_dump())
        logg.debug(f"Spotify credentials repo: Found credential:{spotify_id}: {result}")

        return result

    async def delete(self, spotify_id: str) -> None:
        """Delete Spotify credentials."""
        await SpotifyCredential.find_one(
            SpotifyCredential.spotify_id == spotify_id
        ).delete()
