from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base
from app.models.book import Book
from app.models.member import Member
from app.utils import current_time


class Transaction(Base):
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    member_id: int = Column(Integer, ForeignKey("members.id"), nullable=False)
    book_id: int = Column(Integer, ForeignKey("books.id"))
    paid_on: datetime = Column(DateTime, default=current_time)
    amount: int = Column(Integer, nullable=False, default=0)

    book: Mapped[Book] = relationship("Book")
    member: Mapped[Member] = relationship("Member")
