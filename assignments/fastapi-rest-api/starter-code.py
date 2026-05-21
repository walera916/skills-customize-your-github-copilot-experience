from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

items_db = {
    1: Item(id=1, name="Laptop", description="Lightweight laptop", price=999.99),
    2: Item(id=2, name="Headphones", description="Noise-cancelling headphones", price=199.99),
}

@app.get("/items", response_model=List[Item])
def list_items(limit: Optional[int] = None):
    """Return a list of available items. Use ?limit=2 to restrict results."""
    items = list(items_db.values())
    return items[:limit] if limit is not None else items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Return a single item by ID or raise a 404 error if not found."""
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=201)
def create_item(item_data: ItemCreate):
    """Create a new item and return the created object."""
    new_id = max(items_db.keys(), default=0) + 1
    new_item = Item(id=new_id, **item_data.dict())
    items_db[new_id] = new_item
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemUpdate):
    """Update an existing item or raise a 404 error if it does not exist."""
    existing_item = items_db.get(item_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_data = item_data.dict(exclude_unset=True)
    updated_item = existing_item.copy(update=updated_data)
    items_db[item_id] = updated_item
    return updated_item

# To run the API locally:
# uvicorn starter-code:app --reload
