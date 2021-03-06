import json
import os
from tests.conftest import test_app
from unittest import TestCase, mock
from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from infrastructure.db.course_category_schema import CourseCategory

header = {"apikey": os.getenv("API_KEY")}

test_request_payload = {"id": 1, "name": "Math", "photo_url": "https://www.collegechoice.net/app/uploads/2017/09/Arts_Humanities-Badge-273x300.png"}


class CourseCategoryTest(TestCase):
    @mock.patch.object(CourseCategoryRepositoryPostgres, "add_course_category")
    def test_create_category(self, mock_method):

        mock_method.return_value = CourseCategory(id=1, name="Math", photo_url="https://www.collegechoice.net/app/uploads/2017/09/Arts_Humanities-Badge-273x300.png")
        response = test_app.post("/courses/category/", data=json.dumps(test_request_payload), headers=header)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json["id"] == 1
        assert response_json["name"] == "Math"
        assert response_json["photo_url"] == "https://www.collegechoice.net/app/uploads/2017/09/Arts_Humanities-Badge-273x300.png"

    @mock.patch.object(CourseCategoryRepositoryPostgres, "get_course_category")
    def test_get_existing_category(self, mock_method):

        mock_method.return_value = CourseCategory(id=1, name="Math", photo_url="https://www.collegechoice.net/app/uploads/2017/09/Arts_Humanities-Badge-273x300.png")
        response = test_app.get("/courses/category/1", headers=header)

        response_json = response.json()

        assert response.status_code == 200
        assert response_json["id"] == 1
        assert response_json["name"] == "Math"
        assert response_json["photo_url"] == "https://www.collegechoice.net/app/uploads/2017/09/Arts_Humanities-Badge-273x300.png"

    @mock.patch.object(CourseCategoryRepositoryPostgres, "get_all_categories")
    def test_get_all_categories(self, mock_method):

        mock_method.return_value = [CourseCategory(id=1, name="Math", photo_url="hola"), CourseCategory(id=2, name="Programming", photo_url="chau")]

        response = test_app.get("/courses/category/", headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json == [{"id": 1, "name": "Math", "photo_url": "hola"}, {"id": 2, "name": "Programming", "photo_url": "chau"}]

    @mock.patch.object(CourseCategoryRepositoryPostgres, "delete_course_category")
    @mock.patch.object(CourseCategoryRepositoryPostgres, "get_course_category")
    def test_delete_category(self, mock_delete, mock_get):

        response = test_app.delete("/courses/category/1", headers=header)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["message"] == "The category 1 was deleted successfully"
