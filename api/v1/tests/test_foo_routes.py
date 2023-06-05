from fastapi.testclient import TestClient
from app import app
from utils.test_utils import BaseTestCase
import pytest
from exceptions import MyFastAPIAppException


class TestFooApi(BaseTestCase):
    def test_foo(self):
        client = TestClient(app)
        response = client.get("/api/v1/foo")
        assert response.status_code == 200
        assert response.json() == []

        response = client.post("/api/v1/foo/", json={"name": "test"})
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == {"id": 1, "name": "test"}

        response = client.delete("/api/v1/foo/1")
        assert response.status_code == 200

        response = client.get("/api/v1/foo")
        assert response.status_code == 200
        assert response.json() == []

    def test_exception_example(self):
        response = TestClient(app).get("/api/v1/foo/exception_example")
        assert response.status_code == 400
        assert response.json() == {"message": "This is an example exception"}
