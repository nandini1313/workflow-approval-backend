from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RequestCreate(BaseModel):
    title: str
    description: str
    priority: str
    reviewer_id: Optional[int] = None


class RequestResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str

    created_by: Optional[int] = None
    reviewer_id: Optional[int] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True