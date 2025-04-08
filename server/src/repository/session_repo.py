from beanie import PydanticObjectId
from src.dtos.session_dto import SessionCreateInputDto
from src.models.sessions_model import Session
from src.repository.base_repo import BaseRepo


class SessionRepo(BaseRepo):
    def __init__(self):
        pass

    async def create(self, session: SessionCreateInputDto) -> Session:
        """Create a new session."""
        return await Session(**session.model_dump()).insert()

    async def get_by_id(self, session_id: PydanticObjectId) -> Session | None:
        """Get a session by id."""
        session = await Session.get(session_id)
        return session
