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
                {"name": "Books", "url": request.url_for("books_root")},
                {"name": "Members", "url": request.url_for("members_root")},
                {"name": "Borrowed Books", "url": request.url_for("borrowed_books_root")},
                {"name": "Import Books", "url": request.url_for("books_import")},
            ],
        },
    )
