import json
import os
from tests.conftest import test_app
from unittest import TestCase, mock
from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from infrastructure.db.course_module_schema import CourseModule

global_module_id = "8b2ef0a0-33a9-401a-a4bb-afc458512c48"
global_course_id = "9b2ef0a0-33a9-401a-a4bb-afc458512c48"

header = {"apikey": os.getenv("API_KEY")}

test_request_payload = {"course_id": global_course_id, "title": "Module 1", "content": "asdf"}


class CourseModuleTest(TestCase):
    @mock.patch.object(CourseModuleRepositoryPostgres, "add_module")
    def test_create_module(self, mock_method):

        mock_method.return_value = CourseModule(
            id=global_module_id, course_id=global_course_id, title="Module 1", content="asdf"
        )

        response = test_app.post("/courses/"+str(global_course_id)+"/modules/", data=json.dumps(test_request_payload), headers=header)
        response_json = response.json()
        print(response_json);

        assert response.status_code == 201
        assert response_json["title"] == "Module 1"
        assert response_json["content"] == "asdf"

    @mock.patch.object(CourseModuleRepositoryPostgres, "get_module")
    def test_get_existing_module(self, mock_method):

        mock_method.return_value = CourseModule(
            id=global_module_id, course_id=global_course_id, title="Module 1", content="asdf"
        )

        response = test_app.get("/courses/"+str(global_course_id)+"/modules/" + str(global_module_id + "/"), headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["title"] == "Module 1"
        assert response_json["content"] == "asdf"

    @mock.patch.object(CourseModuleRepositoryPostgres, "get_all_modules_by_course_id")
    def test_get_all_modules(self, mock_method):

        mock_method.return_value = [
            CourseModule(id=global_module_id, course_id=global_course_id, title="Module 1", content="asdf")
        ]

        response = test_app.get("/courses/" + str(global_course_id) + "/modules/", headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["modules"][0]["title"] == "Module 1"
        assert response_json["modules"][0]["content"] == "asdf"

    @mock.patch.object(CourseModuleRepositoryPostgres, "update_module")
    @mock.patch.object(CourseModuleRepositoryPostgres, "get_module")
    def test_update_module(self, mock_update, mock_get):

        test_patch_payload = {"title": "Module number 1", "content": "abcd"}

        mock_update.return_value = CourseModule(
            id=global_module_id, course_id=global_course_id, title="Module number 1", content="abcd"
        )

        response = test_app.patch(
            "/courses/"+str(global_course_id)+"/modules/" + str(global_module_id), data=json.dumps(test_patch_payload), headers=header
        )
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["title"] == "Module number 1"
        assert response_json["content"] == "abcd"

    @mock.patch.object(CourseModuleRepositoryPostgres, "delete_module")
    @mock.patch.object(CourseModuleRepositoryPostgres, "get_module")
    def test_delete_module(self, mock_delete, mock_get):

        response = test_app.delete("/courses/"+str(global_course_id)+"/modules/" + str(global_module_id), headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["message"] == "The module {} was deleted successfully".format(global_module_id)
