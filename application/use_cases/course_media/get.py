from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from errors.http_error import NotFoundError

cmrp = CourseMediaRepositoryPostgres()

async def get_all_course_media(course_id):

    media_list = await cmrp.get_all_course_media(course_id)
    if media_list is None or len(media_list) == 0:
        raise NotFoundError("Media of course {}".format(course_id))
    return media_list
    

async def get_course_media(course_id, media_id):

    course_media = await cmrp.get_course_media(course_id, media_id)
    if course_media is None:
        raise NotFoundError("Media {}".format(media_id))
    return course_media