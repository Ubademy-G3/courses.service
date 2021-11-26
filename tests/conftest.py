'''import os
import pytest
from main import app
from infrastructure.db.database import Base, get_db, engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

@pytest.fixture(scope = "class", autouse = False)
def test_app():
    
    client = TestClient(app)
    TestingSessionLocal = sessionmaker(autocommit = False,
                                       autoflush = False,
                                       bind = engine)
    Base.metadata.create_all(bind = engine)

    def get_testing_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = get_testing_db

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield client'''

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.database import Base, get_db
from main import app
import pytest


DATABASE_TEST_URL = "postgresql://hello_fastapi:hello_fastapi@db/test"
engine = create_engine(DATABASE_TEST_URL)

@pytest.fixture(scope = "session", autouse = False)
def test_app():

    client = TestClient(app)
    TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield client
