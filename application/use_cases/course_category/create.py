from persistence.repositories.course_category_repository_postgres import CourseCategoryRepositoryPostgres
from domain.course_category_model import *
from application.serializers.course_category_serializer import CourseCategorySerializer
ccrp = CourseCategoryRepositoryPostgres()

async def add_course_category(args):

    new_category = CourseCategory(
        id = args.id,
        name = args.name
    )

    await ccrp.add_course_category(new_category)
    return CourseCategorySerializer.serialize(new_category)