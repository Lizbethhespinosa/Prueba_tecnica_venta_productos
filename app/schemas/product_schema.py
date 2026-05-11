from pydantic import BaseModel

class ProductCreate(BaseModel):
    nombre: str
    precio: float
    image_url: str