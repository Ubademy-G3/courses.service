from infrastructure.db.database import Base
from sqlalchemy import (Column, String, Text, ForeignKey, ARRAY)
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CourseModule(Base):

    __tablename__ = "course_modules"
    id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4())
    title = Column(String(255), nullable = False)
    media_id = Column(ARRAY(UUID(as_uuid=True)),nullable = True)
    content = Column(Text, nullable = True)

    def __init__(self, id, title, media_id, content):

        self.id = id
        self.title = title
        self.media_id = media_id
        self.content = content