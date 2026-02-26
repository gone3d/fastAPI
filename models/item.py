"""
Item-related Pydantic models
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Item(BaseModel):
    """
    Item model for CRUD operations
    """
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    created_at: Optional[datetime] = None


class Message(BaseModel):
    """
    Generic message response model
    """
    message: str
    timestamp: datetime
