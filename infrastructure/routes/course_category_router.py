from fastapi import APIRouter, Header, Depends
from typing import Optional
from infrastructure.db.database import Session, get_db
from application.controllers.course_category_controller import *
from application.services.auth import auth_service
from domain.course_category_model import *

router = APIRouter()

@router.post('/', response_model = CourseCategoryDB, status_code = 201)
async def create_category(
                            payload: CourseCategorySchema,
                            db: Session = Depends(get_db),
                            apikey: Optional[str] = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return CourseCategoryController.create_category(db, payload)


@router.get('/{category_id}', response_model = CourseCategoryDB, status_code = 200)
async def get_category(
                        category_id: int,
                        db: Session = Depends(get_db),
                        apikey: Optional[str] = Header(None)                        
                    ):

    auth_service.check_api_key(apikey)
    return CourseCategoryController.get_course_category(db, category_id)


@router.delete('/{category_id}', response_model = dict, status_code = 200)
async def delete_category(
                            category_id: int,
                            db: Session = Depends(get_db),
                            apikey: Optional[str] = Header(None)                            
                        ):

    auth_service.check_api_key(apikey)
    CourseCategoryController.delete_course_category(db, category_id)
    return {
        "message": "The category {} was deleted successfully".format(category_id)
        }