from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
   title:str
   content:str
   published: bool= True
   
#     #rating : Optional [int] = None

class PostCreate(PostBase):
   pass


class Post(PostBase):
    id:int
    created_at: datetime
    user_id: int

    class config:
      orm_mode = True

class UserCreate(BaseModel):
   email : EmailStr
   password : str

class UserOut(BaseModel):
   email : EmailStr
   id : int   
   created_at : datetime

   class config:
      orm_mode = True

class UserLogin(BaseModel):
   email:EmailStr
   password:str

class token(BaseModel):
   access_token: str
   token_type: str

class tokenData(BaseModel):
   id: Optional [str] = None
