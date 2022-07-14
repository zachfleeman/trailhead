from fastapi import APIRouter

from api.endpoints import records, credentials

api_router = APIRouter()
api_router.include_router(records.router, prefix="/records", tags=["records"])
api_router.include_router(credentials.router, prefix="/credentials", tags=["credentials"])