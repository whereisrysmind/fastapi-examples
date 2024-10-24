# Fast API Examples

This project is meant to show different uses and patterns for Fast API.

## Quickstart

**Prerequisites**

* Python 3.10
* Poetry

**Run the App**

```bash
# from the project root
poetry install
poetry run fastapi dev main.py
```

Navigate to a browser and open `http://127.0.0.1:8000/docs`

## Example Patterns

### Versioning API Routes

Versioning API routes allows for development of new functionality in existing routes without breaking existing contracts for clients and customers of those routes. In order to version our API routes, the routers are defined in their own scripts and organized into a file structure hierarchy that separates the different versions.

``` text
# Example Folder Structure
fastapi_examples/
  routes/
    v1/
      items.py  # Version 1 router code goes here
    v2/
      items.py  # Version 2 router code goes here
```

Each router is then to be imported into `main.py` and added as a router to the application with a route `prefix` thusly:

``` python
from fastapi import FastAPI
from fastapi_examples.routes.v1.items import router as items_router_v1
from fastapi_examples.routes.v2.items import router as items_router_v2

app = FastAPI()

app.include_router(items_router_v1, prefix="/v1")
app.include_router(items_router_v2, prefix="/v2")
```
