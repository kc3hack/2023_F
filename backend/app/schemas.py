# フロントエンドに渡す情報を定義する

from pydantic import BaseModel


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
    title: str
    have_books: int
    resist_date: str
    new_books: int
    user_id: int
