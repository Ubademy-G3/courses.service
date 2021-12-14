from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class CourseModuleSchema(BaseModel):
    title: str
    course_id: UUID
    media_id: Optional[list] = None
    content: Optional[str] = None


class CourseModuleDB(CourseModuleSchema):
    id: UUID


class CourseModuleList(BaseModel):
    amount: int
    course_id: UUID
    modules: List[CourseModuleDB]


class CourseModulePatch(BaseModel):
    title: Optional[str] = None
    media_id: Optional[list] = None
    content: Optional[str] = None