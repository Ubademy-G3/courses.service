from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

crp = CourseRepositoryPostgres()

async def add_course(course):
    return await crp.add_course(course)