from sqlalchemy import Column, Float, Integer, String

from app.db.base_class import Base


class Book(Base):
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title: str = Column(String, index=True)
    authors: str = Column(String, index=True)
    publisher: str = Column(String)
    average_rating: float = Column(Float)  # type: ignore
    isbn: str = Column(String, index=True, unique=True)
    stock: int = Column(Integer, nullable=False, default=1)
