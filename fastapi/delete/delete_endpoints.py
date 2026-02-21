from fastapi import APIRouter, HTTPException
from database import item_inventory
from objects.item_schema import Item

router = APIRouter(tags=["Delete"])

@router.delete("/item/{item_id}")
def delete_item(item_id: int):
    if item_id not in item_inventory.keys():
        raise HTTPException(status_code=404, detail="This Resource Does Not Exist")
    item_inventory[item_id] = None
    output = {
        "status":200,
        "message": "Resource Successfully Deleted"
    }
    return output