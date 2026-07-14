from fastapi import FastAPI
import uvicorn
from src.api import __all__
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Main gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
for router in __all__:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app" , port=8000, reload=True)