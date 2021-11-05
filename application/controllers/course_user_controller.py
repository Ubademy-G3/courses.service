from fastapi import HTTPException
from domain.course_user_model import CourseUser
from application.serializers.course_user_serializer import CourseUserSerializer
from application.use_cases.course_user import (create, get, delete)

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
        await create.add_course_user(new_user)
        return CourseUserSerializer.serialize(new_user)

    @classmethod
    async def get_all_course_users(self):
        return await get.get_all_course_users()

    @classmethod
    async def delete_course_user_by_id(self, user_id):
        return await delete.delete_course_user_by_id(user_id)
        
    @classmethod
    async def delete_all_course_users(self):
        return await delete.delete_all_course_users()