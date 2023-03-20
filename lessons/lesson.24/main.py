import json
import os

from fastapi import FastAPI, Response
from views.items import router as items_router
from views.users.views import router as users_router
from views.users_old.views_old import router as users_router_old

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)
app.include_router(users_router_old, prefix="/old")


@app.get("/")
def read_root():
    # return json.dumps({"hello": "root"})
    return Response(
        content=json.dumps({"hello": "root"}),
        media_type="application/json",
    )


@app.get("/hello")
def hello(name: str = "OTUS"):
    return {
        "message": f"Hello {name}!",
        "foobar": os.getenv("foobar"),
    }


@app.get("/hello2")
def hello2(name: str | None = None):
    if name is None:
        name = "World"
    return {
        "message": f"Hello {name}!",
    }