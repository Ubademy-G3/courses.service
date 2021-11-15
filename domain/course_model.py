from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional, List


class Course(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    kind: str
    subscription_type: str
    location: str
    info: dict
    profile_picture: str


class CoursePatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    kind: Optional[str] = None
    subscription_type: Optional[str] = None
    location: Optional[str] = None
    info: Optional[dict] = None
    profile_picture: Optional[str] = None
    

class CourseSchema(BaseModel):
    name: str
    description: str
    category: str
    kind: str
    subscription_type: str
    location: str
    info: dict
    profile_picture: str

class CourseDB(CourseSchema):
    id: UUID
