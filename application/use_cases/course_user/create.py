from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from fastapi import HTTPException
from domain.course_user_model import *
from application.serializers.course_user_serializer import CourseUserSerializer

curp = CourseUserRepositoryPostgres()

async def add_course_user(course_id, args):

    new_user = CourseUser(
        course_id = course_id,
        user_id = args.user_id,
        user_type = args.user_type,
        progress = args.progress,
        aprobal_state = args.aprobal_state
    )
    await curp.add_course_user(new_user)
    return CourseUserSerializer.serialize(new_user)