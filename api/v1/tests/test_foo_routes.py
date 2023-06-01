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
        assert response.json() == []

        response = client.post("/api/v1/foo/", json={"name": "test"})
        print(response)
        print(response.text)
        assert response.status_code == 200
        print(response.json())
        response_json = response.json()
        response_json[0].pop('timestamp')
        assert response.json() == [{'id': 1, 'name': 'test'}]
