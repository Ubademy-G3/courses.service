from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from domain.course_model import *
from application.serializers.course_serializer import CourseSerializer

crp = CourseRepositoryPostgres()

async def add_course(args):
    
    new_course = Course(
        id = uuid4(),
        name = args.name,
        description = args.description,
        category = args.category,
        kind = args.kind,
        subscription_type = args.subscription_type,
        location = args.location,
        info = args.info,
        profile_picture = args.profile_picture
    )

    await crp.add_course(new_course)
    return CourseSerializer.serialize(new_course)