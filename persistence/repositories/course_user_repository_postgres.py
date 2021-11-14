from domain.course_user_model import (CourseUser, CourseUserPatch, Optional)
from infrastructure.db.database import database
from infrastructure.db.course_user_schema import course_users
from domain.course_user_repository import CourseUserRepository
from sqlalchemy import and_


class CourseUserRepositoryPostgres(CourseUserRepository):

    async def add_course_user(self, payload: CourseUser):
        query = course_users.insert().values(**payload.dict())
        return await database.execute(query=query)


    async def get_all_course_users(self, course_id: str, user_type: str):
        if user_type != None:
            query = course_users.select(course_users.c.course_id == course_id).\
            where(course_users.c.user_type == user_type.lower())
        else:
            query = course_users.select(course_users.c.course_id == course_id)
        return await database.fetch_all(query=query)


    async def get_course_user(self, course_id: str, user_id: str):
        query = course_users.select().where(and_(course_users.c.course_id == course_id,
                                            course_users.c.user_id == user_id))
        return await database.fetch_one(query=query)


    async def update_course_user(self, course_id: str, user_id: str, payload: CourseUserPatch):
        query = (course_users.update().
                 where(and_(course_users.c.course_id == course_id, course_users.c.user_id == user_id))
                 .values(**payload.dict()))
        return await database.execute(query=query)
        

    async def delete_course_user(self, course_id, user_id: str):
        query = course_users.delete().where(and_(course_users.c.course_id == course_id,
                                            course_users.c.user_id == user_id))
        return await database.execute(query=query)
