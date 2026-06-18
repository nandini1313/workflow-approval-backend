from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.services.request_service import (
    RequestService
)

from backend.app.dependencies.auth import (
    require_admin
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/stats"
)
def get_dashboard_stats(
    current_user=Depends(
        require_admin
    ),
    db: Session = Depends(get_db)
):
    return RequestService.get_dashboard_stats(
        db
    )