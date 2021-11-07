from application.use_cases.course import (create,delete,get,update)
from domain.course_model import *

class CourseController:
    @classmethod
    async def create_course(self,args):

        return await create.add_course(args)

    @classmethod
    async def get_all_courses(self):

        return await get.get_all_courses()

    @classmethod
    async def get_course(self, course_id):

        return await get.get_course(course_id)

    @classmethod
    async def update_course(self, course_id, update_args):
       
        return await update.update_course(course_id, update_args)

    @classmethod
    async def delete_course(self, course_id):

        return await delete.delete_course(course_id)
        
    @classmethod
    async def delete_all_courses(self):
        
        return await delete.delete_all_courses()