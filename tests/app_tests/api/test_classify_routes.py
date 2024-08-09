from app.config import settings
from app.main import app_factory
from fastapi.testclient import TestClient

client = TestClient(app_factory())


def test_v1_classify_target(requests_classify_critical):
    df = requests_classify_critical
    for _, row in df.iterrows():
        response = client.get(
            "/v1/classify",
            params={"query": row.text, "is_use_score": False},
        )
        assert response.status_code == 200
        assert "classify_score" in response.json()
        assert isinstance(response.json()["classify_score"], float)


def test_v1_classify_score(requests_classify_all):
    df = requests_classify_all
    for _, row in df.iterrows():
        response = client.get(
            "/v1/classify",
            params={"query": row.text, "is_use_score": True},
        )
        assert response.status_code == 200
        assert "classify_score" in response.json()
        score = response.json()["classify_score"]
        assert isinstance(score, float)
