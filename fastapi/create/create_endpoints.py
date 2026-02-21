from fastapi import APIRouter, HTTPException
from objects.item_schema import Item
from database import item_inventory

router = APIRouter(tags=["Create"])

@router.post("/items/{item_id}")
def create_item(item_id: int, item:Item):
    if item_id in item_inventory:
        raise HTTPException(status_code=400, detail="Item Already Exists For That ID")
    item_inventory[item_id] = item
    output = {
        "status":201,
        "message":"Item Created Successfully",
        "data": item
        }
    return output