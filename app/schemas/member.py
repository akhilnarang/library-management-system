from pydantic import BaseModel, EmailStr, validator


class MemberBase(BaseModel):
    name: str | None
    email: EmailStr | None
    outstanding_payment: int | None


class MemberCreate(MemberBase):
    name: str
    email: EmailStr

    @validator("name")
    def name_must_not_be_empty(cls, name: str) -> str:
        if len(name.strip()) == 0:
            raise ValueError("Name must not be empty")
        return name


class MemberUpdate(MemberBase):
    pass


class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True
