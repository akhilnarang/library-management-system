from pydantic import BaseModel, validator


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

    @validator("title")
    def title_must_not_be_empty(cls, title: str) -> str:
        if len(title.strip()) == 0:
            raise ValueError("Title must not be empty")
        return title

    @validator("authors")
    def authors_must_not_be_empty(cls, authors: str) -> str:
        if len(authors.strip()) == 0:
            raise ValueError("Authors must not be empty")
        return authors

    @validator("isbn")
    def isbn_must_not_be_empty(cls, isbn: str) -> str:
        if len(isbn.strip()) == 0:
            raise ValueError("ISBN must not be empty")
        return isbn


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
