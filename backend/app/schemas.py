from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str

    class Config:
        orm_model = True


class CreateUser(BaseUser):
    password: str


class User(BaseUser):
    id: int
