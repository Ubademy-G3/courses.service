from application.use_cases.course_media import (create, get, delete)
from domain.course_media_model import *

class CourseMediaController:
    @classmethod
    async def create_course_media(self, args, course_id):

        return await create.add_course_media(course_id, args)


    @classmethod
    def get_all_course_media(self, course_id):

        return get.get_all_course_media(course_id)


    @classmethod
    def get_course_media(self, course_id, media_id):

        return get.get_course_media(course_id, media_id)


    @classmethod
    def delete_course_media(self, course_id, media_id):
        
        return delete.delete_course_media(course_id, media_id)
