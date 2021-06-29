from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    email:str
    password:str
    is_admin: bool = False


class ShowUser(BaseModel):
    email: str
    is_admin: bool
    # roles: List[Role] = []

    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
