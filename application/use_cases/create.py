from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()

async def add_course(course):
    return await crp.add_course(course)

async def add_course_media(course_media):
    return await cmrp.add_course_media(course_media)