from fastapi import Depends
from src.core.config import CONFIG
from src.dtos.auth_dto import AuthRegisterSuccessResponse
from src.dtos.session_dto import SessionCreateInputDto
from src.dtos.user_dto import UserCreateInputDto
from src.repository.user_repo import UserRepo

from src.services.session_service import SessionService
from src.utils.jwt_utils import JWT_UTILS


class AuthService:
    def __init__(
        self,
        user_repo: UserRepo = Depends(),
        session_service: SessionService = Depends(),
    ):
        self.__user_repo = user_repo
        self.__session_service = session_service

    async def register(
        self, user_create_dto: UserCreateInputDto
    ) -> AuthRegisterSuccessResponse:
        """Register a new user and create a new session for them."""

        try:
            _user = await self.__user_repo.get_by_spotify_id(user_create_dto.spotify_id)

            if _user is None:
                # Create a new user
                _user = await self.__user_repo.create(user_create_dto)

            # new_user = await self.__user_repo.create(user_create_dto)

            refresh_token = JWT_UTILS.generate_random_token()

            # create a new session
            create_session_dto = SessionCreateInputDto(
                user_id=_user.id,  # type: ignore
                refresh_token=refresh_token.token,
                ip_address=user_create_dto.ip_address,
                user_agent=user_create_dto.user_agent,
                expires_at=refresh_token.expiration_date,
            )

            new_session = await self.__session_service.create_new_session(
                create_session_dto
            )

            """ Generate access and refresh token for user.
            Access token will have the following signed in it:
                - user_data
                - session_id
                - exp: which will be the expiration date of the token, and 
                is added in the generate_token method based on the expires_delta given
            """

            user_data = _user.model_dump(
                # exclude={"created_at", "updated_at"}
            )  # to avoid the datetime serialization error

            access_token = JWT_UTILS.generate_token(
                payload={
                    "user_data": user_data,
                    "session_id": new_session.session_id,
                },
                expires_delta=CONFIG.ACCESS_TOKEN_LIFETIME,
            )

            return AuthRegisterSuccessResponse(
                id=str(_user.id),
                access_token=access_token.token,
                refresh_token=refresh_token.token,
                token_type="Bearer",
                expires_at=access_token.expiration_date.timestamp(),
            )

        except Exception as e:
            raise e
