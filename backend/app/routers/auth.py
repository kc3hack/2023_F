from fastapi import APIRouter, Depends
from fastapi.param_functions import Depends as authDepends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, oauth2


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
def get_token(
    request: OAuth2PasswordRequestForm = authDepends(),
    db: Session = Depends(database.get_db),
):
    return oauth2.login(name=request.username, password=request.password, db=db)
