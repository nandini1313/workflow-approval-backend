from sqlalchemy.orm import Session

from backend.app.models.approval_request import ApprovalRequest
from backend.app.models.review_action import ReviewAction


class RequestRepository:

    @staticmethod
    def create(
        db: Session,
        request_data: dict
    ):
        request = ApprovalRequest(**request_data)

        db.add(request)
        db.commit()
        db.refresh(request)

        return request

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(
            ApprovalRequest
        ).all()

    @staticmethod
    def get_by_id(
        db: Session,
        request_id: int
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.id == request_id
        ).first()

    @staticmethod
    def get_my_requests(
        db: Session,
        user_id: int
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.created_by == user_id
        ).all()

    @staticmethod
    def get_total_requests(
        db: Session
    ):
        return db.query(
            ApprovalRequest
        ).count()

    @staticmethod
    def get_pending_requests(
        db: Session
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.status == "PENDING"
        ).count()

    @staticmethod
    def get_approved_requests(
        db: Session
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.status == "APPROVED"
        ).count()

    @staticmethod
    def get_rejected_requests(
        db: Session
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.status == "REJECTED"
        ).count()

    @staticmethod
    def update(
        db: Session,
        request_id: int,
        data: dict
    ):
        request = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.id == request_id
        ).first()

        if not request:
            return None

        for key, value in data.items():
            setattr(
                request,
                key,
                value
            )

        db.commit()
        db.refresh(request)

        return request

    @staticmethod
    def delete(
        db: Session,
        request_id: int
    ):
        request = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.id == request_id
        ).first()

        if not request:
            return False

        db.query(
            ReviewAction
        ).filter(
            ReviewAction.request_id == request_id
        ).delete()

        db.delete(request)
        db.commit()

        return True

    @staticmethod
    def approve_request(
        db: Session,
        request_id: int
    ):
        request = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.id == request_id
        ).first()

        if not request:
            return None

        request.status = "APPROVED"

        db.commit()
        db.refresh(request)

        return request

    @staticmethod
    def reject_request(
        db: Session,
        request_id: int
    ):
        request = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.id == request_id
        ).first()

        if not request:
            return None

        request.status = "REJECTED"

        db.commit()
        db.refresh(request)

        return request

    @staticmethod
    def get_requests_for_reviewer(
        db: Session,
        reviewer_id: int
    ):
        return db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.reviewer_id == reviewer_id
        ).all()