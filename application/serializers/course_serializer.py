from infrastructure.db.course_schema import Course


class CourseSerializer:
    @classmethod
    def serialize(self, course: Course):

        return {
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "category": course.category,
            "subscription_type": course.subscription_type,
            "location": course.location,
            "profile_picture": course.profile_picture,
            "duration": course.duration,
            "language": course.language,
            "level": course.level,
            "metrics": {},
        }
