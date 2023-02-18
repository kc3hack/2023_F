# データベースに登録する情報を定義する

from sqlalchemy import Column, Integer, String, TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    shelf_id = Column(Integer, ForeignKey("Shelf.id"))
    shelf = relationship("Shelf", back_populates="book_id", uselist=False)

class Books(Base):
    # 本の登録を行うクラス
    # title, have_books, resist_date, new_books
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    have_books = Column(Integer)
    resist_date = Column(TIMESTAMP(timezone=True))
    new_books = Column(Integer)
    shelf_id = Column(Integer, ForeignKey("Shelf.id"))
    shelf = relationship("Shelf", back_populates="book_id")

class Shelf(Base):
    # 本棚に登録を行うクラス
    __tablename__ = "Shelf"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    books = relationship("Books", back_populates="shelf")
