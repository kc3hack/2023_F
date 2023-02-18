# フロントエンドに渡す情報を定義する

from pydantic import BaseModel
from typing import Union


# ユーザーの名前
class BaseUser(BaseModel):
    name: str

    class Config:
        orm_model = True


# ユーザーの名前とパスワード
class CreateUser(BaseUser):
    password: str


# ユーザーの名前とid
class User(BaseUser):
    id: int


# 本の情報
class Books(BaseModel):
    title: Union[str, None]
    have_books: Union[int, None]
    resist_date: Union[str, None]
    new_books: Union[int, None]
    user_id: Union[int, None]


class CreateBook(BaseModel):
    title: Union[str, None]
    resist_date: Union[str, None]
    new_books: Union[int, None]
