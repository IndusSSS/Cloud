from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..services.websocket_manager import manager

router = APIRouter()

@router.websocket("/ws/battery/{device_id}")
async def websocket_endpoint(websocket: WebSocket, device_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # This is a simple echo, in a real app you might process the data
            await manager.send_personal_message(f"You wrote: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
