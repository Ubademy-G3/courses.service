from fastapi import APIRouter, HTTPException
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

@courses.get('/',response_model=List[Course])
async def index():
    return await crp.get_all_courses()


@courses.put('/{id}')
async def update_course(id: int, payload: Course):
    course = await crp.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    update_data = payload.dict(exclude_unset=True)
    course_in_db = Course(**course)

    updated_course = course_in_db.copy(update=update_data)
    return await crp.update_course(id, updated_course)

@courses.delete('/{id}')
async def delete_course(id: int):
    course = await crp.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code = 404, detail="Course not found")
    return await crp.delete_course(id)

@courses.delete('/')
async def delete_all_courses():
    return await crp.delete_all_courses()