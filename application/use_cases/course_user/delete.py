from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

curp = CourseUserRepositoryPostgres()


async def delete_course_user(course_id, user_id):
    user = await curp.get_course_user(course_id, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await curp.delete_course_user(course_id, user_id)