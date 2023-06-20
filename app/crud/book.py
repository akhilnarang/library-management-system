from sqlalchemy import column
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

from .base import CRUDBase


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_by_isbn(self, db: Session, *, isbn: str) -> Book | None:
        return db.query(self.model).where(column("isbn") == isbn).first()


book = CRUDBook(Book)
