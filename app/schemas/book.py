from pydantic import BaseModel


class BookBase(BaseModel):
    title: str | None
    authors: str | None
    average_rating: float | None
    isbn: str | None
    stock: int | None


class BookCreate(BookBase):
    title: str
    authors: str
    isbn: str


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
