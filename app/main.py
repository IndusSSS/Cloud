import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import redis.asyncio as aioredis

from .api.battery import router as battery_router
from .websocket_manager import WebSocketManager

app = FastAPI()
app.include_router(battery_router)

manager = WebSocketManager()


@app.websocket("/ws/battery")
async def websocket_endpoint(websocket: WebSocket, device_id: str) -> None:
    await manager.connect(websocket)
    redis_url = aioredis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
    pubsub = redis_url.pubsub()
    await pubsub.subscribe(f"battery:{device_id}")
    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"])
    except WebSocketDisconnect:
        pass
    finally:
        await pubsub.unsubscribe(f"battery:{device_id}")
        await pubsub.close()
        await redis_url.close()
        manager.disconnect(websocket)
