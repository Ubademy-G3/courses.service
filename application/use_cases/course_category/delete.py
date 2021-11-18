from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from exceptions.http_error import NotFoundError

ccrp = CourseCategoryRepositoryPostgres()

def delete_course_category(db, category_id):

    category = ccrp.get_course_category(db, category_id)
    if not category:
        raise NotFoundError("Category")
    ccrp.delete_course_category(db, category)