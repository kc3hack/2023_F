from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, cruds, schemas, oauth2

router = APIRouter(prefix="/shelf", tags=["shelf"])
@router.post("/create")
def create_shelf(book_id:int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return cruds.registar_shelf(user_id=current_user.id, db=db)