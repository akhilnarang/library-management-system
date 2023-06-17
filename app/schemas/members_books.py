from datetime import datetime

from pydantic import BaseModel


class MembersBooksBase(BaseModel):
    member_id: int | None
    book_id: int | None
    borrowed_on: datetime | None


class MembersBooksCreate(MembersBooksBase):
    member_id: int
    book_id: int


class MembersBooksUpdate(MembersBooksBase):
    pass


class MembersBooks(MembersBooksBase):
    class Config:
        orm_mode = True


class MembersBooksReturnRequest(BaseModel):
    member_id: int
    book_id: int
    paid_fee: bool
