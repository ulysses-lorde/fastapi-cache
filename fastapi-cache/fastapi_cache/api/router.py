from fastapi import APIRouter

from .routes.movies import router as movies_router


router = APIRouter()

router.include_router(movies_router, tags=["Movies"], prefix="/movies")