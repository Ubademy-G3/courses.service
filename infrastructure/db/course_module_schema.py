from infrastructure.db.database import Base
from sqlalchemy import (Column, String, Text, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CourseModule(Base):

    __tablename__ = "course_modules"
    id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4())
    title = Column(String(255), nullable = False)
    media_id = Column(UUID(as_uuid=True), ForeignKey('course_media.id', ondelete="CASCADE"), nullable = True)
    content = Column(Text, nullable = True)
    exam_id = Column(UUID(as_uuid=True), nullable = True)

    def __init__(self, id, title, media_id, content, exam_id):

        self.id = id
        self.title = title
        self.media_id = media_id
        self.content = content
        self.exam_id = exam_id