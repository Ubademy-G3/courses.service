from pydantic import BaseModel
from typing import List


class CourseCategorySchema(BaseModel):
    id: int
    name: str
