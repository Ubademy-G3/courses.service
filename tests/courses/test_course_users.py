import json
import os
import uuid
from tests.conftest import test_app
from unittest import TestCase, mock
from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from infrastructure.db.course_user_schema import CourseUser

header = {"apikey": os.getenv('API_KEY')}

global_course_id = uuid.uuid4()
global_user_id = uuid.uuid4()
global_user_id_pkey = None

test_request_payload = {
    "user_id": str(global_user_id),
    "user_type": "student",
    "progress": 0.0,
    "approval_state": False
}

class CourseUserTest(TestCase):

    @mock.patch.object(CourseUserRepositoryPostgres, "add_course_user")
    @mock.patch.object(CourseUserRepositoryPostgres, "get_course_user")
    @mock.patch.object(CourseRepositoryPostgres, "get_course_by_id")   
    def test_add_course_user(self, mock_method_post, mock_get, mock_course):

        mock_method_post.return_value.status_code = 201
        mock_get.return_value = None
        mock_course.return_value = 'as'
        
        response = test_app.post("/courses/"+str(global_course_id)+"/users/",
                                data = json.dumps(test_request_payload),
                                headers = header)
        
        response_json = response.json()
        global global_user_id_pkey
        global_user_id_pkey = response_json['id']

        assert response.status_code == 201
        assert response_json == {
            "user_id": str(global_user_id),
            "user_type": "student",
            "progress": 0.0,
            "approval_state": False,
            "id": global_user_id_pkey
        }
    

    @mock.patch.object(CourseUserRepositoryPostgres, "get_all_course_users")
    def test_get_all_course_users(self, mock_method):

        mock_method.return_value = [
            CourseUser(
                id = global_user_id_pkey,
                course_id = global_course_id,
                user_id = global_user_id,
                user_type = "student",
                progress = 0.0,
                approval_state = False
            )
        ]

        response = test_app.get("/courses/"+str(global_course_id)+"/users/",
                                headers = header)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json == {
            "amount": 1,
            "course_id": str(global_course_id),
            "users": [{
                "user_id": str(global_user_id),
                "user_type": "student",
                "progress": 0.0,
                "approval_state": False,
                "id": global_user_id_pkey
            }]
        }
        
    
    @mock.patch.object(CourseUserRepositoryPostgres, "update_course_user")
    @mock.patch.object(CourseUserRepositoryPostgres, "get_course_user")    
    def test_update_user(self, mock_update, mock_get):

        test_patch_payload = {
            "user_type": "instructor",
            "progress": 50.0,
            "approval_state": False
        }

        mock_update.return_value = CourseUser(
            id = global_user_id_pkey,
            course_id = global_course_id,
            user_id = global_user_id,
            user_type = "instructor",
            progress = 50.0,
            approval_state = False
        )

        response = test_app.patch("/courses/"+str(global_course_id)+"/users/"+str(global_user_id_pkey),
                                data = json.dumps(test_patch_payload),
                                headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json['user_id'] == str(global_user_id)
        assert response_json['user_type'] == "instructor"
        assert response_json['progress'] == 50.0
        assert response_json['approval_state'] == False
        assert response_json['id'] == str(global_user_id_pkey)