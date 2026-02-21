from fastapi import APIRouter, HTTPException
from database import item_inventory
from typing import Optional
from pydantic import BaseModel

router = APIRouter(tags=["Update"])

class patch_Item(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None

@router.patch("/item/{item_id}")
def update_item(item_id: int, item: patch_Item):
    if item_id not in item_inventory.keys():
        raise HTTPException(status_code=404, message="This Resource Does Not Exist")
    var = item_inventory[item_id]
    for key in item.keys():
        var[key] = item[key]
    item_inventory[item_id] = var
    output = {
        "status": 200,
        "message": "Resource Updated Successfully",
        "data": item_inventory[item_id]
    }
    return output