from pydantic import BaseModel

class UserBase(BaseModel):
  username: str

class UserCreate(UserBase):
  nickname: str
  hashed_password: str

class UserRead(UserBase):
  id: int
  nickname: str

  class Config:
    orm_mode = True