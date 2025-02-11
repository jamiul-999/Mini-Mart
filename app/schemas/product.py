from pydantic import BaseModel, Field
from typing import Optional, List
from .base import BaseSchema

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True
    
class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    
class Category(CategoryBase, BaseSchema):
    slug: str
    products: Optional[List["Product"]] = []
    
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    category_id: int
    is_available: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(gt=0, default=None)
    stock: Optional[int] = Field(ge=0, default=None)
    category_id: Optional[int] = None
    is_available: Optional[bool] = None
    
class Product(ProductBase, BaseSchema):
    slug: str
    category: Optional[Category] = None