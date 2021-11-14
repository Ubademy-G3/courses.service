from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List


class CourseMedia(BaseModel):
    id: UUID
    course_id: UUID
    url: str


class CourseMediaSchema(BaseModel):
    url: str


class CourseMediaDB(CourseMediaSchema):
    id: UUID


class CourseMediaList(BaseModel):
    amount: int
    course_id: UUID
    course_media: List[CourseMediaDB]