import os
import pytest
from main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope="class", autouse = False)
def test_app():
    
    client = TestClient(app)
    yield client
