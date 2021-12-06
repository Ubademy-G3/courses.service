from infrastructure.db.course_user_schema import CourseUser

class CourseUserSerializer:

    @classmethod
    def serialize(self, user: CourseUser):
        
        return {
            "id": user.id,
            "course_id": user.course_id,
            "user_id": user.user_id,
            "user_type": user.user_type,
            "progress": user.progress,
            "approval_state": user.approval_state
        }