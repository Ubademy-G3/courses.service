from domain.course_model import (Course, CoursePatch, uuid4, UUID)
from infrastructure.db.database import database
from infrastructure.db.course_schema import courses
from domain.course_repository import CourseRepository


class CourseRepositoryPostgres(CourseRepository):

    async def add_course(self, payload: Course):
        query = courses.insert().values(**payload.dict())
        return await database.execute(query=query)


    async def get_all_courses(self):
        query = courses.select()
        return await database.fetch_all(query=query)
        

    async def get_course_by_id(self, course_id: str):
        query = courses.select(courses.c.id == course_id)
        return await database.fetch_one(query=query)


    async def update_course(self, course_id: str, payload: CoursePatch):
        query = (courses.update().
                 where(courses.c.id == course_id)
                 .values(**payload.dict()))
        return await database.execute(query=query)


    async def delete_course(self, course_id: str):
        query = courses.delete().where(courses.c.id == course_id)
        return await database.execute(query=query)
        

    async def delete_all_courses(self):
        query = courses.delete()
        return await database.execute(query=query)
