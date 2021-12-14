from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from exceptions.http_error import NotFoundError

cmorp = CourseModuleRepositoryPostgres()


def delete_module(db, module_id):

    module = cmorp.get_module(db, module_id)
    if module is None:
        raise NotFoundError("Module")
    cmorp.delete_module(db, module)
