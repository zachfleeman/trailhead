from fastapi import APIRouter

from api.endpoints import logs, credentials

api_router = APIRouter()
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
api_router.include_router(credentials.router, prefix="/credentials", tags=["credentials"])