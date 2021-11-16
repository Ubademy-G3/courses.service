from infrastructure.db.database import Base
from sqlalchemy import (Column, Float, String, Boolean, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CourseUser(Base):

    __tablename__ = 'course_users'
    id = Column(UUID, primary_key = True, default = uuid.uuid4())
    course_id = Column(UUID, ForeignKey('courses.id'), nullable = False)
    user_id = Column(UUID, nullable = False)
    user_type = Column(String(255), nullable = False)
    progress = Column(Float, nullable = False)
    aprobal_state = Column(Boolean, nullable = False)

    def __init__(self, id, course_id, user_id, user_type, progress, aprobal_state):
        
        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.user_type = user_type
        self.progress = progress
        self.aprobal_state = aprobal_state