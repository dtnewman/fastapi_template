import os

from .default import Default


class Development(Default):
    ENV: str = "Development"
    SQLALCHEMY_DATABASE_URI: os.environ.get("SQLALCHEMY_DATABASE_URI")
    # NOTE: For running locally, storing the database URI is ok, but I suggest that for deployements,
    # you store actual database credentials in AWS Secrets manager or a similar service.
