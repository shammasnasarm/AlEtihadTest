from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import AsyncSessionLocal, engine, Base
from app import schemas
from app.repositories import BookRepository, MemberRepository, CheckoutRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Library API with Repository", lifespan=lifespan)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        yield db


@app.post("/books")
async def create_book(data: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    return await BookRepository(db).create(data)


@app.get("/books")
async def list_books(db: AsyncSession = Depends(get_db)):
    return await BookRepository(db).list()


@app.get("/books/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    return await BookRepository(db).get(book_id)


@app.post("/members")
async def create_member(data: schemas.MemberCreate, db: AsyncSession = Depends(get_db)):
    return await MemberRepository(db).create(data)


@app.get("/members")
async def list_members(db: AsyncSession = Depends(get_db)):
    return await MemberRepository(db).list()


@app.get("/members/{member_id}")
async def get_member(member_id: int, db: AsyncSession = Depends(get_db)):
    return await MemberRepository(db).get(member_id)


@app.post("/checkout")
async def checkout_book(data: schemas.CheckoutCreate, db: AsyncSession = Depends(get_db)):
    return await CheckoutRepository(db).checkout_book(data)


@app.get("/checkout/{checkout_id}")
async def get_checkout(checkout_id: int, db: AsyncSession = Depends(get_db)):
    return await CheckoutRepository(db).get(checkout_id)


@app.get("/checkout")
async def list_checkouts(db: AsyncSession = Depends(get_db)):
    return await CheckoutRepository(db).list()


@app.post("/return/{checkout_id}")
async def return_book(checkout_id: int, db: AsyncSession = Depends(get_db)):
    return await CheckoutRepository(db).return_book(checkout_id)
