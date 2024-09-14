from fastapi import FastAPI
import uvicorn

from src.converter.router import router as converter_router
from src.config import settings

app = FastAPI()
app.include_router(converter_router, prefix="/api")
