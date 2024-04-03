from fastapi import FastAPI
from core.api.base import base_router


def include_router(app):
    app.include_router(base_router)

def start_app():
    app = FastAPI()
    include_router(app)
    return app


app = start_app()


@app.get("/")
async def home():
    return {"Hola":"World"}