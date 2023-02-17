from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, cruds, schemas, oauth2

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
def read_books(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return cruds.get_books_by_id(id=id, db=db)


@router.put("/update")
def update_books(
    id: int,
    book: schemas.Books,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return cruds.update_book(id=id, book=book, db=db)