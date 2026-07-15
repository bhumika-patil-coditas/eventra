from fastapi import FastAPI, WebSocket, Depends
import uvicorn
from src.api import __all__
from fastapi.middleware.cors import CORSMiddleware
from src.service import PUBSUB, Auth
from src.schema import TokenPayload

app = FastAPI(title="Main gateway")

@app.get("/ping")
def health():
    return "pong"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in __all__:
    app.include_router(router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, user:TokenPayload = Depends(Auth.RBAC(allowed_roles=[]))):
    await PUBSUB.subscribe(
        websocket,
        [
            user.role.value,
            f"user:{user.sub}"
        ],
    )

    try:
        while True:
            await websocket.receive_text()
    finally:
        await PUBSUB.unsubscribe(websocket)

if __name__ == "__main__":
    uvicorn.run("main:app" , port=8000, reload=False)