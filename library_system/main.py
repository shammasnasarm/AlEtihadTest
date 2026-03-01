from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from app import schemas
from app.repositories import BookRepository, MemberRepository, CheckoutRepository

app = FastAPI(title="Library API with Repository + Alembic")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books")
def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    return BookRepository(db).create(data)


@app.get("/books")
def list_books(db: Session = Depends(get_db)):
    return BookRepository(db).list()


@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    return BookRepository(db).get(book_id)


@app.post("/members")
def create_member(data: schemas.MemberCreate, db: Session = Depends(get_db)):
    return MemberRepository(db).create(data)


@app.get("/members")
def list_members(db: Session = Depends(get_db)):
    return MemberRepository(db).list()


@app.get("/members/{member_id}")
def get_member(member_id: int, db: Session = Depends(get_db)):
    return MemberRepository(db).get(member_id)


@app.post("/checkout")
def checkout_book(data: schemas.CheckoutCreate, db: Session = Depends(get_db)):
    return CheckoutRepository(db).checkout_book(data)


@app.get("/checkout/{checkout_id}")
def get_checkout(checkout_id: int, db: Session = Depends(get_db)):
    return CheckoutRepository(db).get(checkout_id)


@app.get("/checkout")
def list_checkouts(db: Session = Depends(get_db)):
    return CheckoutRepository(db).list()

@app.post("/return/{checkout_id}")
def return_book(checkout_id: int, db: Session = Depends(get_db)):
    return CheckoutRepository(db).return_book(checkout_id)