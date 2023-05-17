from pydantic import BaseSettings


class Default(BaseSettings):
    ENV: str = ""
    SQLALCHEMY_DATABASE_URI: str = ""
    CUSTOM_DOMAIN: str = ""
    ROOT_PATH: str = None
