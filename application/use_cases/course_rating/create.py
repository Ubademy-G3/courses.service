from persistence.repositories.course_rating_repository_postgres import CourseRatingRepositoryPostgres
from exceptions.http_error import NotFoundError
from exceptions.ubademy_error import CourseAlreadyScored
from exceptions.ubademy_error import CourseNotAcquired
from infrastructure.db.course_rating_schema import CourseRating
from application.serializers.course_rating_serializer import CourseRatingSerializer
from application.use_cases.course.get import course_exists
from application.use_cases.course_user.get import course_already_acquired
from application.use_cases.course_rating.get import course_already_scored
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)

crrp = CourseRatingRepositoryPostgres()

def add_course_rating(db, course_id, args):

    if not course_exists(db, course_id):
        logger.warning("Course %s not found", course_id)
        raise NotFoundError("Course {}".format(course_id))

    if not course_already_acquired(db, course_id, args.user_id):
        logger.warning("Course %s already acquired by user %s", course_id, args.user_id)
        raise CourseNotAcquired()

    if course_already_scored(db, course_id, args.user_id):
        logger.warning("Course %s already scored by user %s", course_id, args.user_id)
        raise CourseAlreadyScored()

    new_course_rating = CourseRating(
        id = uuid4(),
        course_id = course_id,
        user_id = args.user_id,
        score = args.score,
        opinion = args.opinion
    )
    
    crrp.add_course_rating(db, new_course_rating)
    return CourseRatingSerializer.serialize(new_course_rating)