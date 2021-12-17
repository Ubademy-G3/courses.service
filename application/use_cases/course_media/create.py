from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from infrastructure.db.course_media_schema import CourseMedia
from application.serializers.course_media_serializer import CourseMediaSerializer
from uuid import uuid4
from exceptions.http_error import NotFoundError
from application.use_cases.course_module import get as module_get

cmrp = CourseMediaRepositoryPostgres()


def add_course_media(db, course_id, args):

    new_course_media = CourseMedia(id=uuid4(), course_id=course_id, module_id=args.module_id, url=args.url)

    module = module_get.get_module(db, args.module_id)
    if not module:
        raise NotFoundError("Module")

    cmrp.add_course_media(db, new_course_media)
    return CourseMediaSerializer.serialize(new_course_media)
