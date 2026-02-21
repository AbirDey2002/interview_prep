from fastapi import HTTPException, APIRouter
from database import item_inventory
from objects.item_schema import Item

router = APIRouter(tags=["Fetch"])

@router.get("/items")
def get_all_items():
    output = {
        "status":200,
        "message":"Inventory Retrieved Successfully",
        "data":item_inventory if item_inventory else "No Items In Inventory"
    }
    return output

@router.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id not in item_inventory.keys():
        raise HTTPException(status_code=404, detail="This Resource Does Not Exist")
    output = {
        "status":200,
        "message": "Inventory Item Retrieved Successfully",
        "data": item_inventory[item_id]
    }
    return output