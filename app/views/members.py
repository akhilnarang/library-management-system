from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from .. import crud
from ..api.annotations import DB
from ..core.config import settings
from .template import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def members_root(request: Request, db: DB) -> Response:
    members = crud.member.get_multi(db)
    return templates.TemplateResponse(
        "members.html", {"request": request, "app_name": settings.APP_NAME, "members": members}
    )


@router.get("/create", response_class=HTMLResponse)
def members_create(
    request: Request,
) -> Response:
    return templates.TemplateResponse("members_create.html", {"request": request, "app_name": settings.APP_NAME})


@router.get("/update/{member_id}", response_class=HTMLResponse)
def members_update(
    request: Request,
    member_id: int,
    db: DB,
) -> Response:
    return templates.TemplateResponse(
        "members_update.html",
        {"request": request, "app_name": settings.APP_NAME, "member": crud.member.get(db, id=member_id)},
    )
