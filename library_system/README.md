# Library Management REST API (FastAPI)

A clean REST API built using **FastAPI**, **SQLAlchemy** and **pydantic** with:

- Repository Pattern
- SQLite Database

------------------------------------------------------------------------

## Architecture Overview

- **Models** → `app/models.py`
- **Schemas** → `app/schemas.py`
- **Repository Layer** → `app/repositories.py`
- **Main** → `main.py`

------------------------------------------------------------------------

## Project Structure

    library_system/
    │
    ├── app/
    │   ├── models.py
    │   ├── repositories.py
    │   └── schemas.py
    │
    ├── config/
    │   └── database.py
    │
    ├── main.py
    └── requirements.txt

------------------------------------------------------------------------

## Setup Instructions

### Clone the repository

```bash
git clone git@github.com:shammasnasarm/AlEtihadTest.git
cd library_system
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

- Windows:

```bash
venv\Scripts\activate
```

- Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### Running the Application

```bash
uvicorn main:app --reload
```

Open:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Available Endpoints

### Books

- `POST /books` → Create a book
- `GET /books` → List all books
- `GET /books/{book_id}` → Get a book

### Members

- `POST /members` → Create a member
- `GET /members` → List all members
- `GET /members/{member_id}` → Get a member

### Checkout

- `POST /checkout` → Checkout a book
- `GET /checkout` → List all checkouts
- `GET /checkout/{checkout_id}` → Get a checkout
- `POST /return/{checkout_id}` → Return a book

------------------------------------------------------------------------

### Business Rules Implemented

- Book must exist to checkout
- Member must exist
- Book must be available
- Cannot return a book twice
- Book becomes available after return

------------------------------------------------------------------------

### Benefits:

Clear separation of concerns\
Easy to test repository logic independently\
Readable and maintainable

------------------------------------------------------------------------

### Future Improvements

- Add authentication (JWT)
- Add unit tests
- Add pagination / filtering
- Add Alembic migrations
- Use PostgreSQL instead of SQLite

----------------------------------------------------------------------