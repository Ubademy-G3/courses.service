from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from infrastructure.db.course_category_schema import CourseCategory
from application.serializers.course_category_serializer import CourseCategorySerializer

ccrp = CourseCategoryRepositoryPostgres()


def add_course_category(db, args):

    new_category = CourseCategory(id=args.id, name=args.name)

    ccrp.add_course_category(db, new_category)
    return CourseCategorySerializer.serialize(new_category)
