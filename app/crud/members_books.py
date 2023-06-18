import logging

from sqlalchemy import column
from sqlalchemy.orm import Session

from app.models.members_books import MembersBooks
from app.schemas.members_books import MembersBooksCreate, MembersBooksUpdate

from ..exceptions import NotFoundException
from .base import CRUDBase


class CRUDMembersBooks(CRUDBase[MembersBooks, MembersBooksCreate, MembersBooksUpdate]):
    def get(self, db: Session, id: int) -> MembersBooks | None:
        raise NotImplementedError

    def delete(self, db: Session, *, id: int) -> MembersBooks | None:
        raise NotImplementedError

    def get_members_books_by_member_id(self, db: Session, *, member_id: int) -> list[MembersBooks]:
        return db.query(MembersBooks).where(column("member_id") == member_id).all()

    def get_members_books_by_book_id(self, db: Session, *, book_id: int) -> list[MembersBooks]:
        return db.query(MembersBooks).where(column("book_id") == book_id).all()

    def get_members_books_by_member_id_and_book_id(
        self, db: Session, *, member_id: int, book_id: int
    ) -> MembersBooks | None:
        return (
            db.query(MembersBooks).where(column("member_id") == member_id).where(column("book_id") == book_id).first()
        )

    def remove_members_books_by_member_id_and_book_id(
        self, db: Session, *, member_id: int, book_id: int, commit: bool = True
    ) -> MembersBooks | None:
        if (
            obj := db.query(MembersBooks)
            .where(column("member_id") == member_id)
            .where(column("book_id") == book_id)
            .first()
        ):
            db.delete(obj)
            try:
                if commit:
                    db.commit()
                else:
                    db.flush()
            except Exception as e:
                logging.error("Failed to delete object", e.__str__())
                db.rollback()
                raise e
            db.refresh(obj)
            return obj
        logging.error(f"Failed to delete object {member_id=} {book_id=}")
        raise NotFoundException(detail="Object with the given details not found")


members_books = CRUDMembersBooks(MembersBooks)
