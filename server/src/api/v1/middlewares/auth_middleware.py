from fastapi import Response, Request, HTTPException, status
from src.utils.logger import logg
from pydantic import ValidationError
from starlette.middleware.base import BaseHTTPMiddleware
from functools import wraps

from src.core.exceptions import (
    MalformedTokenError,
    TokenExpiredError,
    TokenNotFoundError,
)
from src.dtos.auth_dto import AuthAccessTokenSignedData
from src.utils.helper_functions import get_current_time
from src.utils.jwt_utils import JWT_UTILS


def ensure_user_authenticated(request: Request) -> None:
    """Centralized function to check if the request is authenticated."""

    if not getattr(request.state, "auth", None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthenticated user"
        )
    try:
        auth_token_signed_data = AuthAccessTokenSignedData.model_validate(
            request.state.auth
        )

        # Check if the access token has expired
        if auth_token_signed_data.expiration_time > get_current_time():
            raise TokenExpiredError()

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth data"
        )


class AuthUserExtractFromTokenMiddleware(BaseHTTPMiddleware):
    """Middleware to handle extracting and validating the JWT token from the request header."""

    async def dispatch(self, request: Request, call_next):
        try:
            authorization_header = request.headers.get("Authorization")
            logg.debug(
                f"Authorization header: {authorization_header}, request: {request.url}"
            )
            if authorization_header:
                parts = authorization_header.split(" ")

                if len(parts) != 2:
                    raise MalformedTokenError()

                token = parts[1]

                logg.debug(f"Token: {token}")

                decoded_token = JWT_UTILS.decode_jwt(token)

                logg.debug(f"Decoded Info: {decoded_token}")
                authdata = AuthAccessTokenSignedData.model_validate(decoded_token)
                logg.debug(f"Auth data: {authdata}")

                # save the auth data in the request state, for access in later processes
                request.state.auth = authdata

            response = await call_next(request)
            return response

        except (MalformedTokenError, ValidationError) as e:
            return Response(content="Malformed header defect", status_code=400)

        except TokenNotFoundError:
            return await call_next(request)

        except Exception:
            return await call_next(request)


async def UnauthorizedUserBlockMiddleware(request: Request):
    """Middleware to block unauthorized users using the centralized authentication check."""
    try:
        ensure_user_authenticated(request)
    except HTTPException as e:
        raise e
    except Exception:
        return Response(content="Something went wrong", status_code=500)


def authenticated_only(func):
    """Decorator that ensures the endpoint is accessed by an authenticated user."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Find the Request object
        request = kwargs.get("request")
        if not request:
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
        if not request:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Request not provided."
            )

        ensure_user_authenticated(request)
        return await func(*args, **kwargs)

    return wrapper
