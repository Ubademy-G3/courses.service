from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.course_media_controller import *

router = APIRouter()

@router.post('/', response_model=CourseMediaDB, status_code = 201)
async def create_course_media(payload: CourseMediaSchema, course_id: str):

    return await CourseMediaController.create_course_media(payload, course_id)


@router.get('/', response_model=CourseMediaList, status_code = 200)
async def get_all_course_media(course_id: str):

    course_media_list = await CourseMediaController.get_all_course_media(course_id)
    return {"amount": len(course_media_list),
            "course_id": course_id,
            "course_media": course_media_list}    


@router.delete('/{id}')
async def delete_course_media(id: str):
    
    return await CourseMediaController.delete_course_media_by_id(id)

