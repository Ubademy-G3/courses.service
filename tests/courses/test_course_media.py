import json
import os
import uuid
from tests.conftest import test_app
from unittest import TestCase, mock
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from infrastructure.db.course_media_schema import CourseMedia


header = {"apikey": os.getenv("API_KEY")}

global_course_id = uuid.uuid4()
global_media_id = None
global_module_id = str(uuid.uuid4())

test_request_payload = {"url": "www.google.com", "module_id": global_module_id}


class CourseMediaTest(TestCase):
    @mock.patch.object(CourseMediaRepositoryPostgres, "add_course_media")
    @mock.patch.object(CourseModuleRepositoryPostgres, "get_module")
    def test_create_course_media(self, mock_method, mock_get_module):

        mock_method.return_value.status_code = 201
        mock_get_module.return_value = 1
        response = test_app.post(
            "/courses/" + str(global_course_id) + "/media/", data=json.dumps(test_request_payload), headers=header
        )
        response_json = response.json()
        global global_media_id
        global_media_id = response_json["id"]

        assert response.status_code == 201
        assert response_json["url"] == test_request_payload["url"]
        assert response_json["module_id"] == test_request_payload["module_id"]

    @mock.patch.object(CourseMediaRepositoryPostgres, "get_course_media")
    def test_get_existing_media(self, mock_method):

        mock_method.return_value = CourseMedia(
            id=global_media_id, course_id=global_course_id, module_id=global_module_id, url="www.google.com"
        )
        response = test_app.get("/courses/" + str(global_course_id) + "/media/" + str(global_media_id), headers=header)

        response_json = response.json()

        assert response.status_code == 200
        assert response_json["url"] == "www.google.com"
        assert response_json["id"] == global_media_id
        assert response_json["module_id"] == global_module_id

    @mock.patch.object(CourseMediaRepositoryPostgres, "get_all_course_media")
    def test_get_all_media(self, mock_method):

        mock_method.return_value = [
            CourseMedia(id=global_media_id, course_id=global_course_id, module_id=global_module_id, url="www.google.com")
        ]

        response = test_app.get("/courses/" + str(global_course_id) + "/media/", headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json == {
            "amount": 1,
            "course_id": str(global_course_id),
            "course_media": [{"url": "www.google.com", "id": str(global_media_id), "module_id": global_module_id}],
        }

    @mock.patch.object(CourseMediaRepositoryPostgres, "get_all_course_module_media")
    def test_get_all_media_by_module(self, mock_method):

        mock_method.return_value = [
            CourseMedia(id=global_media_id, course_id=global_course_id, module_id=global_module_id, url="www.google.com")
        ]

        response = test_app.get("/courses/" + str(global_course_id) + "/media/module/" + global_module_id, headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json == {
            "amount": 1,
            "module_id": str(global_module_id),
            "course_media": [{"url": "www.google.com", "id": str(global_media_id), "module_id": global_module_id}],
        }

    @mock.patch.object(CourseMediaRepositoryPostgres, "delete_course_media")
    @mock.patch.object(CourseMediaRepositoryPostgres, "get_course_media")
    def test_delete_media(self, mock_method_delete, mock_method_get):

        response = test_app.delete("/courses/" + str(global_course_id) + "/media/" + str(global_media_id), headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["message"] == "The media {} was deleted successfully".format(global_media_id)
