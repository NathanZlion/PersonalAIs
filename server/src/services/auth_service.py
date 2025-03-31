"""
Authentication Service which handles things like

- User Registration
- User Login
- Password Changes
- Email Confirmation
- User Deletion
"""

import logging

from fastapi import Depends
from src.dtos.user_dto import UserRegisterInputDto, UserCreateOutDto
from src.models.users_model import User
from src.repository.user_repo import UserRepo


_log = logging.getLogger(__name__)


class AuthService:
    def __init__(self, user_repo: UserRepo = Depends()):
        _log.debug("AuthService initialized")
        self.__user_repo = user_repo

    async def register(self, user_create_dto: UserRegisterInputDto) -> UserCreateOutDto:
        _log.debug(f"Registering user {user_create_dto}")

        new_user = User(**user_create_dto.model_dump())
        created_user = await self.__user_repo.create(new_user)
        print(created_user.model_dump())

        result = UserCreateOutDto.model_validate(created_user.model_dump())
        result = UserCreateOutDto(email="lwlw@gmail.com")

        return result
