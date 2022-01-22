from fastapi import APIRouter

from .article import article_router

router = APIRouter()

router.include_router(
    article_router,
    prefix="/article"
)
