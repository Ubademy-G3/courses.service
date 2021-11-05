from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

curp = CourseUserRepositoryPostgres()


async def delete_all_course_users():
    return await curp.delete_all_course_users()

async def delete_course_user_by_id(id):
    user = await curp.get_course_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await curp.delete_course_user_by_id(id)