from re import S
from typing import List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr
from src.models.base_models import CreatedUpdatedAt


class SpotifyImage(BaseModel):
    """Spotify Image schema."""

    url: str
    height: int
    width: int


class UserBase(BaseModel):
    """User base schema."""

    spotify_id: str
    email: EmailStr
    display_name: Optional[str] = None
    country: str
    images: Optional[List[SpotifyImage]] = []  # could be empty


class UserCreateInputDto(UserBase):
    """User Registration schema with email and password."""

    # information to log into the session
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    device_type: Optional[str] = None
    operating_system: Optional[str] = None


class UserGetResultDto(UserBase, CreatedUpdatedAt):
    id: PydanticObjectId


class UserCreateResultDto(UserCreateInputDto, CreatedUpdatedAt):
    id: PydanticObjectId

class UserSpotifyProfileDto(BaseModel):
    """
    This is the response from the /me endpoint of the Spotify API.
    reference: https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile

    Sample Resopnse:
        {
            "country": "string",
            "display_name": "string",
            "email": "string",
            "explicit_content": {
                "filter_enabled": false,
                "filter_locked": false
            },
            "external_urls": {
                "spotify": "string"
            },
            "followers": {
                "href": "string",
                "total": 0
            },
            "href": "string",
            "id": "string",
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228",
                    "height": 300,
                    "width": 300
                }
            ],
            "product": "string",
            "type": "string",
            "uri": "string"
        }
    """

    id: str
    email: EmailStr
    country: str  # two letter country code
    display_name: Optional[str] = None
    explicit_content: Optional[dict] = None
    external_urls: Optional[dict] = None
    followers: Optional[dict] = None
    href: Optional[str] = None
    images: Optional[List[SpotifyImage]] = None
    product: Optional[str] = None
    type: Optional[str] = None
    uri: Optional[str] = None


class UserDeleteDto(UserBase):
    """User delete schema."""

    email: EmailStr
