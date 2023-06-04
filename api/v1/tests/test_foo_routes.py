from fastapi.testclient import TestClient
from app import app
from utils.test_utils import BaseTestCase


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
