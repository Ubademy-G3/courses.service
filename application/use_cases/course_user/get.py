from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_user_serializer import CourseUserSerializer

curp = CourseUserRepositoryPostgres()

def get_all_course_users(db, course_id, user_type):

    users = curp.get_all_course_users(db, course_id, user_type)
    if users is None or len(users) == 0:
        raise NotFoundError("Users")
    users_list = []
    for user in users:
        users_list.append(CourseUserSerializer.serialize(user))
    return users_list


def get_all_user_courses(db, user_id, aprobal_state, user_type):

    courses = curp.get_all_user_courses(db, user_id, aprobal_state, user_type)
    if courses is None or len(courses) == 0:
        raise NotFoundError("Courses of user {}".format(user_id))
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
        raise NotFoundError("User {} in course {}".format(user_id,course_id))
    return CourseUserSerializer.serialize(user)


def course_already_acquired(db, course_id, user_id):

    return curp.get_course_user(db, course_id, user_id) != None