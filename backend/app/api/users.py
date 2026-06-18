from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.schemas.user import (
    UserResponse,
    UserRoleUpdate
)

from backend.app.repositories.user_repository import (
    UserRepository
)

from backend.app.dependencies.auth import (
    require_admin
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "",
    response_model=list[UserResponse]
)
def get_users(
    current_user=Depends(
        require_admin
    ),
    db: Session = Depends(get_db)
):
    return UserRepository.get_all(db)


@router.put(
    "/{user_id}/role",
    response_model=UserResponse
)
def update_user_role(
    user_id: int,
    role_data: UserRoleUpdate,
    current_user=Depends(
        require_admin
    ),
    db: Session = Depends(get_db)
):
    user = UserRepository.update_role(
        db,
        user_id,
        role_data.role
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user