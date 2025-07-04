from fastapi import FastAPI
from .routers import battery, ws

def create_app():
    app = FastAPI()
    app.include_router(battery.router)
    app.include_router(ws.router)
    return app
