from datetime import datetime, timedelta

from jose import jwt
from jose import JWTError

from backend.app.core.config import (
    SECRET_KEY,
    JWT_ALGORITHM
)


def create_access_token(
    data: dict,
    expires_minutes: int = 60
):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=expires_minutes
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )


def verify_access_token(
    token: str
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        return payload

    except JWTError:
        return None