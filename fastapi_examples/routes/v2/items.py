from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"version": "2.0", "item_id": item_id, "q": q}
