from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from errors.http_error import NotFoundError
from application.serializers.course_user_serializer import CourseUserSerializer

curp = CourseUserRepositoryPostgres()

def update_course_user(db, course_id, user_id, new_args):
    
    user_to_update = curp.get_course_user(db, course_id, user_id)
    if not user_to_update:
        raise NotFoundError("User {}".format(user_id))

    if new_args.user_type is not None:
        user_to_update.user_type = new_args.user_type
        
    if new_args.progress is not None:
        user_to_update.progress = new_args.progress
        if new_args.progress == float(100):
            user_to_update.aprobal_state = True

    if new_args.aprobal_state is not None:
        user_to_update.aprobal_state = new_args.aprobal_state
                
    curp.update_course_user(db)
    return CourseUserSerializer.serialize(user_to_update)