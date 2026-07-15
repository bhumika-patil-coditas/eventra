from collections import defaultdict
from fastapi import WebSocket

class WebSocketManager:
    def __init__(self):
        self.channels: dict[str, set[WebSocket]] = defaultdict(set)

    async def subscribe(self, websocket: WebSocket, channels: list[str]):
        await websocket.accept()

        for channel in channels:
            self.channels[channel].add(websocket)

    async def unsubscribe(self, websocket: WebSocket):
        for sockets in self.channels.values():
            sockets.discard(websocket)

    async def publish(self, channel: str, message: dict):
        dead = []

        for websocket in self.channels.get(channel, set()):
            try:
                await websocket.send_json(message)
            except Exception:
                dead.append(websocket)

        for websocket in dead:
            await self.unsubscribe(websocket)

PUBSUB = WebSocketManager()