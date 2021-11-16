from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from errors.http_error import NotFoundError

ccrp = CourseCategoryRepositoryPostgres()

async def get_course_category(category_id):

    category = await ccrp.get_course_category(category_id)
    if category is None:
        raise NotFoundError("Category")
    return category