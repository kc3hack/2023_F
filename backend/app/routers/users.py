from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, cruds, schemas, oauth2

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def read_users(user_name: str, db: Session = Depends(database.get_db)):
    return cruds.get_user_by_name(name=user_name, db=db)


@router.post("/create")
def create_user(user: schemas.CreateUser, db: Session = Depends(database.get_db)):
    cruds.create_user(user=user, db=db)
    access_token = oauth2.login(name=user.name, password=user.password, db=db)
    return access_token
