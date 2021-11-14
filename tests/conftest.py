'''import os
import pytest
from main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope = "module")
def test_app():
    
    client = TestClient(app)
    yield client'''
