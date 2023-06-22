from fastapi import APIRouter

from .endpoints import books, librarian, members, members_books, transactions

router = APIRouter()

router.include_router(books.router, prefix="/books", tags=["books"])
router.include_router(members.router, prefix="/members", tags=["members"])
router.include_router(members_books.router, prefix="/members_books", tags=["members_books"])
router.include_router(librarian.router, prefix="/librarian", tags=["librarian"])
router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
