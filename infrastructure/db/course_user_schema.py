from infrastructure.db.database import Base
from sqlalchemy import Column, Float, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CourseUser(Base):

    __tablename__ = "course_users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    user_type = Column(String(255), nullable=False)
    progress = Column(Float, nullable=False)
    approval_state = Column(Boolean, nullable=False)

    def __init__(self, id, course_id, user_id, user_type, progress, approval_state):

        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.user_type = user_type
        self.progress = progress
        self.approval_state = approval_state
