from fastapi.security import OAuth2PasswordBearer
from jose.exceptions import JWTError
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from fastapi.param_functions import Depends
from typing import Union
from datetime import datetime, timedelta
from jose import jwt
from . import database, cruds, bcrypt, env

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def login(name: str, password: str, db: Session):
    user = cruds.get_user_by_name(name=name, db=db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )
    if not bcrypt.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=env.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


def create_access_token(data: dict, expires_delta: Union[int, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, env.SECRET_KEY, algorithm=env.ALGORITHM)
    return encoded_jwt


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Colud not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=env.ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = cruds.get_user_by_name(name=username, db=db)
    if user is None:
        raise credentials_exception
    return user
