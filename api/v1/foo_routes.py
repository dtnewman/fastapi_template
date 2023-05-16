from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from exceptions import MyFastAPIAppException

router = APIRouter(dependencies=[], prefix="/api/v1/foo", tags=["Foo API v1"])


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/exception_example")
def exception_example():
    raise MyFastAPIAppException(message="This is an example exception", status_code=400)
