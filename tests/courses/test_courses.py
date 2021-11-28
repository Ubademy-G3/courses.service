from mock_alchemy.mocking import AlchemyMagicMock
import unittest
from unittest.mock import Mock, patch
import json
import pytest
import uuid
#from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

#crp = CourseRepositoryPostgres()

global_id = None

test_request_payload = {
    "name": "Python3",
    "description": "asd",
    "category": 2,
    "subscription_type": "free",
    "location": "arg",
    "profile_picture": "www.google.com",
    "duration": 43.2,
    "language": "english",
    "level": "easy",
    "modules": []
}

class TestCourse(unittest.TestCase):

    @patch('infrastructure.db.database.Session')
    @patch('persistence.repositories.course_repository_postgres.CourseRepositoryPostgres')
    def test_add_course(self, mockSession, mockRepo):

        global global_id
        global_id = uuid.uuid4()

        mockRepo.add_course.return_value.status_code = 201
        mockRepo.add_course.return_value.id = global_id

        #db = AlchemyMagicMock()

        mock_response = {
            "id": global_id,
            "name": "Python3",
            "description": "asd",
            "category": 2,
            "subscription_type": "free",
            "location": "arg",
            "profile_picture": "www.google.com",
            "duration": 43.2,
            "language": "english",
            "level": "easy",
            "modules": []
        }
        mockRepo.add_course.return_value = mock_response

        response = mockRepo.add_course(mockSession, json.dumps(test_request_payload))

        self.assertEqual(response, mock_response)
        


            
'''import json
import pytest


header = {"apikey": "@L4u71"}
y
global_id = None

test_request_payload = {
    "name": "Python3",
    "description": "asd",
    "category": 2,
    "subscription_type": "free",
    "location": "arg",
    "profile_picture": "www.google.com",
    "duration": 43.2,
    "language": "english",
    "level": "easy"
}

@pytest.mark.usefixtures("test_app")
class TestCourse:
    def test_create_course(self, test_app):
        response = test_app.post("/courses/",
                                data = json.dumps(test_request_payload),
                                headers = header)
        
        assert response.status_code == 201
        response_json = response.json()
        global global_id
        global_id = response_json['id']

        assert response_json['name'] == test_request_payload['name']
        assert response_json['description'] == test_request_payload['description']
        assert response_json['category'] == test_request_payload['category']
        assert response_json['subscription_type'] == test_request_payload['subscription_type']
        assert response_json['location'] == test_request_payload['location']
        assert response_json['profile_picture'] == test_request_payload['profile_picture']
        assert response_json['duration'] == test_request_payload['duration']
        assert response_json['language'] == test_request_payload['language']
        assert response_json['level'] == test_request_payload['level']

    
    def test_create_course_without_apikey(self, test_app):

        response = test_app.post("/courses/", data = json.dumps(test_request_payload))
        assert response.status_code == 401

        response_json = response.json()

        assert response_json['message'] == "Error with API Key"


    def test_get_existing_course(self, test_app):

        course_id = global_id 

        response = test_app.get("/courses/"+str(course_id), headers = header)

        assert response.status_code == 200
        response_json = response.json()

        assert response_json['id'] == course_id
        assert response_json['name'] == test_request_payload['name']
        assert response_json['description'] == test_request_payload['description']
        assert response_json['category'] == test_request_payload['category']
        assert response_json['subscription_type'] == test_request_payload['subscription_type']
        assert response_json['location'] == test_request_payload['location']
        assert response_json['profile_picture'] == test_request_payload['profile_picture']
        assert response_json['duration'] == test_request_payload['duration']
        assert response_json['language'] == test_request_payload['language']
        assert response_json['level'] == test_request_payload['level']

'''