from domain.course_model import Course

class CourseSerializer:

    @classmethod
    def serialize(self, course: Course):
        
        return {
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "category": course.category,
            "kind": course.kind,
            "subscription_type": course.subscription_type,
            "location": course.location,
            "info": course.info
        }