import pytest
from app import create_app


@pytest.fixture
def app():
    # Create the app with the "testing" configuration
    app = create_app("testing")
    yield app  # This will return the app to the test function


@pytest.fixture
def client(app):
    # Create a test client using the app
    return app.test_client()


def test_app_running(client):
    # Test if the app is running by making a simple request to the root
    response = client.get("/")
    assert response.status_code == 200
