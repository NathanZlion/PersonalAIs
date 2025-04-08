from typing import Optional
from src.dtos.spotify_credentials_dto import (
    SpotifyCredentialsCreateInputDto,
    SpotifyCredentialsOutputDto,
)
from src.models.spotify_credentials_model import SpotifyCredential
from src.repository.base_repo import BaseRepo


class SpotifyCredentialsRepo(BaseRepo):
    def __init__(self):
        pass

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
            print("Spofiy credentials repo: get_by_spotify_id", spotify_id)
            _credentials = await SpotifyCredential.find_one(
                SpotifyCredential.spotify_id == spotify_id
            )
        except Exception as e:
            print("Exception during find_one:", e)
            raise e

        print("Spofiy credentials repo: credentials: ", _credentials)
        if not _credentials:
            return None

        result = SpotifyCredentialsOutputDto(**_credentials.model_dump())
        print("Spofiy credentials repo: result: ", result)

        return result

    async def delete(self, spotify_id: str) -> None:
        """Delete Spotify credentials."""
        await SpotifyCredential.find_one(
            SpotifyCredential.spotify_id == spotify_id
        ).delete()
