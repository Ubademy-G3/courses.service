from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_category_serializer import CourseCategorySerializer

ccrp = CourseCategoryRepositoryPostgres()

def get_course_category(db, category_id):

    category = ccrp.get_course_category(db, category_id)
    if category is None:
        raise NotFoundError("Category")
    return CourseCategorySerializer.serialize(category)


def get_all_categories(db):

    categories = ccrp.get_all_categories(db)
    if categories is None or len(categories) == 0:
        raise NotFoundError("Categories")
    cat_list = []
    for c in categories:
        cat_list.append(CourseCategorySerializer.serialize(c))
    return cat_list