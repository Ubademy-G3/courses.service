from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres

crp = CourseRepositoryPostgres()

async def update_course(id, new_args):
    return await crp.update_course(id, new_args)