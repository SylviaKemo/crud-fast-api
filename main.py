from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# in memory "database"
items = {}

# pydantic model
class Item(BaseModel):
    name: str
    desc: str
    price: float

# create
@app.post("/item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return {"message": "Item created", "item": item}

# Read all
@app.get("/items")
def read_all_items():
    return items

# Read One
@app.get("/items/{items_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, details="Item not found")
    return items[item_id]

# Update
@app.put("/items/item_id")
def update_item(item_id: int, updated_item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated_item
    return {"message": "Item Updated", "item": updated_item}

# Delete
@app.delete("/items/item_id")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}