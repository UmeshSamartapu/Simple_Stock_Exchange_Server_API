from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    email: EmailStr
    hashed_password: str
    portfolio: List[dict] = []

class UserInDB(User):
    id: Optional[str] = Field(alias="_id")

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Order(BaseModel):
    user_email: EmailStr
    stock_symbol: str
    quantity: int
    order_type: str  # buy or sell
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class OrderInDB(Order):
    id: Optional[str] = Field(alias="_id")
