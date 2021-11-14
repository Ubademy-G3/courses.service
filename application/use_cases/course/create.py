from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from domain.course_model import *
from domain.course_entity import Course
from application.serializers.course_serializer import CourseSerializer

crp = CourseRepositoryPostgres()

async def add_course(args):
    
    new_course = Course(
        name = args.name,
        description = args.description,
        category = args.category,
        kind = args.kind,
        subscription_type = args.subscription_type,
        location = args.location,
        info = args.info
    )

    await crp.add_course(new_course)
    return CourseSerializer.serialize(new_course)