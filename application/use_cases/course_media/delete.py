from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from exceptions.http_error import NotFoundError

cmrp = CourseMediaRepositoryPostgres()

def delete_course_media(db, course_id, media_id):

    course_media = cmrp.get_course_media(db, course_id, media_id)
    if not course_media:
        raise NotFoundError("Media {} in course {}".format(media_id,course_id))
    cmrp.delete_course_media(db, course_media)