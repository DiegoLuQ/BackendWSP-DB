from fastapi import APIRouter
from .v1.base_v1 import api_router

base_router = APIRouter()

base_router.include_router(
    api_router,
    prefix="/v1"
)