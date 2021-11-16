from fastapi import APIRouter, Header
from typing import List, Dict, Optional
from application.controllers.course_rating_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model = CourseRating, status_code = 201)
async def add_course_rating(
                            payload: CourseRatingSchema,
                            course_id: str,
                            apikey: Optional[str] = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return await CourseRatingController.create_course_rating(payload, course_id)


@router.get('/', response_model = Dict, status_code = 200)
async def get_all_course_ratings(
                                course_id: str,
                                apikey: Optional[str] = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    course_ratings = await CourseRatingController.get_all_course_ratings(course_id)
    
    avg = 0
    for rating in course_ratings:
        avg += rating["score"]
    avg /= len(course_ratings)  
    
    return {
        "amount": len(course_ratings),
        "course_id": course_id,
        "rating": avg,
        "reviews": course_ratings
    }


@router.delete('/{rating_id}', response_model = str, status_code = 200)
async def delete_course_rating(
                                course_id: str,
                                rating_id: str,
                                apikey: Optional[str] = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    rating_deleted = await CourseRatingController.delete_course_rating(course_id, rating_id)
    return "The review {} was deleted successfully".format(rating_id)