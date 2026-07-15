from fastapi import Depends, FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.api import __all__ as routers
from src.schema import TokenPayload
from src.service import Auth, PUBSUB


app = FastAPI(
    title="Main Gateway",
    summary="API Gateway for routing requests to internal microservices.",
)


@app.get("/ping", summary="Health check")
def health() -> str:
    """Simple health check endpoint."""
    return "pong"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


for router in routers:
    app.include_router(router)


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    user: TokenPayload = Depends(Auth.RBAC()),
) -> None:
    """
    Establish a websocket connection and subscribe the user
    to their role channel and personal channel.
    """
    await PUBSUB.subscribe(
        websocket=websocket,
        channels=[
            user.role.value,
            f"user:{user.sub}",
        ],
    )

    try:
        while True:
            # Keeps the websocket alive.
            await websocket.receive_text()
    finally:
        await PUBSUB.unsubscribe(websocket)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )