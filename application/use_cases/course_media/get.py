from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_media_serializer import CourseMediaSerializer
import logging

logger = logging.getLogger(__name__)

cmrp = CourseMediaRepositoryPostgres()


def get_all_course_media(db, course_id):

    media = cmrp.get_all_course_media(db, course_id)
    media_list = []
    for m in media:
        media_list.append(CourseMediaSerializer.serialize(m))
    return media_list


def get_course_media(db, course_id, media_id):

    course_media = cmrp.get_course_media(db, course_id, media_id)
    if course_media is None:
        logger.warning("Media %s not found in course %s", media_id, course_id)
        raise NotFoundError("Media {}".format(media_id))
    return CourseMediaSerializer.serialize(course_media)


def get_all_module_media(db, module_id):

    media = cmrp.get_all_course_module_media(db, module_id)
    media_list = []
    for m in media:
        media_list.append(CourseMediaSerializer.serialize(m))
    return media_list
