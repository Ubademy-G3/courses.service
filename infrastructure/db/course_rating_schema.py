from infrastructure.db.database import Base
from sqlalchemy import (Column, String, ForeignKey, Float)
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CourseRating(Base):

    __tablename__ = 'course_ratings'
    id = Column(UUID, primary_key = True, default = uuid.uuid4())
    course_id = Column(UUID, ForeignKey('courses.id'), nullable = False)
    user_id = Column(UUID, nullable = False)
    score = Column(Float, nullable = False)
    opinion = Column(String(500), nullable = True)

    def __init__(self, id, course_id, user_id, score, opinion):

        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.score = score
        self.opinion = opinion