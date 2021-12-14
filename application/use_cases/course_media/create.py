from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from infrastructure.db.course_media_schema import CourseMedia
from application.serializers.course_media_serializer import CourseMediaSerializer
from uuid import uuid4

cmrp = CourseMediaRepositoryPostgres()


def add_course_media(db, course_id, args):

    new_course_media = CourseMedia(id=uuid4(), course_id=course_id, module_id=args.module_id, url=args.url)

    cmrp.add_course_media(db, new_course_media)
    return CourseMediaSerializer.serialize(new_course_media)
