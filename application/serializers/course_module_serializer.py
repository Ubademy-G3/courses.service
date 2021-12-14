from infrastructure.db.course_module_schema import CourseModule

class CourseModuleSerializer:

    @classmethod
    def serialize(self, module: CourseModule):
        
        return {
            "id": module.id,
            "course_id": module.course_id,
            "title": module.title,
            "media_id": module.media_id,
            "content": module.content
        }