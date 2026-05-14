from pydantic import BaseModel
from datetime import datetime


class PurchaseCreate(BaseModel):
    user_id: int
    product_id: int
    total_productos: int


class PurchaseResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    total_productos: int
    created_at: datetime

    class Config:
        from_attributes = True