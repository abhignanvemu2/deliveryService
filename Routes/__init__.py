from fastapi import APIRouter
from .Delivery import router as Delivery

router = APIRouter()

router.include_router(Delivery, prefix="/delivery", tags=['delivery'])