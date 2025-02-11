from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from .base import BaseSchema

class UserBase(BaseModel):
    email: EmailStr
    name: str
    is_active: bool = True
    is_superuser: bool = False
    
class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseSchema):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    
class User(UserBase, BaseSchema):
    pass

class UserInDB(User):
    hashed_password: str