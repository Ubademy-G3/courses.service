from sqlalchemy import func, or_
from infrastructure.db.course_schema import Course
import logging

logger = logging.getLogger(__name__)


class CourseRepositoryPostgres:
    def add_course(self, db, payload):
        db.add(payload)
        db.commit()

        logger.info("New course added")
        logger.debug("Name of the new course: %s", payload.name)

    def get_all_courses(self, db, category, subscription_type, text):

        partial_query = db.query(Course)

        if category is not None:
            logger.debug("Get courses with filter category %s", str(category))
            partial_query = partial_query.filter(Course.category.in_(category))

        if subscription_type is not None:
            logger.debug("Get courses with filter subscription_type %s", subscription_type)
            subscription_lower = [subs.lower() for subs in subscription_type]
            partial_query = partial_query.filter(Course.subscription_type.in_(subscription_lower))

        if text is not None:
            logger.debug("Get courses with filter text %s", text)
            partial_query = partial_query.filter(
                or_(func.lower(Course.name).contains(text.lower()), func.lower(Course.description).contains(text.lower()))
            )

        courses_list = partial_query.all()
        logger.debug("Getting all courses")
        return courses_list

    def get_course_by_id(self, db, course_id):
        course = db.query(Course).get(course_id)
        logger.debug("Get course with id %s", course_id)
        return course

    def update_course(self, db):
        db.commit()

    def delete_course(self, db, course):
        db.delete(course)
        db.commit()
        logger.debug("Delete course with id %s", course.id)
        logger.info("Course deleted")
