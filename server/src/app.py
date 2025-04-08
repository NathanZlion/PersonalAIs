from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie  # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import CONFIG
from src.models.sessions_model import Session
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
    print("Connecting to db...")

    # TODO: Uncomment the following lines when the database is needed
    app.db_client = AsyncIOMotorClient(CONFIG.MONGO_URI, server_api=ServerApi("1")).test_db  # type: ignore[attr-defined]
    await init_beanie(app.db_client, document_models=[User, SpotifyCredential, Session])  # type: ignore[arg-type,attr-defined]

    print("Connecting to db complete")
    yield
    print("Application Shutdown complete")


app = FastAPI(
    title="PersonalAIs",
    description=DESCRIPTION,
    lifespan=lifespan,
    version="0.1.0",
)

origins = [
    # "*",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
