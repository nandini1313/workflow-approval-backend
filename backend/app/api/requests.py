from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.schemas.request import (
    RequestCreate,
    RequestResponse
)

from backend.app.schemas.review import (
    ReviewRequest,
    ReviewResponse
)

from backend.app.services.request_service import (
    RequestService
)

from backend.app.core.security import (
    verify_access_token
)

from backend.app.dependencies.auth import (
    require_reviewer,
    get_current_user
)

router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)

security = HTTPBearer()


@router.post(
    "",
    response_model=RequestResponse
)
def create_request(
    request: RequestCreate,
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    request_data = request.model_dump()

    request_data["created_by"] = payload[
        "user_id"
    ]

    return RequestService.create_request(
        db,
        request_data
    )


@router.get(
    "/my",
    response_model=list[RequestResponse]
)
def get_my_requests(
    current_user=Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    return RequestService.get_my_requests(
        db,
        current_user.id
    )


@router.get(
    "",
    response_model=list[RequestResponse]
)
def get_requests(
    db: Session = Depends(get_db)
):
    return RequestService.get_requests(db)


@router.get(
    "/{request_id}",
    response_model=RequestResponse
)
def get_request_by_id(
    request_id: int,
    db: Session = Depends(get_db)
):
    return RequestService.get_request_by_id(
        db,
        request_id
    )


@router.get(
    "/{request_id}/history",
    response_model=list[ReviewResponse]
)
def get_request_history(
    request_id: int,
    db: Session = Depends(get_db)
):
    return RequestService.get_request_history(
        db,
        request_id
    )


@router.put(
    "/{request_id}",
    response_model=RequestResponse
)
def update_request(
    request_id: int,
    request: RequestCreate,
    db: Session = Depends(get_db)
):
    return RequestService.update_request(
        db,
        request_id,
        request.model_dump()
    )


@router.delete(
    "/{request_id}"
)
def delete_request(
    request_id: int,
    db: Session = Depends(get_db)
):
    deleted = RequestService.delete_request(
        db,
        request_id
    )

    if deleted:
        return {
            "message": "Request deleted successfully"
        }

    return {
        "message": "Request not found"
    }


@router.post(
    "/{request_id}/approve",
    response_model=RequestResponse
)
def approve_request(
    request_id: int,
    review: ReviewRequest,
    current_user=Depends(
        require_reviewer
    ),
    db: Session = Depends(get_db)
):
    return RequestService.approve_request(
        db=db,
        request_id=request_id,
        comments=review.comments,
        reviewed_by=current_user.id
    )


@router.post(
    "/{request_id}/reject",
    response_model=RequestResponse
)
def reject_request(
    request_id: int,
    review: ReviewRequest,
    current_user=Depends(
        require_reviewer
    ),
    db: Session = Depends(get_db)
):
    return RequestService.reject_request(
        db=db,
        request_id=request_id,
        comments=review.comments,
        reviewed_by=current_user.id
    )