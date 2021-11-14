from domain.course_user_model import CourseUser
from infrastructure.db.database import database
from infrastructure.db.course_user_schema import course_users
from domain.course_user_repository import CourseUserRepository
from sqlalchemy import and_


class CourseUserRepositoryPostgres(CourseUserRepository):

    async def add_course_user(self, payload: CourseUser):
        query = course_users.insert().values(**payload.dict())
        return await database.execute(query=query)


    async def get_all_course_users(self, course_id: str):
        query = course_users.select(course_users.c.course_id == course_id)
        return await database.fetch_all(query=query)


    async def get_course_user(self, course_id: str, user_id: str):
        query = course_users.select().where(and_(course_users.c.course_id == course_id,
                                            course_users.c.user_id == user_id))
        return await database.fetch_one(query=query)
        

    async def delete_course_user(self, course_id, user_id: str):
        query = course_users.delete().where(and_(course_users.c.course_id == course_id,
                                            course_users.c.user_id == user_id))
        return await database.execute(query=query)
