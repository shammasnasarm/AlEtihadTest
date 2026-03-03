from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class Task(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    due_date: Optional[date] = None
    is_done: bool = False
    created_at: datetime