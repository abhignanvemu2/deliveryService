from fastapi import APIRouter
from .create import router as CreateDeliveryAgent
from .is_avalilable import router as IsAvailable
from .DeliveryStatus import router as DeliveryStatusUpdate

router = APIRouter()

router.include_router(CreateDeliveryAgent)
router.include_router(IsAvailable)
router.include_router(DeliveryStatusUpdate)
