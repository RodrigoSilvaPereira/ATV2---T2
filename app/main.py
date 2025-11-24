from fastapi import FastAPI, HTTPException, status

from app.models import Item, ItemCreate, ItemUpdate

app = FastAPI(title="TDD FastAPI Project", version="1.0.0")

# Mock database - simula um banco de dados em memória
items_db = {
    1: {"id": 1, "name": "Item 1", "description": "First item"},
    2: {"id": 2, "name": "Item 2", "description": "Second item"},
    3: {"id": 3, "name": "Item 3", "description": "Third item"},
}


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI TDD Project", "version": "1.0.0"}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """Get item by ID - deve retornar 404 se o item não existir"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não existe"
        )
    return items_db[item_id]


@app.get("/items/", response_model=list[Item])
async def read_all_items():
    """Get all items"""
    return list(items_db.values())


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item"""
    new_id = max(items_db.keys()) + 1 if items_db else 1
    new_item = {"id": new_id, **item.dict()}
    items_db[new_id] = new_item
    return new_item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não existe"
        )

    # Atualiza apenas os campos fornecidos
    update_data = item.dict(exclude_unset=True)
    items_db[item_id].update(update_data)

    return items_db[item_id]


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não existe"
        )

    del items_db[item_id]
    return None
