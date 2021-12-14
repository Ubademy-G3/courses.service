from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List


class CourseMediaSchema(BaseModel):
    url: str
    module_id: UUID


class CourseMediaDB(CourseMediaSchema):
    id: UUID


class CourseMediaList(BaseModel):
    amount: int
    course_id: UUID
    course_media: List[CourseMediaDB]


class CourseMediaByModuleList(BaseModel):
    amount: int
    module_id: UUID
    course_media: List[CourseMediaDB]
