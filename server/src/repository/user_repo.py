from beanie import PydanticObjectId
from src.dtos.user_dto import UserCreateInputDto, UserCreateResultDto, UserGetResultDto
from src.models.users_model import User
from src.repository.base_repo import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self):
        pass

    async def create(self, user: UserCreateInputDto) -> UserCreateResultDto:

        new_user = await User(**user.model_dump()).insert()
        return UserCreateResultDto(**new_user.model_dump())

    async def get(self, user_id: PydanticObjectId) -> UserGetResultDto:
        user = await User.get(user_id)
        if not user:
            raise Exception("User not found")

        return UserGetResultDto(**user.model_dump())

    async def get_by_spotify_id(self, spotify_id: str) -> UserGetResultDto:
        user = await User.find_one(User.spotify_id == spotify_id)
        if not user:
            raise Exception("User not found")

        return UserGetResultDto(**user.model_dump())
