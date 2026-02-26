"""
Items router - CRUD operations for items
"""
from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from models.item import Item

# Create router
router = APIRouter(
    prefix="/api/items",
    tags=["Items"],
)

# In-memory storage (for demo purposes)
items_db: List[Item] = []
item_counter = 1


@router.get("", response_model=List[Item])
async def get_items():
    """
    Get all items
    """
    return items_db


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """
    Get a specific item by ID
    """
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("", response_model=Item)
async def create_item(item: Item):
    """
    Create a new item
    """
    global item_counter
    item.id = item_counter
    item.created_at = datetime.now()
    items_db.append(item)
    item_counter += 1
    return item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """
    Update an existing item
    """
    for idx, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            item.id = item_id
            item.created_at = existing_item.created_at
            items_db[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    """
    Delete an item
    """
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
