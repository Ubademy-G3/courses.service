from domain.course_media_model import CourseMedia

class CourseMediaSerializer:

    @classmethod
    def serialize(self, media: CourseMedia):
        return {
            "id": media.id,
            "course_id": media.course_id,
            "url": media.url
        }