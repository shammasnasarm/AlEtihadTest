from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from datetime import datetime
from .models import Book, Member, Checkout


class BookRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data):
        book = Book(**data.model_dump())
        self.db.add(book)
        await self.db.commit()
        await self.db.refresh(book)
        return book

    async def get(self, book_id: int):
        result = await self.db.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    async def list(self):
        result = await self.db.execute(select(Book))
        return result.scalars().all()


class MemberRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data):
        member = Member(**data.model_dump())
        self.db.add(member)
        await self.db.commit()
        await self.db.refresh(member)
        return member

    async def list(self):
        result = await self.db.execute(select(Member))
        return result.scalars().all()

    async def get(self, member_id: int):
        result = await self.db.execute(select(Member).where(Member.id == member_id))
        return result.scalar_one_or_none()


class CheckoutRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, checkout_id: int):
        result = await self.db.execute(select(Checkout).where(Checkout.id == checkout_id))
        return result.scalar_one_or_none()

    async def list(self):
        result = await self.db.execute(select(Checkout))
        return result.scalars().all()

    async def checkout_book(self, data):
        book_result = await self.db.execute(select(Book).where(Book.id == data.book_id))
        book = book_result.scalar_one_or_none()
        if not book:
            raise HTTPException(404, "Book not found")

        if not book.available:
            raise HTTPException(400, "Book not available")

        member_result = await self.db.execute(select(Member).where(Member.id == data.member_id))
        member = member_result.scalar_one_or_none()
        if not member:
            raise HTTPException(404, "Member not found")

        book.available = False

        checkout = Checkout(
            book_id=data.book_id,
            member_id=data.member_id,
        )

        self.db.add(checkout)
        await self.db.commit()
        await self.db.refresh(checkout)
        return checkout

    async def return_book(self, checkout_id: int):
        result = await self.db.execute(select(Checkout).where(Checkout.id == checkout_id))
        checkout = result.scalar_one_or_none()

        if not checkout:
            raise HTTPException(404, "Checkout not found")

        if checkout.return_date:
            raise HTTPException(400, "Already returned")

        book_result = await self.db.execute(select(Book).where(Book.id == checkout.book_id))
        book = book_result.scalar_one_or_none()
        book.available = True

        checkout.return_date = datetime.utcnow()
        await self.db.commit()
        await self.db.refresh(checkout)
        return checkout
