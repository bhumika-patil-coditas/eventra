from fastapi import FastAPI
from src.apis import __all__


app: FastAPI = FastAPI(title="AWS service.")

@app.get("/ping")
def health():
    return "pong"


for router in __all__:
    app.include_router(router)