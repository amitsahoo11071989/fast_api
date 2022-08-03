from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime

class UserStruct(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PostStructBase(BaseModel):
    title: str
    content: str

class PostStruct(PostStructBase):
    pass

class PostResponse(PostStructBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class Tokendata(BaseModel):
    id: Optional[int]= None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


