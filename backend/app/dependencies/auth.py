from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.core.security import verify_access_token
from backend.app.repositories.user_repository import UserRepository

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = UserRepository.get_by_id(
        db,
        payload["user_id"]
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def require_reviewer(
    user=Depends(get_current_user)
):
    if user.role != "REVIEWER":
        raise HTTPException(
            status_code=403,
            detail="Reviewer access required"
        )

    return user


def require_admin(
    user=Depends(get_current_user)
):
    if user.role != "ADMIN":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user