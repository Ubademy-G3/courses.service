from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_module_controller import *
from application.services.auth import auth_service
from domain.course_module_model import *
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=CourseModuleList, status_code=200)
async def get_all_modules_by_course_id(course_id: str, db: Session = Depends(get_db), apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    course_module_list = CourseModuleController.get_all_modules_by_course_id(db, course_id)
    return {"amount": len(course_module_list), "course_id": course_id, "modules": course_module_list}
