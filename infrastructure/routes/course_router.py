from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.course_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/',response_model = Course, status_code = 201)
async def create_course(
                        payload: CourseSchema,
                        authorization: Optional[str] = Header(None)
                    ):
    auth_service.check_api_key(authorization)
    return await CourseController.create_course(payload)


@router.get('/',response_model = List[Course], status_code = 200)
async def get_all_courses(
                            authorization: Optional[str] = Header(None)
                        ):
    auth_service.check_api_key(authorization)
    return await CourseController.get_all_courses()


@router.get('/{course_id}', response_model = Course, status_code = 200)
async def get_course(
                    course_id: str,
                    authorization: Optional[str] = Header(None)
                ):

    auth_service.check_api_key(authorization)
    return await CourseController.get_course(course_id)


@router.patch('/{course_id}', response_model = Course, status_code = 200)
async def update_course(
                        course_id: str,
                        course: CoursePatch,
                        authorization: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(authorization)
    return await CourseController.update_course(course_id, course)


@router.delete('/{course_id}')
async def delete_course(
                        course_id: str,
                        authorization: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(authorization)
    return await CourseController.delete_course(course_id)
