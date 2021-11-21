from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_module_serializer import CourseModuleSerializer

cmorp = CourseModuleRepositoryPostgres()

def update_module(db, module_id, new_args):
    
    module_to_update = cmorp.get_module(db, module_id)
    if module_to_update is None:
        raise NotFoundError("Module {}".format(module_id))

    if new_args.title is not None:
        module_to_update.title = new_args.title
        
    if new_args.media_id is not None:
        module_to_update.media_id = new_args.media_id

    if new_args.content is not None:
        module_to_update.content = new_args.content
        
    if new_args.exam_id is not None:
        module_to_update.exam_id = new_args.exam_id
                
    cmorp.update_module(db)
    return CourseModuleSerializer.serialize(module_to_update)
