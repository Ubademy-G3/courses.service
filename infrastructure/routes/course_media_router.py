from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from typing import List
from application.controllers.course_media_controller import *
from application.services.auth import auth_service
from domain.course_media_model import *
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/', response_model = CourseMediaDB, status_code = 201)
async def create_course_media(
                            payload: CourseMediaSchema,
                            course_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    logger.debug("Adding media in course %s ...", course_id)
    auth_service.check_api_key(apikey)
    return CourseMediaController.create_course_media(db, payload, course_id)


@router.get('/', response_model = CourseMediaList, status_code = 200)
async def get_all_course_media(
                            course_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    course_media_list = CourseMediaController.get_all_course_media(db, course_id)
    return {"amount": len(course_media_list),
            "course_id": course_id,
            "course_media": course_media_list}    


@router.get('/{media_id}', response_model = CourseMediaDB, status_code = 200)
async def get_course_media(
                            course_id: str,
                            media_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return CourseMediaController.get_course_media(db, course_id, media_id)
    

@router.get('/module/{module_id}', response_model = CourseMediaByModuleList, status_code = 200)
async def get_all_module_media(
                            course_id: str,
                            module_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    lis = CourseMediaController.get_all_module_media(db, module_id)
    return {
        "amount": len(lis),
        "module_id": module_id,
        "course_media": lis
    }
    

@router.delete('/{media_id}', response_model = dict, status_code = 200)
async def delete_course_media(
                                course_id: str,
                                media_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):    
                            
    auth_service.check_api_key(apikey)                    
    course_deleted = CourseMediaController.delete_course_media(db, course_id, media_id)
    return {
        "message": "The media {} was deleted successfully".format(media_id)
    }
