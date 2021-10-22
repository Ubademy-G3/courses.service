from pydantic import BaseModel
from uuid import uuid4, UUID


class Course(BaseModel):
    id: UUID = uuid4()
    name: str
    description: str
    hashtags: list
    kind: str
    subscription_type: str
    location: str