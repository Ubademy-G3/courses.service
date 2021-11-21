from infrastructure.db.course_module_schema import CourseModule

class CourseModuleSerializer:

    @classmethod
    def serialize(self, module: CourseModule):
        
        return {
            "id": module.id,
            "title": module.title,
            "media_id": module.media_id,
            "content": module.content,
            "exam_id": module.exam_id
        }