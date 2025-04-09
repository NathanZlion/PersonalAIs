from beanie import PydanticObjectId
from fastapi import Depends

from src.dtos.session_dto import (
    SessionCreateInputDto,
    SessionCreateResultDto,
    SessionGetByIdResultDto,
)
from src.repository.session_repo import SessionRepo


class SessionService:
    def __init__(
        self,
        session_repo: SessionRepo = Depends(),
    ):
        self.__session_repo = session_repo

    async def create_new_session(
        self,
        create_session_dto: SessionCreateInputDto,
    ) -> SessionCreateResultDto:
        try:
            new_session = await self.__session_repo.create(session=create_session_dto)
            assert new_session.id is not None, "Session creation failed"
            return SessionCreateResultDto(
                **new_session.model_dump(), session_id=new_session.id
            )
        except Exception as e:
            raise e

    async def get_session_by_id(
        self,
        session_id: PydanticObjectId,
    ) -> SessionGetByIdResultDto:
        session = await self.__session_repo.get_by_id(session_id=session_id)

        assert session is not None, "Session not found"
        assert session.id is not None, "Session ID is None"

        return SessionGetByIdResultDto(
            **session.model_dump(),
            session_id=session.id,
        )
