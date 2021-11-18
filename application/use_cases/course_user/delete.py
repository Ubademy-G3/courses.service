from persistence.repositories.course_user_repository_postgres import CourseUserRepositoryPostgres
from exceptions.http_error import NotFoundError

curp = CourseUserRepositoryPostgres()

def delete_course_user(db, course_id, user_id):

    user = curp.get_course_user(db, course_id, user_id)
    if not user:
        raise NotFoundError("User {} in Course {}".format(user_id,course_id))
    curp.delete_course_user(db, user)