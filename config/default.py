from pydantic import BaseSettings


class Default(BaseSettings):
    ENV: str = ""
    SQLALCHEMY_DATABASE_URI: str = ""
