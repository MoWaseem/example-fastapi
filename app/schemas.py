from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel): # this pydantic class to get and return body with pydantic formatic
    title:str
    content:str
    published :bool=True
   
    
class PostCreate(PostBase): 
      pass

class UserBase(BaseModel):
      email:EmailStr
      password:str
      
      
class UserCreate(UserBase):
      p_num:str
      pass
      
     
class UserOut(BaseModel):
      id:int
      email:EmailStr
      created_at:datetime
      p_num:str
      class Config:
          orm_mode =True
class Post(PostBase):
     id:int
     created_at:datetime
     owner_id:int 
     owner:UserOut
     #if we want to send Response back to body, we need to use orm_mode=True 
     class Config:
          orm_mode =True

class PostOut(BaseModel):
      Post:Post
      like:int

class UserLogin(BaseModel):
      email:EmailStr
      password:str

class Token(BaseModel):
      access_token:str
      token_type:str
 
class TokenData(BaseModel):
      id:Optional[str]=None

class Vote(BaseModel):
      post_id:int
      dir:conint(le=1)