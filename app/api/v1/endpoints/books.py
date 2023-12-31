from typing import Annotated

from fastapi import APIRouter, Query

from app import crud, schemas
from app.api.annotations import DB
from app.exceptions import ConflictException, NotFoundException

router = APIRouter()


@router.get("/")
def get_books(db: DB, skip: int = 0, limit: int = 100) -> list[schemas.Book]:
    """
    An endpoint that returns a given count of books from the database.
    """
    return [schemas.Book.from_orm(book) for book in crud.book.get_multi(db, skip=skip, limit=limit)]


@router.post("/")
def create_book(db: DB, book_create: schemas.BookCreate) -> schemas.Book:
    """
    An endpoint that creates a book in the database.
    """
    if crud.book.get_by_isbn(db, isbn=book_create.isbn):
        raise ConflictException(
            detail="This book already exists!",
        )
    return schemas.Book.from_orm(crud.book.create(db, obj_in=book_create))


@router.put("/{book_id}")
def update_book(db: DB, book_id: int, book_update: schemas.BookUpdate) -> schemas.Book:
    """
    An endpoint that updates a book in the database.
    """
    if book := crud.book.get(db, id=book_id):
        return schemas.Book.from_orm(crud.book.update(db, db_obj=book, obj_in=book_update))
    raise NotFoundException(detail="The requested book does not exist!")


@router.delete("/{book_id}")
def delete_book(db: DB, book_id: int) -> schemas.Book:
    """
    An endpoint that deletes a book from the database.
    """
    if crud.members_books.get_members_books_by_book_id(db, book_id=book_id):
        raise ConflictException(
            detail="This book is currently issued to a member!",
        )
    return schemas.Book.from_orm(crud.book.remove(db, id=book_id))


@router.get("/search")
def search_books(
    db: DB,
    title: Annotated[str | None, Query(description="Title of the book you want to search for")] = None,
    author: Annotated[str | None, Query(description="Author of the book you want to search for")] = None,
) -> list[schemas.Book]:
    """
    An endpoint that returns a given count of books from the database.
    """
    return [schemas.Book.from_orm(book) for book in crud.book.search(db, title=title, authors=author)]
