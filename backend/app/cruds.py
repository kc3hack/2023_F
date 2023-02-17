from sqlalchemy.orm import Session
from . import models, schemas, bcrypt


def create_user(user: schemas.CreateUser, db: Session):
    hashed_pwd = bcrypt.hash(user.password)
    new_user = models.User(name=user.name, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_name(name: str, db: Session):
    return db.query(models.User).filter(models.User.name == name).first()


def get_all_books(user_id: int, db: Session):
    return db.query(models.Books).filter(user_id == models.Books.user_id).all()


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
