from domain.course_model import Course
from infrastructure.db.database import database
from infrastructure.db.course_schema import courses
from domain.course_repository import CourseRepository

class CourseRepositoryPostgres(CourseRepository):

    async def add_course(self, payload: Course):
        query = courses.insert().values(**payload.dict())
        return await database.execute(query=query)

