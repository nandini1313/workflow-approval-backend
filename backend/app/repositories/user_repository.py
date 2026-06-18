from sqlalchemy.orm import Session

from backend.app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(User).all()

    @staticmethod
    def update_role(
        db: Session,
        user_id: int,
        role: str
    ):
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return None

        user.role = role

        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def create_user(
        db: Session,
        name: str,
        email: str,
        google_id: str,
        role: str = "REQUESTER"
    ):
        user = User(
            name=name,
            email=email,
            google_id=google_id,
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user