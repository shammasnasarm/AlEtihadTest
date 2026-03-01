from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    available = Column(Boolean, default=True)


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class Checkout(Base):
    __tablename__ = "checkouts"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    checkout_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)

    book = relationship("Book")
    member = relationship("Member")