from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_rating_controller import *
from application.services.auth import auth_service
from domain.course_rating_model import *

router = APIRouter()

@router.post('/', response_model = CourseRatingDB, status_code = 201)
async def add_course_rating(
                            payload: CourseRatingSchema,
                            course_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return CourseRatingController.create_course_rating(db, payload, course_id)


@router.get('/', response_model = CourseRatingList, status_code = 200)
async def get_all_course_ratings(
                                course_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    course_ratings = CourseRatingController.get_all_course_ratings(db, course_id)
    
    avg = 0
    if len(course_ratings) != 0:
        for rating in course_ratings:
            avg += rating["score"]
        avg /= len(course_ratings)  
    
    return {
        "amount": len(course_ratings),
        "course_id": course_id,
        "rating": avg,
        "reviews": course_ratings
    }


@router.delete('/{rating_id}', response_model = dict, status_code = 200)
async def delete_course_rating(
                                course_id: str,
                                rating_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    rating_deleted = CourseRatingController.delete_course_rating(db, course_id, rating_id)
    return {
        "message": "The review {} was deleted successfully".format(rating_id)
    }