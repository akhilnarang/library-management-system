from sqlalchemy import column
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

from .base import CRUDBase


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_by_isbn(self, db: Session, *, isbn: str) -> Book | None:
        return db.query(self.model).where(column("isbn") == isbn).first()

    def search(self, db: Session, *, title: str | None, authors: str | None) -> list[Book]:
        filters = []
        print(f"{title=} {authors=}")
        if title:
            filters.append(column("title").ilike(f"%{title}%"))
        if authors:
            filters.append(column("authors").ilike(f"%{authors}%"))
        return db.query(self.model).filter(*filters).all()


book = CRUDBook(Book)
