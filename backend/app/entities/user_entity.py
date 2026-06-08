from dataclasses import dataclass
from typing import Optional


@dataclass
class UserEntity:
    id: Optional[int] = None
    nombre: str = ""
    email: str = ""
    password: str = ""