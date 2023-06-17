from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from app import exceptions, exception_handlers

app = FastAPI()


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception) -> Response:
    return await exception_handlers.handle_internal_server_error(request, exc)


@app.exception_handler(exceptions.HTTPException)
async def handle_http_exception(
    request: Request, exc: exceptions.HTTPException
) -> Response:
    return await exception_handlers.http_exception_handler(request, exc)


@app.get("/")
async def root():
    return {"message": "Hello World"}
