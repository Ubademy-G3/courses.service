from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class CourseModuleSchema(BaseModel):
    title: str
    content: Optional[str] = None


class CourseModuleDB(CourseModuleSchema):
    id: UUID
    course_id: UUID


class CourseModuleList(BaseModel):
    amount: int
    course_id: UUID
    modules: List[CourseModuleDB]


class CourseModulePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
