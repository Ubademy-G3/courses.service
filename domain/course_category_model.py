from pydantic import BaseModel


class CourseCategorySchema(BaseModel):
    id: int
    name: str
    photo_url: str
