from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String)

class CourseCategory(Base):

    __tablename__ = 'course_categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)

    def __init__(self, id, name):

        self.id = id
        self.name = name