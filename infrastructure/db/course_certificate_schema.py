from infrastructure.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CourseCertificate(Base):

    __tablename__ = "course_certificates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    pdf_path = Column(String(255), nullable=False)

    def __init__(self, id, course_id, user_id, pdf_path):

        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.pdf_path = pdf_path
