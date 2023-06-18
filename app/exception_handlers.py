import logging

from fastapi import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exceptions import HTTPException


async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """
    Handles HTTPExceptions

    :param _: The starlette request object
    :param exc: The exception object
    :return: A JSONResponse object with the exception details
    """
    response_body = {
        "detail": exc.detail,
        **exc.response,
    }
    return JSONResponse(
        response_body,
        status_code=exc.status_code,
        headers=getattr(exc, "headers", None),
    )


async def handle_internal_server_error(request: Request, exc: Exception) -> JSONResponse:
    """
    Handles internal server errors

    :param request: The starlette request object
    :param exc: The exception object
    :return: A JSONResponse object with the exception details
    """
    logging.error("Internal Server Error", exc_info=exc)
    if not isinstance(exc, HTTPException) or exc.status_code != status.HTTP_500_INTERNAL_SERVER_ERROR:
        # If not an HTTPException, convert to one with the relevant information
        exc = HTTPException(
            detail="Internal Server Error",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return await http_exception_handler(request, exc)
