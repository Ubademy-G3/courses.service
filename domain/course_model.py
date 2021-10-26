from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional


class Course(BaseModel):
    id: UUID = uuid4()
    name: Optional[str] = None
    description: Optional[str] = None
    hashtags: Optional[list] = None
    kind: Optional[str] = None
    subscription_type: Optional[str] = None
    location: Optional[str] = None