from fastapi import APIRouter

from .books import router as books_router
from .members import router as members_router
from .root import router as root_router

router = APIRouter()

router.include_router(root_router, tags=["root"])
router.include_router(books_router, prefix="/books", tags=["books"])
router.include_router(members_router, prefix="/members", tags=["members"])