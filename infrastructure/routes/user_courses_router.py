from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_user_controller import CourseUserController
from application.services.auth import auth_service
from typing import Optional

router = APIRouter()


@router.get("/", response_model=dict, status_code=201)
async def get_all_user_courses(
    user_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
    approval_state: Optional[bool] = None,
    user_type: Optional[str] = None,
):

    auth_service.check_api_key(apikey)
    user_courses_list = CourseUserController.get_all_user_courses(db, user_id, approval_state, user_type)
    return {"amount": len(user_courses_list), "user_id": user_id, "courses": user_courses_list}
