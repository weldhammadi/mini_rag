from fastapi.testclient import TestClient

from api import app


def test_ask_returns_answer_from_corpus():
    with TestClient(app) as client:
        response = client.post("/ask", json={"question": "Quelle est la couleur du chat de Bob ?"})

    assert response.status_code == 200
    assert "bleu" in response.json()["answer"].lower()
