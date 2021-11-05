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


@router.get('/{media_id}', response_model = CourseMediaDB, status_code=200)
async def get_course_media(course_id: str, media_id: str):
    return await CourseMediaController.get_course_media(course_id, media_id)
    

@router.delete('/{media_id}', response_model = str, status_code=200)
async def delete_course_media(course_id: str, media_id: str):    
    course_deleted = await CourseMediaController.delete_course_media(course_id, media_id)
    return "The media {} was deleted successfully".format(media_id)
