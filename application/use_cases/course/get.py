from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from errors.http_error import NotFoundError

crp = CourseRepositoryPostgres()

async def get_all_courses(category, subscription_type):

    courses = await crp.get_all_courses(category, subscription_type)
    if courses is None or len(courses) == 0:
        raise NotFoundError("Courses")
    return courses


async def get_course(course_id):

    course = await crp.get_course_by_id(course_id)
    if course is None:
        raise NotFoundError("Course {}".format(course_id))
    return course
    

async def course_exists(course_id):

    return await crp.get_course_by_id(course_id) != None
    