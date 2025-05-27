from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.price_feed import subscribers

router = APIRouter()

@router.websocket("/ws/stocks")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    subscribers.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        subscribers.remove(websocket)
