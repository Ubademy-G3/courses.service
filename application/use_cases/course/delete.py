from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from exceptions.http_error import NotFoundError
import logging

logger = logging.getLogger(__name__)

crp = CourseRepositoryPostgres()    

def delete_course(db, course_id):

    course = crp.get_course_by_id(db, course_id)
    if not course:
        logger.warning("Course %s not found", course_id)
        raise NotFoundError("Course {}".format(course_id))
    crp.delete_course(db, course)