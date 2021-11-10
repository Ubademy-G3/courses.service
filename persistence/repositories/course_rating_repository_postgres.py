from domain.course_rating_model import CourseRating
from infrastructure.db.database import database
from infrastructure.db.course_rating_schema import course_ratings
from domain.course_rating_repository import CourseRatingRepository
from sqlalchemy import and_


class CourseRatingRepositoryPostgres(CourseRatingRepository):

    async def add_course_rating(self, payload: CourseRating):
        query = course_ratings.insert().values(**payload.dict())
        return await database.execute(query=query)

    async def get_all_course_ratings(self, course_id: str):
        query = course_ratings.select(course_ratings.c.course_id == course_id)
        return await database.fetch_all(query=query)
       
    async def get_course_rating(self, course_id: str, rating_id: str):
        query = course_ratings.select().where(and_(course_ratings.c.id == rating_id,
                                            course_ratings.c.course_id == course_id))
        return await database.fetch_one(query=query)

    async def get_course_rating_from(self, user_id: str, course_id: str):
        query = course_ratings.select().where(and_(course_ratings.c.course_id == course_id,
                                            course_ratings.c.user_id == user_id))

    async def delete_course_rating(self, course_id: str, rating_id: str):
        query = course_ratings.delete().where(and_(course_ratings.c.course_id == course_id,
                                                course_ratings.c.id == rating_id))
        return await database.execute(query=query)