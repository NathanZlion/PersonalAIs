# from datetime import datetime
# from typing import Optional

from pydantic import BaseModel, EmailStr
from src.models.base_models import CreatedUpdatedAt


class UserBase(BaseModel):
    """User base schema."""


class UserRegisterInputDto(UserBase):
    """User Registration schema with email and password."""

    email: EmailStr
    password: str


class UserCreateOutDto(UserBase, CreatedUpdatedAt):
    email: EmailStr


class UserDeleteDto(UserBase):
    """User delete schema."""

    email: EmailStr
