from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()
curp = CourseUserRepositoryPostgres()

async def get_all_courses():
    return await crp.get_all_courses()

async def get_course_by_id(id):
    return await crp.get_course_by_id(id)


def get_all_course_media(course_id):
    return cmrp.get_all_course_media(course_id)

async def get_course_media_by_id(id):
    return await cmrp.get_course_media_by_id(id)


async def get_all_course_users():
    return await curp.get_all_course_users()

async def get_course_user_by_id(id):
    return await curp.get_course_user_by_id(id)