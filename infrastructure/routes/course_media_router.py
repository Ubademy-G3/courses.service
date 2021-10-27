from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.course_media_controller import *
from uuid import uuid4, UUID

router = APIRouter()

@router.post('/', status_code = 201)
async def create_course_media(payload: CourseMedia):
    return await CourseMediaController.create_course_media(payload)


@router.get('/',response_model=List[CourseMedia], status_code = 200)
async def get_all_courses_media():
    return await CourseMediaController.get_all_courses_media()


@router.patch('/{id}', response_model = CourseMedia, status_code = 200)
async def update_course_media(id: str, media: CourseMedia):
    return await CourseMediaController.update_course_media(id, media)


@router.delete('/{id}')
async def delete_course_media(id: str):
    return await CourseMediaController.delete_course_media_by_id(id)


@router.delete('/')
async def delete_all_courses_media():
    return await CourseMediaController.delete_all_courses_media()