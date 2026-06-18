from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class ReviewRequest(BaseModel):
    comments: Optional[str] = None
    reviewed_by: Optional[int] = None


class ReviewResponse(BaseModel):
    id: int
    request_id: int
    action: str
    comments: Optional[str] = None
    reviewed_by: Optional[int] = None
    reviewed_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )