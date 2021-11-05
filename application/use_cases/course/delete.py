from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

crp = CourseRepositoryPostgres()

async def delete_all_courses():
    return await crp.delete_all_courses()

async def delete_course_by_id(id):
    course = await crp.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return await crp.delete_course_by_id(id)