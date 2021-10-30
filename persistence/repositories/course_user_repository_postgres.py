from domain.course_user_model import CourseUser
from infrastructure.db.database import database
from infrastructure.db.course_user_schema import course_users
from domain.course_user_repository import CourseUserRepository


class CourseUserRepositoryPostgres(CourseUserRepository):

    async def add_course_user(self, payload: CourseUser):
        query = course_users.insert().values(**payload.dict())
        return await database.execute(query=query)

    async def get_all_course_users(self):
        query = course_users.select()
        return await database.fetch_all(query=query)

    async def get_course_user_by_id(self, id: str):
        query = course_users.select(course_user.c.id == id)
        return await database.fetch_one(query=query)

    async def delete_course_user(self, id: str):
        query = course_users.delete().where(course_user.c.id == id)
        return await database.execute(query=query)

    async def delete_all_course_users(self):
        query = course_users.delete()
        return await database.execute(query=query)
