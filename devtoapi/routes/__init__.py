from fastapi import APIRouter

from .article import article_router
from .profile import user_router

router = APIRouter()

router.include_router(
    article_router,
    prefix="/article"
)

router.include_router(
    user_router,
    prefix="/profile"
)
