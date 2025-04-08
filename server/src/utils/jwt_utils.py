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

        print("Payload to encode:", jsonable_encoder(payload_to_encode))

        encoded_jwt = jwt.encode(
            payload=jsonable_encoder(payload_to_encode),
            key=SECRET_KEY,
            algorithm=ALGORITHM,
            headers={"alg": ALGORITHM, "typ": "JWT"},
        )

        return Token(
            token=encoded_jwt,
            exp=datetime.now(),
            # exp=exp,
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
            payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except InvalidTokenError as e:
            print(f"InvalidTokenError: {e}")
            raise MalformedTokenError(detail="Token is malformed")
        except Exception as e:
            print(f"Error decoding token: {e}")
            raise MalformedTokenError(detail="Token is malformed")

    @staticmethod
    def generate_random_token(
        expires_delta: timedelta = CONFIG.REFRESH_TOKEN_LIFETIME,
        length: int = 32,
    ) -> Token:
        exp = get_current_time() + expires_delta
        return Token(
            token=base64.urlsafe_b64encode(os.urandom(length)).decode("utf-8"),
            exp=exp,
        )
