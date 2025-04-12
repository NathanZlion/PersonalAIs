from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie  # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import CONFIG
from src.models.sessions_model import Session
from src.utils.logger import logg
from src.models.spotify_credentials_model import SpotifyCredential
from src.models.users_model import User
from pymongo.server_api import ServerApi


DESCRIPTION = """
PersonalAIs API

This is the API for PersonalAIs. It is an API that provides access to the PersonalAIs
backend services. The API is built using FastAPI and is a RESTful API.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    logg.info("Starting application...")
    logg.warning("Connecting to db...")

    db_client = AsyncIOMotorClient(CONFIG.MONGO_URI, server_api=ServerApi("1")).test_db
    await init_beanie(db_client, document_models=[User, SpotifyCredential, Session])

    logg.info("Connection to db established")
    yield


app = FastAPI(
    title="PersonalAIs",
    description=DESCRIPTION,
    lifespan=lifespan,
    version="0.1.0",
)
