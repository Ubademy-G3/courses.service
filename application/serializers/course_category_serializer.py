from domain.course_category_model import CourseCategory

class CourseCategorySerializer:

    @classmethod
    def serialize(self, category: CourseCategory):

        return {
            "id": category.id,
            "name": category.name
        }