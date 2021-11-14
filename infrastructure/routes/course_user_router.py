from fastapi import APIRouter, Header
from typing import List, Dict, Optional
from application.controllers.course_user_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model = CourseUserDB, status_code = 201)
async def create_course_user(
                            payload: CourseUserSchema,
                            course_id: str,
                            api_key: Optional[str] = Header(None)
                        ):

    auth_service.check_api_key(api_key)
    return await CourseUserController.create_course_user(payload, course_id)
    

@router.get('/',response_model = Dict, status_code = 200)
async def get_all_course_users(
                                course_id: str,
                                api_key: Optional[str] = Header(None),
                                user_type: Optional[str] = None
                            ):

    auth_service.check_api_key(api_key)                       
    course_users_list = await CourseUserController.get_all_course_users(course_id, user_type)
    return {"amount": len(course_users_list),
            "course_id": course_id,
            "users": course_users_list}


@router.patch('/{user_id}', response_model = CourseUserDB, status_code = 200)
async def update_course_user(
                        course_id: str,
                        user_id: str,
                        user: CourseUserPatch,
                        api_key: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(api_key)
    return await CourseUserController.update_course_user(course_id, user_id, user)


@router.delete('/{user_id}', response_model = str, status_code = 200)
async def delete_course_user(
                            course_id: str,
                            user_id: str,
                            api_key: Optional[str] = Header(None)
                        ):

    auth_service.check_api_key(api_key)                    
    user_deleted = await CourseUserController.delete_course_user(course_id, user_id)
    return "The user {} was deleted successfully".format(user_id)
