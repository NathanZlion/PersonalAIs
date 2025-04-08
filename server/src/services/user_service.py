from beanie import PydanticObjectId
from fastapi import Depends
from src.dtos.user_dto import UserGetResultDto
from src.repository.user_repo import UserRepo

# from src.services.session_service import SessionService


class UserService:
    def __init__(
        self,
        user_repo: UserRepo = Depends(),
        # session_service: SessionService = Depends(),
    ):
        self.__user_repo = user_repo
        # self.__session_service = session_service

    async def get_user_detail(self, user_id: str) -> UserGetResultDto:
        return await self.__user_repo.get(user_id=PydanticObjectId(user_id))
