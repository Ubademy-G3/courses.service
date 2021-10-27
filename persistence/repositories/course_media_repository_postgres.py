from domain.course_media_model import CourseMedia, uuid4, UUID
from infrastructure.db.database import database
from infrastructure.db.course_media_schema import course_media
from domain.course_media_repository import CourseMediaRepository


class CourseMediaRepositoryPostgres(CourseMediaRepository):

    async def add_course_media(self, payload: CourseMedia):
        query = course_media.insert().values(**payload.dict())
        return await database.execute(query=query)

    async def get_all_courses_media(self):
        query = course_media.select()
        return await database.fetch_all(query=query)

    async def get_course_media_by_id(self, id: str):
        query = course_media.select(course_media.c.id == id)
        return await database.fetch_one(query=query)

    async def update_course_media(self, id: str, payload: CourseMedia):
        query = (course_media.update().
                 where(course_media.c.id == id)
                 .values(**payload.dict()))
        return await database.execute(query=query)

    async def delete_course_media(self, id: str):
        query = course_media.delete().where(course_media.c.id == id)
        return await database.execute(query=query)

    async def delete_all_courses_media(self):
        query = course_media.delete()
        return await database.execute(query=query)