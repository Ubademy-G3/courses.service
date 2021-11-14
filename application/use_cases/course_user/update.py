from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from domain.course_user_model import *
from errors.http_error import NotFoundError
from application.serializers.course_user_serializer import CourseUserSerializer

curp = CourseUserRepositoryPostgres()

async def update_course_user(course_id, user_id, new_args):
    
    user_to_update = await curp.get_course_user(course_id, user_id)
    if not user_to_update:
        raise NotFoundError("User {}".format(user_id))

    user_in_db = CourseUser(**user_to_update)
    if new_args.user_type is not None:
        user_in_db.user_type = new_args.user_type
        
    if new_args.progress is not None:
        user_in_db.progress = new_args.progress
        if new_args.progress == 100:
            user_in_db.aprobal_state = True

    if new_args.aprobal_state is not None:
        user_in_db.aprobal_state = new_args.aprobal_state
                
    update_data = user_in_db.dict(exclude_unset = True)
    updated_user = user_in_db.copy(update = update_data)
    await curp.update_course_user(course_id, user_id, updated_user)
    return CourseUserSerializer.serialize(updated_user)