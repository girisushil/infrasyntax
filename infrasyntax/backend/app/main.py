import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import search
from .core.config import settings
from .core.model import model_loader

Import and setup centralized logger
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '../..')))
from shared.logger import setup_logger
logger = setup_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
# Load the ML model on startup
logger.info("Application starting up...")
model_loader.load_model()
yield
# Clean up resources on shutdown (if any)
logger.info("Application shutting down...")

app = FastAPI(
title=settings.PROJECT_NAME,
version="1.0.0",
lifespan=lifespan
)

app.add_middleware(
CORSMiddleware,
allow_origins=["https://www.google.com/search?q=http://localhost:3000"],
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

app.include_router(search.router, prefix="/api")

@app.get("/")
def read_root():
return {"status": "ok", "message": f"Welcome to the {settings.PROJECT_NAME} API!"}
