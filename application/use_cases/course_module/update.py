from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_module_serializer import CourseModuleSerializer
import logging

logger = logging.getLogger(__name__)

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

    logger.debug("Update module %s", module_id)
    cmorp.update_module(db)
    logger.info("Module updated")
    return CourseModuleSerializer.serialize(module_to_update)
