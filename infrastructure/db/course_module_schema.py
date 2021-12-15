from infrastructure.db.database import Base
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CourseModule(Base):

    __tablename__ = "course_modules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)

    def __init__(self, id, course_id, title, content):

        self.id = id
        self.course_id = course_id
        self.title = title
        self.content = content
