from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import get_db
from sqlalchemy.orm import Session
from application.controllers.course_user_controller import *
from application.services.auth import auth_service
from domain.course_user_model import *

router = APIRouter()

@router.post('/', response_model = CourseUserDB, status_code = 201)
async def create_course_user(
                            payload: CourseUserSchema,
                            course_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return CourseUserController.create_course_user(db, payload, course_id)
    

@router.get('/',response_model = CourseUserList, status_code = 200)
async def get_all_course_users(
                                course_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None),
                                user_type: Optional[str] = None
                            ):

    auth_service.check_api_key(apikey)                       
    course_users_list = CourseUserController.get_all_course_users(db, course_id, user_type)
    return {"amount": len(course_users_list),
            "course_id": course_id,
            "users": course_users_list}


@router.patch('/{user_id}', response_model = CourseUserDB, status_code = 200)
async def update_course_user(
                        course_id: str,
                        user_id: str,
                        user: CourseUserPatch,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return CourseUserController.update_course_user(db, course_id, user_id, user)


@router.delete('/{user_id}', response_model = dict, status_code = 200)
async def delete_course_user(
                            course_id: str,
                            user_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)                    
    user_deleted = CourseUserController.delete_course_user(db, course_id, user_id)
    return {
        "message": "The user {} was deleted successfully".format(user_id)
    }
