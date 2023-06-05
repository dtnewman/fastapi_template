"""
Tests for model Foo
"""

from datetime import datetime
from models.foo_models import Foo
from utils.test_utils import BaseTestCase
import pytest

from exceptions import MyFastAPIAppException


class TestFoo(BaseTestCase):
    def test_init(self):
        name = "test"
        timestamp = datetime.utcnow()
        foo = Foo(name=name, timestamp=timestamp)
        assert foo.name == name
        assert foo.timestamp == timestamp

    def test_get(self):
        foo = Foo.create(session=self.session, name="test")
        retrieved_item = Foo.get(session=self.session, id=foo.id)
        assert retrieved_item.id == foo.id
        assert retrieved_item.name == foo.name

    def test_get_all(self):
        foo1 = Foo.create(session=self.session, name="test1")
        foo2 = Foo.create(session=self.session, name="test2")
        retrieved_items = Foo.get_all(session=self.session)
        assert len(retrieved_items) == 2
        assert retrieved_items[0].id == foo1.id
        assert retrieved_items[0].name == foo1.name
        assert retrieved_items[1].id == foo2.id
        assert retrieved_items[1].name == foo2.name

        Foo.delete(session=self.session, id=foo1.id)
        retrieved_items = Foo.get_all(session=self.session)
        assert len(retrieved_items) == 1

    def test_repr(self):
        foo = Foo.create(session=self.session, name="test")
        assert repr(foo) == "<Foo id=1 name=test>"

    def test_delete_nonexistent(self):
        with pytest.raises(MyFastAPIAppException):
            Foo.delete(session=self.session, id=1)
