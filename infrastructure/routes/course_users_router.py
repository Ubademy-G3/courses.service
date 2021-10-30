from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.course_user_controller import *

router = APIRouter()

@router.post('/', status_code = 201)
async def create_course_user(payload: CourseUser):
    return await CourseUserController.create_course_user(payload)

@router.get('/',response_model=List[CourseUser], status_code = 200)
async def get_all_course_users():
    return await CourseUserController.get_all_courses_users()

@router.delete('/{id}')
async def delete_course_user(id: str):
    return await CourseUserController.delete_course_user_by_id(id)

@router.delete('/')
async def delete_all_course_users():
    return await CourseUserController.delete_all_course_users()