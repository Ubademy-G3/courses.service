from infrastructure.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CourseMedia(Base):

    __tablename__ = "course_media"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    module_id = Column(UUID(as_uuid=True), ForeignKey("course_modules.id", ondelete="CASCADE"), nullable=False)
    url = Column(String(255), nullable=False)

    def __init__(self, id, course_id, module_id, url):

        self.id = id
        self.course_id = course_id
        self.module_id = module_id
        self.url = url
