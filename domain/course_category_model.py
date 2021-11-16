from pydantic import BaseModel
from typing import List


class CourseCategorySchema(BaseModel):
    name: str

class CourseCategoryDB(CourseCategorySchema):
    id: int