from fastapi import HTTPException
from domain.course_media_model import *
from application.serializers.course_media_serializer import CourseMediaSerializer
from application.use_cases.course_media import (create, get, delete)

class CourseMediaController:
    @classmethod
    async def create_course_media(self,args,course_id):

        new_course_media = CourseMedia(
            course_id = course_id,
            url = args.url
        )
        await create.add_course_media(new_course_media)
        return CourseMediaSerializer.serialize(new_course_media)


    @classmethod
    def get_all_course_media(self, course_id):
        return get.get_all_course_media(course_id)


    @classmethod
    def get_course_media(self, course_id, media_id):
        return get.get_course_media(course_id, media_id)


    @classmethod
    def delete_course_media(self, course_id, media_id):
        return delete.delete_course_media(course_id, media_id)
