from pydantic import BaseModel, field
from typing import Optional, List
from datetime import datetime
from .base import BaseSchema
from .product import Product
from ..models.order import OrderStatus

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    
class OrderItem(OrderItem, BaseSchema):
    order_id: int
    product: Optional[Product] = None
    
class OrderBase(BaseModel):
    total_amount: float = Field(gt=0)
    status: OrderStatus = OrderStatus.PENDING
    
class OrderCreate(BaseModel):
    cart_id: int
    
class OrderUpdate(BaseSchema):
    status: Optional[OrderStatus] = None
    
class Order(OrderBase, BaseSchema):
    user_id: int
    items: List[OrderItem] = []