from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie  # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import CONFIG
from pymongo.server_api import ServerApi
from src.models.users_model import User


DESCRIPTION = """
PersonalAIs API

This is the API for PersonalAIs. It is an API that provides access to the PersonalAIs
backend services. The API is built using FastAPI and is a RESTful API.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    print("Starting up...")

    app.db_client = AsyncIOMotorClient(CONFIG.mongo_uri, server_api=ServerApi("1")).test_db  # type: ignore[attr-defined]
    await init_beanie(app.db_client, document_models=[User])  # type: ignore[arg-type,attr-defined]
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(
    title="PersonalAIs",
    description=DESCRIPTION,
    lifespan=lifespan,
)
