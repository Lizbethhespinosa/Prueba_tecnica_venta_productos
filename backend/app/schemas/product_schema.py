from pydantic import BaseModel


# CREAR PRODUCTO
class ProductCreate(BaseModel):

    nombre: str
    precio: float
    image_url: str


# RESPUESTA PRODUCTO
class ProductResponse(BaseModel):

    id: int
    nombre: str
    precio: float
    image_url: str

    class Config:
        from_attributes = True


# ACTUALIZAR PRODUCTO
class ProductUpdate(BaseModel):

    nombre: str
    precio: float
    image_url: str