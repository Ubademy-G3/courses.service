from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from errors.http_error import NotFoundError
curp = CourseUserRepositoryPostgres()

async def get_all_course_users(course_id):

    users_list = await curp.get_all_course_users(course_id)
    if users_list is None or len(users_list) == 0:
        raise NotFoundError("Users")
    return users_list


async def get_course_user(course_id, user_id):

    user = await curp.get_course_user(course_id, user_id)
    if user is None:
        raise NotFoundError("User {} in course {}".format(user_id,course_id))
    return user


async def course_already_acquired(course_id, user_id):

    return await curp.get_course_user(course_id, user_id) != None