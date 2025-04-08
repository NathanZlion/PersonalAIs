from fastapi import Depends

from src.dtos.spotify_credentials_dto import (
    SpotifyCredentialsCreateInputDto,
    SpotifyCredentialsOutputDto,
)
from src.repository.spotify_credentials_repo import SpotifyCredentialsRepo


class SpotifyCredentialsService:
    def __init__(
        self,
        spotify_credentials_repo: SpotifyCredentialsRepo = Depends(),
    ):
        self.__spotify_credentials_repo = spotify_credentials_repo

    # TODO: Add encryption for the credentials!!!
    async def store_credentials(
        self,
        create_spotify_credentials_dto: SpotifyCredentialsCreateInputDto,
        overwrite_existing: bool = True,
    ) -> SpotifyCredentialsOutputDto:
        """Store Spotify credentials."""

        print("Storing Spotify credentials...")
        _existing_credentials = await self.__spotify_credentials_repo.get_by_spotify_id(
            spotify_id=create_spotify_credentials_dto.spotify_id
        )

        if not overwrite_existing and _existing_credentials:
            print("Spotify credentials already exist.")
            raise Exception(
                "Spotify credentials already exist. Set overwrite_existing to True to overwrite."
            )

        if _existing_credentials:
            print("Deleting existing Spotify credentials...")
            # Delete existing credentials if overwrite_existing is True
            await self.__spotify_credentials_repo.delete(
                spotify_id=_existing_credentials.spotify_id
            )

        print("Creating new Spotify credentials...")
        # Check if the credentials already exist
        new_credentials_store = await self.__spotify_credentials_repo.create(
            credentials=create_spotify_credentials_dto,
        )

        print("New Spotify credentials created successfully.")
        return SpotifyCredentialsOutputDto(
            **new_credentials_store.model_dump(),
        )

    # TODO: Decrypt the credentials before returning them
    async def get_credentials(
        self,
        spotify_id: str,
    ) -> SpotifyCredentialsOutputDto:
        """Get Spotify credentials by Spotify ID."""
        _credentials = await self.__spotify_credentials_repo.get_by_spotify_id(
            spotify_id=spotify_id
        )

        if not _credentials:
            raise Exception("Spotify Credentials not found")

        return SpotifyCredentialsOutputDto(**_credentials.model_dump())
