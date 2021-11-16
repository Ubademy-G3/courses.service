from fastapi import APIRouter, Header
from typing import Optional
from application.controllers.course_category_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model = CourseCategoryDB, status_code = 201)
async def create_category(
                            payload: CourseCategory,
                            apikey: Optional[str] = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return await CourseCategoryController.create_category(payload)


@router.get('/{category_id}', response_model = CourseCategoryDB, status_code = 200)
async def get_category(
                        category_id: int,
                        apikey: Optional[str] = Header(None)                        
                    ):

    auth_service.check_api_key(apikey)
    return await CourseCategoryController.get_course_category(category_id)


@router.delete('/{category_id}', response_model = dict, status_code = 200)
async def delete_category(
                            category_id: int,
                            apikey: Optional[str] = Header(None)                            
                        ):

    auth_service.check_api_key(apikey)
    await CourseCategoryController.delete_course_category(category_id)
    return {
        "message": "The category {} was deleted successfully".format(category_id)
        }