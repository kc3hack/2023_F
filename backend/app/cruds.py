from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas, bcrypt
from fastapi import HTTPException, status


def create_user(user: schemas.CreateUser, db: Session):
    hashed_pwd = bcrypt.hash(user.password)
    new_user = models.User(name=user.name, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_name(name: str, db: Session):
    return db.query(models.User).filter(models.User.name == name).first()


def count_same_books(book: schemas.CreateBook, user_id: int, db: Session):
    return (
        db.query(models.Books)
        .filter(models.Books.title == book.title)
        .filter(models.Books.user_id == user_id)
        .count()
    )


def create_book(book: schemas.CreateBook, user_id: int, db: Session):
    new_book = models.Books(
        title=book.title,
        have_books=count_same_books(book=book, user_id=user_id, db=db) + 1,
        resist_date=book.resist_date,
        new_books=book.new_books,
        user_id=user_id,
        image_url=book.image_url
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_all_books(user_id: int, db: Session):
    response = db.execute(
        text(
            """
SELECT
    *
FROM
    books
WHERE
    id IN (
        SELECT
            MAX(id)
        FROM
            books
        GROUP BY
            title,
            new_books,
            user_id
    )
    AND user_id = :user_id
            """
        ),
        {"user_id": user_id},
    )

    keys = [
        "id",
        "title",
        "have_books",
        "resist_date",
        "new_books",
        "user_id",
        "is_inshelf",
    ]
    return [dict(zip(keys, row)) for row in response]


def get_books_by_id(id: int, db: Session):
    return db.query(models.Books).filter(models.Books.id == id).first()


def update_book(id: int, book: schemas.Books, db: Session):
    updated_book = db.query(models.Books).filter(models.Books.id == id).first()
    updated_book.title = book.title
    updated_book.have_books = book.have_books
    updated_book.resist_date = book.resist_date
    updated_book.new_books = book.new_books
    updated_book.user_id = book.user_id
    db.commit()
    db.refresh(updated_book)
    return updated_book


def get_shelf(user_id: int, db: Session):
    books = (
        db.query(models.Books)
        .filter(user_id == models.Books.user_id, models.Books.is_inshelf == True)
        .all()
    )
    if not books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"books not found"
        )

    return (
        db.query(models.Books)
        .filter(user_id == models.Books.user_id, models.Books.is_inshelf == True)
        .all()
    )
