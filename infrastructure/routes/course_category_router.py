from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_category_controller import *
from application.services.auth import auth_service
from domain.course_category_model import *
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=CourseCategorySchema, status_code=201)
async def create_category(payload: CourseCategorySchema, db: Session = Depends(get_db), apikey: str = Header(None)):

    logger.debug("Creating category...")
    auth_service.check_api_key(apikey)
    return CourseCategoryController.create_category(db, payload)


@router.get("/{category_id}", response_model=CourseCategorySchema, status_code=200)
async def get_category(category_id: int, db: Session = Depends(get_db), apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    return CourseCategoryController.get_course_category(db, category_id)


@router.get("/", response_model=List[CourseCategorySchema], status_code=200)
async def get_all_categories(db: Session = Depends(get_db), apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    return CourseCategoryController.get_all_course_categories(db)


@router.delete("/{category_id}", response_model=dict, status_code=200)
async def delete_category(category_id: int, db: Session = Depends(get_db), apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    CourseCategoryController.delete_course_category(db, category_id)
    return {"message": "The category {} was deleted successfully".format(category_id)}
