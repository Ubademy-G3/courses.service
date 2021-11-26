from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_user_controller import *
from application.services.auth import auth_service
from domain.course_user_model import *

router = APIRouter()

@router.get('/', response_model = dict, status_code = 201)
async def get_all_user_courses(
                                user_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None),
                                aprobal_state: Optional[bool] = None,
                                user_type: Optional[str] = None
                            ):

    auth_service.check_api_key(apikey)
    user_courses_list = CourseUserController.get_all_user_courses(db, user_id, aprobal_state, user_type)
    return {
        "amount": len(user_courses_list),
        "user_id": user_id,
        "courses": user_courses_list
    }