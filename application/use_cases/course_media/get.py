from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

cmrp = CourseMediaRepositoryPostgres()

def get_all_course_media(course_id):
    return cmrp.get_all_course_media(course_id)

async def get_course_media(course_id, media_id):
    return await cmrp.get_course_media(course_id, media_id)