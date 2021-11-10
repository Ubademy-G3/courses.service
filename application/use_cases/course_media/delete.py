from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from errors.http_error import NotFoundError

cmrp = CourseMediaRepositoryPostgres()


async def delete_course_media(course_id, media_id):
    course_media = await cmrp.get_course_media(course_id, media_id)
    if not course_media:
        raise NotFoundError("Media {} in course {}".format(media_id,course_id))
    return await cmrp.delete_course_media(course_id, media_id)