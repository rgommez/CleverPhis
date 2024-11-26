import pytest
from src.app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_analyze(client):
    response = client.post("/analyze", json={"email_content": "Test phishing email"})
    assert response.status_code == 200
