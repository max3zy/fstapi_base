from app.config import settings
from app.main import app_factory
from fastapi.testclient import TestClient

client = TestClient(app_factory())


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": f"test-llm-service "
        f"v {settings.SERVICE_VERSION} Команды навыков",
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "OK"


def test_get_configs():
    response = client.get("/get_configs")
    assert response.status_code == 200
    assert all(
        k in response.json() and v == response.json()[k]
        for k, v in settings.as_dict().items()
    )


def test_v1_hello():
    response = client.get("/v1/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}
