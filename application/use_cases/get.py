from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

crp = CourseRepositoryPostgres()

async def get_all_courses():
    return await crp.get_all_courses()

async def get_course_by_id(id):
    return await crp.get_course_by_id(id)