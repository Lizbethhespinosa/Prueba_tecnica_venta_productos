from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductEntity:
    id: Optional[int] = None
    nombre: str = ""
    precio: float = 0
    image_url: str = ""