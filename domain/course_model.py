from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional, List

class CoursePatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[int] = None
    subscription_type: Optional[str] = None
    location: Optional[str] = None
    profile_picture: Optional[str] = None
    duration: Optional[float] = None
    language: Optional[str] = None
    level: Optional[str] = None
    modules: Optional[list] = None
    

class CourseSchema(BaseModel):
    name: str
    description: str
    category: int
    subscription_type: str
    location: str
    profile_picture: str
    duration: float
    language: str
    level: str
    modules: list


class CourseDB(CourseSchema):
    id: UUID


class CourseList(BaseModel):
    amount: int
    courses: List[CourseDB]


