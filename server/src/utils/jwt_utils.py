import base64
from datetime import datetime, timedelta
import os
from typing import Dict, Any
import jwt
from jwt.exceptions import InvalidTokenError
from src.core.config import CONFIG
from src.core.exceptions import MalformedTokenError, TokenNotFoundError
from src.utils.helper_functions import get_current_time
from fastapi.encoders import jsonable_encoder
from src.utils.logger import logg


NEVER_EXPIRE = None


class Token:
    def __init__(self, token: str, exp: datetime):
        self.token = token
        self.expiration_date = exp


class JWT_UTILS:
    @staticmethod
    def generate_token(
        payload: Dict[str, Any],
        expires_delta: timedelta,
        SECRET_KEY: str = CONFIG.JWT_SECRET,
        ALGORITHM: str = CONFIG.JWT_ALGORITHM,
    ) -> Token:

        payload_to_encode = payload.copy()
        exp = get_current_time() + expires_delta
        payload_to_encode.update({"exp": exp.timestamp()})
        # to ensure all values are JSON serializable
        serializable_payload = jsonable_encoder(payload_to_encode)
        logg.debug(f"Payload to encode: {serializable_payload}")

        encoded_jwt = jwt.encode(
            payload=serializable_payload,
            key=SECRET_KEY,
            algorithm=ALGORITHM,
            headers={"alg": ALGORITHM, "typ": "JWT"},
        )

        logg.debug(f"Encoded JWT: {encoded_jwt}")
        return Token(
            token=encoded_jwt,
            exp=exp,
        )

    @staticmethod
    def decode_jwt(
        token: str,
        SECRET_KEY: str = CONFIG.JWT_SECRET,
        ALGORITHM: str = CONFIG.JWT_ALGORITHM,
    ) -> Dict[str, Any]:
        """Decode the JWT token and return the payload."""
        try:
            if not token:
                raise TokenNotFoundError(detail="Found empty token")
            payload = jwt.decode(
                jwt=token,
                key=SECRET_KEY,
                algorithms=[ALGORITHM],
                json_encoder=jsonable_encoder,
            )

            logg.debug(f"Decoded payload: {payload}")
            return payload
        except InvalidTokenError as e:
            logg.exception(f"InvalidTokenError: {e}")
            raise MalformedTokenError(detail="Token is malformed")
        except Exception as e:
            logg.exception(f"Exception decoding token: {e}")
            raise MalformedTokenError(detail="Token is malformed")

    @staticmethod
    def generate_random_token(
        expires_delta: timedelta = CONFIG.REFRESH_TOKEN_LIFETIME,
        length: int = 32,
    ) -> Token:
        exp = get_current_time() + expires_delta
        # Generate a random token using os.urandom and encode it in base64
        random_token = base64.urlsafe_b64encode(os.urandom(length)).decode("utf-8")
        logg.debug(f"Generated random token: {random_token}")
        return Token(
            token=random_token,
            exp=exp,
        )
