from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class CourseUserSchema(BaseModel):
    user_id: UUID
    user_type: str
    progress: float = 0.0
    approval_state: bool = False


class CourseUserDB(CourseUserSchema):
    id: UUID


class CourseUserList(BaseModel):
    amount: int
    course_id: UUID
    users: List[CourseUserDB]


class CourseUserPatch(BaseModel):
    user_type: Optional[str] = None
    progress: Optional[float] = None
    approval_state: Optional[bool] = None
