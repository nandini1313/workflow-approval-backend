from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import (
    SessionMiddleware
)

from backend.app.api.health import router as health_router
from backend.app.api.requests import router as request_router
from backend.app.api.reviewer import router as reviewer_router
from backend.app.api.auth import router as auth_router
from backend.app.api.users import router as users_router
from backend.app.api.dashboard import (
    router as dashboard_router
)

from backend.app.database.base import Base
from backend.app.database.session import engine

from backend.app.models.user import User
from backend.app.models.approval_request import ApprovalRequest
from backend.app.models.review_action import ReviewAction

from backend.app.core.config import SECRET_KEY

# Create database tables

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Workflow Approval Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY
)

app.include_router(health_router)
app.include_router(request_router)
app.include_router(reviewer_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": "Backend is running successfully"
    }