from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from domain.course_user_model import *
from errors.http_error import NotFoundError
from errors.ubademy_error import CourseAlreadyAcquired
from application.serializers.course_user_serializer import CourseUserSerializer
from application.use_cases.course.get import course_is_present
from application.use_cases.course_user.get import user_already_registered

curp = CourseUserRepositoryPostgres()

async def add_course_user(course_id, args):
    
    if not await course_is_present(course_id):
        raise NotFoundError("Course {}".format(course_id))

    if await user_already_registered(course_id, args.user_id):
        raise CourseAlreadyAcquired()

    new_user = CourseUser(
        course_id = course_id,
        user_id = args.user_id,
        user_type = args.user_type,
        progress = args.progress,
        aprobal_state = args.aprobal_state
    )
    await curp.add_course_user(new_user)
    return CourseUserSerializer.serialize(new_user)