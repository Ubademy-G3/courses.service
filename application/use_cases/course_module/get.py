from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_module_serializer import CourseModuleSerializer
import logging

logger = logging.getLogger(__name__)

cmorp = CourseModuleRepositoryPostgres()

def get_module(db, module_id):

    module = cmorp.get_module(db, module_id)
    if module is None:
        logger.warning("Module %s not found", module_id)
        raise NotFoundError("Module")
    return CourseModuleSerializer.serialize(module)