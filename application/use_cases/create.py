from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()
curp = CourseUserRepositoryPostgres()

async def add_course(course):
    return await crp.add_course(course)

async def add_course_media(course_media):
    return await cmrp.add_course_media(course_media)

async def add_course_user(course_user):
    return await curp.add_course_user(course_user)