from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List

class CourseRatingSchema(BaseModel):
    user_id: UUID
    score: float
    opinion:str


class CourseRatingDB(CourseRatingSchema):
    id: UUID
    course_id: UUID   
     

class CourseRatingList(BaseModel):
    amount: int
    course_id: UUID
    rating: List[CourseRatingDB]
    