from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from domain.course_model import *
from errors.http_error import NotFoundError
from application.serializers.course_serializer import CourseSerializer

crp = CourseRepositoryPostgres()

async def update_course(course_id, new_args):
    
    course_to_update = await crp.get_course(course_id)
    if not course_to_update:
        raise NotFoundError("Course {}".format(course_id))

    course_in_db = Course(**course_to_update)
    if new_args.name is not None:
        course_in_db.name = new_args.name
        
    if new_args.description is not None:
        course_in_db.description = new_args.description

    if new_args.category is not None:
        course_in_db.category = new_args.category
        
    if new_args.kind is not None:
        course_in_db.kind = new_args.kind
        
    if new_args.subscription_type is not None:
        course_in_db.subscription_type = new_args.subscription_type

    if new_args.location is not None:
        course_in_db.location = new_args.location

    if new_args.info is not None:
        course_in_db.info = new_args.info

    if new_args.profile_picture is not None:
        course_in_db.profile_picture = new_args.profile_picture
                
    update_data = course_in_db.dict(exclude_unset=True)
    updated_course = course_in_db.copy(update=update_data)
    await crp.update_course(course_id, updated_course)
    return CourseSerializer.serialize(updated_course)
