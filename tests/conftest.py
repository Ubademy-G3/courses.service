import os
import pytest
from main import app
from infrastructure.db.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

@pytest.fixture(scope = "class", autouse = False)
def test_app():

    DATABASE_TEST_URL = "postgresql://hello_fastapi:hello_fastapi@db/test"
    engine = create_engine(DATABASE_TEST_URL)

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

    yield client
