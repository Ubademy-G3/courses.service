from application.use_cases.course_category import (create, get, delete)
from domain.course_category_model import *

class CourseCategoryController:

    @classmethod
    async def create_category(self, args):
        
        return await create.add_course_category(args)

    
    @classmethod
    async def get_course_category(self, category_id):

        return await get.get_course_category(category_id)


    @classmethod
    async def delete_course_category(self, category_id):

        return await delete.delete_course_category(category_id)