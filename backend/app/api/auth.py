from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends
from fastapi import HTTPException

from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from authlib.integrations.starlette_client import OAuth

from backend.app.database.session import get_db

from backend.app.core.config import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)

from backend.app.core.security import (
    create_access_token,
    verify_access_token
)

from backend.app.repositories.user_repository import (
    UserRepository
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

security = HTTPBearer()

oauth = OAuth()

oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=(
        "https://accounts.google.com/"
        ".well-known/openid-configuration"
    ),
    client_kwargs={
        "scope": "openid email profile"
    }
)


@router.get("/google/login")
async def google_login(
    request: Request
):
    redirect_uri = (
        "http://127.0.0.1:8000/auth/google/callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/google/callback")
async def google_callback(
    request: Request,
    db: Session = Depends(get_db)
):
    token = await oauth.google.authorize_access_token(
        request
    )

    user_info = token.get(
        "userinfo"
    )

    user = UserRepository.get_by_email(
        db,
        user_info["email"]
    )

    if not user:
        user = UserRepository.create_user(
            db=db,
            name=user_info["name"],
            email=user_info["email"],
            google_id=user_info["sub"],
            role="REQUESTER"
        )

    jwt_token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role
        }
    )

    frontend_url = (
        f"http://localhost:5173/auth/callback"
        f"?token={jwt_token}"
    )

    return RedirectResponse(
        url=frontend_url
    )


@router.get("/me")
def get_me(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):
    token = credentials.credentials

    payload = verify_access_token(
        token
    )

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return {
        "user_id": payload.get("user_id"),
        "email": payload.get("email"),
        "name": payload.get("name"),
        "role": payload.get("role")
    }