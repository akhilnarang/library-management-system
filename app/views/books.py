from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from .. import crud
from ..api.annotations import DB
from ..core.config import settings
from .template import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def books_root(request: Request, db: DB) -> Response:
    books = crud.book.get_multi(db)
    return templates.TemplateResponse("books.html", {"request": request, "app_name": settings.APP_NAME, "books": books})


@router.get("/create", response_class=HTMLResponse)
def books_create(
    request: Request,
) -> Response:
    return templates.TemplateResponse("books_create.html", {"request": request, "app_name": settings.APP_NAME})


@router.get("/update/{book_id}", response_class=HTMLResponse)
def books_update(
    request: Request,
    book_id: int,
    db: DB,
) -> Response:
    return templates.TemplateResponse(
        "books_update.html", {"request": request, "app_name": settings.APP_NAME, "book": crud.book.get(db, id=book_id)}
    )