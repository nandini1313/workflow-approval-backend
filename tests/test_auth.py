from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_auth_me_without_token():

    response = client.get(
        "/auth/me"
    )

    assert response.status_code in [
        401,
        403
    ]