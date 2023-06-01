from sqlalchemy import BigInteger, Column, DateTime, String
from utils.utils import get_utc_now
from database import Base
from datetime import datetime

from exceptions import MyFastAPIAppException


class Foo(Base):
    __tablename__ = "foo"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    timestamp = Column(DateTime, nullable=False, default=get_utc_now)

    def __init__(self, name: str, timestamp: datetime = None):
        self.name = name
        self.timestamp = timestamp or get_utc_now()

    def __repr__(self):
        return f"<Foo id={self.id} name={self.name}>"

    @classmethod
    def get(cls, session, id: int):
        return session.query(cls).filter(cls.id == id).one_or_none()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def create(cls, session, name: str):
        item = cls(name=name)
        session.add(item)
        session.flush()
        return item

    @classmethod
    def delete(cls, session, id: int):
        existing = cls.get(session, id=id)
        if not existing:
            raise MyFastAPIAppException(f"Foo with id {id} not found")
        session.query(cls).filter(cls.id == id).delete()
        session.flush()
        return True
