import http
from typing import Any

from fastapi import status
from starlette.exceptions import HTTPException as StarletteHTTPException


class HTTPException(StarletteHTTPException):
    def __init__(
        self, status_code: int, reason: str | None = None, **kwargs: Any
    ) -> None:
        self.status_code = status_code
        self.detail = kwargs.pop("detail", http.HTTPStatus(status_code).phrase)
        self.response = kwargs
        self.reason = reason

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"


class BadRequestException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_400_BAD_REQUEST, reason, **kwargs)


class UnauthorizedException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_401_UNAUTHORIZED, reason, **kwargs)


class PaymentRequiredException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_402_PAYMENT_REQUIRED, reason, **kwargs)


class ForbiddenException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_403_FORBIDDEN, reason, **kwargs)


class NotFoundException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_404_NOT_FOUND, reason, **kwargs)


class ConflictException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_409_CONFLICT, reason, **kwargs)


class ServerException(HTTPException):
    def __init__(self, reason: str | None = None, **kwargs: Any):
        super().__init__(status.HTTP_500_INTERNAL_SERVER_ERROR, reason, **kwargs)
