from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_user_serializer import CourseUserSerializer
from application.use_cases.course_certificate.create import add_course_certificate
import logging

logger = logging.getLogger(__name__)

curp = CourseUserRepositoryPostgres()


def update_course_user(db, course_id, user_id, new_args, username):

    user_to_update = curp.get_course_user(db, course_id, user_id)
    if not user_to_update:
        raise NotFoundError("User {}".format(user_id))

    if new_args.user_type is not None:
        user_to_update.user_type = new_args.user_type

    if new_args.progress is not None:
        user_to_update.progress = new_args.progress
        if new_args.progress == float(100):
            user_to_update.approval_state = True
            add_course_certificate(db, course_id, user_id, username)

    if new_args.approval_state is not None:
        user_to_update.approval_state = new_args.approval_state

    logger.debug("Update user %s in course %s", user_id, course_id)
    curp.update_course_user(db)
    logger.info("User updated")
    return CourseUserSerializer.serialize(user_to_update)
