from datetime import datetime
from typing import Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, ConfigDict

from src.dtos.user_dto import UserCreateResultDto
from datetime import datetime, timedelta
from typing import Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, ConfigDict
from src.dtos.user_dto import UserCreateResultDto
from src.utils.helper_functions import get_current_time


class AuthBase(BaseModel):
    """Auth base schema."""


class AuthCallbackInputDto(AuthBase):
    state: str
    code: str
    error: Optional[str] = None


class AuthRegisterSuccessResponse(AuthBase):
    """
    Auth response when the user is successfully registered.
    This is going to be returned to the user.

    """

    id: str
    access_token: str
    refresh_token: str
    token_type: str
    expires_at: float

    model_config = ConfigDict(
        from_attributes=True,
    )


class AuthCallbackResponse(AuthRegisterSuccessResponse, AuthBase):
    user: UserCreateResultDto


class AuthAccessTokenSignedData(AuthBase):
    """
    The Data that is signed into the access token.
        - user_data
        - session_id
        - expiration_time
    """

    user_data: UserCreateResultDto
    session_id: PydanticObjectId
    expiration_time: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class SpotifyGetMeResponse(AuthBase):
    """
    Response from spotify for /me endpoint.
    """

    id: str
    display_name: str
    email: str
    country: Optional[str] = None
    product: Optional[str] = None
    images: Optional[list] = None

    model_config = ConfigDict(
        from_attributes=True,
    )


class SpotifyCallbackResponse(AuthBase):
    """
    Attributes
    -----------

    - access_token: str
    - refresh_token: str
    - token_type: str, always "Bearer".
    - scope: str, A space-separated list of scopes which have been granted for this access_token
    - expires_in: int, The time period (in seconds) for which the access token is valid.
    - expires_at: Optional[float] = None

    """

    access_token: str
    refresh_token: str
    token_type: str
    scope: str
    expires_in: int  # time period in seconds
    expires_at: Optional[float] = None

    model_config = ConfigDict(
        from_attributes=True,
    )

    def __init__(self, **data):
        super().__init__(**data)
        if self.expires_in is not None:
            self.expires_at = (
                get_current_time() + timedelta(seconds=self.expires_in)
            ).timestamp()
