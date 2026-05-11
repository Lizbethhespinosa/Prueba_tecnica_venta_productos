from pydantic import BaseModel


# CREAR COMPRA
class PurchaseCreate(BaseModel):

    user_id: int
    product_id: int
    total_productos: int


# RESPUESTA COMPRA
class PurchaseResponse(BaseModel):

    id: int
    user_id: int
    product_id: int
    total_productos: int

    class Config:
        from_attributes = True