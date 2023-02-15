from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from . import env

SQLALCHEMY_DATABASE_URL = env.SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
