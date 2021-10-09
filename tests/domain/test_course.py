from domain.course import Course


class TestCourse:
    def test_constructor_creates_instance(self):
        course = Course(id="1234", name="Curso01")

        assert course.name == "Curso01"
        assert course.id == "1234"
