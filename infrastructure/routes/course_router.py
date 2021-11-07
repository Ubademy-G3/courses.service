from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.course_controller import *
from uuid import uuid4, UUID

router = APIRouter()

@router.post('/',response_model = Course, status_code = 201)
async def create_course(payload: CourseSchema):
    return await CourseController.create_course(payload)


@router.get('/',response_model = List[Course], status_code = 200)
async def get_all_courses():
    return await CourseController.get_all_courses()


@router.get('/{course_id}', response_model = Course, status_code = 200)
async def get_course(course_id: str):
    return await CourseController.get_course(course_id)


@router.patch('/{course_id}', response_model = Course, status_code = 200)
async def update_course(course_id: str, course: CoursePatch):
    return await CourseController.update_course(course_id, course)


@router.delete('/{id}')
async def delete_course(id: str):
    return await CourseController.delete_course_by_id(id)

