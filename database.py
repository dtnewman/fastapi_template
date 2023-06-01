from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, create_session

from config import settings


def get_connection_string():
    return settings.SQLALCHEMY_DATABASE_URI




engine = None
db_session = scoped_session(lambda: create_session(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine))

Base = declarative_base()

def init_engine(uri=None):
    global engine
    engine = create_engine(uri or get_connection_string(), future=True)
    return engine


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)

