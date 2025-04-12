from fastapi import Depends
from src.dtos.user_dto import UserGetResultDto
from src.repository.user_repo import UserRepo


class UserService:
    def __init__(
        self,
        user_repo: UserRepo = Depends(),
    ):
        self.__user_repo = user_repo

    async def get_user_detail(self, user_id) -> UserGetResultDto:
        return await self.__user_repo.get(user_id=user_id)
