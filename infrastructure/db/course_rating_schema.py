from infrastructure.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CourseRating(Base):

    __tablename__ = "course_ratings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    score = Column(Float, nullable=False)
    opinion = Column(String(500), nullable=True)

    def __init__(self, id, course_id, user_id, score, opinion):

        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.score = score
        self.opinion = opinion
