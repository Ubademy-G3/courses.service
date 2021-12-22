from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_serializer import CourseSerializer
from application.use_cases.course_user.get import get_course_metrics
import logging
from application.use_cases.course_rating.get import get_all_course_ratings

logger = logging.getLogger(__name__)

crp = CourseRepositoryPostgres()


def get_all_courses(db, category, subscription_type, text):

    courses = crp.get_all_courses(db, category, subscription_type, text)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        return []
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        metrics = get_course_metrics(db, serial["id"])
        serial["metrics"] = metrics
        courses_list.append(serial)
    return courses_list


def get_all_courses_with_rating(db, category, subscription_type, text):

    courses = crp.get_all_courses(db, category, subscription_type, text)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        return []
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        serial["metrics"] = get_course_metrics(db, serial["id"])
        course_rating_list = get_all_course_ratings(db, serial["id"])
        avg = 0
        rating_amount = len(course_rating_list)
        if rating_amount != 0:
            for rating in course_rating_list:
                avg += rating["score"]
            avg /= rating_amount
        serial["rating_avg"] = avg
        serial["rating_amount"] = rating_amount
        courses_list.append(serial)
    return courses_list


def get_all_courses_by_user_with_rating(db, user_id, user_type, approval_state, category, subscription_type, text):

    courses = crp.get_all_courses_by_user(db, user_id, user_type, approval_state, category, subscription_type, text)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        return []
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        serial["metrics"] = get_course_metrics(db, serial["id"])
        course_rating_list = get_all_course_ratings(db, serial["id"])
        avg = 0
        rating_amount = len(course_rating_list)
        if rating_amount != 0:
            for rating in course_rating_list:
                avg += rating["score"]
            avg /= rating_amount
        serial["rating_avg"] = avg
        serial["rating_amount"] = rating_amount
        courses_list.append(serial)
    return courses_list


def get_all_courses_from_list(db, course_list):

    courses = crp.get_all_courses_from_list(db, course_list)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        return []
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        metrics = get_course_metrics(db, serial["id"])
        serial["metrics"] = metrics
        courses_list.append(serial)
    return courses_list


def get_all_courses_from_list_with_rating(db, course_list):

    courses = crp.get_all_courses_from_list(db, course_list)
    if courses is None or len(courses) == 0:
        logger.warning("Courses not found")
        return []
    courses_list = []
    for course in courses:
        serial = CourseSerializer.serialize(course)
        serial["metrics"] = get_course_metrics(db, serial["id"])
        course_rating_list = get_all_course_ratings(db, serial["id"])
        avg = 0
        rating_amount = len(course_rating_list)
        if rating_amount != 0:
            for rating in course_rating_list:
                avg += rating["score"]
            avg /= rating_amount
        serial["rating_avg"] = avg
        serial["rating_amount"] = rating_amount
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


def get_course_with_rating(db, course_id):

    course = crp.get_course_by_id(db, course_id)
    if course is None:
        logger.warning("Course %s not found", course_id)
        raise NotFoundError("Course {}".format(course_id))
    serial = CourseSerializer.serialize(course)
    serial["metrics"] = get_course_metrics(db, course_id)
    course_rating_list = get_all_course_ratings(db, course_id)
    avg = 0
    rating_amount = len(course_rating_list)
    if rating_amount != 0:
        for rating in course_rating_list:
            avg += rating["score"]
        avg /= rating_amount
    serial["rating_avg"] = avg
    serial["rating_amount"] = rating_amount
    return serial


def course_exists(db, course_id):

    return crp.get_course_by_id(db, course_id) is not None
