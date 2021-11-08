from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from domain.course_media_model import *
from application.serializers.course_media_serializer import CourseMediaSerializer

cmrp = CourseMediaRepositoryPostgres()

async def add_course_media(course_id, args):

    new_course_media = CourseMedia(
        course_id = course_id,
        url = args.url
    )
    await cmrp.add_course_media(new_course_media)
    return CourseMediaSerializer.serialize(new_course_media)