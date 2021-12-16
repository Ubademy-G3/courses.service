from pydantic import BaseModel
from uuid import UUID
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
    total_exams: Optional[int] = None


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
    total_exams: int


class CourseDB(CourseSchema):
    id: UUID
    metrics: dict


class CourseList(BaseModel):
    amount: int
    courses: List[CourseDB]
