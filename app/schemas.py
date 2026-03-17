from pydantic import BaseModel
from datetime import datetime


class PaymentCreate(BaseModel):
    user_id: int
    amount: float
    status: str = "pending"


class PaymentResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class PaymentStats(BaseModel):
    date: str
    hour: int
    total_amount: float
    payments_count: int