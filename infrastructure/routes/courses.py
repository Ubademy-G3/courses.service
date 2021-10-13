from fastapi import APIRouter
from domain.course_model import Course
from typing import List
from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

# fake_course_db = [
#     {
#         'id': 123,
#         'name': 'Algebra II' 
#     }
# ]

courses = APIRouter()
crp = CourseRepositoryPostgres()
# @courses.get('/', response_model=List[Course])
# async def index():
#     return fake_course_db

@courses.post('/', status_code=201)
async def add_course(payload: Course):
    course_id = await crp.add_course(payload)
    response = {
        'id': course_id,
        **payload.dict()
    }
    return response