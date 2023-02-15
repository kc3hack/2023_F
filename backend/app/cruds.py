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
