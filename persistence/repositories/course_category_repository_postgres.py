from domain.course_category_model import CourseCategory
from infrastructure.db.database import database
from infrastructure.db.course_category_schema import course_categories
from domain.course_category_repository import CourseCategoryRepository

class CourseCategoryRepositoryPostgres(CourseCategoryRepository):

    async def add_course_category(self, payload: CourseCategory):
        query = course_categories.insert().values(**payload.dict())
        return await database.execute(query=query)


    async def get_course_category(self, category_id: int):
        query = course_categories.select(course_categories.c.id == category_id)
        return await database.fetch_one(query=query)


    async def delete_course_category(self, category_id: int):
        query = course_categories.delete().where(course_categories.c.id == category_id)
        return await database.execute(query=query)