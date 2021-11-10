from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional


class Course(BaseModel):
    id: UUID = uuid4()
    name: str
    description: str
    category: str
    kind: str
    subscription_type: list
    location: str

class CoursePatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    kind: Optional[str] = None
    subscription_type: Optional[list] = None
    location: Optional[str] = None

class CourseSchema(BaseModel):
    name: str
    description: str
    category: str
    kind: str
    subscription_type: list
    location: str
