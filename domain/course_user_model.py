from pydantic import BaseModel
from uuid import uuid4, UUID

class CourseUser(BaseModel):
    id: UUID
    course_id: UUID
    user_type: list
    progress: int
    aprobal_state: bool