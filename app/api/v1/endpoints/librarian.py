from fastapi import APIRouter

from app import constants, crud, schemas
from app.api.annotations import DB
from app.exceptions import NotFoundException, PaymentRequiredException

router = APIRouter()


@router.post("/borrow_book")
def borrow_book(db: DB, members_books: schemas.MembersBooksCreate) -> schemas.MembersBooks:
    """
    An endpoint that creates a member-book record in the database.
    """
    if member := crud.member.get(db, id=members_books.member_id):
        if member.outstanding_payment >= constants.MAX_OUTSTANDING_ALLOWED:
            raise PaymentRequiredException(
                detail=f"You have outstanding payment of more than {constants.MAX_OUTSTANDING_ALLOWED}!"
            )
        if book := crud.book.get(db, id=members_books.book_id):
            if book.stock < 1:
                raise NotFoundException(detail="The requested book is not available!")

            crud.book.update(
                db,
                db_obj=book,
                obj_in=schemas.BookUpdate(stock=book.stock - 1),
                commit=False,
            )
            crud.member.update(
                db,
                db_obj=member,
                obj_in=schemas.MemberUpdate(
                    outstanding_payment=member.outstanding_payment + constants.BOOK_RENT_AMOUNT
                ),
                commit=False,
            )

            return schemas.MembersBooks.from_orm(crud.members_books.create(db, obj_in=members_books))
        raise NotFoundException(detail="The requested book does not exist!")
    return schemas.MembersBooks.from_orm(crud.members_books.create(db, obj_in=members_books))


@router.post("/return_book")
def return_book(db: DB, members_books: schemas.MembersBooksReturnRequest) -> schemas.MembersBooks:
    """
    An endpoint that deletes a member-book record from the database.
    """
    if member := crud.member.get(db, id=members_books.member_id):
        if book := crud.book.get(db, id=members_books.book_id):
            crud.book.update(
                db,
                db_obj=book,
                obj_in=schemas.BookUpdate(stock=book.stock + 1),
                commit=False,
            )

            if members_books.paid_fee:
                crud.member.update(
                    db,
                    db_obj=member,
                    obj_in=schemas.MemberUpdate(
                        outstanding_payment=member.outstanding_payment - constants.BOOK_RENT_AMOUNT
                    ),
                    commit=False,
                )

            return schemas.MembersBooks.from_orm(
                crud.members_books.remove_members_books_by_member_id_and_book_id(
                    db, member_id=members_books.member_id, book_id=members_books.book_id
                )
            )
        raise NotFoundException(detail="The requested book does not exist!")
    raise NotFoundException(detail="The requested member does not exist!")
