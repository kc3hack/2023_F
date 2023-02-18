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


@router.post("/create")
def create_book(
    book: schemas.CreateBook,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return cruds.create_book(book=book, user_id=current_user.id, db=db)


@router.get("/all")
def read_all_books(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return cruds.get_all_books(user_id=current_user.id, db=db)


@router.put("/update")
def update_books(
    id: int,
    book: schemas.Books,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return cruds.update_book(id=id, book=book, db=db)

@router.get("/shelf")
def read_shelf_books(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return cruds.get_shelf(user_id=current_user.id, db=db)
