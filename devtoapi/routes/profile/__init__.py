from requests import get
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from .scraper import scrap

user_router = APIRouter()


@user_router.get("/", response_class=PlainTextResponse)
async def index():
    return "profile/<name>"


@user_router.get("/{name}/")
async def scrape_profile(name: str):
    html = get('http://dev.to/' + name).content
    return scrap(html),
