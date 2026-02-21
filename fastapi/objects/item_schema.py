from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: int
    description: Optional[str] = None