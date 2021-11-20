import os
import pytest
from main import app
from infrastructure.db.database import Base, get_db, engine, DATABASE_URL
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

print("DATABASE_URL: {}".format(DATABASE_URL))
'''
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
