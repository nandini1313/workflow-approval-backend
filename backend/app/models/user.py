from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    google_id = Column(String, unique=True, nullable=False)

    role = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )