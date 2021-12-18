from infrastructure.db.database import Base
from sqlalchemy import Column, Integer, String


class CourseCategory(Base):

    __tablename__ = "course_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    photo_url = Column(String(255), nullable=True)

    def __init__(self, id, name, photo_url):

        self.id = id
        self.name = name
        self.photo_url = photo_url
