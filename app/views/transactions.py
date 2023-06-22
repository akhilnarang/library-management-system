from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from .. import crud
from ..api.annotations import DB
from ..core.config import settings
from .template import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def transactions_root(
    request: Request,
    db: DB,
) -> Response:
    return templates.TemplateResponse(
        "transactions.html",
        {"request": request, "app_name": settings.APP_NAME, "transactions": crud.transaction.get_multi(db)},
    )
