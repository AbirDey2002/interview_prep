import uvicorn
import gzip
import pickle
from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Optional
from pydantic import BaseModel
from create.create_endpoints import router as create_router
from delete.delete_endpoints import router as delete_router
from fetch.get_endpoints import router as fetch_router
from update.update_endpoints import router as update_router
from database import item_inventory

@asynccontextmanager
async def lifespan(app: FastAPI):

    '''
    SERVER STARTING: Loading Database
    '''

    try:
        with gzip.open("database.pkl.gz", "rb") as f:
            data = pickle.load(f)
            item_inventory.update(data)
        print("Data Loaded from database.pkl.gz")
    except Exception as e:
        print(f"No Database Zip Found: {e}")

    yield

    '''
    SERVER STOPPING: Saving Database
    '''

    try:
        with gzip.open("database.pkl.gz", "wb") as f:
            pickle.dump(item_inventory, f)
        print("Data Saved To database.pkl.gz")
    except Exception as e:
        print(f"Error saving database: {e}")
    

app = FastAPI(title="Marketplace Middleware", lifespan=lifespan)
app.include_router(create_router)
app.include_router(delete_router)
app.include_router(fetch_router)
app.include_router(update_router)

@app.get("/", tags=["General"])
def home():
    return {"message": "Server Is Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)