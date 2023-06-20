from pydantic import BaseModel


class APIRequestParameters(BaseModel):
    title: str | None = None
    authors: str | None = None
    isbn: str | None = None
    publisher: str | None = None
    page: int | None = None


class Book(BaseModel):
    bookID: int
    title: str
    authors: str
    isbn: str
    publisher: str
    average_rating: float


class APIResponse(BaseModel):
    message: list[Book]
