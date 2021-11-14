from uuid import uuid4, UUID

class CourseUser:
    def __init__(self, course_id, user_id, user_type, progress, aprobal_state):
        self.id = uuid4()
        self.course_id: str = course_id
        self.user_id: str = user_id
        self.user_type: str = user_type
        self.progress: str = progress
        self.aprobal_state: list = aprobal_state