# Packages
from fastapi import APIRouter

# Modules
from .endpoints.dataset import router as dataset
from .endpoints.metrics import router as metrics

router = APIRouter()

router.include_router(dataset)
router.include_router(metrics)
