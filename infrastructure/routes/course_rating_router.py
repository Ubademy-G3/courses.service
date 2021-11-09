from fastapi import APIRouter
from typing import List, Dict
from application.controllers.course_rating_controller import *

router = APIRouter()

@router.post('/', response_model = CourseRating, status_code = 201)
async def add_course_rating(payload: CourseRatingSchema, course_id: str):
    return await CourseRatingController.create_course_rating(payload, course_id)


@router.get('/', response_model = Dict, status_code = 200)
async def get_all_course_ratings(course_id: str):
    course_ratings = await CourseRatingController.get_all_course_ratings(course_id)
    return {
        "amount": len(course_ratings),
        "course_id": course_id,
        "reviews": course_ratings
    }


@router.delete('/{rating_id}', response_model = str, status_code = 200)
async def delete_course_rating(course_id: str, rating_id: str):
    rating_deleted = await CourseRatingController.delete_course_rating(course_id, rating_id)
    return "The review {} was deleted successfully".format(rating_id)