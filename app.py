# https://www.serverless.com/plugins/serverless-python-requirements#dealing-with-lambdas-size-limitations
# sourcery skip: use-contextlib-suppress
try:
    import unzip_requirements  # type: ignore # noqa: F401
except ImportError:
    pass

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from mangum import Mangum


from api.v1 import (
    foo_routes,
)
from database import init_engine
from exceptions import MyFastAPIAppException
from config import settings


def create_app():
    init_engine(settings.SQLALCHEMY_DATABASE_URI)
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,  # For handling CORS (https://fastapi.tiangolo.com/tutorial/cors/)
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=86400,  # Bump for browsers that support > 600 seconds like firefox
    )

    # Handles GZip responses for any request that includes "gzip" in the `Accept-Encoding`` header.
    # (https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.include_router(foo_routes.router)

    @app.get("/", include_in_schema=False)
    def docs():
        return RedirectResponse("/docs")

    @app.get("/status")
    def root():
        return {"status": "ok"}

    @app.exception_handler(MyFastAPIAppException)
    def app_exception_handler(req, exc: MyFastAPIAppException):
        return JSONResponse(status_code=exc.status_code, content=dict(message=exc.message))

    @app.exception_handler(Exception)
    def basic_exception_handler(req, exc: Exception):
        return JSONResponse(status_code=500, content=dict(message="Backend error occurred"))

    return app


app = create_app()
handler = Mangum(app)
