from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base
from app.models.book import Book
from app.models.member import Member
from app.utils import current_time


class MembersBooks(Base):
    member_id: int = Column(Integer, ForeignKey("members.id"), primary_key=True)
    book_id: int = Column(Integer, ForeignKey("books.id"), primary_key=True)
    borrowed_on: datetime = Column(DateTime, default=current_time)

    book: Mapped[Book] = relationship("Book")
    member: Mapped[Member] = relationship("Member")
