from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

cmrp = CourseMediaRepositoryPostgres()

async def update_course_media(id, new_args):
    return await cmrp.update_course_media(id, new_args)