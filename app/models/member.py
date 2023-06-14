from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Member(Base):
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String, index=True)
    email: str = Column(String, index=True, unique=True)
    outstanding_payment: int = Column(Integer, nullable=False, default=0)
