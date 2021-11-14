from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List,Optional

class CourseUser(BaseModel):
    id: UUID
    course_id: UUID
    user_id: UUID
    user_type: list
    progress: int = 0
    aprobal_state: bool = False


class CourseUserSchema(BaseModel):
    user_id: UUID
    user_type: list
    progress: int = 0
    aprobal_state: bool = False


class CourseUserDB(CourseUserSchema):
    id: UUID
    user_id: UUID


class CourseUserList(CourseUserDB):
    amount: int
    course_id: UUID
    users: List[CourseUserDB]
    

class CourseUserPatch(BaseModel):
    user_type: Optional[list] = None
    progress: Optional[int] = None
    aprobal_state: Optional[bool] = None
