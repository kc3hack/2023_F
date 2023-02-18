# フロントエンドに渡す情報を定義する

from pydantic import BaseModel
from typing import List

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
    class Config:
        orm_model = True

# 本の情報
class Books(BaseModel):
    title: str
    have_books: int
    resist_date: str
    new_books: int
    class Config:
        orm_model = True

#本棚の情報
class Shelf(BaseModel):
    user_id:int
    books_id:int
    books:List[Books]
    class Config:
        orm_model = True

class User_shelf(BaseUser):
    shelf:Shelf