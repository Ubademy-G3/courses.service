from pydantic import BaseModel
from typing import List

class CourseCategory(BaseModel):
    id: int
    name: str

class CourseCategorySchema(BaseModel):
    name: str

class CourseCategoryDB(CourseCategorySchema):
    id: int