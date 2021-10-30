from fastapi import HTTPException
from domain.course_user_model import CourseUser
from application.serializers.course_user_serializer import CourseUserSerializer
from application.use_cases.create import add_course_user
from application.use_cases.get import (get_all_course_users,get_course_user_by_id)
from application.use_cases.delete import (delete_all_course_users,delete_course_user_by_id)

class CourseUserController:
    @classmethod
    async def create_course_user(self,args):

        new_user = CourseUser(
            id = args.id,
            course_id = args.course_id,
            user_type = args.user_type,
            progress = args.progress,
            aprobal_state = args.aprobal_state
        )
        await add_course_user(new_user)
        return CourseUserSerializer.serialize(new_user)

    @classmethod
    async def get_all_course_users(self):
        return await get_all_course_users()

    @classmethod
    async def delete_course_user_by_id(self, user_id):
        return await delete_course_user_by_id(user_id)
        
    @classmethod
    async def delete_all_course_users(self):
        return await delete_all_course_users()