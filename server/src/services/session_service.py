from typing import Optional
from beanie import PydanticObjectId
from fastapi import Depends
from src.utils.logger import logg

from src.dtos.session_dto import (
    SessionCreateInputDto,
    # SessionCreateResultDto,
    SessionResultDTO,
)
from src.repository.session_repo import SessionRepo


class SessionService:
    def __init__(self, session_repo: SessionRepo = Depends()):
        self.__session_repo = session_repo

    async def create_new_session(
        self, create_session_dto: SessionCreateInputDto
    ) -> SessionResultDTO:
        try:
            new_session = await self.__session_repo.create(session=create_session_dto)
            return SessionResultDTO(**new_session.model_dump())

        except Exception as e:
            raise e

    async def get_session_by_id(
        self, session_id: PydanticObjectId
    ) -> Optional[SessionResultDTO]:
        session = await self.__session_repo.get_by_id(session_id=session_id)

        if not session:
            return None

        assert session.id is not None, "Session ID is None"

        return SessionResultDTO(
            **session.model_dump(),
        )

    async def delete_session_by_id(
        self, session_id: PydanticObjectId
    ) -> Optional[SessionResultDTO]:
        try:
            deleted_session = await self.__session_repo.delete_by_id(
                session_id=session_id
            )

            if deleted_session is None:
                return None

            return SessionResultDTO(
                **deleted_session.model_dump(),
            )
        except Exception as e:
            logg.exception(f"Error deleting session: {e}")
