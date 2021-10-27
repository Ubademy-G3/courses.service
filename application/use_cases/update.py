from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()

async def update_course(id, new_args):
    return await crp.update_course(id, new_args)

async def update_course_media(id, new_args):
    return await cmrp.update_course_media(id, new_args)