from datetime import datetime

from pydantic import BaseModel, validator


class TransactionBase(BaseModel):
    book_id: int | None
    member_id: int | None
    paid_on: datetime | None
    amount: int | None


class TransactionCreate(TransactionBase):
    member_id: int
    amount: int

    @validator("amount")
    def amount_must_be_positive(cls, amount: int) -> int:
        if amount < 0:
            raise ValueError("Amount must be positive")
        return amount


class TransactionUpdate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
