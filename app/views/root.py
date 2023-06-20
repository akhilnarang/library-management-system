from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from ..core.config import settings
from .template import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request) -> Response:
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
            "options": [
                {"name": "Books", "url": "/books"},
                {"name": "Members", "url": "/members"},
            ],
        },
    )
