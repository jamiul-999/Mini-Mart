from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    cart_items = relationship("CartItem", back_populates="user")
    orders = relationship("Order", back_populates="user")