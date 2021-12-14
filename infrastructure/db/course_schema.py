from infrastructure.db.database import Base, relationship
from sqlalchemy import Column, Integer, String, Table, Text, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Course(Base):

    __tablename__ = "courses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(Integer, nullable=False)
    subscription_type = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=False)
    duration = Column(Float, nullable=False)
    language = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False)

    # Relationships
    media = relationship("CourseMedia", cascade="all, delete")
    user = relationship("CourseUser", cascade="all, delete")
    rating = relationship("CourseRating", cascade="all, delete")
    certificate = relationship("CourseCertificate", cascade="all, delete")

    def __init__(
        self, id, name, description, category, subscription_type, location, profile_picture, duration, language, level
    ):

        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.subscription_type = subscription_type
        self.location = location
        self.profile_picture = profile_picture
        self.duration = duration
        self.language = language
        self.level = level
