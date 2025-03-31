from pydantic import BaseModel
from decouple import config


class Config(BaseModel):
    mongo_uri: str = config("MONGO_URI", cast=str)  # type: ignore


CONFIG = Config()
