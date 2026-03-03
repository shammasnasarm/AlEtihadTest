from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str


class MemberCreate(BaseModel):
    name: str
    email: str


class CheckoutCreate(BaseModel):
    book_id: int
    member_id: int


class CheckoutResponse(BaseModel):
    id: int
    book_id: int
    member_id: int
    checkout_date: datetime
    return_date: datetime | None

    class Config:
        from_attributes = True