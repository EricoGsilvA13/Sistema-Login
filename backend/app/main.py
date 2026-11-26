from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(title="Sistema de Login")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

#python -m uvicorn app.main:app --reload