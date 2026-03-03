from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .models import Book, Member, Checkout


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data):
        book = Book(**data.dict())
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def get(self, book_id: int):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def list(self):
        return self.db.query(Book).all()


class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data):
        member = Member(**data.dict())
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member
    
    def list(self):
        return self.db.query(Member).all()

    def get(self, member_id: int):
        return self.db.query(Member).filter(Member.id == member_id).first()


class CheckoutRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, checkout_id: int):
        return self.db.query(Checkout).filter(Checkout.id == checkout_id).first()
    
    def list(self):
        return self.db.query(Checkout).all()

    def checkout_book(self, data):
        book = self.db.query(Book).filter(Book.id == data.book_id).first()
        if not book:
            raise HTTPException(404, "Book not found")

        if not book.available:
            raise HTTPException(400, "Book not available")

        member = self.db.query(Member).filter(Member.id == data.member_id).first()
        if not member:
            raise HTTPException(404, "Member not found")

        book.available = False

        checkout = Checkout(
            book_id=data.book_id,
            member_id=data.member_id
        )

        self.db.add(checkout)
        self.db.commit()
        self.db.refresh(checkout)
        return checkout

    def return_book(self, checkout_id: int):
        checkout = self.db.query(Checkout).filter(
            Checkout.id == checkout_id
        ).first()

        if not checkout:
            raise HTTPException(404, "Checkout not found")

        if checkout.return_date:
            raise HTTPException(400, "Already returned")

        checkout.return_date = datetime.utcnow()
        checkout.book.available = True
        self.db.commit()
        self.db.refresh(checkout)

        return checkout