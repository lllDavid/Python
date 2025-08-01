from fastapi import FastAPI, HTTPException, Header, Depends, status
from pydantic import BaseModel
import databases
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
database = databases.Database(DATABASE_URL)

API_KEY = "" 

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    await database.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

@app.get("/items/{item_id}", response_model=Item, dependencies=[Depends(verify_api_key)])
async def read_item(item_id: int):
    query = "SELECT id, name, description FROM items WHERE id = :item_id"
    item = await database.fetch_one(query=query, values={"item_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**item)

@app.post("/items/", response_model=Item, dependencies=[Depends(verify_api_key)])
async def create_item(item: Item):
    query = "INSERT INTO items(id, name, description) VALUES (:id, :name, :description)"
    try:
        await database.execute(query=query, values=item.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    return item

@app.put("/items/{item_id}", response_model=Item, dependencies=[Depends(verify_api_key)])
async def update_item(item_id: int, item: Item):
    query = """
    UPDATE items SET name = :name, description = :description WHERE id = :item_id
    """
    values = item.dict()
    values["item_id"] = item_id
    try:
        await database.execute(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    return item

@app.delete("/items/{item_id}", dependencies=[Depends(verify_api_key)])
async def delete_item(item_id: int):
    query = "DELETE FROM items WHERE id = :item_id"
    await database.execute(query=query, values={"item_id": item_id})
    return {"deleted_id": item_id}