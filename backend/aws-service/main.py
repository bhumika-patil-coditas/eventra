from fastapi import FastAPI
from src.apis import __all__
import uvicorn

app: FastAPI = FastAPI(title="AWS service.")

@app.get("/ping")
def health():
    return "pong"


for router in __all__:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app" , port=8001)