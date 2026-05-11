from pydantic import BaseModel


class PurchaseCreate(BaseModel):

    user_id: int
    product_id: int
    total_productos: int


class PurchaseResponse(BaseModel):

    id: int
    user_id: int
    product_id: int
    total_productos: int

    class Config:
        from_attributes = True