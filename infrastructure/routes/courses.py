from fastapi import APIRouter, HTTPException
#from domain.course_model import Course
from typing import List
from application.controllers.course_controller import *
from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from uuid import uuid4, UUID

courses = APIRouter()
crp = CourseRepositoryPostgres()

@courses.post('/', status_code = 201)
async def create_course(payload: Course):
    return await CourseController.create_course(payload)


@courses.get('/',response_model=List[Course], status_code = 200)
async def get_all_courses():
    return await CourseController.get_all_courses()


'''@courses.put('/{id}')
async def update_course(id: UUID, payload: Course):
    return await CourseController.update_course(id, payload)


@courses.delete('/{id}')
async def delete_course(id: int):
    course = await crp.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return await crp.delete_course(id)'''


@courses.delete('/')
async def delete_all_courses():
    return await crp.delete_all_courses()
