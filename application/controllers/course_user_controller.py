from domain.course_user_model import *
from application.use_cases.course_user import (create, get, update, delete)

class CourseUserController:
    @classmethod
    async def create_course_user(self, args, course_id):

        return await create.add_course_user(course_id, args)


    @classmethod
    def get_all_course_users(self, course_id, user_type):

        return get.get_all_course_users(course_id, user_type)


    @classmethod
    async def update_course_user(self, course_id, user_id, update_args):
       
        return await update.update_course_user(course_id, user_id, update_args)


    @classmethod
    async def delete_course_user(self, course_id, user_id):
        
        return await delete.delete_course_user(course_id, user_id)
