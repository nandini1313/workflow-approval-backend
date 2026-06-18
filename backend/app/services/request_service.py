from sqlalchemy.orm import Session

from backend.app.repositories.request_repository import (
    RequestRepository
)

from backend.app.repositories.review_repository import (
    ReviewRepository
)


class RequestService:

    @staticmethod
    def create_request(
        db: Session,
        data: dict
    ):
        return RequestRepository.create(
            db,
            data
        )

    @staticmethod
    def get_requests(
        db: Session
    ):
        return RequestRepository.get_all(db)

    @staticmethod
    def get_my_requests(
        db: Session,
        user_id: int
    ):
        return RequestRepository.get_my_requests(
            db,
            user_id
        )

    @staticmethod
    def get_dashboard_stats(
        db: Session
    ):
        return {
            "total_requests":
                RequestRepository.get_total_requests(db),

            "pending_requests":
                RequestRepository.get_pending_requests(db),

            "approved_requests":
                RequestRepository.get_approved_requests(db),

            "rejected_requests":
                RequestRepository.get_rejected_requests(db)
        }

    @staticmethod
    def get_request_by_id(
        db: Session,
        request_id: int
    ):
        return RequestRepository.get_by_id(
            db,
            request_id
        )

    @staticmethod
    def update_request(
        db: Session,
        request_id: int,
        data: dict
    ):
        return RequestRepository.update(
            db,
            request_id,
            data
        )

    @staticmethod
    def delete_request(
        db: Session,
        request_id: int
    ):
        return RequestRepository.delete(
            db,
            request_id
        )

    @staticmethod
    def approve_request(
        db: Session,
        request_id: int,
        comments: str = None,
        reviewed_by: int = None
    ):
        request = RequestRepository.approve_request(
            db,
            request_id
        )

        if request:
            ReviewRepository.create_review_action(
                db=db,
                request_id=request_id,
                action="APPROVED",
                comments=comments,
                reviewed_by=reviewed_by
            )

        return request

    @staticmethod
    def reject_request(
        db: Session,
        request_id: int,
        comments: str = None,
        reviewed_by: int = None
    ):
        request = RequestRepository.reject_request(
            db,
            request_id
        )

        if request:
            ReviewRepository.create_review_action(
                db=db,
                request_id=request_id,
                action="REJECTED",
                comments=comments,
                reviewed_by=reviewed_by
            )

        return request

    @staticmethod
    def get_requests_for_reviewer(
        db: Session,
        reviewer_id: int
    ):
        return RequestRepository.get_requests_for_reviewer(
            db,
            reviewer_id
        )

    @staticmethod
    def get_request_history(
        db: Session,
        request_id: int
    ):
        return ReviewRepository.get_request_history(
            db,
            request_id
        )