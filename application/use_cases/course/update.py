from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_serializer import CourseSerializer

crp = CourseRepositoryPostgres()

def update_course(db, course_id, new_args):
    
    course_to_update = crp.get_course_by_id(db, course_id)
    if not course_to_update:
        raise NotFoundError("Course {}".format(course_id))

    if new_args.name is not None:
        course_to_update.name = new_args.name
        
    if new_args.description is not None:
        course_to_update.description = new_args.description

    if new_args.category is not None:
        course_to_update.category = new_args.category
        
    if new_args.subscription_type is not None:
        course_to_update.subscription_type = new_args.subscription_type

    if new_args.location is not None:
        course_to_update.location = new_args.location

    if new_args.profile_picture is not None:
        course_to_update.profile_picture = new_args.profile_picture

    if new_args.duration is not None:
        course_to_update.duration = new_args.duration

    if new_args.language is not None:
        course_to_update.language = new_args.language

    if new_args.level is not None:
        course_to_update.level = new_args.level
                
    crp.update_course(db)
    return CourseSerializer.serialize(course_to_update)
