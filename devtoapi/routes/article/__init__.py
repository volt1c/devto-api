from requests import get
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from .scraper import scrap

article_router = APIRouter()


@article_router.get("/", response_class=PlainTextResponse)
async def index():
    return "article/<author>/<title>"


@article_router.get("/{author}/{title}")
async def scrape_article(author: str, title: str):
    html = get('http://dev.to/' + author + '/' + title).content
    return scrap(html),
