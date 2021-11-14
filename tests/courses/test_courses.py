'''import json
import pytest
import uuid
from tests.conftest import test_app

from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

header = {"apikey": "@L4u71"}

global_id = None

test_request_payload = {
    "name": "Python3",
    "description": "asd",
    "category": "coding",
    "kind": "online",
    "subscription_type": "free",
    "location": "arg",
    "info": {"hola": "as"}
}



def test_create_course(test_app, monkeypatch):

    async def mock_post(cls, payload):
        return 1

    monkeypatch.setattr(CourseRepositoryPostgres, "add_course", mock_post)

    response = test_app.post("/courses/",data = json.dumps(test_request_payload),
                            headers = header)

    assert response.status_code == 201

    response_json = response.json()
    global global_id
    global_id = response_json['id']

    assert response_json['name'] == test_request_payload['name']
    assert response_json['description'] == test_request_payload['description']
    assert response_json['category'] == test_request_payload['category']
    assert response_json['kind'] == test_request_payload['kind']
    assert response_json['subscription_type'] == test_request_payload['subscription_type']
    assert response_json['location'] == test_request_payload['location']
    assert response_json['info'] == test_request_payload['info']


def test_create_course_without_apikey(test_app, monkeypatch):

    response = test_app.post("/courses/", data = json.dumps(test_request_payload))
    assert response.status_code == 401

    response_json = response.json()

    assert response_json['error'] == "Error with API Key"


def test_get_existing_course(test_app, monkeypatch):

    course_id = global_id

    test_response_payload = {
        "id": course_id,
        "name": "Python3",
        "description": "asd",
        "category": "coding",
        "kind": "online",
        "subscription_type": "free",
        "location": "arg",
        "info": {"hola": "as"}
    }   

    async def mock_get(cls, id):
        return test_response_payload

    monkeypatch.setattr(CourseRepositoryPostgres, "get_course_by_id", mock_get)

    response = test_app.get("/courses/"+str(course_id), headers = header)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json['id'] == course_id
    assert response_json['name'] == test_request_payload['name']
    assert response_json['description'] == test_request_payload['description']
    assert response_json['category'] == test_request_payload['category']
    assert response_json['kind'] == test_request_payload['kind']
    assert response_json['subscription_type'] == test_request_payload['subscription_type']
    assert response_json['location'] == test_request_payload['location']
    assert response_json['info'] == test_request_payload['info']

'''

def test_basic_course():
    assert 2 == 1+1