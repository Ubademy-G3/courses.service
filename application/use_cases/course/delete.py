from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from errors.http_error import NotFoundError

crp = CourseRepositoryPostgres()    

def delete_course(db, course_id):

    course = crp.get_course_by_id(db, course_id)
    if not course:
        raise NotFoundError("Course {}".format(id))
    crp.delete_course(db, course)