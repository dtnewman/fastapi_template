from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings


def get_connection_string():
    return settings.SQLALCHEMY_DATABASE_URI


Base = declarative_base()


def init_engine(uri=None):
    global engine
    engine = create_engine(uri or get_connection_string(), future=True)
    return engine


def get_session(engine):
    return sessionmaker(engine, expire_on_commit=False)()


engine = None

Session = sessionmaker(engine, expire_on_commit=False)
