from fastapi import HTTPException
from domain.course_media_model import *
from application.serializers.course_media_serializer import CourseMediaSerializer
from application.use_cases.create import *
from application.use_cases.get import *
from application.use_cases.update import *
from application.use_cases.delete import *

class CourseMediaController:
    @classmethod
    async def create_course_media(self,args,course_id):

        new_course_media = CourseMedia(
            course_id = course_id,
            url = args.url
        )
        await add_course_media(new_course_media)
        return CourseMediaSerializer.serialize(new_course_media)

    @classmethod
    def get_all_course_media(self, course_id):
        course_media_list = get_all_course_media(course_id)
        return course_media_list
       

    @classmethod
    def delete_course_media_by_id(self, media_id):
        return delete_course_media_by_id(media_id)
