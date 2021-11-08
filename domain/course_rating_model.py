from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List


class CourseRating(BaseModel):
    id: UUID = uuid4()
    course_id: UUID
    user_id: UUID
    score: int
    opinion: str

class CourseRatingSchema(BaseModel):
    score: int
    opinion:str

class CourseRatingDB(CourseRatingSchema):
    id: UUID
    user_id: UUID    

class CourseRatingResponse(BaseModel):
    amount: int
    course_id: UUID
    rating: List[CourseRatingDB]
    