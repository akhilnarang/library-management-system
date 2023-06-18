from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

from .base import CRUDBase


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    pass


book = CRUDBook(Book)
