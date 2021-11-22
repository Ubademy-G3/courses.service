from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_serializer import CourseSerializer

crp = CourseRepositoryPostgres()

def get_all_courses(db, category, subscription_type, text):

    courses = crp.get_all_courses(db, category, subscription_type, text)
    if courses is None or len(courses) == 0:
        raise NotFoundError("Courses")
    courses_list = []
    for course in courses:
        courses_list.append(CourseSerializer.serialize(course))
    return courses_list


def get_course(db, course_id):

    course = crp.get_course_by_id(db, course_id)
    if course is None:
        raise NotFoundError("Course {}".format(course_id))
    return CourseSerializer.serialize(course)
    

async def course_exists(db, course_id):

    return crp.get_course_by_id(db, course_id) != None
    