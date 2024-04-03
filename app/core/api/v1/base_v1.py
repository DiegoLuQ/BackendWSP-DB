from fastapi import APIRouter
from .api_user import router

api_router = APIRouter()

api_router.include_router(
    router,
    prefix="/user_wsp",
    tags=["Cliente-WSP"]
)