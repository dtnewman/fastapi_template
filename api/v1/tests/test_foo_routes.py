from fastapi.testclient import TestClient
from app import app
from utils.test_utils import BaseTestCase


class TestFooApi(BaseTestCase):
    def test_foo(self):
        client = TestClient(app)
        response = client.get("/api/v1/foo")
        print(response)
        print(response.text)
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

        response = client.get("/api/v1/foo/")
        print(response)
        print(response.text)
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
