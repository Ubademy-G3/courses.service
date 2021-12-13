import json
import os
from tests.conftest import test_app
from unittest import TestCase, mock
from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from infrastructure.db.course_schema import Course
from exceptions.auth_error import ApiKeyError
from exceptions.http_error import NotFoundError

header = {"apikey": os.getenv('API_KEY')}

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

class CourseTest(TestCase):

    @mock.patch.object(CourseRepositoryPostgres, "add_course")
    def test_post_without_apikey(self, mock_method):

        response = test_app.post("/courses/",
                                data = json.dumps(test_request_payload))
        response_json = response.json()

        self.assertRaises(ApiKeyError)


    @mock.patch.object(CourseRepositoryPostgres, "add_course")
    def test_create_course(self, mock_method):

        mock_method.return_value.status_code = 201
        response = test_app.post("/courses/",
                                data = json.dumps(test_request_payload),
                                headers = header)
        
        
        response_json = response.json()
        global global_id
        global_id = response_json['id']
        assert response.status_code == 201
        
        assert response_json['name'] == test_request_payload['name']
        assert response_json['description'] == test_request_payload['description']
        assert response_json['category'] == test_request_payload['category']
        assert response_json['subscription_type'] == test_request_payload['subscription_type']
        assert response_json['location'] == test_request_payload['location']
        assert response_json['profile_picture'] == test_request_payload['profile_picture']
        assert response_json['duration'] == test_request_payload['duration']
        assert response_json['language'] == test_request_payload['language']
        assert response_json['level'] == test_request_payload['level']
        assert response_json['modules'] == test_request_payload['modules']


    @mock.patch.object(CourseRepositoryPostgres, "get_course_by_id")
    def test_get_without_apikey(self, mock_method):

        response = test_app.get("/courses/"+str(global_id))
        response_json = response.json()

        self.assertRaises(ApiKeyError)
        assert response_json['message'] == "Error with API Key"


    @mock.patch.object(CourseRepositoryPostgres, "update_course")
    @mock.patch.object(CourseRepositoryPostgres, "get_course_by_id")
    def test_update_course(self, mock_method_update, mock_method_get):
        
        test_patch_payload = {
            "name": "Python 3",
            "description": "Introduccion a ciencia de datos con python",
            "category": 2,
            "subscription_type": "free",
            "location": "Argentina",
            "profile_picture": "www.google.com",
            "duration": 44,
            "language": "spanish",
            "level": "easy",
            "modules": []
        }
        course_id = global_id

        mock_method_update.return_value.status_code = 200
        mock_method_update.return_value = Course(
            id= course_id,
            name= "Python 3",
            description= "Introduccion a ciencia de datos con python",
            category= 2,
            subscription_type= "free",
            location= "Argentina",
            profile_picture= "www.google.com",
            duration= 44,
            language= "spanish",
            level= "easy",
            modules= []
        )
                
        response = test_app.patch("/courses/"+str(course_id),
                                data = json.dumps(test_patch_payload),
                                headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "id": course_id,
            "name": "Python 3",
            "description": "Introduccion a ciencia de datos con python",
            "category": 2,
            "subscription_type": "free",
            "location": "Argentina",
            "profile_picture": "www.google.com",
            "duration": 44,
            "language": "spanish",
            "level": "easy",
            "modules": [],
            "metrics": {}
        }


    @mock.patch.object(CourseRepositoryPostgres, "delete_course")
    @mock.patch.object(CourseRepositoryPostgres, "get_course_by_id")
    def test_delete_course(self, mock_method_delete, mock_method_get):

        course_id = global_id

        response = test_app.delete("/courses/"+str(course_id),
                                headers = header)
        
        response_json = response.json()
        assert response.status_code == 200
        assert response_json['message'] == "Course {} deleted successfully".format(course_id)


    @mock.patch.object(CourseRepositoryPostgres, "get_course_by_id")
    def test_get_nonexistent_course(self, mock_method):
        
        course_id = global_id 
        mock_method.return_value = None
        
        response = test_app.get("/courses/"+str(course_id), headers = header)
        response_json = response.json()
        
        self.assertRaises(NotFoundError)
        assert response_json['message'] == "Course {} not found".format(course_id)
        