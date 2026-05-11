from pydantic import BaseModel

class PurchaseCreate(BaseModel):
    user_id: int
    product_id: int
    total_productos: int