from fastapi import APIRouter, HTTPException
from typing import List,Dict
from application.controllers.course_user_controller import *

router = APIRouter()

@router.post('/', response_model = CourseUserDB, status_code = 201)
async def create_course_user(payload: CourseUserSchema, course_id: str):
    return await CourseUserController.create_course_user(payload, course_id)
    

@router.get('/',response_model = Dict, status_code = 200)
async def get_all_course_users(course_id: str):
    course_users_list = await CourseUserController.get_all_course_users(course_id)
    return {"amount": len(course_users_list),
            "course_id": course_id,
            "users": course_users_list}


@router.delete('/{user_id}', response_model = str, status_code = 200)
async def delete_course_user(course_id: str, user_id: str):
    user_deleted = await CourseUserController.delete_course_user(course_id, user_id)
    return "The user {} was deleted successfully".format(user_id)
