from fastapi import FastAPI

from fastapi_examples.routes.v1.items import router as items_router_v1
from fastapi_examples.routes.v2.items import router as items_router_v2

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(items_router_v1, prefix="/v1")
app.include_router(items_router_v2, prefix="/v2")
