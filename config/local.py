import os

from .default import Default


class Local(Default):
    ENV = "Local"
    SQLALCHEMY_DATABASE_URI: str = (
        os.environ.get("SQLALCHEMY_DATABASE_URI") or "postgresql://localhost:5432/my-fastapi-app"
    )
