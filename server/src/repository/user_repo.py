import logging
from typing import List

from src.models.users_model import User

_log = logging.getLogger(__name__)


class UserRepo:
    def __init__(self):
        _log.debug("UserRepo initialized")

    async def create(self, user: User) -> User:
        _log.debug(f"Creating user {user}")
        user = await user.insert()
        return user

    async def getUsers(self) -> List[User]:
        _log.debug("Getting all users")
        users = await User.find().to_list()
        return users
