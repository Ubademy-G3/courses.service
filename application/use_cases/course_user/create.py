from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from infrastructure.db.course_user_schema import CourseUser
from exceptions.http_error import NotFoundError
from exceptions.ubademy_error import CourseAlreadyAcquired
from application.serializers.course_user_serializer import CourseUserSerializer
from application.use_cases.course.get import course_exists
from application.use_cases.course_user.get import course_already_acquired
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)

curp = CourseUserRepositoryPostgres()


def add_course_user(db, course_id, args):

    if not course_exists(db, course_id):
        logger.warning("Course %s not found", course_id)
        raise NotFoundError("Course {}".format(course_id))

    if course_already_acquired(db, course_id, args.user_id):
        logger.warning("Course %s already acquired by user %s", course_id, args.user_id)
        raise CourseAlreadyAcquired()

    new_user = CourseUser(
        id=uuid4(),
        course_id=course_id,
        user_id=args.user_id,
        user_type=args.user_type.lower(),
        progress=args.progress,
        approval_state=args.approval_state,
    )

    curp.add_course_user(db, new_user)
    return CourseUserSerializer.serialize(new_user)
