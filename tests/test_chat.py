from app.main import app
from fastapi.testclient import TestClient


def test_chat_endpoint_with_valid_message():
    with TestClient(app) as client:

        response = client.post(
            "/api/v1/chat",
            json={"message": "Hello, how can I reset my password?"},
        )

        assert response.status_code == 200

        data = response.json()
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert len(data["answer"]) > 0