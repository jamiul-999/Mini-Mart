from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    email: str
    
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str]
    stock: int