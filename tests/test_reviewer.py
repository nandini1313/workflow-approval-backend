from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_reviewer_requests():

    response = client.get(
        "/reviewer/requests"
    )

    assert response.status_code in [
        200,
        401,
        403
    ]