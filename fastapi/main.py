from fastapi import FastAPI
from enum import Enum
from items import items

app = FastAPI()

class Shop(str, Enum):
    shop = "Shop"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id in items:
        return {item_id: items[item_id]}
    return {"error": "Item not found"}

@app.get("/shops/{shop_name}")
async def get_model(shop_name: Shop):
    if shop_name == Shop.shop:
        return {"shop_name": shop_name, "message": "Success!"}

# uvicorn main:app --reload
