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


class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text)

    priority = Column(String, nullable=False)

    status = Column(
        String,
        default="PENDING"
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    reviewer_id = Column(
    Integer,
    nullable=True
)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )