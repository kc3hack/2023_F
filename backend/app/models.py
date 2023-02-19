# データベースに登録する情報を定義する

from sqlalchemy import Column, Integer, String, TIMESTAMP, BOOLEAN
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)


class Books(Base):
    # 本の登録を行うクラス
    # title, have_books, resist_date, new_books
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    have_books = Column(Integer)
    resist_date = Column(TIMESTAMP(timezone=True))
    new_books = Column(Integer)
    user_id = Column(Integer)
    is_inshelf = Column(BOOLEAN)
    image_url = Column(String(1024))
