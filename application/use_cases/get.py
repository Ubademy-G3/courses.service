from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()

async def get_all_courses():
    return await crp.get_all_courses()

async def get_course_by_id(id):
    return await crp.get_course_by_id(id)

async def get_all_courses_media():
    return await cmrp.get_all_courses_media()

async def get_course_media_by_id(id):
    return await cmrp.get_course_media_by_id(id)