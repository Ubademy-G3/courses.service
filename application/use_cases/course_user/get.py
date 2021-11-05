from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

curp = CourseUserRepositoryPostgres()

async def get_all_course_users(course_id):
    return await curp.get_all_course_users(course_id)

async def get_course_user_by_id(id):
    return await curp.get_course_user_by_id(id)