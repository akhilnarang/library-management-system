from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from app import exceptions, exception_handlers
from app.api.v1.routes import router as api_v1_router

app = FastAPI()
app.include_router(router=api_v1_router, prefix="/api/v1")


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception) -> Response:
    return await exception_handlers.handle_internal_server_error(request, exc)


@app.exception_handler(exceptions.HTTPException)
async def handle_http_exception(
    request: Request, exc: exceptions.HTTPException
) -> Response:
    return await exception_handlers.http_exception_handler(request, exc)
