from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from backend.app.database.base import Base


class ReviewAction(Base):
    __tablename__ = "review_actions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    request_id = Column(
        Integer,
        ForeignKey("approval_requests.id"),
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    comments = Column(
        Text,
        nullable=True
    )

    reviewed_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    reviewed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )