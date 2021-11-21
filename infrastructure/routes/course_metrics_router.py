from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_user_controller import *
from application.services.auth import auth_service
from domain.course_user_model import *

router = APIRouter()

@router.get('/', response_model = dict, status_code = 201)
async def get_course_metrics(
                                course_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    course_metrics = CourseUserController.get_course_metrics(db, course_id)
    return {
        "course_id": course_id,
        "metrics": course_metrics
    }