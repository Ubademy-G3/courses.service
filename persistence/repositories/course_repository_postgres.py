from sqlalchemy import func, or_
from infrastructure.db.course_schema import Course
from infrastructure.db.course_user_schema import CourseUser
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

    def get_all_courses_by_user(self, db, user_id, user_type, approval_state, category, subscription_type, text):
        logger.debug("Get courses with by user_id %s", str(user_id))
        partial_query = db.query(Course, CourseUser).filter(Course.id == CourseUser.course_id).filter(CourseUser.user_id == user_id)

        if user_type is not None:
            logger.debug("Get courses with filter user_type %s", str(user_type))
            partial_query = partial_query.filter(CourseUser.user_type == user_type.lower())

        if approval_state is not None:
            logger.debug("Get courses with filter approval_state %s", str(approval_state))
            partial_query = partial_query.filter(CourseUser.approval_state == approval_state)

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

        query_result = partial_query.all()
        courses_list = []
        for c, u in query_result:
            courses_list.append(c)
        logger.debug("Getting all courses by user")
        return courses_list

    def get_all_courses_from_list(self, db, course_list):

        courses_list = db.query(Course).filter(Course.id.in_(course_list)).all()
        logger.debug("Getting all courses from list")
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
