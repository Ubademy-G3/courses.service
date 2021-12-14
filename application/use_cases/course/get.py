from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_serializer import CourseSerializer
from application.use_cases.course_user.get import get_course_metrics
import logging

logger = logging.getLogger(__name__)

crp = CourseRepositoryPostgres()


def get_all_courses(db, category, subscription_type, text):

    courses = crp.get_all_courses(db, category, subscription_type, text)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        raise NotFoundError("Courses")
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        metrics = get_course_metrics(db, serial["id"])
        serial["metrics"] = metrics
        courses_list.append(serial)
    return courses_list


def get_course(db, course_id):

    course = crp.get_course_by_id(db, course_id)
    if course is None:
        logger.warning("Course %s not found", course_id)
        raise NotFoundError("Course {}".format(course_id))
    serial = CourseSerializer.serialize(course)
    serial["metrics"] = get_course_metrics(db, course_id)
    return serial


def course_exists(db, course_id):

    return crp.get_course_by_id(db, course_id) != None
