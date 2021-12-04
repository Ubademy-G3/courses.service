from fastapi import APIRouter, Header, Query, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_controller import *
from application.services.auth import auth_service
from domain.course_model import *

router = APIRouter()

@router.post('/',response_model = CourseDB, status_code = 201)
async def create_course(
                        payload: CourseSchema,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return CourseController.create_course(db, payload)


@router.get('/',response_model = CourseList, status_code = 200)
async def get_all_courses(
                            db: Session = Depends(get_db),
                            apikey: str = Header(None),
                            category: Optional[List[int]] = Query(None, alias="category[]"),
                            subscription_type: Optional[List[str]] = Query(None, alias="subscription_type[]"),
                            text: Optional[str] = None
                        ):

    auth_service.check_api_key(apikey)
    courses_list = CourseController.get_all_courses(db, category, subscription_type, text)
    return {
        "amount": len(courses_list),
        "courses": courses_list
    }

@router.get('/{course_id}', response_model = CourseDB, status_code = 200)
async def get_course(
                    course_id: str,
                    db: Session = Depends(get_db),
                    apikey: str = Header(None)
                ):

    auth_service.check_api_key(apikey)
    return CourseController.get_course(db, course_id)


@router.patch('/{course_id}', response_model = CourseDB, status_code = 200)
async def update_course(
                        course_id: str,
                        course: CoursePatch,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return CourseController.update_course(db, course_id, course)


@router.delete('/{course_id}', response_model = dict, status_code = 200)
async def delete_course(
                        course_id: str,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    CourseController.delete_course(db, course_id)
    return {
        "message": "Course {} deleted successfully".format(course_id)
    }
