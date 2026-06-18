from sqlalchemy.orm import Session

from backend.app.models.review_action import ReviewAction


class ReviewRepository:

    @staticmethod
    def create_review_action(
        db: Session,
        request_id: int,
        action: str,
        comments: str = None,
        reviewed_by: int = None
    ):
        review_action = ReviewAction(
            request_id=request_id,
            action=action,
            comments=comments,
            reviewed_by=reviewed_by
        )

        db.add(review_action)
        db.commit()
        db.refresh(review_action)

        return review_action

    @staticmethod
    def get_request_history(
        db: Session,
        request_id: int
    ):
        return (
            db.query(ReviewAction)
            .filter(
                ReviewAction.request_id == request_id
            )
            .all()
        )