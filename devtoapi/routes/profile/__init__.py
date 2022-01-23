from requests import get
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from .scraper import scrap

user_router = APIRouter()


@user_router.get("/", response_class=PlainTextResponse)
async def index():
    return "user/<username>"


@user_router.get("/{username}/")
async def scrape_user(username: str):
    html = get('http://dev.to/' + username).content
    return scrap(html),
