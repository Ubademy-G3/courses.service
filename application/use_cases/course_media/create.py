from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

cmrp = CourseMediaRepositoryPostgres()

async def add_course_media(course_media):
    return await cmrp.add_course_media(course_media)