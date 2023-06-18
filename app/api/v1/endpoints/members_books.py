from fastapi import APIRouter

from app import crud, schemas
from app.api.annotations import DB
from app.exceptions import NotFoundException

router = APIRouter()


@router.get("/")
def get_members_books(db: DB, skip: int = 0, limit: int = 100) -> list[schemas.MembersBooks]:
    """
    An endpoint that returns a given count of member-book records from the database.
    """
    return [
        schemas.MembersBooks.from_orm(members_books)
        for members_books in crud.members_books.get_multi(db, skip=skip, limit=limit)
    ]


@router.post("/")
def create_members_books(db: DB, members_books: schemas.MembersBooksCreate) -> schemas.MembersBooks:
    """
    An endpoint that creates a member-book record in the database.
    """
    return schemas.MembersBooks.from_orm(crud.members_books.create(db, obj_in=members_books))


@router.get("/members_by_book/{book_id}")
def get_members_books_by_id(db: DB, book_id: int) -> list[schemas.MembersBooks]:
    """
    An endpoint that returns a list of member-books records for a certain book from the database.
    """
    return [
        schemas.MembersBooks.from_orm(members_books)
        for members_books in crud.members_books.get_members_books_by_book_id(db, book_id=book_id)
    ]


@router.get("/books_by_member/{member_id}")
def get_books_by_member_id(db: DB, member_id: int) -> list[schemas.MembersBooks]:
    """
    An endpoint that returns a list of member-book records for a certain member from the database.
    """
    return [
        schemas.MembersBooks.from_orm(members_books)
        for members_books in crud.members_books.get_members_books_by_member_id(db, member_id=member_id)
    ]


@router.get("/{member_id}/{book_id}")
def get_members_books_by_member_id_and_book_id(db: DB, member_id: int, book_id: int) -> schemas.MembersBooks:
    """
    An endpoint that returns a member-book record from the database.
    """
    return schemas.MembersBooks.from_orm(
        crud.members_books.get_members_books_by_member_id_and_book_id(db, member_id=member_id, book_id=book_id)
    )


@router.put("/{member_id}/{book_id}")
def update_members_books(
    db: DB,
    member_id: int,
    book_id: int,
    members_books_update: schemas.MembersBooksUpdate,
) -> schemas.MembersBooks:
    """
    An endpoint that updates a member-book record in the database.
    """
    if members_books := crud.members_books.get_members_books_by_member_id_and_book_id(
        db, member_id=member_id, book_id=book_id
    ):
        return schemas.MembersBooks.from_orm(
            crud.members_books.update(db, db_obj=members_books, obj_in=members_books_update)
        )
    raise NotFoundException(detail="Requested object not found")


@router.delete("/{member_id}/{book_id}")
def delete_members_books(db: DB, member_id: int, book_id: int) -> schemas.MembersBooks:
    """
    An endpoint that deletes a member-book record-book record from the database.
    """
    return schemas.MembersBooks.from_orm(
        crud.members_books.remove_members_books_by_member_id_and_book_id(db, member_id=member_id, book_id=book_id)
    )
