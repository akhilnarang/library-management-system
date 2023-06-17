from pydantic import BaseModel, EmailStr


class MemberBase(BaseModel):
    name: str | None
    email: EmailStr | None
    outstanding_payment: int | None


class MemberCreate(MemberBase):
    name: str
    email: EmailStr


class MemberUpdate(MemberBase):
    pass


class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True
