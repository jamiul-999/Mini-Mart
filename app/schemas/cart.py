from pydantic import BaseModel, Field
from typing import Optional, List
from .base import BaseSchema
from .product import Product

class CartItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    
class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseSchema):
    quantity: Optional[int] = Field(gt=0, default=None)
    
class CartItem(CartItemBase, BaseSchema):
    user_id: int
    product: Optional[product] = None
    
class CartSummary(BaseModel):
    items: List[CartItem]
    total_amount: float