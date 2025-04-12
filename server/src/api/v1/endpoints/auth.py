from typing import Dict
import urllib.parse
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from src.api.v1.middlewares.auth_middleware import authenticated_only
from src.services.session_service import SessionService
from src.utils.logger import logg
from pydantic_core import ValidationError
import urllib
from requests import get, post

from src.core.container import Container
from src.core.exceptions import NotFoundError, TokenExpiredError
from src.dtos.auth_dto import (
    AuthAccessTokenSignedData,
    AuthCallbackInputDto,
    AuthCallbackResponse,
    AuthLogoutResponse,
    SpotifyCallbackResponse,
)
from src.dtos.spotify_credentials_dto import SpotifyCredentialsCreateInputDto
from src.dtos.user_dto import (
    UserCreateInputDto,
    UserCreateResultDto,
    UserSpotifyProfileDto,
)
from src.services.auth_service import AuthService
from src.core.config import CONFIG
from src.services.spotify_credentials_service import SpotifyCredentialsService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login", response_model=Dict)
@inject
async def login() -> JSONResponse:
    """Login via spotify, will redirect the user to the spotify login page of our app."""
    # TODO: validate state key for already logged in users
    # If the user is already logged in, we should not redirect them, instead refresh the access token and return it.

    scopes = CONFIG.SPOTIFY_PERMISSIONS_SCOPE
    params = {
        "client_id": CONFIG.SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": CONFIG.SPOTIFY_AUTH_REDIRECT_URI,
        "scope": scopes,
        "show_dialog": "true",
        "state": "test",
    }

    redirect_url = f"{CONFIG.SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"

    return JSONResponse(status_code=200, content={"redirect_url": redirect_url})


@router.post("/callback", response_model=AuthCallbackResponse)
@inject
async def callback(
    callback_input: AuthCallbackInputDto,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
    spotify_credentials_service: SpotifyCredentialsService = Depends(
        Provide[Container.spotify_credentials_service]
    ),
) -> AuthCallbackResponse:
    """Callback with the code for the authorization code flow."""

    try:
        logg.info(f"Auth Callback input : {callback_input.model_dump()}")
        if callback_input.error:
            raise HTTPException(status_code=400, detail=callback_input.error)

        if not callback_input.state or not callback_input.code:
            raise HTTPException(status_code=400)

        token_response = post(
            CONFIG.SPOTIFY_TOKEN_URL,
            data={
                "code": callback_input.code,
                "grant_type": "authorization_code",
                "redirect_uri": CONFIG.SPOTIFY_AUTH_REDIRECT_URI,
                "client_id": CONFIG.SPOTIFY_CLIENT_ID,
                "client_secret": CONFIG.SPOTIFY_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            json=True,
        )

        if token_response.status_code != 200:
            raise TokenExpiredError()

        auth_callback_response = SpotifyCallbackResponse.model_validate(
            token_response.json()
        )

        logg.debug(f"Spotify Authentication Reponse: {auth_callback_response} ")

        spotify_user_info_response = get(
            f"{CONFIG.SPOTIFY_API_BASE_URL}/me",
            headers={"Authorization": f"Bearer {auth_callback_response.access_token}"},
        )

        spotify_user_info = UserSpotifyProfileDto.model_validate(
            spotify_user_info_response.json()
        )

        logg.info(f"Spotify User Response: {spotify_user_info}")

        # store the credentials in the database
        await spotify_credentials_service.store_credentials(
            create_spotify_credentials_dto=SpotifyCredentialsCreateInputDto(
                **auth_callback_response.model_dump(),
                spotify_id=spotify_user_info.id,
            )
        )

        # register the user in the database
        registration_success_response = await auth_service.register(
            user_create_dto=UserCreateInputDto(
                email=spotify_user_info.email,
                display_name=spotify_user_info.display_name,
                country=spotify_user_info.country,
                spotify_id=spotify_user_info.id,
                images=spotify_user_info.images,
                # TODO: Add user agent, device type and operating system to the user data
                # Will add a middleware to extract such info if I need it in someother places as well to avoid duplication
                # if not I will extract it here manually
            )
        )

        return AuthCallbackResponse(
            id=registration_success_response.id,
            access_token=registration_success_response.access_token,
            refresh_token=registration_success_response.refresh_token,
            expires_at=registration_success_response.expires_at,
            token_type=registration_success_response.token_type,
            user=UserCreateResultDto(
                id=registration_success_response.id,
                email=spotify_user_info.email,
                display_name=spotify_user_info.display_name,
                country=spotify_user_info.country,
                spotify_id=spotify_user_info.id,
                images=spotify_user_info.images,
            ),
        )
    except ValidationError as e:
        logg.exception(f"Validation Error: {e}")
        raise HTTPException(status_code=400, detail="Validation error")

    except Exception as e:
        logg.exception(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="Unknown error")


@router.post("/logout", response_model=AuthLogoutResponse)
@authenticated_only
@inject
async def logout(
    request: Request,
    session_service: SessionService = Depends(Provide[Container.session_service]),
) -> AuthLogoutResponse:
    """Logout, end the current session of the user."""

    token_data: AuthAccessTokenSignedData = request.state.auth
    session_id = token_data.session_id

    # delete the session, invalidating the refresh token in the process
    session = await session_service.delete_session_by_id(
        session_id=session_id,
    )

    if not session:
        raise NotFoundError(detail="Session not found")

    return AuthLogoutResponse(message="Logged out successfully")
