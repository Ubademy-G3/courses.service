from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres

curp = CourseUserRepositoryPostgres()

async def add_course_user(course_user):
    return await curp.add_course_user(course_user)