from fastapi import APIRouter
from interfaces.controllers.forgot_controller import router as forgot_router
from interfaces.controllers.reset_controller  import router as reset_router

router = APIRouter(prefix="/api/password")
router.include_router(forgot_router)
router.include_router(reset_router)
