from typing import Optional
from fastapi import APIRouter
from exceptions import MyFastAPIAppException
from pydantic import BaseModel

from models.foo_models import Foo
from database import db_session


class FooInput(BaseModel):
    name: str


class FooResponse(BaseModel):
    id: Optional[int]
    name: str


router = APIRouter(dependencies=[], prefix="/api/v1/foo", tags=["Foo API v1"])


@router.get("/")
async def read_root():
    return Foo.get_all(db_session)


@router.post("/", response_model=FooResponse)
async def create_foo(post_data: FooInput):
    x = Foo.create(db_session, name=post_data.name)
    db_session.commit()
    return FooResponse(id=x.id, name=x.name)


@router.delete("/{id}", response_model=dict)
async def delete_foo(id: int):
    Foo.delete(db_session, id=id)
    db_session.commit()
    return {"status": "success"}


@router.get("/exception_example")
async def exception_example():
    raise MyFastAPIAppException(message="This is an example exception", status_code=400)
