from fastapi import FastAPI
import uvicorn
import os

from src.converter.router import router as converter_router

app = FastAPI()
app.include_router(converter_router, prefix="/api")

if __name__ == '__main__':
    port = int(os.getenv("SITE_PORT", 8000))
    host = os.getenv("SITE_HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
