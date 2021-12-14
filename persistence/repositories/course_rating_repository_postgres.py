from infrastructure.db.course_rating_schema import CourseRating
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)


class CourseRatingRepositoryPostgres:
    def add_course_rating(self, db, payload):
        db.add(payload)
        db.commit()
        logger.info("New review added")
        logger.debug("Opinion of the new review: %s", payload.opinion)

    def get_all_course_ratings(self, db, course_id):
        course_rating_list = db.query(CourseRating).filter(CourseRating.course_id == course_id).all()
        logger.debug("Getting all ratings of course %s", course_id)
        return course_rating_list

    def get_course_rating(self, db, course_id, rating_id):
        rating = (
            db.query(CourseRating).filter(CourseRating.course_id == course_id).filter(CourseRating.id == rating_id).first()
        )
        logger.debug("Get rating %s of course %s", rating_id, course_id)
        return rating

    def get_course_rating_from(self, db, user_id, course_id):
        rating = (
            db.query(CourseRating).filter(CourseRating.course_id == course_id).filter(CourseRating.user_id == user_id).first()
        )
        logger.debug("Get rating of user %s in course %s", user_id, course_id)
        return rating

    def delete_course_rating(self, db, rating):
        db.delete(rating)
        db.commit()
        logger.debug("Delete rating with id %s", rating.id)
        logger.info("Rating deleted")
