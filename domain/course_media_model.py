from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional


class CourseMedia(BaseModel):
    id: UUID = uuid4()
    course_id: UUID
    url: Optional[str] = None