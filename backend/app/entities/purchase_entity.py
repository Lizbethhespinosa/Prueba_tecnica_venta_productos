from dataclasses import dataclass
from typing import Optional


@dataclass
class PurchaseEntity:
    id: Optional[int] = None
    user_id: int = 0
    product_id: int = 0
    total_productos: int = 0