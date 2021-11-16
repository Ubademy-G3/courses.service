from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from errors.http_error import NotFoundError

ccrp = CourseCategoryRepositoryPostgres()

async def delete_category(category_id):

    category = await ccrp.get_course_category(category_id)
    if not category:
        raise NotFoundError("Category")
    return await ccrp.delete_course_category(category_id)