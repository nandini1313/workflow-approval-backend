from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.schemas.request import (
RequestResponse
)

from backend.app.services.request_service import (
RequestService
)

from backend.app.dependencies.auth import (
require_reviewer
)

router = APIRouter(
prefix="/reviewer",
tags=["Reviewer"]
)

@router.get(
"/requests",
response_model=list[RequestResponse]
)
def get_reviewer_requests(
current_user=Depends(require_reviewer),
db: Session = Depends(get_db)
):
        
    return RequestService.get_requests_for_reviewer(
    db,
    current_user.id
)
