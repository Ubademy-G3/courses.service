from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from errors.http_error import NotFoundError

curp = CourseUserRepositoryPostgres()

async def delete_course_user(course_id, user_id):

    user = await curp.get_course_user(course_id, user_id)
    if not user:
        raise NotFoundError("User {} in Course {}".format(user_id,course_id))
    return await curp.delete_course_user(course_id, user_id)