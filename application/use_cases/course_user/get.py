from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_user_serializer import CourseUserSerializer
import logging

logger = logging.getLogger(__name__)

curp = CourseUserRepositoryPostgres()

def get_all_course_users(db, course_id, user_type):

    users = curp.get_all_course_users(db, course_id, user_type)
    if users is None or len(users) == 0:
        logger.warning("Users not found in course %s", course_id)
        return []
    users_list = []
    for user in users:
        users_list.append(CourseUserSerializer.serialize(user))
    return users_list


def get_all_user_courses(db, user_id, approval_state, user_type):

    courses = curp.get_all_user_courses(db, user_id, approval_state, user_type)
    if courses is None or len(courses) == 0:
        logger.warning("Courses of user %s not found", user_id)
        return []
    courses_list = []
    for user in courses:
        dicty = CourseUserSerializer.serialize(user)
        del dicty['id']
        del dicty['user_id']
        courses_list.append(dicty)
    return courses_list


def get_course_user(db, course_id, user_id):

    user = curp.get_course_user(db, course_id, user_id)
    if user is None:
        logger.warning("User %s not found in %s", user_id, course_id)
        raise NotFoundError("User {} in course {}".format(user_id,course_id))
    return CourseUserSerializer.serialize(user)


def course_already_acquired(db, course_id, user_id):

    return curp.get_course_user(db, course_id, user_id) != None


def get_course_metrics(db, course_id):

    return curp.get_course_metrics(db, course_id)
