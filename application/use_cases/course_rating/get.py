from persistence.repositories.course_rating_repository_postgres import CourseRatingRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_rating_serializer import CourseRatingSerializer
import logging

logger = logging.getLogger(__name__)

crrp = CourseRatingRepositoryPostgres()


def get_all_course_ratings(db, course_id):

    ratings = crrp.get_all_course_ratings(db, course_id)
    if ratings is None or len(ratings) == 0:
        logger.warning("Ratings of course %s not found", course_id)
        return []
    ratings_list = []
    for rating in ratings:
        ratings_list.append(CourseRatingSerializer.serialize(rating))
    return ratings_list


def get_course_rating(db, course_id, rating_id):

    rating = crrp.get_course_rating(db, course_id, rating_id)
    if rating is None:
        logger.warning("Rating %s not found in course %s", rating_id, course_id)
        raise NotFoundError("Rating {}".format(rating_id))
    return CourseRatingSerializer.serialize(rating)


def course_already_scored(db, course_id, user_id):

    return crrp.get_course_rating_from(db, user_id, course_id) != None
