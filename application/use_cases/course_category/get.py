from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from errors.http_error import NotFoundError
from application.serializers.course_category_serializer import CourseCategorySerializer

ccrp = CourseCategoryRepositoryPostgres()

def get_course_category(db, category_id):

    category = ccrp.get_course_category(db, category_id)
    if category is None:
        raise NotFoundError("Category")
    return CourseCategorySerializer.serialize(course_media)