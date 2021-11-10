from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from errors.http_error import NotFoundError

crp = CourseRepositoryPostgres()

async def delete_all_courses():

    return await crp.delete_all_courses()

async def delete_course(course_id):

    course = await crp.get_course(course_id)
    if not course:
        raise NotFoundError("Course {}".format(id))
    return await crp.delete_course(course_id)