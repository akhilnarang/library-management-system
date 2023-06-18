from fastapi import APIRouter

from .endpoints import books, members, members_books

router = APIRouter()

router.include_router(books.router, prefix="/books", tags=["books"])
router.include_router(members.router, prefix="/members", tags=["members"])
router.include_router(members_books.router, prefix="/members_books", tags=["members_books"])
