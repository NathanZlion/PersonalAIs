# type: ignore

from pydantic import BaseModel
from decouple import config
from datetime import timedelta


class Config(BaseModel):
    MONGO_URI: str = config("MONGO_URI", cast=str)

    SPOTIFY_CLIENT_ID: str = config("SPOTIFY_CLIENT_ID", cast=str)
    SPOTIFY_CLIENT_SECRET: str = config("SPOTIFY_CLIENT_SECRET", cast=str)
    SPOTIFY_AUTH_URL: str = config("SPOTIFY_AUTH_URL", cast=str)
    SPOTIFY_AUTH_REDIRECT_URI: str = config("SPOTIFY_AUTH_REDIRECT_URI", cast=str)
    SPOTIFY_API_BASE_URL: str = config("SPOTIFY_API_BASE_URL", cast=str)
    SPOTIFY_TOKEN_URL: str = config("SPOTIFY_TOKEN_URL", cast=str)
    SPOTIFY_PERMISSIONS_SCOPE: str = " ".join(
        # TODO: Don't forget to uncomment code below when further permissions are needed
        [
            # "playlist-read-private",
            # "playlist-read-collaborative",
            # "playlist-modify-private",
            # "playlist-modify-public",
            # "user-read-playback-position",
            # "user-top-read",
            # "user-read-recently-played",
            # "user-library-modify",
            # "user-library-read",
            "user-read-email",
            "user-read-private",
        ]
    )

    GEMINI_PROJECT_ID: str = config("GEMINI_PROJECT_ID", cast=str)
    GEMINI_API_KEY: str = config("GEMINI_API_KEY", cast=str)

    FRONTEND_URL: str = config("FRONTEND_URL", cast=str)
    FRONTEND_AUTH_CALLBACK_URL: str = config("FRONTEND_AUTH_CALLBACK_URL", cast=str)

    JWT_SECRET: str = config("JWT_SECRET", cast=str)
    ACCESS_TOKEN_LIFETIME: timedelta = timedelta(minutes=15)
    REFRESH_TOKEN_LIFETIME: timedelta = timedelta(weeks=8)
    JWT_ALGORITHM: str = "HS256"


CONFIG = Config()
