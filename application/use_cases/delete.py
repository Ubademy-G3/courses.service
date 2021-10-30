from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres
from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

crp = CourseRepositoryPostgres()
cmrp = CourseMediaRepositoryPostgres()
curp = CourseUserRepositoryPostgres()

async def delete_all_courses():
    return await crp.delete_all_courses()

async def delete_course_by_id(id):
    course = await crp.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return await crp.delete_course_by_id(id)


async def delete_all_courses_media():
    return await cmrp.delete_all_courses_media()

async def delete_course_media_by_id(id):
    course_media = await cmrp.get_course_by_id(id)
    if not course_media:
        raise HTTPException(status_code=404, detail="Media not found")
    return await cmrp.delete_course_media_by_id(id)


async def delete_all_course_users():
    return await curp.delete_all_course_users()

async def delete_course_user_by_id(id):
    user = await curp.get_course_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await curp.delete_course_user_by_id(id)