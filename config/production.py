import os

from .default import Default


class Production(Default):
    ENV: str = "Production"
    # Note: For running locally, storing the database URI is ok, but I suggest that for deployements,
    # you store actual database credentials in AWS Secrets manager or a similar service.
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI", "")

    # Note: Serverless adds /prod to the root path when you deploy to prod, so you need to set that here
    # unless using a custom domain.
    ROOT_PATH: str = "/prod"
