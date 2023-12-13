from fastapi import APIRouter

from app.api.routes.ships import router as ship_router
from app.api.routes.ports import router as ports_router
from app.api.routes.containers import router as containers_router
from app.api.routes.items import router as items_router

router = APIRouter()
router.include_router(ports_router, prefix="/ports", tags=["ports"])
router.include_router(ship_router, prefix="/ships", tags=["ships"])
router.include_router(containers_router, prefix="/containers", tags=["containers"])
router.include_router(items_router, prefix="/items", tags=["items"])
