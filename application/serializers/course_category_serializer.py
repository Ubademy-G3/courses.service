from infrastructure.db.course_category_schema import CourseCategory


class CourseCategorySerializer:
    @classmethod
    def serialize(self, category: CourseCategory):

        return {"id": category.id, "name": category.name}
