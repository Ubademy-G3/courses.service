from pydantic import BaseModel
from uuid import UUID
from typing import List


class CourseRatingSchema(BaseModel):
    user_id: UUID
    score: float
    opinion: str


class CourseRatingDB(CourseRatingSchema):
    id: UUID
    course_id: UUID


class CourseRatingList(BaseModel):
    amount: int
    course_id: UUID
    rating: float
    reviews: List[CourseRatingDB]
